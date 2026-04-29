# Webster Cycle Bootstrap Prompt

## Purpose
Get a quick first-cut cycle estimate from volume and geometry data alone, before diving into the multi-objective Pareto search.

## Prompt Template

I need a Webster-formula initial cycle length estimate for the following intersection (single isolated, not yet considering coordination):

- **Intersection:** [name / LOC NUM]
- **Number of phases:** [phases in the ring-and-barrier plan]
- **Lost time per phase:** [s — typically 4 s; use this if unspecified]
- **Lane groups + critical-movement volumes (vph):**
  - [movement, lanes, volume]
  - [...]
- **Saturation flow per lane (vphgpl):** [base 1900; provide adjusted s if available]
- **Heavy-vehicle %:** [%HV]
- **Approach grade %:** [optional]
- **Pedestrian phase requirements:** [walk + clearance per ped phase, if controlling]
- **Agency cycle cap:** [max allowed cycle, s]

Please compute:

1. Flow ratios `y_i = v_i / s_i` for each critical lane group.
2. Sum of critical flow ratios `Y = sum(y_i)`. Confirm `Y < 1`; if not, the intersection is over capacity.
3. Total lost time `L = phases * lost_time_per_phase`.
4. Webster's optimal cycle `C* = (1.5 * L + 5) / (1 - Y)`.
5. Compare to:
   - Pedestrian-controlled minimum (longest ped phase × number of barriers).
   - Agency cycle cap.
   - Practical floor (60 s typical).
6. Recommend the seed cycle for the Pareto search (Webster, clamped to the binding constraint).

## Expected Output
- Per-movement flow ratios in a table
- Y, L, C*, and the binding constraint (Webster, ped, cap, or floor)
- Seed cycle for `/eco-optimize`
- One-sentence flag if the intersection appears over-capacity (sum y > 0.85)
