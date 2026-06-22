# /cue-sheet-build

Normalize a show script, product list, and music map into the canonical timed cue model that every other command verifies against.

## Inputs

- Show script / cue list (Finale 3D, FWsim, Visual Show Director, ShowSim export, or a CSV).
- Product list with bores/effect types (and ToF / fallout radius if the data sheet gives them).
- Site diagram: firing positions (x, y), spectator line, no-fire zones.
- Firing-system map: modules and channel/pin assignments (if known yet).
- *(Optional)* the music track length and beat/downbeat map.

## Steps

1. **Resolve the timeline ambiguity first.** Determine whether the source's time column is `t_fire` (system-commanded) or `t_effect` (visual). If unclear, stop and ask — do not guess. Record which it is.
2. Read `context/concepts.md` for the canonical field set and `context/references.md` for bore→ToF/radius defaults.
3. For each cue, populate: `id`, `t_fire`, `device`/`effect`, `position`, `channel`, `lift/tof`, `t_effect = t_fire + tof`, `duration`, `t_clear = t_effect + descent`, `radius`. Fill ToF/radius from the product sheet; fall back to the reference table and mark the value `(est)`.
4. Validate completeness: every cue has a position and a channel (or an explicit `TBD` flagged for `/rack-allocation`); no negative `t_fire`; `t_effect ≤ t_clear`.
5. Emit the canonical cue sheet sorted by `t_fire`, plus a sorted-by-`t_effect` view (the visual timeline).

## Output

`outputs/cue-sheet-YYYY-MM-DD.md` (and/or `.csv`): the canonical cue table with both timelines, an inventory summary (count by bore/effect), and a list of any `(est)` or `TBD` fields that downstream commands must treat as assumptions.

## Notes

- This is the single source of truth — every other command reads it; if it's wrong, every proof is wrong.
- Keep `t_fire` and `t_effect` as separate columns forever. Never collapse them.
- Re-run after any cue edit and re-snapshot; stale cue sheets silently invalidate the ledger.
