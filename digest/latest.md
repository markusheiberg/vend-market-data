# Vend market digest

Generated 2026-10-27 10:30 UTC. Data up to **2026-10-26**.
Read `CATALOG.md` for what each series means and `events.csv` before trusting a jump.

## Series with no value today

- biltorvet.dk · mobility_cars · dealer · listings
- biltorvet.dk · mobility_cars · private · listings
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
| bilbasen.dk | mobility_cars | dealer | 47 815 | 2026-10-26 | +1.1% | +0.8% |
| bilbasen.dk | mobility_cars | private | 4 399 | 2026-10-26 | +0.1% | +6.5% |
| bilhandel.dk | mobility_cars | dealer | 27 686 | 2026-10-26 | +0.6% | +4.7% |
| bilhandel.dk | mobility_cars | private | 2 098 | 2026-10-26 | -7.1% | -3.5% |
| biltorvet.dk | mobility_cars | dealer | 44 631 | 2026-10-20 ⚠️ |  |  |
| biltorvet.dk | mobility_cars | private | 2 284 | 2026-10-20 ⚠️ |  |  |
| blocket.se | mobility_cars | dealer | 126 829 | 2026-10-26 | +0.7% | +3.3% |
| blocket.se | mobility_cars | private | 26 531 | 2026-10-26 | +0.6% | +2.2% |
| blocket.se | mobility_other | dealer | 62 910 | 2026-10-26 | +0.1% | -1.3% |
| blocket.se | mobility_other | private | 14 648 | 2026-10-26 | -9.1% | -28.8% |
| etuovi.com | real_estate_homes | - | 51 801 | 2026-10-26 | -0.2% | -1.4% |
| finn.no | jobs_listings | - | 13 524 | 2026-10-26 | -1.4% | -7.0% |
| finn.no | jobs_positions | - | 27 449 | 2026-10-26 | -1.4% | -6.4% |
| finn.no | mobility_cars | dealer | 54 540 | 2026-10-26 | +1.1% | +3.8% |
| finn.no | mobility_cars | private | 19 122 | 2026-10-26 | +1.7% | +5.6% |
| finn.no | mobility_other | dealer | 28 984 | 2026-10-26 | +1.7% | +7.6% |
| finn.no | mobility_other | private | 9 218 | 2026-10-26 | -7.3% | -26.8% |
| finn.no | real_estate_homes | - | 22 361 | 2026-10-26 | -0.5% | -0.3% |
| finn.no | real_estate_homes_new | - | 17 426 | 2026-10-26 | -0.1% | -3.4% |
| finn.no | real_estate_other | - | 26 274 | 2026-10-26 | -0.7% | -0.5% |
| hemnet.se | real_estate_homes | - | 41 229 | 2026-10-25 |  | +16.0% |
| hemnet.se | real_estate_homes_upcoming | - | 5 723 | 2026-10-05 ⚠️ |  |  |
| hjem.no | real_estate_homes | - | 8 699 | 2026-10-26 | -0.7% | -0.6% |
| oikotie.fi | real_estate_homes | - | 47 499 | 2026-10-26 | -0.1% | -1.2% |
| tradera.com | mobility_cars | dealer | 51 021 | 2026-10-26 | +1.5% | +8.2% |
| tradera.com | mobility_cars | private | 3 180 | 2026-10-26 | +3.1% | +6.6% |
| wayke.se | mobility_cars | dealer | 53 039 | 2026-10-08 ⚠️ |  |  |

## Package mix

Shares in %. Car packages are a 10% sample of dealer listings; finn homes is a
full crawl of used homes.

| site | vertical | latest week | mix now | mix 4 runs earlier |
|---|---|---|---|---|
| blocket.se | mobility_cars | 2026-10-19 | basis 67.0 / pluss 1.9 / premium 31.1 | basis 66.2 / pluss 3.3 / premium 30.6 |
| finn.no | mobility_cars | 2026-10-19 | basis 35.2 / pluss 23.9 / premium 40.9 | basis 33.3 / pluss 24.4 / premium 42.3 |
| finn.no | real_estate_homes | 2026-10-25 | large 63.4 / medium 33.5 / small 3.1 | large 62.1 / medium 35.0 / small 2.9 |

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
- 2026-10-26 · www.finn.no · [Priser fra 1. juni 2026](https://www.finn.no/bedriftskunde/motor/priser/priser-subvertikaler#notice-33c72f53d5f0)
- 2026-10-26 · www.blocket.se · [Den 1 februari 2027 får annonspaketen nya priser. Läs mer och räkna ut era priser för 2027 här .](https://www.blocket.se/for-foretag/fordon/annonspaket-priser-och-rabattstruktur-foer-2027)
- 2026-10-26 · www.blocket.se · [Den 1 februari 2027 får annonspaketen nya priser. Läs mer och räkna ut era priser för 2027 här .](https://www.blocket.se/for-foretag/fordon/annonspaket#notice-7bb8f67210dc)
- 2026-10-26 · www.blocket.se · [Den 1 februari 2027 får annonspaketen Bas, Plus och Premium för bilar och transportbilar nya priser. Läs mer och räkna ut era priser för 2027 här .](https://www.blocket.se/for-foretag/fordon/priser#notice-578e5425038a)
- 2026-10-26 · www.finn.no · [Priser 2027](https://www.finn.no/bedriftskunde/motor/pakker-priser-og-rabatter-for-2027)
- 2026-10-26 · www.finn.no · [Annonsepakkene på FINN motor er derfor utviklet i samarbeid med bransjen, for å sikre at dere får elementene som er viktige for dere. Her ser du våre pakker og priser for bil fra 1. juni 2026.](https://www.finn.no/bedriftskunde/motor/priser/priser-bilannonsering#notice-91d5be82e9b8)

## Data events touching the last 30 days

- **E12** 2026-09-02→ongoing · leboncoin.fr mobility_cars · info: DataDome blocks the scraper and robots.txt disallows the path. Only two manual observations exist; the series is not tracked.
- **E14** 2026-09-26→2026-10-08 · hemnet.se real_estate_homes* · info: Cloudflare challenges intermittently NULL either hemnet count (2026-09-26 and 2026-10-06 to 10-08).
- **E15** 2026-10-02→2026-10-03 · finn.no jobs · exclude: All 8 finn_jobb prices read 10 000 kr on 2026-10-02 and reverted on 2026-10-03: a calculator placeholder, not a price change. Both days are excluded; the net change is zero.
- **E16** 2026-10-06→2026-10-08 · * * · info: Upstream outlier filter (all-time mean ± 3 std dev) blanked genuine values on trending series: biltorvet.dk cars private and blocket.se mobility_other private, 2026-10-06 to 10-08. Fixed 2026-10-09 (vend-scraper-v2 PR #11): a stock value is now blanked only if it is also a sudden break from its recent level. The values reappear in the next export.
