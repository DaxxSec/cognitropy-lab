# /ecms-tune

Tune the ECMS equivalence factor *s* — or the A-ECMS adaptation law — for the trip-length posterior.

## Inputs

- Vehicle architecture and current ECMS implementation.
- Trip-length posterior (mean + variance, or categorical over short/medium/long).
- Cycle ensemble for evaluation.
- Existing baseline *s* (or "no baseline; cold-start tune").

## Steps

1. Read `context/workflows.md` "ECMS Equivalence-Factor Tuning under Bayesian Update".
2. If cold-start: solve a coarse offline DP on a representative cycle to get *s\* such that ΔSOC ≈ 0 over the typical CS-mode trip. This is the prior.
3. Pick the adaptation law (PI on SOC error, frequency-decomposed, Kalman on *s*) and document.
4. Sweep step Δs caps (e.g. 0.001, 0.005, 0.01 per segment) on a held-out cycle ensemble.
5. Pick the cap that gives the lowest fuel cost without inducing oscillation (visible in the *s* trajectory).
6. Validate on out-of-sample cycles drawn from the *tails* of the trip-length posterior, not the mean.
7. Write the tuned *s*, the adaptation law, and the validation results to `outputs/`.

## Output

A markdown file `outputs/ecms-tune-YYYY-MM-DD.md` containing: cold-start *s\**, chosen adaptation law, Δs cap, in-sample fuel cost vs. baseline, out-of-sample validation summary, and a small plot description for the *s* trajectory across a representative cycle.

## Notes

- *s* drifting outside [0.5×, 2×] of the DP-optimal value usually means the trip prior is stale — refresh it via `/posterior-update`.
- Charge sustainability failure (large negative ΔSOC at trip end) → either *s* too low (favours electric) or terminal-cost weight needs raising in the supervisor.
- A-ECMS is **not** a substitute for MPC when the future is highly informative (mapped route ahead) — it's the right tool when the trip is unknown.
