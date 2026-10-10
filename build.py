"""Build the consolidated Vend market dataset from the four scraper repos' data/.

    python build.py --sources sources --out .

`sources/` holds one checkout per repo (the nightly workflow clones them there):

    sources/vend-scraper-v2/data/...
    sources/finn-mobility-packages/data/...
    sources/finn-bolig-packages/data/...
    sources/vend-price-monitor/data/...

Writes:
    facts/listings.csv        every count series, one long table (see CATALOG.md)
    facts/prices.csv          price-list history (new / changed / removed)
    facts/price_changes.csv   one row per changed price field
    facts/news.csv            news articles from the sites' B2B blogs
    reference/*.csv           cross-sections copied as-is (latest price lists, geo grid)
    digest/latest.md          what moved, what broke, what changed

A missing source repo or file is reported and skipped, never fatal: one repo
not exporting must not stop the other three from refreshing. Stdlib only.
"""
from __future__ import annotations

import argparse
import csv
import fnmatch
import shutil
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from statistics import mean
from typing import Iterable, Optional

COUNTRY = {
    "finn.no": "NO", "hjem.no": "NO",
    "bilbasen.dk": "DK", "biltorvet.dk": "DK", "bilhandel.dk": "DK", "bilinfo.dk": "DK",
    "blocket.se": "SE", "wayke.se": "SE", "tradera.com": "SE", "hemnet.se": "SE",
    "oikotie.fi": "FI", "etuovi.com": "FI",
    "leboncoin.fr": "FR",
}

# vend-price-monitor source -> (site, vertical, currency)
PRICE_SOURCE = {
    "finn": ("finn.no", "real_estate", "NOK"),
    "finn_cars": ("finn.no", "mobility_cars", "NOK"),
    "finn_other_mobility": ("finn.no", "mobility_other", "NOK"),
    "finn_jobb": ("finn.no", "jobs", "NOK"),
    "blocket_cars": ("blocket.se", "mobility_cars", "SEK"),
    "blocket_private": ("blocket.se", "private_listings", "SEK"),
    "bilbasen": ("bilbasen.dk", "mobility_cars", "DKK"),
}

LISTING_COLS = ["date", "grain", "country", "site", "vertical", "segment", "package",
                "metric", "value", "unit", "is_sample", "quality_flag", "source"]

missing: list[str] = []


def read_csv(path: Path, required: bool = True) -> list[dict]:
    if not path.exists():
        if required:
            missing.append(str(path))
        return []
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, cols: list[str], rows: Iterable[dict]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow(r)
            n += 1
    return n


def num(s: Optional[str]) -> Optional[float]:
    if s is None or s == "":
        return None
    return float(s)


def fmt(v: Optional[float]):
    if v is None:
        return ""
    return int(v) if float(v).is_integer() else round(v, 4)


def row(d, grain, site, vertical, segment, metric, value, unit, source,
        package="", is_sample=0, flag=""):
    return {"date": d, "grain": grain, "country": COUNTRY.get(site, ""), "site": site,
            "vertical": vertical, "segment": segment or "", "package": package,
            "metric": metric, "value": fmt(value), "unit": unit,
            "is_sample": is_sample, "quality_flag": flag, "source": source}


# ── sources ──────────────────────────────────────────────────────────────────

def daily_series(src: Path) -> list[dict]:
    """vend-scraper-v2 daily counts. The filtered value is used; where the outlier
    filter blanked a value, the raw one is kept and flagged rather than dropped."""
    out = []
    for r in read_csv(src / "vend-scraper-v2/data/daily_filtered.csv"):
        for metric, raw_col, col in (("listings", "all_listings_raw", "all_listings"),
                                     ("new_listings", "published_today_raw", "published_today")):
            raw, clean = num(r[raw_col]), num(r[col])
            if raw is None and clean is None:
                continue
            flag = "" if clean is not None else "outlier"
            out.append(row(r["run_date"], "daily", r["domain"], r["vertical"],
                           r["seller_type"], metric, clean if clean is not None else raw,
                           "listings", "vend-scraper-v2/daily_filtered", flag=flag))
    return out


