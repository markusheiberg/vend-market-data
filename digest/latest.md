# Vend market digest

Generated 2026-11-22 13:18 UTC. Data up to **2026-11-21**.
Read `CATALOG.md` for what each series means and `events.csv` before trusting a jump.

## Series with no value today

- hemnet.se · real_estate_homes · - · listings
- hemnet.se · real_estate_homes · - · new_listings
- hemnet.se · real_estate_homes_incl_upcoming · - · new_listings

## Listings stock (daily series)

7-day average against the previous 7 days, and against the same window 4 weeks
earlier. Event-excluded values are left out. † = latest value was blanked by the
outlier filter (raw shown). ⚠️ = latest value older than a day.

| site | vertical | segment | latest | date | 7d vs prior 7d | vs 4 weeks ago |
|---|---|---|---:|---|---:|---:|
| bilbasen.dk | mobility_cars | dealer | 50 231 | 2026-11-21 | +1.8% | +4.0% |
| bilbasen.dk | mobility_cars | private | 4 127 | 2026-11-21 | -2.5% | -4.7% |
| bilhandel.dk | mobility_cars | dealer | 27 674 | 2026-11-21 | +2.5% | -1.1% |
| bilhandel.dk | mobility_cars | private | 2 102 | 2026-11-21 | -0.3% | +0.6% |
| biltorvet.dk | mobility_cars | dealer | 44 631 | 2026-10-20 ⚠️ |  |  |
| biltorvet.dk | mobility_cars | private | 2 284 | 2026-10-20 ⚠️ |  |  |
| blocket.se | mobility_cars | dealer | 133 310 | 2026-11-21 | +1.8% | +4.2% |
| blocket.se | mobility_cars | private | 25 538 | 2026-11-21 | -1.7% | -2.5% |
| blocket.se | mobility_other | dealer | 64 534 | 2026-11-21 | +0.3% | +2.3% |
| blocket.se | mobility_other | private | 10 835 | 2026-11-21 | -7.2% | -28.3% |
| etuovi.com | real_estate_homes | - | 50 792 | 2026-11-21 | -0.6% | -2.1% |
| finn.no | jobs_listings | - | 13 283 | 2026-11-21 | -2.5% | -2.9% |
| finn.no | jobs_positions | - | 26 632 | 2026-11-21 | -2.8% | -1.5% |
| finn.no | mobility_cars | dealer | 59 571 | 2026-11-21 | +2.0% | +8.1% |
| finn.no | mobility_cars | private | 18 024 | 2026-11-21 | -3.0% | -2.9% |
| finn.no | mobility_other | dealer | 29 864 | 2026-11-21 | +0.5% | +3.1% |
| finn.no | mobility_other | private | 6 598 | 2026-11-21 | -8.8% | -29.3% |
| finn.no | real_estate_homes | - | 20 848 | 2026-11-21 |  | -7.7% |
| finn.no | real_estate_homes_new | - | 17 226 | 2026-11-21 |  | -1.0% |
| finn.no | real_estate_other | - | 26 107 | 2026-11-21 |  | -0.9% |
| hemnet.se | real_estate_homes | - | 41 229 | 2026-10-25 ⚠️ |  |  |
| hemnet.se | real_estate_homes_incl_upcoming | - | 68 560 | 2026-11-21 |  |  |
| hemnet.se | real_estate_homes_upcoming | - | 5 723 | 2026-10-05 ⚠️ |  |  |
| hjem.no | real_estate_homes | - | 8 051 | 2026-11-21 | -2.7% | -8.5% |
| oikotie.fi | real_estate_homes | - | 46 774 | 2026-11-21 | +495.5% | -15.6% |
| tradera.com | mobility_cars | dealer | 54 535 | 2026-11-21 | +1.9% | +6.8% |
| tradera.com | mobility_cars | private | 3 249 | 2026-11-21 | +1.3% | +5.8% |
| wayke.se | mobility_cars | dealer | 53 039 | 2026-10-08 ⚠️ |  |  |

## Package mix

Shares in %. Car packages are a 10% sample of dealer listings; finn homes is a
full crawl of used homes.

