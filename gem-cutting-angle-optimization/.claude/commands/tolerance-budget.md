# /tolerance-budget — Allocate the Angle-Error Budget

Translate an optimized design's required angle tolerance into a budget across the machine's error sources, and decide whether the bench can currently hold the cut. This is the command that couples the optics to the machine.

## Inputs

- Required hold tolerance for the design (e.g. ±0.15°) from `/optimize-pavilion-angle` / `/tangent-ratio-adapt`.
- Current condition readings: spindle TIR, lap flatness deviation, index repeatability, and an operator-skill allowance — from the latest `/spindle-runout-trend` and `/lap-wear-forecast`, or measured now.
- Dop length (to convert spindle runout in µm into an angle in degrees).

## Steps

1. Convert each physical error into an angle: spindle runout `σ_spindle ≈ arctan(TIR / dop_length)`; lap flatness into a radial angle variation; index repeatability already in degrees; operator allowance from skill (typ. 0.03–0.08°).
2. Combine by root-sum-square: `σ_total = sqrt(σ_spindle² + σ_lap² + σ_index² + σ_operator²)`.
3. Compare `σ_total` to the required tolerance. Compute headroom (or overrun).
4. Identify the **dominant source** — the term contributing most to the RSS — since RSS is driven by its largest member.
5. Decide: **GO** (under budget with headroom), **CAUTION** (within ~80–100% of budget — cut, but watch), or **NO-GO** (over budget — schedule maintenance before cutting).
6. If NO-GO or CAUTION, hand the dominant source to `/pdm-schedule`.

## Output

A budget breakdown: each source's angle contribution, the RSS total, required tolerance, headroom, dominant source, and a GO/CAUTION/NO-GO verdict. Save to `outputs/<stone-id>-tolerance-budget.md`.

## Notes

- RSS is dominated by the largest term — fixing the worst source buys more than trimming three small ones.
- Tightening the design tolerance (a broader-plateau angle from `/optimize-pavilion-angle`) is a valid alternative to a machine fix when a service can't be done in time.
