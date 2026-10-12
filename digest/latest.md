# Vend market digest

Generated 2026-10-12 13:08 UTC. Data up to **2026-10-11**.
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
| bilbasen.dk | mobility_cars | dealer | 47 352 | 2026-10-11 | -0.1% | +0.1% |
| bilbasen.dk | mobility_cars | private | 4 366 | 2026-10-11 | +1.8% | +8.0% |
| bilhandel.dk | mobility_cars | dealer | 27 452 | 2026-10-11 | +2.4% | +5.1% |
| bilhandel.dk | mobility_cars | private | 2 253 | 2026-10-11 | +1.9% | +5.8% |
| biltorvet.dk | mobility_cars | dealer | 44 591 | 2026-10-11 | +0.7% | +2.0% |
| biltorvet.dk | mobility_cars | private | 2 142 | 2026-10-11 | +5.4% | +23.6% |
| blocket.se | mobility_cars | dealer | 125 034 | 2026-10-11 | +1.3% | +3.3% |
| blocket.se | mobility_cars | private | 26 499 | 2026-10-11 | +0.8% | +4.7% |
| blocket.se | mobility_other | dealer | 62 763 | 2026-10-11 | -0.9% | +1.1% |
| blocket.se | mobility_other | private | 17 856 | 2026-10-11 | -8.0% | -22.7% |
| etuovi.com | real_estate_homes | - | 51 998 | 2026-10-11 | -0.5% | -1.2% |
| finn.no | jobs_listings | - | 14 260 | 2026-10-11 | -1.7% | -3.5% |
| finn.no | jobs_positions | - | 28 641 | 2026-10-11 | -1.7% | -2.8% |
| finn.no | mobility_cars | dealer | 53 084 | 2026-10-11 | +1.2% | +2.8% |
| finn.no | mobility_cars | private | 18 660 | 2026-10-11 | +1.5% | +4.3% |
| finn.no | mobility_other | dealer | 27 744 | 2026-10-11 | +2.0% | +5.4% |
| finn.no | mobility_other | private | 10 859 | 2026-10-11 | -7.8% | -25.7% |
| finn.no | real_estate_homes | - | 22 720 | 2026-10-11 | +1.2% | -1.7% |
| finn.no | real_estate_homes_new | - | 17 831 | 2026-10-11 | -0.5% | -0.9% |
| finn.no | real_estate_other | - | 26 677 | 2026-10-11 | +0.7% | +0.7% |
| hemnet.se | real_estate_homes | - | 39 940 | 2026-10-10 | +11.6% | +9.2% |
| hemnet.se | real_estate_homes_upcoming | - | 5 723 | 2026-10-05 ⚠️ |  |  |
| hjem.no | real_estate_homes | - | 8 843 | 2026-10-11 | +1.3% | -1.6% |
| oikotie.fi | real_estate_homes | - | 47 683 | 2026-10-11 | -0.4% | -1.2% |
| tradera.com | mobility_cars | dealer | 49 300 | 2026-10-11 | +2.5% | +8.7% |
| tradera.com | mobility_cars | private | 3 035 | 2026-10-11 | +1.0% | +8.3% |
| wayke.se | mobility_cars | dealer | 53 039 | 2026-10-08 ⚠️ | +1.2% | +3.5% |

## Package mix

Shares in %. Car packages are a 10% sample of dealer listings; finn homes is a
full crawl of used homes.

| site | vertical | latest week | mix now | mix 4 runs earlier |
|---|---|---|---|---|
| blocket.se | mobility_cars | 2026-09-28 | basis 67.2 / pluss 2.6 / premium 30.2 | basis 64.3 / pluss 5.1 / premium 30.6 |
| finn.no | mobility_cars | 2026-09-28 | basis 34.5 / pluss 25.3 / premium 40.2 | basis 32.3 / pluss 26.5 / premium 41.2 |
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
