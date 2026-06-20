# /bottleneck-delay-analysis

Quantify the per-piece delay each stage queue imposes and price the capacity-investment decision — a second wheel vs. a second kiln vs. a drying cabinet — so equipment money goes where it actually removes delay.

## Inputs

- Per-stage saturation flow and degree of saturation `X` (from `/throwing-saturation-flow`).
- Arrival rate `q` (pieces/period) and the green ratio `λ = g/C` for the bottleneck stage.
- Cost of candidate capacity additions (second kiln, extra wheel, drying cabinet) and their effect on the bottleneck's capacity.

## Steps

1. Identify the controlling bottleneck (highest `X`). Confirm it is the kiln in the usual case — but verify, do not assume.
2. Compute Webster delay at the bottleneck: `d = C(1−λ)²/[2(1−λX)] + X²/[2q(1−X)]`. Note the overflow term blows up as `X → 1` — the last increment of utilization costs the most delay.
3. For each candidate investment, recompute capacity → new `X` → new delay. The delta in delay per piece × pieces/period = the throughput value purchased.
4. Reject investments that target a non-bottleneck stage — adding wheels when the kiln is the constraint buys *zero* throughput (the classic, expensive error).
5. Add the EIA dimension: a second kiln adds firing capacity but also a second standing energy draw; a drying cabinet adds modest energy; favor the option whose marginal throughput per marginal footprint is best, and say so.

## Output

`outputs/bottleneck-delay-YYYY-MM-DD.md`: the bottleneck, per-piece delay now, the delay/throughput/footprint delta for each candidate investment, and a ranked recommendation with payback.

## Notes

- The most common studio mistake this command prevents: buying wheels to fix a kiln-bound studio.
- Marginal-throughput-per-dollar and marginal-throughput-per-kgCO₂e can disagree; report both and let the owner choose.