def interpolate_weekly(known: dict[date, float], first: date, last: date) -> dict[date, tuple]:
    """Every Monday from first to last -> (value, interpolated?). A missing week is
    filled on the straight line between its nearest known neighbours, by date.
    Nothing is extrapolated past the first or last known week."""
    pts = sorted(known)
    out, j = {}, 0
    w = first
    while w <= last:
        if w in known:
            out[w] = (known[w], False)
        else:
            while pts[j + 1] < w:
                j += 1
            a, b = pts[j], pts[j + 1]
            t = (w - a).days / (b - a).days
            out[w] = (known[a] + t * (known[b] - known[a]), True)
        w += timedelta(days=7)
    return out


# The days-to-sell basis break, as defined in vend-scraper-v2's
# build_bilinfo_workbook.py (the bilinfo Excel). Read from that file on every
# build so the two can never disagree; these are only the fallback.
DAYS_BASIS_BREAK = date(2026, 6, 8)
DAYS_ADJ_FACTOR = 56 / 41


def days_basis(src: Path) -> tuple[date, float]:
    """(break date, factor) from the workbook source, else the pinned fallback."""
    import re
    p = src / "vend-scraper-v2/build_bilinfo_workbook.py"
    if p.exists():
        text = p.read_text(encoding="utf-8")
        b = re.search(r"^DAYS_BASIS_BREAK = dt\.date\((\d+), (\d+), (\d+)\)", text, re.M)
        f = re.search(r"^DAYS_ADJ_FACTOR = (\d+(?:\.\d+)?)\s*/\s*(\d+(?:\.\d+)?)", text, re.M)
        if b and f:
            return date(*map(int, b.groups())), float(f.group(1)) / float(f.group(2))
    missing.append(f"{p} (DAYS_BASIS_BREAK / DAYS_ADJ_FACTOR; using 2026-06-08, 56/41)")
    return DAYS_BASIS_BREAK, DAYS_ADJ_FACTOR


