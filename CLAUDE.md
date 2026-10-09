# vend-market-data — context for Claude Code

Consolidation layer over four scraper repos. No scraping, no GCP: the nightly
workflow clones the source repos (secret `SOURCES_TOKEN`), runs `build.py`, and
commits `facts/`, `reference/` and `digest/`. Read `CATALOG.md` for the schema.

- **Never edit `facts/`, `reference/` or `digest/` by hand.** They are rebuilt.
- **`events.csv` is hand-maintained** and is where knowledge about data quality
  lives. An `exclude` row tags matching facts as `exclude:E##` on the next build.
  Add rows when a source repo documents a new outage or methodology change.
- Upstream numbers are never altered. Fix data problems in the source repo; record
  them here.
- A missing source file is a warning in the digest, not a failure, so one source
  repo breaking does not stop the others refreshing.
- Tests: `python -m unittest discover -s tests` (stdlib, offline). To build
  locally, symlink the four checkouts into `sources/` and run `python build.py`.
- Commits to `main` happen only from the workflow on `main`; a branch run prints
  the diff instead.
