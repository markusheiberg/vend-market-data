# Vend market digest

Generated 2026-11-05 13:10 UTC. Data up to **2026-11-04**.
Read `CATALOG.md` for what each series means and `events.csv` before trusting a jump.

## Series with no value today

- biltorvet.dk · mobility_cars · dealer · listings
- biltorvet.dk · mobility_cars · private · listings
- finn.no · real_estate_homes · - · listings
- finn.no · real_estate_homes · - · new_listings
- finn.no · real_estate_homes_new · - · listings
- finn.no · real_estate_homes_new · - · new_listings
- finn.no · real_estate_other · - · listings
- finn.no · real_estate_other · - · new_listings
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
| bilbasen.dk | mobility_cars | dealer | 48 426 | 2026-11-04 | +0.5% | +1.5% |
| bilbasen.dk | mobility_cars | private | 4 406 | 2026-11-04 | -0.5% | +2.4% |
| bilhandel.dk | mobility_cars | dealer | 26 454 | 2026-11-04 | -3.9% | -2.0% |
| bilhandel.dk | mobility_cars | private | 2 116 | 2026-11-04 | +1.1% | -4.3% |
| biltorvet.dk | mobility_cars | dealer | 44 631 | 2026-10-20 ⚠️ |  |  |
| biltorvet.dk | mobility_cars | private | 2 284 | 2026-10-20 ⚠️ |  |  |
| blocket.se | mobility_cars | dealer | 127 901 | 2026-11-04 | +0.0% | +2.6% |
| blocket.se | mobility_cars | private | 26 480 | 2026-11-04 | -0.5% | -0.9% |
| blocket.se | mobility_other | dealer | 63 449 | 2026-11-04 | +0.3% | -1.3% |
| blocket.se | mobility_other | private | 13 258 | 2026-11-04 | -8.5% | -30.4% |
| etuovi.com | real_estate_homes | - | 51 314 | 2026-11-04 | -0.8% | -1.2% |
| finn.no | jobs_listings | - | 13 372 | 2026-11-04 | -3.6% | -5.5% |
| finn.no | jobs_positions | - | 27 480 | 2026-11-04 | -1.7% | -2.7% |
| finn.no | mobility_cars | dealer | 57 318 | 2026-11-04 | +2.1% | +6.1% |
| finn.no | mobility_cars | private | 19 226 | 2026-11-04 | +0.3% | +4.0% |
| finn.no | mobility_other | dealer | 29 420 | 2026-11-04 | +0.9% | +7.2% |
| finn.no | mobility_other | private | 8 224 | 2026-11-04 | -8.7% | -28.1% |
| finn.no | real_estate_homes | - | 22 000 | 2026-11-01 ⚠️ |  |  |
| finn.no | real_estate_homes_new | - | 17 332 | 2026-11-01 ⚠️ |  |  |
| finn.no | real_estate_other | - | 26 149 | 2026-11-01 ⚠️ |  |  |
| hemnet.se | real_estate_homes | - | 41 229 | 2026-10-25 ⚠️ |  |  |
| hemnet.se | real_estate_homes_upcoming | - | 5 723 | 2026-10-05 ⚠️ |  |  |
| hjem.no | real_estate_homes | - | 8 570 | 2026-11-04 | -2.8% | -2.4% |
| oikotie.fi | real_estate_homes | - | 47 197 | 2026-11-04 | -0.6% | -1.0% |
| tradera.com | mobility_cars | dealer | 52 228 | 2026-11-04 | +0.4% | +6.2% |
| tradera.com | mobility_cars | private | 3 188 | 2026-11-04 | -0.0% | +5.5% |
| wayke.se | mobility_cars | dealer | 53 039 | 2026-10-08 ⚠️ |  |  |

## Package mix

Shares in %. Car packages are a 10% sample of dealer listings; finn homes is a
full crawl of used homes.

| site | vertical | latest week | mix now | mix 4 runs earlier |
|---|---|---|---|---|
| blocket.se | mobility_cars | 2026-10-26 | basis 67.2 / pluss 1.8 / premium 31.0 | basis 67.2 / pluss 2.6 / premium 30.2 |
| finn.no | mobility_cars | 2026-10-26 | basis 36.3 / pluss 22.4 / premium 41.4 | basis 34.5 / pluss 25.3 / premium 40.2 |
| finn.no | real_estate_homes | 2026-11-01 | large 63.7 / medium 33.1 / small 3.2 | large 62.7 / medium 34.3 / small 3.0 |

## Danish dealer market (bilinfo, weekly)

Cars per week. Implied sold = last week's stock x 7 / adjusted days to sell;
implied added = change in stock + sold. Adjusted days put the history on one
basis across bilinfo's 2026-06-08 definition change (E17), as the bilinfo
workbook does. Days are whole numbers, so one day moves sold by ~2%.
* = a week with no report, interpolated.

| week | stock | adj. days to sell | implied sold | implied added |
|---|---:|---:|---:|---:|
| 2026-09-14 | 51 800 | 57 | 6 337 | 6 537 |
| 2026-09-21 | 51 600 | 57 | 6 361 | 6 161 |
| 2026-09-28 | 51 400 | 57 | 6 337 | 6 137 |
| 2026-10-05 * | 51 450 | 57 | 6 312 | 6 362 |
| 2026-10-12 * | 51 500 | 57 | 6 318 | 6 368 |
| 2026-10-19 | 51 500 | 57 | 6 325 | 6 325 |

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
- **E14** 2026-09-26→2026-10-08 · hemnet.se real_estate_homes* · info: Cloudflare challenges intermittently NULL either hemnet count (2026-09-26 and 2026-10-06 to 10-08).
- **E16** 2026-10-06→2026-10-08 · * * · info: Upstream outlier filter (all-time mean ± 3 std dev) blanked genuine values on trending series: biltorvet.dk cars private and blocket.se mobility_other private, 2026-10-06 to 10-08. Fixed 2026-10-09 (vend-scraper-v2 PR #11): a stock value is now blanked only if it is also a sudden break from its recent level. The values reappear in the next export.
