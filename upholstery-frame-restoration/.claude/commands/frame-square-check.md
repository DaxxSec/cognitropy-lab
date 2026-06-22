# /frame-square-check — Dimensional Conformance Inspection

Inspect a bare frame's geometry (squareness, seat-opening dimensions, leg-length spread) against the tolerances for its piece type, and report each characteristic as in / borderline / out — with the datum and measurement metadata that make the numbers comparable.

## Inputs

- Piece type and period (e.g. "Edwardian open-arm chair", "mid-century sofa seat box").
- Measured values with their datum faces: front/back diagonal pair (for squareness), seat opening width & depth, the four leg lengths, and any other tracked dimension.
- Tolerance set (from `/restoration-traveler` or `context/references.md` defaults; conservation pieces use looser, object-appropriate tolerances).
- Wood MC and ambient RH/temperature at measurement time.

## Steps

1. Compute **squareness** as the diagonal difference Δd = |d₁ − d₂| across the seat box; convert to an out-of-square angle if useful. A rectangle is square when its diagonals are equal.
2. Compute the **leg-length spread** (max − min of the four legs) — the usual cause of a rocking chair on a flat floor.
3. Compare each characteristic to its tolerance band; tag **green / borderline / out**.
4. For any out value, check whether it is physically real or a **measurement artifact** (wrong datum, tape sag, off-EMC wood) before flagging — re-measure or defer to `/gage-rr` if the gauge is unstudied.
5. Append each measured value to its running chart input so `/control-chart` can place it in process context (one frame ≠ a process verdict).

## Output

A conformance report: characteristic table (value, tolerance, status, datum), squareness Δd and leg spread, flagged items with real-vs-artifact note, and the metadata block (instrument, operator, MC, RH). Save to `outputs/<frame-id>-square-check.md`.

## Notes

- Squareness is meaningless without naming the diagonal endpoints — always record the datum faces.
- A single in-tolerance frame does not mean the process is capable; a single out frame may be common-cause. Read this command's output through `/control-chart`, never in isolation.
- For antique pieces, "out of nominal but original and sound" is a *keep*, not a defect — note it as conservation-retained.