def bilinfo(src: Path) -> list[dict]:
    """bilinfo.dk weekly market report (the Bilbasen dealer market), plus implied flows.

    Days to sell changed basis on 2026-06-08: before it, bilinfo measured the top
    50 models only, which sell faster, so reported days jumped 41 -> 56 in one
    week with no market change. adj_days_to_sell puts the history on one basis
    (reported x 56/41 before the break), exactly as the bilinfo workbook does, and
    every derived flow uses it.

    Stock and ADJUSTED days are interpolated across weeks with no report (holiday
    breaks) on a straight line by date, flagged `interpolated`. Reported days and
    visits are left as reported.

    Implied flows for week w, matching build_bilinfo_workbook.add_implied_flows
    (opening stock = the previous week's, days = this week's adjusted):
        implied_cars_sold  = stock_{w-1} x 7 / adj_days_to_sell_w     (outflow)
        implied_cars_added = stock_w - stock_{w-1} + implied_cars_sold
    "Sold" is really outflow: cars also leave unsold, so it bounds sales from above.
    A flow is flagged `interpolated` when any input to it was.
    """
    src_tag = "vend-scraper-v2/bilinfo_weekly"
    brk, factor = days_basis(src)
    out, stock, adj = [], {}, {}
    for r in read_csv(src / "vend-scraper-v2/data/bilinfo_weekly.csv"):
        w = date.fromisoformat(r["week_start_date"])
        args = (w.isoformat(), "weekly", "bilinfo.dk", "mobility_cars", "")
        if num(r["visits"]) is not None:
            out.append(row(*args, "visits", num(r["visits"]), "visitors", src_tag))
        d = num(r["avg_days_to_sell"])
        if d is not None:
            out.append(row(*args, "avg_days_to_sell", d, "days", src_tag))
            # rounded to 0.1 as the workbook does, so the flows match it exactly
            adj[w] = round(d * factor, 1) if w < brk else d
        if num(r["supply_cars"]) is not None:
            stock[w] = num(r["supply_cars"])
    if not stock or not adj:
        return out
    first, last = max(min(stock), min(adj)), min(max(stock), max(adj))
    S = interpolate_weekly(stock, first, last)
    A = interpolate_weekly(adj, first, last)
    flag = lambda *xs: "interpolated" if any(x[1] for x in xs) else ""
    flows = "vend-market-data, as build_bilinfo_workbook.add_implied_flows"
    for w in sorted(S):
        args = (w.isoformat(), "weekly", "bilinfo.dk", "mobility_cars", "")
        out.append(row(*args, "supply_cars", round(S[w][0]), "listings", src_tag, flag=flag(S[w])))
        out.append(row(*args, "adj_days_to_sell", round(A[w][0], 1), "days",
                       f"{src_tag}, x {factor:.4f} before {brk}", flag=flag(A[w])))
        prev = w - timedelta(days=7)
        if prev in S:
            sold = S[prev][0] * 7 / A[w][0]
            f = flag(S[prev], S[w], A[w])
            out.append(row(*args, "implied_cars_sold", round(sold), "cars_per_week", flows, flag=f))
            out.append(row(*args, "implied_cars_added", round(S[w][0] - S[prev][0] + sold),
                           "cars_per_week", flows, flag=f))
    return out
    first, last = max(min(stock), min(days)), min(max(stock), max(days))
    S = interpolate_weekly(stock, first, last)
    D = interpolate_weekly(days, first, last)
    flag = lambda *xs: "interpolated" if any(x[1] for x in xs) else ""
    for w in sorted(S):
        args = (w.isoformat(), "weekly", "bilinfo.dk", "mobility_cars", "")
        out.append(row(*args, "supply_cars", round(S[w][0]), "listings", src_tag, flag=flag(S[w])))
        out.append(row(*args, "avg_days_to_sell", round(D[w][0], 1), "days", src_tag, flag=flag(D[w])))
        sold = S[w][0] * 7 / D[w][0]
        out.append(row(*args, "implied_cars_sold", round(sold), "cars_per_week",
                       "vend-market-data: supply_cars x 7 / avg_days_to_sell", flag=flag(S[w], D[w])))
        nxt = w + timedelta(days=7)
        if nxt in S:
            out.append(row(*args, "implied_cars_added", round(S[nxt][0] - S[w][0] + sold),
                           "cars_per_week",
                           "vend-market-data: next week's supply_cars - supply_cars + implied_cars_sold",
                           flag=flag(S[w], S[nxt], D[w])))
    return out


def leboncoin(src: Path) -> list[dict]:
    return [row(r["observed_date"], "point", "leboncoin.fr", "mobility_cars", r["seller_type"],
                "listings", num(r["all_listings"]), "listings",
                "vend-scraper-v2/leboncoin_manual", flag="manual")
            for r in read_csv(src / "vend-scraper-v2/data/leboncoin_manual.csv")]


def mobility_packages(src: Path) -> list[dict]:
    """Dealer car package mix. Counts are a SAMPLE of listings, not the market."""
    site = {"finn": "finn.no", "blocket": "blocket.se"}
    out = []
    for r in read_csv(src / "finn-mobility-packages/data/weekly_package_mix.csv"):
        for pkg in ("premium", "pluss", "basis"):
            args = (r["week"], "weekly", site[r["site"]], "mobility_cars", "dealer")
            out.append(row(*args, "package_sample_count", num(r[pkg]), "sampled_listings",
                           "finn-mobility-packages/weekly_package_mix", package=pkg, is_sample=1))
            out.append(row(*args, "package_share", num(r[pkg + "_pct"]), "pct",
                           "finn-mobility-packages/weekly_package_mix", package=pkg, is_sample=1))
        # Present since the source started recording it (2026-10). Counts are only
        # comparable between weeks with the same fraction.
        if r.get("sample_fraction"):
            out.append(row(*args, "sample_fraction", num(r["sample_fraction"]), "fraction",
                           "finn-mobility-packages/weekly_package_mix"))
    return out


