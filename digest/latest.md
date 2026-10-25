# Vend market digest

Generated 2026-10-25 09:47 UTC. Data up to **2026-10-24**.
Read `CATALOG.md` for what each series means and `events.csv` before trusting a jump.

## Series with no value today

- biltorvet.dk · mobility_cars · dealer · listings
- biltorvet.dk · mobility_cars · private · listings
- hemnet.se · real_estate_homes · - · listings
- hemnet.se · real_estate_homes_upcoming · - · listings
- wayke.se · mobility_cars · dealer · listings

## Listings stock (daily series)

7-day average against the previous 7 days, and against the same window 4 weeks
earlier. Event-excluded values are left out. † = latest value was blanked by the
outlier filter (raw shown). ⚠️ = latest value older than a day.

| site | vertical | segment | latest | date | 7d vs prior 7d | vs 4 weeks ago |
|---|---|---|---:|---|---:|---:|
| bilbasen.dk | mobility_cars | dealer | 48 371 | 2026-10-24 | +0.7% | +0.4% |
| bilbasen.dk | mobility_cars | private | 4 392 | 2026-10-24 | +1.4% | +7.7% |
| bilhandel.dk | mobility_cars | dealer | 27 904 | 2026-10-24 | +0.3% | +4.3% |
| bilhandel.dk | mobility_cars | private | 2 081 | 2026-10-24 | -6.5% | -1.9% |
| biltorvet.dk | mobility_cars | dealer | 44 631 | 2026-10-20 ⚠️ |  |  |
| biltorvet.dk | mobility_cars | private | 2 284 | 2026-10-20 ⚠️ |  |  |
| blocket.se | mobility_cars | dealer | 127 137 | 2026-10-24 | +0.7% | +3.2% |
| blocket.se | mobility_cars | private | 26 605 | 2026-10-24 | +0.7% | +2.7% |
| blocket.se | mobility_other | dealer | 63 057 | 2026-10-24 | +0.2% | -1.0% |
| blocket.se | mobility_other | private | 15 016 | 2026-10-24 | -8.8% | -28.2% |
| etuovi.com | real_estate_homes | - | 51 945 | 2026-10-24 | -0.2% | -1.4% |
| finn.no | jobs_listings | - | 13 967 | 2026-10-24 | -1.7% | -6.6% |
| finn.no | jobs_positions | - | 28 068 | 2026-10-24 | -2.3% | -6.2% |
| finn.no | mobility_cars | dealer | 55 111 | 2026-10-24 | +1.0% | +3.5% |
| finn.no | mobility_cars | private | 18 919 | 2026-10-24 | +1.9% | +5.8% |
| finn.no | mobility_other | dealer | 29 101 | 2026-10-24 | +2.0% | +7.5% |
| finn.no | mobility_other | private | 9 326 | 2026-10-24 | -6.9% | -26.6% |
| finn.no | real_estate_homes | - | 22 849 | 2026-10-24 | -0.3% | -0.7% |
| finn.no | real_estate_homes_new | - | 17 438 | 2026-10-24 | -0.6% | -3.6% |
| finn.no | real_estate_other | - | 26 256 | 2026-10-24 | -0.8% | -0.1% |
| hemnet.se | real_estate_homes | - | 40 966 | 2026-10-23 |  | +13.7% |
| hemnet.se | real_estate_homes_upcoming | - | 5 723 | 2026-10-05 ⚠️ |  |  |
| hjem.no | real_estate_homes | - | 8 841 | 2026-10-24 | -0.2% | -1.0% |
| oikotie.fi | real_estate_homes | - | 47 631 | 2026-10-24 | -0.1% | -1.2% |
| tradera.com | mobility_cars | dealer | 50 894 | 2026-10-24 | +1.4% | +8.1% |
| tradera.com | mobility_cars | private | 3 174 | 2026-10-24 | +2.2% | +6.2% |
| wayke.se | mobility_cars | dealer | 53 039 | 2026-10-08 ⚠️ |  |  |

## Package mix

Shares in %. Car packages are a 10% sample of dealer listings; finn homes is a
full crawl of used homes.

| site | vertical | latest week | mix now | mix 4 runs earlier |
|---|---|---|---|---|
| blocket.se | mobility_cars | 2026-10-12 | basis 67.6 / pluss 1.9 / premium 30.5 | basis 67.6 / pluss 2.1 / premium 30.4 |
| finn.no | mobility_cars | 2026-10-12 | basis 34.4 / pluss 23.6 / premium 42.0 | basis 33.8 / pluss 23.5 / premium 42.7 |
| finn.no | real_estate_homes | 2026-10-18 | large 63.1 / medium 33.9 / small 3.0 | large 61.5 / medium 35.7 / small 2.8 |

## Danish dealer market (bilinfo, weekly)

Cars per week. Implied sold = last week's stock x 7 / adjusted days to sell;
implied added = change in stock + sold. Adjusted days put the history on one
basis across bilinfo's 2026-06-08 definition change (E17), as the bilinfo
workbook does. Days are whole numbers, so one day moves sold by ~2%.
* = a week with no report, interpolated.

| week | stock | adj. days to sell | implied sold | implied added |
|---|---:|---:|---:|---:|
| 2026-09-07 | 51 600 | 57 | 6 312 | 6 512 |
| 2026-09-14 | 51 800 | 57 | 6 337 | 6 537 |
| 2026-09-21 | 51 600 | 57 | 6 361 | 6 161 |
| 2026-09-28 | 51 400 | 57 | 6 337 | 6 137 |
| 2026-10-05 * | 51 450 | 57 | 6 312 | 6 362 |
| 2026-10-12 * | 51 500 | 57 | 6 318 | 6 368 |

## Price changes, last 30 days

None (excluding glitches listed in `events.csv`).

## Price-related news, last 30 days

- 2026-10-01 · www.finn.no · [Tesla Model 3 og Rebil tok prisene i Årets bruktbil 2026!](https://www.finn.no/bedriftskunde/aktuelt/finn-motor/arets-bruktbil-2026)

## Data events touching the last 30 days

- **E12** 2026-09-02→ongoing · leboncoin.fr mobility_cars · info: DataDome blocks the scraper and robots.txt disallows the path. Only two manual observations exist; the series is not tracked.
- **E14** 2026-09-26→2026-10-08 · hemnet.se real_estate_homes* · info: Cloudflare challenges intermittently NULL either hemnet count (2026-09-26 and 2026-10-06 to 10-08).
- **E15** 2026-10-02→2026-10-03 · finn.no jobs · exclude: All 8 finn_jobb prices read 10 000 kr on 2026-10-02 and reverted on 2026-10-03: a calculator placeholder, not a price change. Both days are excluded; the net change is zero.
- **E16** 2026-10-06→2026-10-08 · * * · info: Upstream outlier filter (all-time mean ± 3 std dev) blanked genuine values on trending series: biltorvet.dk cars private and blocket.se mobility_other private, 2026-10-06 to 10-08. Fixed 2026-10-09 (vend-scraper-v2 PR #11): a stock value is now blanked only if it is also a sudden break from its recent level. The values reappear in the next export.
