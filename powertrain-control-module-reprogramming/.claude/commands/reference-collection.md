# /reference-collection

Build and query the conservator's **reference collection** — the curated library of known-good calibrations indexed by model/year/market with verified hashes. The "study skin drawer" you select baselines from and file new verified specimens into.

## Inputs

- Either a **query** (model, year, engine, market, regime, altitude band) to *find* a cal, or
- A **new verified specimen** (from `/specimen-intake` with a matching stock CVN) to *file*
- The collection index location (default `context/references.md` index + `outputs/specimens/`)

## Steps

1. **Determine intent:** query (retrieve a baseline) or deposit (file a verified cal).
2. **On query:** filter the index by {model, year, engine, market/regime, fuel, altitude}; rank candidates by closeness of fit; return CAL-ID, hash, market, and fitment notes.
3. **On deposit:** confirm the specimen's CVN matches a known stock value (or mark as a verified *modified* baseline); record CAL-ID, market, hardware form, hash, and source.
4. **Deduplicate.** If a candidate already exists with the same CAL-ID/hash, link rather than duplicate.
5. **Update the index** so the new entry is queryable next time.

## Output

Either a ranked list of candidate baselines (query) or a confirmed new index entry (deposit), written/updated in the collection index with VIN/CAL-ID ↔ market ↔ hash mapping.

## Notes

- The collection's value is integrity: only file cals whose provenance you trust (stock CVN match, or clearly labelled known-modified).
- A query that returns **no exact regional match** is an answer — escalate to an OEM/TSB source rather than forcing a near-miss.
- Consider a SQLite/database MCP to back the index once the collection grows past a few dozen entries.
