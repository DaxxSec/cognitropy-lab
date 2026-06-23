# /plan-digitization-queue — Optimize the digitization priority queue

Turn a raw collection inventory into a defensible, optimization-driven digitization queue that maximizes preservation + access value under fixed lab capacity.

## Inputs

- A collection inventory (CSV/JSON/Markdown) with, per lot: extent (items/pages/reels), material type, physical condition grade, rights/access status, scholarly or public demand signal, and any preservation-risk flag (vinegar syndrome, brittle paper, magnetic media decay).
- Lab capacity for the planning horizon: available capture-station-hours, staff FTE, and budget ceiling.
- Optional: a weighting policy (how to trade preservation urgency vs. access demand vs. effort) — defaults provided below.

## Steps

1. **Normalize the inventory.** Coerce every lot to a common unit (estimated images) using throughput rates from `context/references.md`. Flag rows with missing condition/rights — they cannot be scheduled until resolved.
2. **Score value per lot.** Compute a weighted value `V = w_p·preservation_urgency + w_d·access_demand + w_u·uniqueness − w_r·rights_risk`. Use the default weights (0.40 / 0.30 / 0.20 / 0.10) unless the user supplies a policy. Normalize each factor to 0–1 first so the weights mean what they say.
3. **Estimate cost per lot.** Cost in capture-hours = `images × per-image-time × condition-handling-multiplier` (multipliers in `context/references.md`: pristine 1.0 → fragile 2.5 → conserve-first ∞ until stabilized).
4. **Solve the selection.** Treat it as a 0/1 knapsack: maximize Σ value subject to Σ cost ≤ capacity. Use dynamic programming for ≤ a few hundred lots; for larger sets fall back to the greedy value-density (`V / cost`) ratio and note the optimality gap. Run the workflow in `context/workflows.md §Prioritization`.
5. **Sequence the chosen lots.** Within the selected set, order by preservation-urgency-first (decaying media never waits behind a low-risk lot), breaking ties by value density.
6. **Stress-test.** Re-solve at 80% and 120% capacity to show what falls off / comes on at the margin — this is the negotiation surface for stakeholders.

## Output

`outputs/digitization-queue-<date>.md`: the ranked queue table (lot, value, cost-hrs, cumulative-hrs, in/out at planned capacity), the weighting policy used, the knapsack vs. greedy method note with optimality gap, and the ±20% capacity sensitivity table. Save the scoring inputs alongside so the run is reproducible.

## Notes

- Preservation urgency is a hard override, not just a heavy weight: anything flagged as actively decaying (acetate film, lacquer discs) is pinned to the front regardless of demand. Optimization allocates the *rest* of the capacity.
- Keep the weighting policy explicit in the output — "we chose access over preservation this quarter" is a governance decision that should be visible, not buried in a constant.
- Re-run whenever capacity or the inventory changes; the queue is a living artifact, not a one-time ranking.
