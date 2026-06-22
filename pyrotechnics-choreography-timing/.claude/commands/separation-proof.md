# /separation-proof

Prove no two live effects — and no effect's fallout — violate spatial safety distance, accounting for downwind drift and the worst-case forecast wind.

## Inputs

- The canonical cue sheet (positions, `radius`, `t_effect`, `t_clear`).
- Site geometry: spectator-line polyline, no-fire-zone polygons, firing-position coordinates.
- Wind: nominal and **worst-case forecast** vector (speed + direction), and per-effect descent time.

## Steps

1. For each cue, build its danger footprint: a disc of `radius` at `position`, translated by `wind_vector × descent_time` to the drifted center, live over `[t_effect, t_clear]`.
2. **FALLOUT:** intersect every drifted footprint with the spectator line and no-fire zones. Any intersection ⇒ counterexample (cue id, intrusion distance, wind vector used).
3. **SEP:** form the set of cue pairs whose live intervals overlap in time; for each, test footprint-disc intersection (center distance < sum of radii). Any overlap ⇒ counterexample (both ids, overlap distance, overlap time window).
4. Repeat the whole pass for the **worst-case** wind vector, not just nominal; record which vector each verdict used.
5. Report the minimum clearance margin across all pairs and lines — the show's spatial slack — and rank the tightest 5 for attention.

## Output

`outputs/separation-proof-YYYY-MM-DD.md`: SEP and FALLOUT verdicts, every counterexample with geometry, the min-clearance margin, and the wind vector assumed. Feeds SEP/FALLOUT rows of the verification report.

## Notes

- Geometry violations are **not** fixable by retiming — they need re-positioning or a tighter wind gate. Route them to the constraint-violation triage tree accordingly.
- Time-overlap-only SEP failures (footprints fine if staggered) **are** retiming-fixable: push the later cue to `t_fire ≥ t_clear(prev)`.
- Always state the wind vector behind a discharge; "separation-safe" with no wind assumption is meaningless.
