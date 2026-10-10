# Vend market digest

Generated 2026-10-10 11:09 UTC. Data up to **2026-10-09**.
Read `CATALOG.md` for what each series means and `events.csv` before trusting a jump.

## Series with no value today

- hemnet.se · real_estate_homes · - · listings
- hemnet.se · real_estate_homes_upcoming · - · listings
- wayke.se · mobility_cars · dealer · listings

## Listings stock (daily series)

7-day average against the previous 7 days, and against the same window 4 weeks
earlier. Event-excluded values are left out. † = latest value was blanked by the
outlier filter (raw shown). ⚠️ = latest value older than a day.

| site | vertical | segment | latest | date | 7d vs prior 7d | vs 4 weeks ago |
|---|---|---|---:|---|---:|---:|
| bilbasen.dk | mobility_cars | dealer | 48 024 | 2026-10-09 | -0.1% | +0.4% |
| bilbasen.dk | mobility_cars | private | 4 296 | 2026-10-09 | +2.0% | +8.4% |
| bilhandel.dk | mobility_cars | dealer | 27 854 | 2026-10-09 | +3.0% | +5.5% |
| bilhandel.dk | mobility_cars | private | 2 224 | 2026-10-09 | +1.8% | +5.8% |
| biltorvet.dk | mobility_cars | dealer | 45 183 | 2026-10-09 | +1.0% | +2.2% |
| biltorvet.dk | mobility_cars | private | 2 105 | 2026-10-09 | +5.4% | +22.9% |
| blocket.se | mobility_cars | dealer | 126 097 | 2026-10-09 | +1.0% | +3.4% |
| blocket.se | mobility_cars | private | 26 641 | 2026-10-09 | +1.5% | +5.0% |
| blocket.se | mobility_other | dealer | 63 022 | 2026-10-09 | -0.4% | +1.7% |
| blocket.se | mobility_other | private | 18 305 | 2026-10-09 | -7.6% | -21.5% |
| etuovi.com | real_estate_homes | - | 52 061 | 2026-10-09 | -0.6% | -1.1% |
| finn.no | jobs_listings | - | 14 787 | 2026-10-09 | -3.6% | -2.6% |
| finn.no | jobs_positions | - | 29 606 | 2026-10-09 | -3.9% | -1.9% |
| finn.no | mobility_cars | dealer | 54 325 | 2026-10-09 | +0.8% | +2.6% |
| finn.no | mobility_cars | private | 18 390 | 2026-10-09 | +1.4% | +4.2% |
| finn.no | mobility_other | dealer | 27 980 | 2026-10-09 | +1.8% | +4.8% |
| finn.no | mobility_other | private | 11 066 | 2026-10-09 | -7.6% | -25.1% |
| finn.no | real_estate_homes | - | 23 100 | 2026-10-09 | +0.4% | -1.7% |
| finn.no | real_estate_homes_new | - | 17 895 | 2026-10-09 | -0.4% | -0.8% |
| finn.no | real_estate_other | - | 27 050 | 2026-10-09 | +0.7% | +0.4% |
| hemnet.se | real_estate_homes | - | 39 715 | 2026-10-07 ⚠️ | +6.0% | +3.8% |
| hemnet.se | real_estate_homes_upcoming | - | 5 723 | 2026-10-05 ⚠️ |  |  |
| hjem.no | real_estate_homes | - | 8 948 | 2026-10-09 | +0.6% | -1.3% |
| oikotie.fi | real_estate_homes | - | 47 699 | 2026-10-09 | -0.6% | -1.1% |
| tradera.com | mobility_cars | dealer | 49 844 | 2026-10-09 | +2.4% | +8.6% |
| tradera.com | mobility_cars | private | 3 010 | 2026-10-09 | +1.1% | +8.4% |
| wayke.se | mobility_cars | dealer | 53 039 | 2026-10-08 | +0.8% | +3.9% |

## Package mix

Shares in %. Car packages are a 10% sample of dealer listings; finn homes is a
full crawl of used homes.

| site | vertical | latest week | mix now | mix 4 runs earlier |
|---|---|---|---|---|
| blocket.se | mobility_cars | 2026-09-28 | basis 67.2 / pluss 2.6 / premium 30.2 | basis 64.3 / pluss 5.1 / premium 30.6 |
| finn.no | mobility_cars | 2026-09-28 | basis 34.5 / pluss 25.3 / premium 40.2 | basis 32.3 / pluss 26.5 / premium 41.2 |
| finn.no | real_estate_homes | 2026-10-04 | large 62.7 / medium 34.3 / small 3.0 | large 61.7 / medium 35.4 / small 2.9 |

## Danish dealer market (bilinfo, weekly)

Cars per week. Implied sold = last week's stock x 7 / adjusted days to sell;
implied added = change in stock + sold. Adjusted days put the history on one
basis across bilinfo's 2026-06-08 definition change (E17), as the bilinfo
workbook does. Days are whole numbers, so one day moves sold by ~2%.
* = a week with no report, interpolated.

| week | stock | adj. days to sell | implied sold | implied added |
|---|---:|---:|---:|---:|
| 2026-08-24 | 51 200 | 56 | 6 362 | 6 662 |
| 2026-08-31 | 51 400 | 56 | 6 400 | 6 600 |
| 2026-09-07 | 51 600 | 57 | 6 312 | 6 512 |
| 2026-09-14 | 51 800 | 57 | 6 337 | 6 537 |
| 2026-09-21 | 51 600 | 57 | 6 361 | 6 161 |
| 2026-09-28 | 51 400 | 57 | 6 337 | 6 137 |

## Price changes, last 30 days

None (excluding glitches listed in `events.csv`).

## Price-related news, last 30 days

- 2026-10-01 · www.finn.no · [Tesla Model 3 og Rebil tok prisene i Årets bruktbil 2026!](https://www.finn.no/bedriftskunde/aktuelt/finn-motor/arets-bruktbil-2026)

## Data events touching the last 30 days

- **E12** 2026-09-02→ongoing · leboncoin.fr mobility_cars · info: DataDome blocks the scraper and robots.txt disallows the path. Only two manual observations exist; the series is not tracked.
- **E13** 2026-09-15→2026-09-17 · hemnet.se real_estate_homes · info: Cloudflare bot challenge (HTTP 403) on the filtered page; new listings NULL three nights.
- **E14** 2026-09-26→2026-10-08 · hemnet.se real_estate_homes* · info: Cloudflare challenges intermittently NULL either hemnet count (2026-09-26 and 2026-10-06 to 10-08).
- **E15** 2026-10-02→2026-10-03 · finn.no jobs · exclude: All 8 finn_jobb prices read 10 000 kr on 2026-10-02 and reverted on 2026-10-03: a calculator placeholder, not a price change. Both days are excluded; the net change is zero.
- **E16** 2026-10-06→2026-10-08 · * * · info: Upstream outlier filter (all-time mean ± 3 std dev) blanked genuine values on trending series: biltorvet.dk cars private and blocket.se mobility_other private, 2026-10-06 to 10-08. Fixed 2026-10-09 (vend-scraper-v2 PR #11): a stock value is now blanked only if it is also a sudden break from its recent level. The values reappear in the next export.
