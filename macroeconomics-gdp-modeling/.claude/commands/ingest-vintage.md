# /ingest-vintage — Pull and Seal a Real-Time Vintage

Retrieve today's vintage of one or more configured series and append it to the sealed evidence store. Idempotent: if the source has not republished since the last seal, the command short-circuits and logs a no-op.

## Required Inputs

- Source: one of `fred-alfred`, `oecd-mei`, `eurostat-sdmx`, `bea-nipa`, `bls`, `national` (custom).
- Series IDs: from `context/project.md`. Default to all configured series if none specified.
- Optional vintage date override: by default `today` UTC; override only for backfilling.

## Steps

### 1. Confirm clean git state
Refuse to ingest into a dirty working tree. Custody manifests pin a git SHA — that SHA must reference a clean commit.

### 2. Retrieve
Use the source-specific client (see `context/for-agent/tools.md`):
- **FRED ALFRED:** GET `https://api.stlouisfed.org/fred/series/observations?series_id=<id>&realtime_start=<date>&realtime_end=<date>&api_key=...&file_type=json`
- **OECD SDMX:** SDMX 2.1 dataflow request scoped to the dataset, jurisdiction, and frequency.
- **Eurostat SDMX:** Equivalent SDMX 2.1 request against the Eurostat endpoint.
- **BEA NIPA:** BEA API with TableID + Frequency.

For each series, parse the response and persist the *raw response body* to `outputs/vintages/<source>/<series>/raw/<vintage>.json` *before* any transformation. The raw bytes are the evidence; the parsed parquet is a derived artifact.

### 3. Hash and write parquet
- SHA-256 the raw response body. Store the digest in the manifest.
- Parse into a typed pandas DataFrame with columns `(date, value, vintage_date, units)`.
- Write `outputs/vintages/<source>/<series>/v<YYYY-MM-DD>.parquet` (append-only — refuse to overwrite an existing file; if the vintage is identical to yesterday's seal by hash, log and skip).

### 4. Append to the custody manifest
Add an entry to `outputs/manifests/INDEX.json` and produce a per-day manifest at `outputs/manifests/v<YYYY-MM-DD>.json`:

```json
{
  "schema": 1,
  "kind": "vintage",
  "source": "fred-alfred",
  "series_id": "GDPC1",
  "vintage_date": "2026-04-30",
  "retrieved_utc": "2026-04-30T13:02:11Z",
  "raw_path": "outputs/vintages/fred-alfred/GDPC1/raw/2026-04-30.json",
  "parquet_path": "outputs/vintages/fred-alfred/GDPC1/v2026-04-30.parquet",
  "raw_sha256": "…",
  "parquet_sha256": "…",
  "license": "FRED Terms of Use",
  "git_sha": "…",
  "agent": "claude-code:macroeconomics-gdp-modeling/v1.0"
}
```

### 5. Optional — sign
If the user enabled GPG signing, run `gpg --detach-sign --armor outputs/manifests/v<YYYY-MM-DD>.json` and store the `.asc` alongside.

### 6. Diff against the prior vintage
For each series, load the most recent prior parquet (if any) and compute `(rows_added, rows_revised, max_abs_revision_pct)`. Write the diff summary to `work-log/<YYYY-MM-DD>.md`. This is what feeds `/audit-revision` later.

## Output

- New `outputs/vintages/<source>/<series>/v<YYYY-MM-DD>.parquet` files (append-only).
- New `outputs/manifests/v<YYYY-MM-DD>.json` (and `.asc` if signed).
- Updated `outputs/manifests/INDEX.json`.
- A `work-log/<YYYY-MM-DD>.md` block with the diff summary and any anomalies.

## Failure Modes

- **API throttling:** retry with exponential backoff (max 5 attempts). Log the retry trail.
- **Schema drift:** if the source response shape changes, abort the seal and surface the diff to the user — never silently coerce.
- **Hash collision with prior seal:** the source has not updated; record a `noop` manifest entry and exit.
