# /wear-vs-fuel-pareto

Compute and plot the Pareto frontier of fuel consumption vs. battery wear for a controller across a cycle ensemble.

## Inputs

- Controller (one or more candidates).
- Cycle ensemble (the evaluation suite from `/cycle-evaluate`).
- Wear proxy choice: throughput (Ah-equivalent), DOD-weighted, or rainflow equivalent full cycles.
- Weight-sweep grid for the multi-objective cost (e.g. λ ∈ {0, 0.1, 0.5, 1, 2, 5, 10}).

## Steps

1. Read `context/workflows.md` "Pareto Frontier — Fuel vs. Battery Wear".
2. Decide and document the wear proxy. (Different choices produce different frontiers — never compare across proxies without flagging.)
3. For each weight λ in the sweep, modify the controller's cost function: `J(λ) = J_fuel + λ · J_wear`. Re-run on the cycle ensemble.
4. Tabulate (λ, fuel, wear) per run.
5. Plot fuel on x-axis, wear on y-axis; identify the Pareto-dominant points (no other point is lower in both).
6. Locate the knee (point of maximum fuel-vs-wear trade-off curvature) — this is usually a defensible default.
7. Report multiple candidate operating points (low-fuel, knee, low-wear) so stakeholders can choose.

## Output

A markdown file `outputs/pareto-YYYY-MM-DD.md` containing: wear proxy choice (and rationale), the (λ, fuel, wear) table, ASCII or text-described plot of the frontier, identified knee point, and three recommended operating points (extreme fuel, knee, extreme wear) with their cost-function weights.

## Notes

- A flat frontier means wear is decoupled from fuel in this regime; default to lowest fuel.
- A steep frontier at the knee means small fuel concession buys large wear reduction; favour wear if pack replacement cost matters.
- If λ has to go very high (e.g. >100) before wear registers, the wear proxy is insensitive — pick a more discriminating proxy (rainflow > throughput in most realistic regimes).
- Never collapse the Pareto frontier to a single weighted-sum number in a stakeholder conversation; the choice is theirs, not the optimiser's.
