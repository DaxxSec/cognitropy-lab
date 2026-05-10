# /mpc-horizon-tune

Pick the MPC prediction horizon *N* and terminal-cost weight *Q_f* given the trip-length posterior and the embedded compute budget.

## Inputs

- MPC formulation: state vector, decision variables, constraints, baseline cost function.
- Trip-length posterior (mean + variance).
- Embedded compute budget (per-step max wall-clock budget, e.g. 50 ms).
- Cycle ensemble for evaluation.

## Steps

1. Read `context/workflows.md` "MPC Horizon and Terminal-Cost Tuning".
2. Identify the dominant disturbance time-scale (typically driver torque demand): the horizon must cover at least one acceleration-cruise-deceleration triplet (~10-20 s commonly).
3. Sweep N ∈ {5, 10, 15, 20, 30 s} on the in-sample cycle ensemble. Record per-step compute time alongside fuel cost.
4. For each N, sweep terminal-cost weight Q_f to balance instantaneous cost against end-of-horizon SOC.
5. Pick the smallest N that gets within X% (e.g. 2%) of the largest-horizon fuel cost AND fits the compute budget.
6. Validate on out-of-sample cycles drawn from the trip-posterior tails — short-trip and long-trip alike. The terminal cost has to handle both.
7. Write results to `outputs/`.

## Output

A markdown file `outputs/mpc-tune-YYYY-MM-DD.md` containing: horizon sweep table (N, fuel cost, per-step compute, max constraint margin), Q_f sweep at chosen N, out-of-sample validation summary, and recommended (N, Q_f) with the rationale.

## Notes

- Compute exceeding the budget → reduce horizon, switch to explicit MPC with offline-precomputed regions, or relax the QP solver tolerance.
- Fuel improvement plateaus quickly with N → the terminal cost is doing the work; tune Q_f harder rather than extending N.
- Out-of-sample regression on tail trips → terminal cost is over-fit to in-sample trip lengths; widen the trip prior or re-tune with the broader ensemble.
- Stochastic MPC variants (sample-tree over the disturbance posterior) are worth considering when the posterior is wide; the deterministic-equivalent shortcut leaves robustness on the table.
