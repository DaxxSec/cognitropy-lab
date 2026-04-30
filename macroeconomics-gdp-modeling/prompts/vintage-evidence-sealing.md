# Prompt — Vintage Evidence Sealing

Use when the agent ingests a new data vintage and must produce a custody-compliant manifest entry.

---

You are sealing a real-time data vintage as forensic evidence. Treat the source response body as the primary evidence — the parsed parquet is a derived artifact.

**Inputs you will be given:**
- `source` (e.g. `fred-alfred`)
- `series_id` (e.g. `GDPC1`)
- `vintage_date` (ISO date)
- `raw_bytes_path` (path to the saved raw response)
- `parquet_path` (path to the parsed parquet)
- `git_sha` (current clean commit)
- `license` (per source policy)
- `embargoed_until` (timestamp or null)

**Your task:**

1. Compute SHA-256 of `raw_bytes_path` and `parquet_path`.
2. Build a JSON manifest entry following the schema in `resources/custody-manifest-schema.md` with `kind: "vintage"`.
3. Append the entry to `outputs/manifests/INDEX.json` (append-only).
4. Write a per-day manifest at `outputs/manifests/v<vintage_date>.json` containing this entry.
5. If `embargoed_until` is non-null, mark the entry `embargoed_until` and add a top-level note: this vintage cannot be included in any release bundle before the embargo lifts.
6. Compute the diff against the prior sealed vintage of this series (rows added, rows revised, max absolute revision percent). Include the diff summary in the manifest entry under `prior_vintage_diff`.
7. Print a one-line confirmation: `sealed: <source>/<series_id> v<vintage_date> sha256=<short> diff=<rows_added>/<rows_revised>`.

**Refuse to proceed if:**
- The git tree is dirty.
- The parquet file already exists at the same path with a different hash (this is a tamper attempt or a logic bug — surface it loudly).
- The raw bytes file is missing or empty.

Output only the manifest entry JSON and the one-line confirmation.