# private_cars_se metric -> (fact metric, unit). The census writes more (price and
# age distributions by band); those go to facts/private_cars_se.csv whole.
PRIVATE_CARS_SCALARS = {
    ("tradera", "median_price_sek"): ("median_price", "SEK"),
    ("tradera", "p25_price_sek"): ("p25_price", "SEK"),
    ("tradera", "p75_price_sek"): ("p75_price", "SEK"),
    ("tradera", "median_age_published_days"): ("median_days_since_published", "days"),
    ("blocket", "median_price_sek"): ("median_price", "SEK"),
    ("blocket", "p25_price_sek"): ("p25_price", "SEK"),
    ("blocket", "p75_price_sek"): ("p75_price", "SEK"),
    # Blocket shows no publish date; this is the ID-sequence estimate (see CATALOG)
    ("blocket", "median_age_published_id_estimate_days"): ("median_days_since_published", "days"),
    ("blocket", "median_age_published_or_renewed_days"): ("median_days_since_renewed", "days"),
}
PRIVATE_CARS_SITE = {"tradera": "tradera.com", "blocket": "blocket.se"}
PRIVATE_CARS_REL = "finn-mobility-packages/data/private_cars_se/history.csv"


def private_cars_runs(src: Path) -> list[tuple[str, list[dict]]]:
    """Census runs keyed by ISO week (Monday). Two runs in one week keep the later."""
    by_run: dict[str, list[dict]] = defaultdict(list)
    for r in read_csv(src / PRIVATE_CARS_REL):
        by_run[r["run_timestamp"]].append(r)
    weeks: dict[str, tuple[str, list[dict]]] = {}
    for ts in sorted(by_run):
        d = date.fromisoformat(ts[:10])
        weeks[(d - timedelta(days=d.weekday())).isoformat()] = (ts, by_run[ts])
    return [(monday, rows) for monday, (_, rows) in sorted(weeks.items())]


def private_cars(src: Path) -> list[dict]:
    """Tradera vs Blocket private car census: median price and listing age per week."""
    out = []
    for monday, rows in private_cars_runs(src):
        for r in rows:
            m = PRIVATE_CARS_SCALARS.get((r["site"], r["metric"]))
            if m and r["value"] != "":
                out.append(row(monday, "weekly", PRIVATE_CARS_SITE[r["site"]], "mobility_cars",
                               "private", m[0], num(r["value"]), m[1],
                               "finn-mobility-packages/history"))
    return out


def bolig_packages(src: Path) -> list[dict]:
    """finn used-home package mix: a full crawl, so counts are the real totals.
    Two runs on one date (2026-05-15 setup) keep the later one."""
    latest: dict[str, dict] = {}
    for r in read_csv(src / "finn-bolig-packages/data/packages_history.csv"):
        latest[r["run_date"]] = r
    out = []
    for d, r in sorted(latest.items()):
        for pkg in ("large", "medium", "small"):
            args = (d, "weekly", "finn.no", "real_estate_homes", "")
            out.append(row(*args, "package_count", num(r[pkg + "_count"]), "listings",
                           "finn-bolig-packages/packages_history", package=pkg))
            out.append(row(*args, "package_share", num(r[pkg + "_pct"]), "pct",
                           "finn-bolig-packages/packages_history", package=pkg))
    return out


def prices(src: Path) -> tuple[list[dict], list[dict]]:
    def enrich(r):
        site, vertical, cur = PRICE_SOURCE.get(r["source"], ("", "", ""))
        return {**r, "site": site, "country": COUNTRY.get(site, ""), "vertical": vertical,
                "currency": cur}
    base = src / "vend-price-monitor/data"
    return ([enrich(r) for r in read_csv(base / "price_history.csv")],
            [enrich(r) for r in read_csv(base / "price_changes.csv")])


def news(src: Path) -> list[dict]:
    return read_csv(src / "vend-price-monitor/data/articles.csv")


# ── events ───────────────────────────────────────────────────────────────────

def load_events(path: Path) -> list[dict]:
    return read_csv(path)


def _match(pattern: str, value: str) -> bool:
    return pattern in ("", "*") or fnmatch.fnmatch(value or "", pattern)


def event_applies(e: dict, d: str, site: str, vertical: str, segment: str, metric: str) -> bool:
    if d < e["date_from"] or (e["date_to"] and d > e["date_to"]):
        return False
    return (_match(e["site"], site) and _match(e["vertical"], vertical)
            and _match(e["segment"], segment) and _match(e["metric"], metric))


