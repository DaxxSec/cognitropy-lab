# /cycle-length-optimize

Compute the studio's optimal production-cycle length using Webster's signal-timing formula, so the batch cadence maximizes throughput against the kiln's load/unload lost time.

## Inputs

- Per-stage lost time `L`: wedging, wheel cleanup, and especially kiln load + unload + cool changeover (minutes or hours).
- Demand per product line `qᵢ` (pieces wanted per period) and measured saturation flow `sᵢ` per line (from `/throwing-saturation-flow`).
- The natural cycle unit (a firing cycle, a production day, or a week).

## Steps

1. Read `context/concepts.md` → "Webster's optimal cycle length" and the formula cheat-sheet in `context/references.md`.
2. Compute each line's critical flow ratio `yᵢ = qᵢ/sᵢ`, then `Y = Σ yᵢ`. If `Y ≥ 1`, stop: the studio is oversaturated — report that no cycle length helps and route to `/bottleneck-delay-analysis` for a capacity decision.
3. Compute `C₀ = (1.5·L + 5)/(1 − Y)` in the chosen unit.
4. Interpret: high kiln lost time `L` drives a longer optimal cycle (fewer, fuller firings). State the trade — longer cycles cut amortized lost time but raise queue delay (cross-check with `/bottleneck-delay-analysis`).
5. Note the environmental corollary: the same longer-cycle direction that Webster recommends also lowers per-piece firing energy, so flag the convergence explicitly.

## Output

`outputs/cycle-length-YYYY-MM-DD.md`: the `yᵢ` table, `Y`, the optimal cycle length, the firings-per-period it implies, and the throughput-vs-delay trade with the EIA convergence noted.

## Notes

- Webster is only valid for `Y < 1`. Treat `Y` between 0.9 and 1 as a warning band — the studio is near saturation and delay is already nonlinear.
- The "+5" and "1.5" constants are Webster's traffic calibration; keep them for the analogy's integrity but note they are heuristic when transposed to a studio unit.
