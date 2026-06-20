# /kiln-load-density

Optimize kiln stacking to maximize pieces per firing — the single lever that raises throughput (saturation flow) and cuts per-piece energy at the same time.

## Inputs

- Kiln interior dimensions (W × D × H) and usable firing height (below the lid/elements clearance).
- Shelf inventory: shelf dimensions, thickness, and post/stilt heights available.
- Target form dimensions (height + footprint), and the firing type (bisque can nest/stack; glaze ware cannot touch).

## Steps

1. Read `context/concepts.md` → "kiln as a signalized batch server" and `context/references.md` → kiln energy figures.
2. Lay out shelf levels: divide usable height by (form height + post height + shelf thickness); compute pieces per shelf from footprint and required clearance for even heat.
3. For **bisque**: exploit nesting/stacking (bowls in bowls, rims down) to raise density; note the practical limit before heat-distribution suffers.
4. For **glaze**: enforce no-contact spacing; pieces cannot touch each other or the shelf glaze-side-down. Density is lower — plan separately.
5. Report load density (pieces/firing) and the marginal piece each extra shelf level adds; identify the binding dimension (height vs. footprint).
6. Compute energy/piece at the optimized density (hand to `/firing-energy-audit`) and state the footprint reduction versus the baseline load.

## Output

`outputs/kiln-load-YYYY-MM-DD.md`: a level-by-level loading plan, pieces/firing for bisque and glaze, the binding dimension, and the energy-per-piece improvement.

## Notes

- Leave deliberate clearance for airflow/element radiation — a maximally crammed kiln that fires unevenly is a false optimum that scraps ware.
- This is the convergence command: every extra piece that fits both raises capacity and lowers per-piece kWh. Prioritize it before buying equipment.