def apply_exclusions(rows: list[dict], events: list[dict], metric_key="metric") -> None:
    """Tag rows covered by an `exclude` event, so trends can drop them by filter."""
    excl = [e for e in events if e["flag"] == "exclude"]
    for r in rows:
        d = r.get("date") or r.get("observed_date", "")
        for e in excl:
            if event_applies(e, d, r["site"], r["vertical"], r.get("segment", ""),
                             r.get(metric_key) or "price"):
                r["quality_flag"] = f"exclude:{e['id']}"
                break


# ── weekly rollup ────────────────────────────────────────────────────────────

# Same thresholds as the BigQuery weekly_avg view: a stock needs 2 clean days in
# the week, a flow 4, or the week is left out rather than averaged from a scrap.
MIN_DAYS = {"listings": 2, "new_listings": 4}
# Lean on purpose: every column is repeated ~10k times, and the file has to fit
# whole in a project. grain is always weekly; quality_flag and source live in
# facts/listings.csv for anyone who needs them.
WEEKLY_COLS = ["date", "country", "site", "vertical", "segment", "package", "metric",
               "value", "unit", "is_sample", "valid_days"]


def weekly_rollup(listings: list[dict]) -> list[dict]:
    """facts/listings.csv at a weekly grain, small enough to sit whole in a Claude
    project's context (the daily file is ~225k tokens). Daily series become the
    mean of their clean days in the ISO week (Monday date); weekly series pass
    through unchanged; one-off manual points are left out."""
    groups: dict[tuple, list] = defaultdict(list)
    out = []
    for r in listings:
        if r["grain"] == "weekly":
            out.append({**r, "valid_days": ""})
        elif r["grain"] == "daily" and not r["quality_flag"]:
            d = date.fromisoformat(r["date"])
            monday = (d - timedelta(days=d.weekday())).isoformat()
            key = (monday, r["country"], r["site"], r["vertical"], r["segment"], r["metric"], r["unit"])
            groups[key].append(float(r["value"]))
    for (monday, country, site, vertical, segment, metric, unit), vals in groups.items():
        if len(vals) < MIN_DAYS.get(metric, 2):
            continue
        out.append({"date": monday, "grain": "weekly", "country": country, "site": site,
                    "vertical": vertical, "segment": segment, "package": "", "metric": metric,
                    "value": fmt(round(mean(vals), 1)), "unit": unit, "is_sample": 0,
                    "quality_flag": "", "valid_days": len(vals)})
    out.sort(key=lambda r: (r["date"], r["site"], r["vertical"], r["segment"],
                            r["package"], r["metric"]))
    return out


# ── digest ───────────────────────────────────────────────────────────────────

def _pct(new, old):
    return None if not old or new is None else (new - old) / old * 100


def _p(v):
    return "" if v is None else f"{v:+.1f}%"


def _n(v):
    return "" if v is None else f"{v:,.0f}".replace(",", " ")


def listings_table(listings: list[dict], as_of: date) -> list[str]:
    """Each daily stock series: latest clean value, 7-day avg vs prior 7 days,
    and vs 4 weeks earlier. A window needs 4 clean days to report."""
    # Outlier-flagged values are KEPT here: the 3-std-dev filter upstream also
    # blanks genuine values on series that trend (see CATALOG.md), and dropping
    # them would hide exactly the moves this table exists to show.
    series, flagged = defaultdict(dict), set()
    for r in listings:
        if (r["grain"] == "daily" and r["metric"] == "listings"
                and not r["quality_flag"].startswith("exclude")):
            key = (r["site"], r["vertical"], r["segment"])
            d = date.fromisoformat(r["date"])
            series[key][d] = float(r["value"])
            if r["quality_flag"] == "outlier":
                flagged.add((key, d))

    def window(vals, end, days=7):
        xs = [v for d, v in vals.items() if end - timedelta(days=days) < d <= end]
        return mean(xs) if len(xs) >= 4 else None

    lines = ["| site | vertical | segment | latest | date | 7d vs prior 7d | vs 4 weeks ago |",
             "|---|---|---|---:|---|---:|---:|"]
    rows = []
    for key, vals in series.items():
        last_d = max(vals)
        cur = window(vals, as_of)
        rows.append((key, vals[last_d], last_d, (key, last_d) in flagged,
                     _pct(cur, window(vals, as_of - timedelta(days=7))),
                     _pct(cur, window(vals, as_of - timedelta(days=28)))))
    for (site, vert, seg), last, last_d, is_flagged, wow, m4 in sorted(rows):
        stale = " ⚠️" if (as_of - last_d).days > 1 else ""
        mark = " †" if is_flagged else ""
        lines.append(f"| {site} | {vert} | {seg or '-'} | {_n(last)}{mark} | {last_d}{stale} | "
                     f"{_p(wow)} | {_p(m4)} |")
    return lines


