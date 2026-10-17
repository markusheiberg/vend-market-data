# Vend market digest

Generated 2026-10-17 09:19 UTC. Data up to **2026-10-16**.
Read `CATALOG.md` for what each series means and `events.csv` before trusting a jump.

## Series with no value today

- hemnet.se · real_estate_homes · - · listings
- hemnet.se · real_estate_homes · - · new_listings
- hemnet.se · real_estate_homes_upcoming · - · listings
- wayke.se · mobility_cars · dealer · listings

## Listings stock (daily series)

7-day average against the previous 7 days, and against the same window 4 weeks
earlier. Event-excluded values are left out. † = latest value was blanked by the
outlier filter (raw shown). ⚠️ = latest value older than a day.

| site | vertical | segment | latest | date | 7d vs prior 7d | vs 4 weeks ago |
|---|---|---|---:|---|---:|---:|
| bilbasen.dk | mobility_cars | dealer | 47 747 | 2026-10-16 | -0.2% | -0.2% |
| bilbasen.dk | mobility_cars | private | 4 407 | 2026-10-16 | +1.9% | +8.0% |
| bilhandel.dk | mobility_cars | dealer | 27 744 | 2026-10-16 | +0.7% | +4.2% |
| bilhandel.dk | mobility_cars | private | 2 278 | 2026-10-16 | +1.7% | +6.1% |
| biltorvet.dk | mobility_cars | dealer | 44 912 | 2026-10-16 | -0.1% | +1.4% |
| biltorvet.dk | mobility_cars | private | 2 235 | 2026-10-16 | +5.7% | +25.8% |
| blocket.se | mobility_cars | dealer | 127 278 | 2026-10-16 | +1.2% | +3.1% |
| blocket.se | mobility_cars | private | 26 315 | 2026-10-16 | -0.9% | +3.3% |
| blocket.se | mobility_other | dealer | 63 214 | 2026-10-16 | -1.4% | +0.0% |
| blocket.se | mobility_other | private | 16 782 | 2026-10-16 | -8.5% | -25.2% |
| etuovi.com | real_estate_homes | - | 52 041 | 2026-10-16 | -0.1% | -1.2% |
| finn.no | jobs_listings | - | 14 510 | 2026-10-16 | -0.3% | -5.2% |
| finn.no | jobs_positions | - | 28 989 | 2026-10-16 | +1.0% | -3.7% |
| finn.no | mobility_cars | dealer | 54 865 | 2026-10-16 | +1.3% | +3.1% |
| finn.no | mobility_cars | private | 18 523 | 2026-10-16 | +1.2% | +4.5% |
| finn.no | mobility_other | dealer | 28 713 | 2026-10-16 | +2.3% | +6.8% |
| finn.no | mobility_other | private | 10 231 | 2026-10-16 | -7.8% | -26.6% |
| finn.no | real_estate_homes | - | 23 207 | 2026-10-16 | +1.2% | -1.9% |
| finn.no | real_estate_homes_new | - | 17 455 | 2026-10-16 | -1.9% | -2.6% |
| finn.no | real_estate_other | - | 26 634 | 2026-10-16 | -0.4% | +0.6% |
| hemnet.se | real_estate_homes | - | 39 033 | 2026-10-14 ⚠️ | +7.8% | +12.2% |
| hemnet.se | real_estate_homes_upcoming | - | 5 723 | 2026-10-05 ⚠️ |  |  |
| hjem.no | real_estate_homes | - | 8 983 | 2026-10-16 | +1.1% | -2.5% |
| oikotie.fi | real_estate_homes | - | 47 636 | 2026-10-16 | -0.1% | -1.1% |
| tradera.com | mobility_cars | dealer | 50 675 | 2026-10-16 | +2.4% | +8.0% |
| tradera.com | mobility_cars | private | 3 031 | 2026-10-16 | +0.8% | +7.1% |
| wayke.se | mobility_cars | dealer | 53 039 | 2026-10-08 ⚠️ |  |  |

## Package mix

Shares in %. Car packages are a 10% sample of dealer listings; finn homes is a
full crawl of used homes.

| site | vertical | latest week | mix now | mix 4 runs earlier |
|---|---|---|---|---|
| blocket.se | mobility_cars | 2026-10-05 | basis 68.4 / pluss 2.0 / premium 29.6 | basis 66.3 / pluss 2.4 / premium 31.3 |
| finn.no | mobility_cars | 2026-10-05 | basis 33.9 / pluss 23.4 / premium 42.7 | basis 31.0 / pluss 28.9 / premium 40.1 |
| finn.no | real_estate_homes | 2026-10-11 | large 62.8 / medium 34.2 / small 3.0 | large 61.6 / medium 35.6 / small 2.8 |

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
