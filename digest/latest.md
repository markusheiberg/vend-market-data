# Vend market digest

Generated 2026-11-28 14:09 UTC. Data up to **2026-11-27**.
Read `CATALOG.md` for what each series means and `events.csv` before trusting a jump.

## Series with no value today

- hemnet.se · real_estate_homes_incl_upcoming · - · listings

## Series blanked by the outlier filter today

The scrape returned a value but `daily_filtered` nulled it as >3 std dev from
the series' all-time mean. On a trending series that is usually a real move,
not a bad scrape: compare against the days before in `facts/listings.csv`.

- bilhandel.dk · mobility_cars · private · listings

## Listings stock (daily series)

7-day average against the previous 7 days, and against the same window 4 weeks
earlier. Event-excluded values are left out. † = latest value was blanked by the
outlier filter (raw shown). ⚠️ = latest value older than a day.

| site | vertical | segment | latest | date | 7d vs prior 7d | vs 4 weeks ago |
|---|---|---|---:|---|---:|---:|
| bilbasen.dk | mobility_cars | dealer | 51 192 | 2026-11-27 | +1.3% | +4.5% |
| bilbasen.dk | mobility_cars | private | 3 961 | 2026-11-27 | -4.7% | -7.1% |
| bilhandel.dk | mobility_cars | dealer | 28 571 | 2026-11-27 | +2.4% | +0.1% |
| bilhandel.dk | mobility_cars | private | 330 † | 2026-11-27 | -36.9% | -35.6% |
| biltorvet.dk | mobility_cars | dealer | 44 631 | 2026-10-20 ⚠️ |  |  |
| biltorvet.dk | mobility_cars | private | 2 284 | 2026-10-20 ⚠️ |  |  |
| blocket.se | mobility_cars | dealer | 134 948 | 2026-11-27 | +1.4% | +5.5% |
| blocket.se | mobility_cars | private | 24 788 | 2026-11-27 | -3.2% | -4.9% |
| blocket.se | mobility_other | dealer | 65 089 | 2026-11-27 | +0.4% | +2.7% |
| blocket.se | mobility_other | private | 9 920 | 2026-11-27 | -8.4% | -28.3% |
| etuovi.com | real_estate_homes | - | 50 304 | 2026-11-27 | -0.8% | -2.6% |
| finn.no | jobs_listings | - | 13 376 | 2026-11-27 | -3.8% | -5.3% |
| finn.no | jobs_positions | - | 27 386 | 2026-11-27 | -4.4% | -4.6% |
| finn.no | mobility_cars | dealer | 61 062 | 2026-11-27 | +1.8% | +8.4% |
| finn.no | mobility_cars | private | 17 488 | 2026-11-27 | -3.6% | -5.6% |
| finn.no | mobility_other | dealer | 29 821 | 2026-11-27 | -0.2% | +2.0% |
| finn.no | mobility_other | private | 6 136 | 2026-11-27 | -8.8% | -29.8% |
| finn.no | real_estate_homes | - | 20 276 | 2026-11-27 | -3.2% | -9.1% |
| finn.no | real_estate_homes_new | - | 17 342 | 2026-11-27 | +0.0% | -0.7% |
| finn.no | real_estate_other | - | 25 831 | 2026-11-27 | -0.7% | -1.0% |
| hemnet.se | real_estate_homes | - | 41 229 | 2026-10-25 ⚠️ |  |  |
| hemnet.se | real_estate_homes_incl_upcoming | - | 68 560 | 2026-11-21 ⚠️ |  |  |
| hemnet.se | real_estate_homes_upcoming | - | 5 723 | 2026-10-05 ⚠️ |  |  |
| hjem.no | real_estate_homes | - | 7 810 | 2026-11-27 | -3.0% | -9.5% |
| oikotie.fi | real_estate_homes | - | 46 252 | 2026-11-27 | +38.9% | -2.2% |
| tradera.com | mobility_cars | dealer | 55 455 | 2026-11-27 | +1.7% | +7.1% |
| tradera.com | mobility_cars | private | 3 213 | 2026-11-27 | -1.5% | +1.5% |
| wayke.se | mobility_cars | dealer | 53 039 | 2026-10-08 ⚠️ |  |  |

## Package mix

Shares in %. Car packages are a 10% sample of dealer listings; finn homes is a
full crawl of used homes.

| site | vertical | latest week | mix now | mix 4 runs earlier |
|---|---|---|---|---|
| blocket.se | mobility_cars | 2026-11-16 | basis 69.7 / pluss 0.7 / premium 29.6 | basis 67.0 / pluss 1.9 / premium 31.1 |
| finn.no | mobility_cars | 2026-11-16 | basis 33.9 / pluss 24.0 / premium 42.2 | basis 34.4 / pluss 23.6 / premium 42.0 |
| finn.no | real_estate_homes | 2026-11-22 | large 63.8 / medium 32.8 / small 3.4 | large 62.8 / medium 34.2 / small 3.0 |

## Danish dealer market (bilinfo, weekly)

Cars per week. Implied sold = last week's stock x 7 / adjusted days to sell;
implied added = change in stock + sold. Adjusted days put the history on one
basis across bilinfo's 2026-06-08 definition change (E17), as the bilinfo
workbook does. Days are whole numbers, so one day moves sold by ~2%.
* = a week with no report, interpolated.

| week | stock | adj. days to sell | implied sold | implied added |
|---|---:|---:|---:|---:|
| 2026-10-12 * | 51 500 | 57 | 6 318 | 6 368 |
| 2026-10-19 | 51 500 | 57 | 6 325 | 6 325 |
| 2026-10-26 | 51 700 | 57 | 6 325 | 6 525 |
| 2026-11-02 | 51 700 | 57 | 6 349 | 6 349 |
| 2026-11-09 | 51 700 | 57 | 6 349 | 6 349 |
| 2026-11-16 | 52 000 | 57 | 6 349 | 6 649 |

## Price changes, last 30 days

None (excluding glitches listed in `events.csv`).

## Price-related news, last 30 days

None.

## Data events touching the last 30 days

- **E12** 2026-09-02→ongoing · leboncoin.fr mobility_cars · info: DataDome blocks the scraper and robots.txt disallows the path. Only two manual observations exist; the series is not tracked.
- **E19** 2026-11-09→2026-11-18 · * * · info: vend-market-data build failed on all 10 scheduled runs 2026-11-09 to 11-18: package_table() raised on a blank package_share value from finn-mobility-packages week 2026-11-09 (finn 0/0/0 after finn refused every ad fetch with 403). facts/ and digest/ stayed at data up to 2026-11-07. Fixed 2026-11-19 (7b65649); rebuilt to data up to 2026-11-18 after the upstream zero rows were deleted.
- **E20** 2026-11-09→2026-11-15 · * mobility_cars · info: No Tradera vs Blocket private car census for the week of 2026-11-09: on 2026-11-15 22:59 UTC tradera.com answered the census's first request with 403 four times and the run wrote nothing. One-off in 30 days; vend-scraper-v2 read Tradera normally the same night. Not recoverable: the census is a point-in-time snapshot. finn-mobility-packages health.md now flags a missed census.
