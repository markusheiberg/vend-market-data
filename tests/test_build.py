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
               "week,site,premium,pluss,basis,total,premium_pct,pluss_pct,basis_pct",
               ["2026-05-11,blocket,0,0,5940,5940,0.0,0.0,100.0",
                "2026-09-28,finn,2118,1332,1819,5269,40.2,25.3,34.5"])
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


if __name__ == "__main__":
    unittest.main()