| site | vertical | latest week | mix now | mix 4 runs earlier |
|---|---|---|---|---|
| blocket.se | mobility_cars | 2026-11-09 | basis 69.5 / pluss 0.6 / premium 29.9 | basis 67.6 / pluss 1.9 / premium 30.5 |
| finn.no | mobility_cars | 2026-11-02 | basis 34.3 / pluss 24.7 / premium 41.0 | basis 33.9 / pluss 23.4 / premium 42.7 |
| finn.no | real_estate_homes | 2026-11-01 | large 63.7 / medium 33.1 / small 3.2 | large 62.7 / medium 34.3 / small 3.0 |

## Danish dealer market (bilinfo, weekly)

Cars per week. Implied sold = last week's stock x 7 / adjusted days to sell;
implied added = change in stock + sold. Adjusted days put the history on one
basis across bilinfo's 2026-06-08 definition change (E17), as the bilinfo
workbook does. Days are whole numbers, so one day moves sold by ~2%.
* = a week with no report, interpolated.

| week | stock | adj. days to sell | implied sold | implied added |
|---|---:|---:|---:|---:|
| 2026-10-05 * | 51 450 | 57 | 6 312 | 6 362 |
| 2026-10-12 * | 51 500 | 57 | 6 318 | 6 368 |
| 2026-10-19 | 51 500 | 57 | 6 325 | 6 325 |
| 2026-10-26 | 51 700 | 57 | 6 325 | 6 525 |
| 2026-11-02 | 51 700 | 57 | 6 349 | 6 349 |
| 2026-11-09 | 51 700 | 57 | 6 349 | 6 349 |

## Price changes, last 30 days

None (excluding glitches listed in `events.csv`).

## Price-related news, last 30 days

- 2026-10-26 · www.finn.no · [Priser fra 1. juni 2026](https://www.finn.no/bedriftskunde/motor/priser/priser-subvertikaler#notice-33c72f53d5f0)
- 2026-10-26 · www.blocket.se · [Den 1 februari 2027 får annonspaketen nya priser. Läs mer och räkna ut era priser för 2027 här .](https://www.blocket.se/for-foretag/fordon/annonspaket-priser-och-rabattstruktur-foer-2027)
- 2026-10-26 · www.blocket.se · [Den 1 februari 2027 får annonspaketen nya priser. Läs mer och räkna ut era priser för 2027 här .](https://www.blocket.se/for-foretag/fordon/annonspaket#notice-7bb8f67210dc)
- 2026-10-26 · www.blocket.se · [Den 1 februari 2027 får annonspaketen Bas, Plus och Premium för bilar och transportbilar nya priser. Läs mer och räkna ut era priser för 2027 här .](https://www.blocket.se/for-foretag/fordon/priser#notice-578e5425038a)
- 2026-10-26 · www.finn.no · [Priser 2027](https://www.finn.no/bedriftskunde/motor/pakker-priser-og-rabatter-for-2027)
- 2026-10-26 · www.finn.no · [Annonsepakkene på FINN motor er derfor utviklet i samarbeid med bransjen, for å sikre at dere får elementene som er viktige for dere. Her ser du våre pakker og priser for bil fra 1. juni 2026.](https://www.finn.no/bedriftskunde/motor/priser/priser-bilannonsering#notice-91d5be82e9b8)
- 2026-10-27 · bilinfo.dk · [2027 Priser BILINFO Abonnementer BILINFO Webprodukter Bilbasen Annoncering](https://bilinfo.dk/2027priser)

## Data events touching the last 30 days

- **E12** 2026-09-02→ongoing · leboncoin.fr mobility_cars · info: DataDome blocks the scraper and robots.txt disallows the path. Only two manual observations exist; the series is not tracked.
- **E19** 2026-11-09→2026-11-18 · * * · info: vend-market-data build failed on all 10 scheduled runs 2026-11-09 to 11-18: package_table() raised on a blank package_share value from finn-mobility-packages week 2026-11-09 (finn 0/0/0 after finn refused every ad fetch with 403). facts/ and digest/ stayed at data up to 2026-11-07. Fixed 2026-11-19 (7b65649); rebuilt to data up to 2026-11-18 after the upstream zero rows were deleted.
- **E20** 2026-11-09→2026-11-15 · * mobility_cars · info: No Tradera vs Blocket private car census for the week of 2026-11-09: on 2026-11-15 22:59 UTC tradera.com answered the census's first request with 403 four times and the run wrote nothing. One-off in 30 days; vend-scraper-v2 read Tradera normally the same night. Not recoverable: the census is a point-in-time snapshot. finn-mobility-packages health.md now flags a missed census.