def failing_series(listings: list[dict], as_of: date) -> tuple[list[str], list[str]]:
    """Daily series that reported in the 30 days before as_of but not cleanly on
    as_of. Split in two: no value at all (the scrape failed), and a value the
    upstream outlier filter blanked (the scrape worked; the filter may be wrong)."""
    seen, clean, filtered = set(), set(), set()
    for r in listings:
        if r["grain"] != "daily":
            continue
        d = date.fromisoformat(r["date"])
        key = (r["site"], r["vertical"], r["segment"], r["metric"])
        if as_of - timedelta(days=30) <= d < as_of and not r["quality_flag"]:
            seen.add(key)
        if d == as_of:
            (filtered if r["quality_flag"] == "outlier" else clean).add(key)
    line = lambda k: f"- {k[0]} · {k[1]} · {k[2] or '-'} · {k[3]}"
    return ([line(k) for k in sorted(seen - clean - filtered)],
            [line(k) for k in sorted((seen & filtered) - clean)])


def package_table(listings: list[dict]) -> list[str]:
    shares = defaultdict(dict)
    for r in listings:
        if r["metric"] == "package_share" and not r["quality_flag"]:
            shares[(r["site"], r["vertical"])].setdefault(r["date"], {})[r["package"]] = float(r["value"])
    lines = ["| site | vertical | latest week | mix now | mix 4 runs earlier |", "|---|---|---|---|---|"]
    for (site, vert), by_date in sorted(shares.items()):
        ds = sorted(by_date)
        fmtmix = lambda m: " / ".join(f"{k} {v:.1f}" for k, v in m.items())
        earlier = fmtmix(by_date[ds[-5]]) if len(ds) >= 5 else ""
        lines.append(f"| {site} | {vert} | {ds[-1]} | {fmtmix(by_date[ds[-1]])} | {earlier} |")
    return lines


def bilinfo_table(listings: list[dict], weeks: int = 6) -> list[str]:
    """Latest weeks of the Danish dealer market from the bilinfo report."""
    by_week: dict[str, dict] = defaultdict(dict)
    interp: dict[str, bool] = defaultdict(bool)
    for r in listings:
        if r["site"] == "bilinfo.dk":
            by_week[r["date"]][r["metric"]] = float(r["value"])
            interp[r["date"]] |= r["quality_flag"] == "interpolated"
    lines = ["| week | stock | adj. days to sell | implied sold | implied added |",
             "|---|---:|---:|---:|---:|"]
    for w in sorted(by_week)[-weeks:]:
        m = by_week[w]
        mark = " *" if interp[w] else ""
        lines.append(f"| {w}{mark} | {_n(m.get('supply_cars'))} | {_n(m.get('adj_days_to_sell'))} | "
                     f"{_n(m.get('implied_cars_sold'))} | {_n(m.get('implied_cars_added'))} |")
    return lines


