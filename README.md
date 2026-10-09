# vend-market-data

One read-only view of everything the Vend scrapers collect: listing counts across
13 marketplaces, package mix, price lists and pricing news. Rebuilt every morning
from four source repos by `.github/workflows/build.yml`.

Start with [`digest/latest.md`](digest/latest.md). [`CATALOG.md`](CATALOG.md)
explains every file and column. [`events.csv`](events.csv) lists every known
outage, glitch and methodology break.

## Using it from a Claude Cowork project

Connect this repo (GitHub connector) or a synced copy of it as the project's
knowledge, and paste this into the project instructions:

> Data lives in the vend-market-data repo. Read `digest/latest.md` first for the
> current state, `CATALOG.md` for what every column means, and `events.csv`
> before interpreting any jump. Use `facts/listings.csv` for trends: filter
> `quality_flag` to blank (keep `outlier` rows on trending series), never sum
> finn.no used and new homes by default, never sum leboncoin segments, and use
> `package_share`, not `package_sample_count`, for car package trends. Prices are
> in the `currency` column's currency. When you find a new data problem, propose a
> row for `events.csv`.

## Setup (once)

1. Create a fine-grained personal access token with **read-only Contents** on
   `vend-scraper-v2`, `finn-mobility-packages`, `finn-bolig-packages` and
   `vend-price-monitor`.
2. Add it to this repo as the Actions secret `SOURCES_TOKEN`.
3. Run "Build consolidated data" from the Actions tab once.

## Local

    python -m unittest discover -s tests
    python build.py --sources <dir with the four repos checked out> --out .

Stdlib only, no installs.
