"""Offline tests for build.py, on a small synthetic copy of the four source repos."""
import csv
import shutil
import sys
import tempfile
import unittest
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import build  # noqa: E402


def _write(path: Path, header: str, rows: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join([header, *rows]) + "\n", encoding="utf-8")


def _read(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


class BuildTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.src, self.out = self.tmp / "sources", self.tmp / "out"
        self.out.mkdir()
        shutil.copyfile(ROOT / "events.csv", self.out / "events.csv")

        start = date(2026, 9, 1)
        daily = []
        for i in range(38):
            d = (start + timedelta(days=i)).isoformat()
            daily.append(f"{d},x,finn.no,mobility_cars,dealer,{1000 + i},{1000 + i},50,50")
            # last day: the outlier filter blanked a genuine value
            clean = "" if i == 37 else 200 + i
            daily.append(f"{d},x,blocket.se,mobility_other,private,{200 + i},{clean},,")
        # a series that stops reporting on the last day
        daily += [f"{(start + timedelta(days=i)).isoformat()},x,hemnet.se,real_estate_homes,,"
                  f"{900},{900},," for i in range(37)]
        _write(self.src / "vend-scraper-v2/data/daily_filtered.csv",
               "run_date,series,domain,vertical,seller_type,all_listings_raw,all_listings,"
               "published_today_raw,published_today", daily)
        _write(self.src / "finn-mobility-packages/data/weekly_package_mix.csv",
               "week,site,premium,pluss,basis,total,premium_pct,pluss_pct,basis_pct,sample_fraction",
               ["2026-05-11,blocket,0,0,5940,5940,0.0,0.0,100.0,0.05",
                "2026-09-28,finn,2118,1332,1819,5269,40.2,25.3,34.5,0.10"])
        _write(self.src / "finn-bolig-packages/data/packages_history.csv",
               "run_date,run_time_utc,site,large_count,medium_count,small_count,total_count,"
               "large_pct,medium_pct,small_pct",
               ["2026-05-15,14:57:06,finn,1,1,1,3,33.3,33.3,33.3",
                "2026-05-15,15:08:47,finn,12767,7160,642,20569,62.1,34.8,3.1"])
        _write(self.src / "vend-price-monitor/data/price_changes.csv",
               "observed_at,observed_date,source,year,category,subcategory,package,geo,"
               "unit_range,field,old_value,new_value,change_pct",
               ["t,2026-10-02,finn_jobb,2026,jobb,Heltid,Kategori 1,,,price_from_nok,10400,10000,-3.85",
                "t,2026-10-07,blocket_cars,2026,bil,bilannonser,Bas,,1-10,price_from_nok,100,110,10.0"])
        # bilinfo, leboncoin, price_history, articles deliberately missing

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def _build(self):
        build.build(self.src, self.out, now=datetime(2026, 10, 8, 6, tzinfo=timezone.utc))
        return _read(self.out / "facts/listings.csv")

    def test_long_format_and_outlier_kept(self):
        rows = self._build()
        last = [r for r in rows if r["site"] == "blocket.se" and r["date"] == "2026-10-08"]
        self.assertEqual(len(last), 1)
        self.assertEqual(last[0]["value"], "237")
        self.assertEqual(last[0]["quality_flag"], "outlier")
        self.assertEqual(last[0]["country"], "SE")

    def test_exclude_event_tags_rows(self):
        rows = self._build()
        blk = [r for r in rows if r["site"] == "blocket.se" and r["metric"] == "package_share"]
        self.assertTrue(blk and all(r["quality_flag"] == "exclude:E02" for r in blk))
        finn = [r for r in rows if r["site"] == "finn.no" and r["metric"] == "package_share"
                and r["vertical"] == "mobility_cars"]
        self.assertTrue(finn and all(r["quality_flag"] == "" for r in finn))
        self.assertTrue(all(r["is_sample"] == "1" for r in finn))

    def test_sample_fraction_carried(self):
        rows = self._build()
        frac = {(r["site"], r["date"]): r["value"] for r in rows if r["metric"] == "sample_fraction"}
        self.assertEqual(frac, {("blocket.se", "2026-05-11"): "0.05", ("finn.no", "2026-09-28"): "0.1"})

    def test_weekly_rollup(self):
        self._build()
        weekly = _read(self.out / "facts/listings_weekly.csv")
        finn = {r["date"]: r for r in weekly
                if r["site"] == "finn.no" and r["metric"] == "listings" and r["vertical"] == "mobility_cars"}
        # 2026-09-07 is a Monday: days 6..12 of the fixture carry 1006..1012
        self.assertEqual(finn["2026-09-07"]["value"], "1009")
        self.assertEqual(finn["2026-09-07"]["valid_days"], "7")
        # the outlier-flagged last day is not averaged in
        blk = [r for r in weekly if r["site"] == "blocket.se" and r["metric"] == "listings"]
        self.assertEqual(blk[-1]["valid_days"], "3")    # Mon Oct 5-7 clean, Oct 8 flagged
        # weekly package rows pass through
        self.assertTrue(any(r["metric"] == "package_share" for r in weekly))

    def test_bilinfo_interpolation_and_implied_flows(self):
        _write(self.src / "vend-scraper-v2/data/bilinfo_weekly.csv",
               "week_start_date,report_year,report_week,year_week,visits,supply_cars,avg_days_to_sell,report_date,publish_lag_days",
               ["2026-05-18,2026,21,2026-W21,437000,49000,41,2026-05-26,8",
                # 2026-05-25 and 06-01 have no report; 2026-06-08 is the basis break
                "2026-06-08,2026,24,2026-W24,436000,52000,56,2026-06-16,8",
                "2026-06-15,2026,25,2026-W25,427000,52700,59,2026-06-23,8"])
        rows = self._build()
        b = {(r["date"], r["metric"]): r for r in rows if r["site"] == "bilinfo.dk"}
        # adjusted = reported x 56/41 before the break, reported from it
        self.assertEqual(b[("2026-05-18", "adj_days_to_sell")]["value"], "56")
        self.assertEqual(b[("2026-05-18", "avg_days_to_sell")]["value"], "41")
        self.assertEqual(b[("2026-06-15", "adj_days_to_sell")]["value"], "59")
        # stock and ADJUSTED days interpolated on a straight line; reported days not
        self.assertEqual(b[("2026-05-25", "supply_cars")]["value"], "50000")
        self.assertEqual(b[("2026-06-01", "supply_cars")]["value"], "51000")
        self.assertEqual(b[("2026-06-01", "adj_days_to_sell")]["value"], "56")
        self.assertEqual(b[("2026-06-01", "supply_cars")]["quality_flag"], "interpolated")
        self.assertNotIn(("2026-06-01", "avg_days_to_sell"), b)
        self.assertNotIn(("2026-06-01", "visits"), b)
        # week 06-15: opening stock 52000, adjusted days 59
        # sold = 52000 x 7 / 59 = 6169.5; added = 52700 - 52000 + sold = 6869.5
        self.assertEqual(b[("2026-06-15", "implied_cars_sold")]["value"], "6169")
        self.assertEqual(b[("2026-06-15", "implied_cars_added")]["value"], "6869")
        self.assertEqual(b[("2026-06-15", "implied_cars_sold")]["quality_flag"], "")
        # across the break: sold uses adjusted days, so no step from the definition
        # change (reported 41 would give 49000 x 7 / 41 = 8366)
        self.assertEqual(b[("2026-05-25", "implied_cars_sold")]["value"], "6125")
        self.assertEqual(b[("2026-05-25", "implied_cars_sold")]["quality_flag"], "interpolated")
        # the first week has no opening stock
        self.assertNotIn(("2026-05-18", "implied_cars_sold"), b)
        digest = (self.out / "digest/latest.md").read_text()
        self.assertIn("| 2026-06-01 * | 51 000 | 56 |", digest)

    def test_private_cars_census(self):
        hdr = "run_timestamp,site,metric,band,value"
        rows = []
        # a Saturday test run and the Sunday run land in one ISO week: keep the later
        for ts, med in (("2026-10-10T18:50:00+00:00", "49000.0"), ("2026-10-11T22:10:00+00:00", "50000.0")):
            rows += [f"{ts},tradera,median_price_sek,,{med}",
                     f"{ts},tradera,median_age_published_days,,22.4",
                     f"{ts},blocket,median_age_published_id_estimate_days,,25.1",
                     f"{ts},blocket,median_age_published_or_renewed_days,,15.0",
                     f"{ts},blocket,price_pct,0k–25k,14.4",
                     f"{ts},tradera,listings_site_count,,3011.0"]
        _write(self.src / "finn-mobility-packages/data/private_cars_se/history.csv", hdr, rows)
        facts = self._build()
        pc = {(r["site"], r["metric"]): r for r in facts if r["segment"] == "private"
              and r["source"] == "finn-mobility-packages/history"}
        self.assertEqual(pc[("tradera.com", "median_price")]["value"], "50000")
        self.assertEqual(pc[("tradera.com", "median_price")]["date"], "2026-10-05")
        self.assertEqual(pc[("blocket.se", "median_days_since_published")]["value"], "25.1")
        self.assertEqual(pc[("blocket.se", "median_days_since_renewed")]["value"], "15")
        # site counts would duplicate the daily listings series; distributions go elsewhere
        self.assertNotIn(("tradera.com", "listings_site_count"), pc)
        self.assertEqual(len(pc), 4)
        dist = _read(self.out / "facts/private_cars_se.csv")
        self.assertEqual(len(dist), 6)
        self.assertEqual({r["run_timestamp"][:10] for r in dist}, {"2026-10-11"})
        self.assertIn({"site": "blocket.se", "band": "0k–25k", "value": "14.4"},
                      [{k: r[k] for k in ("site", "band", "value")} for r in dist])

    def test_same_day_runs_keep_later(self):
        rows = self._build()
        large = [r for r in rows if r["metric"] == "package_count" and r["package"] == "large"]
        self.assertEqual([r["value"] for r in large], ["12767"])

    def test_price_glitch_excluded_from_digest(self):
        self._build()
        changes = {r["observed_date"]: r for r in _read(self.out / "facts/price_changes.csv")}
        self.assertEqual(changes["2026-10-02"]["quality_flag"], "exclude:E15")
        self.assertEqual(changes["2026-10-07"]["currency"], "SEK")
        digest = (self.out / "digest/latest.md").read_text()
        self.assertIn("2026-10-07 | blocket.se", digest)
        self.assertNotIn("2026-10-02 | finn.no", digest)

    def test_digest_separates_failed_from_filtered(self):
        self._build()
        digest = (self.out / "digest/latest.md").read_text()
        no_value, filtered = digest.split("## Series blanked by the outlier filter today")
        self.assertIn("hemnet.se · real_estate_homes", no_value)
        self.assertIn("blocket.se · mobility_other · private", filtered.split("##")[0])
        self.assertIn("Missing inputs", digest)          # absent files are reported, not fatal
        self.assertIn("| finn.no | mobility_cars | dealer | 1 037 |", digest)

    def test_missing_input_keeps_previous_data(self):
        self._build()
        before_changes = _read(self.out / "facts/price_changes.csv")
        self.assertEqual(len(before_changes), 2)
        # upstream export disappears: previous rows must survive, with a warning
        (self.src / "vend-price-monitor/data/price_changes.csv").unlink()
        (self.src / "finn-mobility-packages/data/weekly_package_mix.csv").unlink()
        rows = self._build()
        self.assertEqual(len(_read(self.out / "facts/price_changes.csv")), 2)
        kept = [r for r in rows if r["source"] == "finn-mobility-packages/weekly_package_mix"]
        self.assertEqual(len(kept), 14)
        self.assertTrue(all(r["quality_flag"] == "exclude:E02" for r in kept
                            if r["site"] == "blocket.se" and r["metric"].startswith("package_")))
        digest = (self.out / "digest/latest.md").read_text()
        self.assertIn("weekly_package_mix.csv", digest.split("##")[1])


if __name__ == "__main__":
    unittest.main()
