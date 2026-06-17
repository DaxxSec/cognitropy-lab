# /reconstruct-timeline — Assemble the Confidence-Tagged Whole

Merge authenticated fragments, deposition strata, and geospatial events into one super-timeline — the reconstruction proper, with the conservator's evidence/conjecture boundary enforced on every entry.

## Inputs

- The trusted-artifact set (from `/anachronism-sweep`) and provenance chains (from `/artifact-provenance`).
- Stratigraphy output (`/layer-stratigraphy`) and any geospatial events (`/geo-spread-map`), if run.
- Telemetry exports for the incident window, all normalized to UTC.

## Steps

1. **Normalize and merge** every event to a single UTC timeline; record the source for each row.
2. **Order by deposition, not discovery**: place events by corroborated time-of-occurrence, not the order you found them.
3. **Tag every entry** `CONFIRMED` (direct corroborated telemetry), `INFERRED` (forced by surrounding evidence), or `CONJECTURE` (interpolation across a gap).
4. **Document lacunae**: where telemetry is missing, insert an explicit gap marker rather than bridging it silently — leave a documented seam, never an invented one.
5. **Annotate with ATT&CK** technique IDs and link each entry to its provenance/stratum so the reader can audit any claim.

## Output

`outputs/timeline-<incident>-<date>.md`: a chronological table (UTC time · event · host · ATT&CK ID · source · **confidence**), an explicit list of evidence gaps, and a one-paragraph narrative that uses only `CONFIRMED`/`INFERRED` material.

## Notes

- A timeline whose narrative leans on `CONJECTURE` is a hypothesis, not a finding — keep them visibly separate.
- Feed the finished timeline into `/condition-report` and `/custody-dossier`.
