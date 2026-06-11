# /composition-temperature-tune

Back out the composition and alloying change needed to land the transformation temperatures on a target — and propagate the punishing Ni-sensitivity into a tolerance budget.

## Inputs

- Target transformation temperature (usually Af, sometimes Ms) and the allowed tolerance (± °C).
- Current alloy composition (at% Ni, ternary additions) and its measured Af, if iterating from an existing melt.
- Constraints: biomedical (must stay binary NiTi per ASTM F2063), high-temperature need (Hf/Pd/Pt additions), or cost ceiling.

## Steps

1. Read `context/concepts.md` for the Ni-rich sensitivity rule (≈ −10 °C per +0.1 at% Ni above 50 at%) and the Ti-rich clamp (temperatures plateau due to Ti₂Ni precipitation).
2. Locate the target on the composition–temperature map; decide whether binary Ni:Ti tuning suffices or a ternary addition is required (Hf/Zr/Pd/Pt raise temps; Cu narrows hysteresis; Fe/Cr/Co lower temps).
3. Compute the required at% Ni shift, then convert to a melt-composition target and a **weighing tolerance** — show how tight the Ni control must be to hold the ± °C spec (this is the headline finding: ~0.01 at% Ni control for ~1 °C).
4. Add an **aging pathway** option: for Ni-rich alloys, Ni₄Ti₃ precipitation (400–500 °C aging) raises Af by depleting matrix Ni — a post-melt lever that relaxes the casting tolerance.
5. Flag interstitial pickup (O, C) risk — each shifts temperatures and consumes Ti, mimicking a Ni-rich shift.
6. Hand the chosen composition to `/lca-cradle-to-gate` so the environmental cost of any Pd/Pt/Hf addition is counted, not just its thermal benefit.

## Output

`outputs/composition-tune-<target>C-YYYY-MM-DD.md`: target vs. predicted Af, the composition/alloying recommendation, the melt-control tolerance budget, an optional aging schedule, and an environmental-cost flag for any costly ternary addition.

## Notes

- The Ni:Ti sensitivity is the single hardest manufacturing constraint in NiTi — treat the tolerance budget as the deliverable, not an afterthought.
- Pt and Pd raise temperatures effectively but carry large embodied-carbon and supply-risk penalties — never recommend them without the LCA cross-check.
- Composition from EDS is unreliable for the Ni:Ti ratio at this precision; specify wet-chemistry / ICP or calibrated WDS.