def build_digest(listings, price_changes, articles, events, as_of: date, now: datetime) -> str:
    since30 = (as_of - timedelta(days=30)).isoformat()
    out = ["# Vend market digest", "",
           f"Generated {now:%Y-%m-%d %H:%M} UTC. Data up to **{as_of}**.",
           "Read `CATALOG.md` for what each series means and `events.csv` before trusting a jump.", ""]

    if missing:
        out += ["## ⚠️ Missing inputs", "", *[f"- `{m}`" for m in missing], ""]

    fails, filtered = failing_series(listings, as_of)
    out += ["## Series with no value today", "",
            *(fails or ["None. Every daily series that reported in the last 30 days reported today."]), ""]
    if filtered:
        out += ["## Series blanked by the outlier filter today", "",
                "The scrape returned a value but `daily_filtered` nulled it as >3 std dev from",
                "the series' all-time mean. On a trending series that is usually a real move,",
                "not a bad scrape: compare against the days before in `facts/listings.csv`.", "",
                *filtered, ""]

    out += ["## Listings stock (daily series)", "",
            "7-day average against the previous 7 days, and against the same window 4 weeks",
            "earlier. Event-excluded values are left out. † = latest value was blanked by the",
            "outlier filter (raw shown). ⚠️ = latest value older than a day.", "",
            *listings_table(listings, as_of), ""]

    out += ["## Package mix", "",
            "Shares in %. Car packages are a 10% sample of dealer listings; finn homes is a",
            "full crawl of used homes.", "", *package_table(listings), ""]

    out += ["## Danish dealer market (bilinfo, weekly)", "",
            "Cars per week. Implied sold = last week's stock x 7 / adjusted days to sell;",
            "implied added = change in stock + sold. Adjusted days put the history on one",
            "basis across bilinfo's 2026-06-08 definition change (E17), as the bilinfo",
            "workbook does. Days are whole numbers, so one day moves sold by ~2%.",
            "* = a week with no report, interpolated.", "", *bilinfo_table(listings), ""]

    recent = [c for c in price_changes if c["observed_date"] >= since30 and not c.get("quality_flag")]
    out += ["## Price changes, last 30 days", ""]
    if recent:
        out += ["| date | site | what | field | old | new | change |", "|---|---|---|---|---:|---:|---:|"]
        for c in recent:
            what = " · ".join(x for x in (c["category"], c["subcategory"], c["package"],
                                          c["geo"], c["unit_range"]) if x)
            out.append(f"| {c['observed_date']} | {c['site']} | {what} | {c['field']} | "
                       f"{c['old_value']} | {c['new_value']} | {c['change_pct']}% |")
    else:
        out.append("None (excluding glitches listed in `events.csv`).")
    out.append("")

    arts = [a for a in articles if a["seen_date"] >= since30 and a["price_related"] == "1"]
    out += ["## Price-related news, last 30 days", ""]
    out += [f"- {a['seen_date']} · {a['site']} · [{a['title']}]({a['url']})" for a in arts] or ["None."]
    out.append("")

    active = [e for e in events if not e["date_to"] or e["date_to"] >= since30]
    out += ["## Data events touching the last 30 days", ""]
    out += [f"- **{e['id']}** {e['date_from']}→{e['date_to'] or 'ongoing'} · {e['site']} "
            f"{e['vertical']} · {e['flag']}: {e['summary']}" for e in active] or ["None."]
    out.append("")
    return "\n".join(out)


# ── main ─────────────────────────────────────────────────────────────────────

