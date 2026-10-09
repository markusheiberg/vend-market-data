# Vend market data: catalog

This repo is the one place to read everything the Vend scrapers collect. It is
rebuilt every morning from four source repos and contains no scraping code of its
own. **Read `digest/latest.md` first, then `events.csv` before trusting any jump.**

| file | grain | what |
|---|---|---|
| `digest/latest.md` | snapshot | what moved, what broke, price changes and news, last 30 days |
| `events.csv` | one row per known event | outages, glitches, methodology breaks, fixed bugs. Hand-maintained |
| `facts/listings.csv` | one row per series × date × metric | every count series, in one long table |
| `facts/listings_weekly.csv` | one row per series × ISO week × metric | the same at a weekly grain, ~39k tokens: **the file a Claude project holds**. Daily series = mean of clean days (stock needs 2, new listings 4, as the BigQuery `weekly_avg` view); weekly series pass through; dates are Mondays; `valid_days` says how many days fed the mean |
| `facts/prices.csv` | one row per price-row state | price lists over time: `new`, `changed`, `removed` |
| `facts/price_changes.csv` | one row per changed price field | old, new, % change |
| `facts/news.csv` | one row per article | B2B blog posts from finn and blocket |
| `reference/price_list_latest.csv` | one row per price | every tracked price list today |
| `reference/finn_homes_package_prices.csv` | year × zone × package × band | what finn charges for a home listing (typed in, validated) |
| `reference/finn_homes_geo_zone_latest.csv` | zone × price band | latest finn used-home listings by geo zone and price band |

## `facts/listings.csv`

| column | meaning |
|---|---|
| `date` | ISO date. Daily series: the scrape date (Oslo). Weekly series: the **Monday** of the ISO week |
| `grain` | `daily`, `weekly` or `point` (one-off manual observation) |
| `country`, `site` | `NO`/`SE`/`DK`/`FI`/`FR` and the domain, e.g. `finn.no` |
| `vertical` | `mobility_cars`, `mobility_other`, `real_estate_homes`, `real_estate_homes_new`, `real_estate_homes_upcoming`, `real_estate_other`, `jobs_positions`, `jobs_listings` |
| `segment` | `dealer`, `private`, or blank (no seller split) |
| `package` | package name for package metrics, else blank |
| `metric` | see below |
| `value` | the number |
| `unit` | `listings`, `pct`, `sampled_listings`, `fraction`, `visitors`, `days`, `cars_per_week` |
| `is_sample` | `1` when the value comes from a sample and is not a market total |
| `quality_flag` | blank = clean. `interpolated` = no report that week, filled on a straight line (bilinfo only; fine for trends). `outlier` = upstream filter blanked it, raw value kept. `manual` = typed in. `exclude:E##` = covered by an exclude event |
| `source` | source repo and file |

Metrics:

| metric | sites | meaning |
|---|---|---|
| `listings` | all daily sites | live listing stock |
| `new_listings` | finn.no, blocket.se, hemnet.se (for-sale only), oikotie.fi, etuovi.com | listings published that day |
| `package_share` | finn.no, blocket.se cars (dealer); finn.no used homes | % of listings on each package |
| `package_sample_count` | finn.no, blocket.se cars (dealer) | sampled listings per package. **A sample, not a market count** |
| `package_count` | finn.no used homes | listings per package, full crawl |
| `sample_fraction` | finn.no, blocket.se cars (dealer) | share of listings the car package scrape classified that week: 0.05 until 2026-07-20, 0.10 since. Compare `package_sample_count` only between weeks with the same value |
| `visits`, `supply_cars`, `avg_days_to_sell` | bilinfo.dk | bilinfo's weekly report on the Danish dealer market (Bilbasen). Stock and days to sell are filled across weeks with no report by straight-line interpolation, flagged `interpolated`; visits are not |
| `implied_cars_sold` | bilinfo.dk | estimate, cars per week: `supply_cars` × 7 / `avg_days_to_sell` (stock turns over once per days-to-sell) |
| `implied_cars_added` | bilinfo.dk | estimate, cars per week: next week's `supply_cars` − this week's + `implied_cars_sold` (stock only changes by what comes in minus what goes out). Missing for the latest week until the next report |

## Rules that are easy to get wrong

- **For trends, keep `quality_flag` blank or `interpolated`.** Keep `outlier` rows if a series
  is trending: the upstream filter compares against the all-time mean, so a
  steady seasonal move eventually gets blanked (see E16).
- **finn.no `real_estate_homes` is USED homes only, on purpose.** It is the revenue
  signal. `real_estate_homes_new` is context. Do not add them by default.
- **leboncoin.fr has a `total` segment that overlaps `dealer` + `private`.** Never
  sum segments for that site. It is also only two manual points (E12).
- **Car package counts are a sample** (`is_sample=1`) and doubled on 2026-07-20 when
  the sample went from 5% to 10% (E07). Use `package_share` for trends.
- **Package names differ by vertical.** Cars: premium / pluss / basis. Homes:
  large / medium / small (finn's Stor / Medium / Liten).
- **bilinfo's implied sold and added are estimates.** Days to sell is reported in
  whole days, so a one-day change moves implied sold by about 2%; read them as a
  trend over several weeks, not week to week. Both assume the stock figure is the
  stock at the start of the week.
- **Weekly dates are Mondays.** A run on Sunday 2026-10-04 is dated 2026-09-28.
  finn homes package rows are the exception: they carry the run date.
- **Prices are in the site's own currency** (`currency` column) despite the
  `price_*_nok` column names, and ex. VAT for finn.
- **Price history starts 2026-07-12** (E08). A new year's price list shows as
  `removed` + `new` rows, not changes, because `year` is part of the identity.

## `events.csv`

| column | meaning |
|---|---|
| `id` | `E##`, referenced from `quality_flag` |
| `date_from`, `date_to` | inclusive. Blank `date_to` = ongoing |
| `site`, `vertical`, `segment`, `metric` | which rows it covers. `*`, blank or a glob (`jobs_*`) matches all |
| `kind` | `outage`, `glitch`, `methodology`, `new_series`, `fixed`, `blocked`, `filter`, `coverage`, `duplicate` |
| `flag` | `exclude` = values are wrong, tagged in facts. `break` = do not compare across this date. `info` = context |
| `summary`, `source` | what happened, and where it is documented |

Add a row when you find something new. A new `exclude` event is applied to the
facts on the next build.

## Where it comes from

| source repo | cadence | feeds |
|---|---|---|
| `vend-scraper-v2` | daily scrape 23:50 Oslo, exported ~23:00–03:00 UTC | daily listings, bilinfo weekly, leboncoin manual |
| `finn-mobility-packages` | weekly, Sunday night | car package mix |
| `finn-bolig-packages` | weekly, Sunday night | home package mix, geo grid, finn home prices |
| `vend-price-monitor` | daily 06:00 Oslo, exported 18:30 UTC | price lists, news |

Each source repo's own `data/health.md` and `CLAUDE.md` hold the detail. This
repo copies; it never edits upstream numbers. The only transformations are
reshaping to the long format, choosing the filtered over the raw daily value
(keeping the raw one when the filter blanked it), keeping the later of two
same-day finn homes runs, and tagging `exclude` events.
