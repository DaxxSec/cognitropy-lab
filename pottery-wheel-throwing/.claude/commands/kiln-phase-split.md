# /kiln-phase-split

Allocate the kiln's limited firing capacity — its "green time" — across competing firing types (bisque vs. glaze) and product lines, the way a signal splits green across competing movements.

## Inputs

- Kiln capacity per cycle and firings available per period (from `/throwing-saturation-flow`).
- Product mix: each line's demand `qᵢ` and saturation flow `sᵢ`.
- The bisque:glaze firing ratio the body/glaze requires (often ~1:1 by count, but bisque packs denser).

## Steps

1. Compute each line's critical flow ratio `yᵢ = qᵢ/sᵢ` and `Y = Σ yᵢ`.
2. Split available firing slots proportional to `yᵢ` — the line with the larger critical ratio gets more slots, exactly as green time is apportioned in proportion to demand-to-saturation.
3. Reserve bisque vs. glaze slots: bisque ware can nest and pack tight (high density); glaze ware cannot touch — account for the density difference when counting "slots."
4. Check no line is starved: every line must clear within its required lead time. If one cannot, the split is infeasible → reduce demand or add a firing (route to `/bottleneck-delay-analysis`).
5. Layer the EIA lens: prefer splits that keep each firing full (high utilization) over splits that fire partial loads to serve every line every cycle — a partial firing is a footprint penalty.

## Output

`outputs/kiln-phase-split-YYYY-MM-DD.md`: the slot allocation per line and firing type, the resulting per-line lead time, utilization per firing, and any starved line flagged.

## Notes

- Bisque and glaze are different "phases" with different packing rules — never count their capacity as interchangeable.
- A split that serves everyone but fires half-empty kilns fails both the throughput and footprint objectives; full firings first.
