# /functional-fatigue-budget

Model how the transformation degrades under repeated cycling — drift in Af, accumulated residual strain, and lost actuator stroke — and turn it into a cycle-life budget.

## Inputs

- Required service life in transformation cycles (e.g. 10⁴ thermal actuations, 4×10⁸ cardiac cycles for a stent).
- Per-cycle strain amplitude and stress (or actuator load and stroke).
- Any cycling data available: stroke vs. cycle count, Af shift vs. cycles, or residual strain vs. cycles.

## Steps

1. Read `context/concepts.md` on **functional fatigue** (dislocation accumulation degrading functional properties) versus **structural fatigue** (crack-driven fracture) — they have different mitigations and must be budgeted separately.
2. Characterize the degradation trajectory: transformation temperatures drift, the stress plateau drops, residual (unrecovered) strain grows, and actuator stroke decays — typically fastest in the first ~10²–10³ cycles, then stabilizing.
3. Fit a decay model (logarithmic or power-law) to the available data; project residual strain and stroke at the required cycle count.
4. Compare projected end-of-life stroke / recovery against the functional requirement; report the **margin** and the cycle at which the spec is first violated.
5. Identify mitigations and rank them: lower strain amplitude (strongest lever), stabilization pre-cycling / training, Ni-rich + aging for stronger matrix, lower operating temperature relative to Af, surface finish for the structural-fatigue side.
6. Pass the chosen design point to `/eco-performance-frontier` — extending fatigue life via larger or pre-trained parts has an embodied-energy cost worth surfacing.

## Output

`outputs/fatigue-budget-<part>-YYYY-MM-DD.md`: the degradation fit, projected stroke/residual-strain at end of life, the functional and structural fatigue margins, the first-violation cycle, and a ranked mitigation list.

## Notes

- Functional fatigue saturates; structural fatigue does not — a part can be "trained stable" yet still crack. Budget both.
- Strain amplitude dominates life: dropping peak strain from 6% to 4% can extend functional life by orders of magnitude.
- Cite the cycling temperature and load — a fatigue curve is meaningless without them.