def build(src: Path, out: Path, now: Optional[datetime] = None) -> None:
    now = now or datetime.now(timezone.utc)
    missing.clear()
    events = load_events(out / "events.csv")

    # A source whose input is missing keeps its rows from the previous build, so a
    # broken upstream export shows up as a warning and stale data, never as data
    # silently disappearing from facts/.
    previous = read_csv(out / "facts/listings.csv", required=False)
    listings = []
    for loader, rel in ((daily_series, "vend-scraper-v2/data/daily_filtered.csv"),
                        (bilinfo, "vend-scraper-v2/data/bilinfo_weekly.csv"),
                        (leboncoin, "vend-scraper-v2/data/leboncoin_manual.csv"),
                        (mobility_packages, "finn-mobility-packages/data/weekly_package_mix.csv"),
                        (bolig_packages, "finn-bolig-packages/data/packages_history.csv"),
                        (private_cars, PRIVATE_CARS_REL)):
        if (src / rel).exists():
            listings += loader(src)
        else:
            missing.append(str(src / rel))
            tag = rel.split("/")[0] + "/" + Path(rel).stem
            listings += [r for r in previous if r["source"] == tag]
    for r in listings:
        r["quality_flag"] = "" if r["quality_flag"].startswith("exclude") else r["quality_flag"]
    apply_exclusions(listings, events)
    listings.sort(key=lambda r: (r["date"], r["site"], r["vertical"], r["segment"],
                                 r["package"], r["metric"]))

    pm = src / "vend-price-monitor/data"
    have_hist, have_changes = (pm / "price_history.csv").exists(), (pm / "price_changes.csv").exists()
    price_hist, price_changes = prices(src)
    for r in price_hist + price_changes:
        r["quality_flag"] = ""
    for r in price_changes:
        r["metric"] = "price"
    apply_exclusions(price_changes, events)
    apply_exclusions(price_hist, events, metric_key="_none")
    articles = news(src)

    n = write_csv(out / "facts/listings.csv", LISTING_COLS, listings)
    write_csv(out / "facts/listings_weekly.csv", WEEKLY_COLS, weekly_rollup(listings))
    if not have_changes:
        # Keep the previous file; the digest still reads it.
        price_changes = [{**r, "quality_flag": r.get("quality_flag", "")}
                         for r in read_csv(out / "facts/price_changes.csv", required=False)]
    hist_cols = ["observed_date", "country", "site", "vertical", "currency", "event", "source",
                 "year", "category", "subcategory", "package", "geo", "unit_range",
                 "price_from_nok", "price_to_nok", "price_per_month_nok", "vat_included",
                 "quality_flag", "observed_at", "url"]
    chg_cols = ["observed_date", "country", "site", "vertical", "currency", "source", "year",
                "category", "subcategory", "package", "geo", "unit_range", "field",
                "old_value", "new_value", "change_pct", "quality_flag", "observed_at"]
    if have_hist:
        write_csv(out / "facts/prices.csv", hist_cols, price_hist)
    if have_changes:
        write_csv(out / "facts/price_changes.csv", chg_cols, price_changes)
    if (src / "vend-price-monitor/data/articles.csv").exists():
        write_csv(out / "facts/news.csv",
                  ["seen_date", "site", "price_related", "title", "description", "url",
                   "news_source", "seen_at"], articles)
    else:
        articles = read_csv(out / "facts/news.csv", required=False)

    if (src / PRIVATE_CARS_REL).exists():
        write_csv(out / "facts/private_cars_se.csv",
                  ["date", "country", "site", "segment", "metric", "band", "value", "run_timestamp"],
                  ({"date": monday, "country": "SE", "site": PRIVATE_CARS_SITE.get(r["site"], r["site"]),
                    "segment": "private", "metric": r["metric"], "band": r["band"],
                    "value": fmt(num(r["value"])), "run_timestamp": r["run_timestamp"]}
                   for monday, rows in private_cars_runs(src) for r in rows))

    for rel, name in (("vend-price-monitor/data/price_list_latest.csv", "price_list_latest.csv"),
                      ("finn-bolig-packages/data/package_prices.csv", "finn_homes_package_prices.csv"),
                      ("finn-bolig-packages/data/geo_zone_summary.csv", "finn_homes_geo_zone_latest.csv")):
        p = src / rel
        if p.exists():
            (out / "reference").mkdir(parents=True, exist_ok=True)
            shutil.copyfile(p, out / "reference" / name)
        else:
            missing.append(str(p))

    daily_dates = [r["date"] for r in listings if r["grain"] == "daily"]
    as_of = date.fromisoformat(max(daily_dates)) if daily_dates else now.date()
    digest = build_digest(listings, price_changes, articles, events, as_of, now)
    (out / "digest").mkdir(parents=True, exist_ok=True)
    (out / "digest/latest.md").write_text(digest, encoding="utf-8")

    print(f"listings rows: {n}, price states: {len(price_hist)}, price changes: "
          f"{len(price_changes)}, articles: {len(articles)}, data up to {as_of}")
    for m in missing:
        print(f"[WARN] missing input: {m}", file=sys.stderr)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--sources", default="sources")
    ap.add_argument("--out", default=".")
    a = ap.parse_args()
    build(Path(a.sources), Path(a.out))


if __name__ == "__main__":
    main()
