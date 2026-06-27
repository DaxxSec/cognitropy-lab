# /calibrate-bkt

Fit BKT parameters from historical response data and diagnose identifiability and degenerate
fits before the model is trusted for live mastery decisions.

## Inputs
- Historical response logs (learner, skill, ordered correct/incorrect).
- Optional: parameter bounds, a held-out split for predictive checks.

## Steps
1. Fit `p-init, p-transit, p-slip, p-guess` per skill (e.g. `pyBKT`, EM or Bayesian estimation).
2. **Degeneracy check:** reject/constrain any fit with `p-slip ≥ 0.30` or `p-guess ≥ 0.30` — the
   model is "gaming" the data; bound `S,G < 0.3` and refit, or flag the item for revision.
3. **Identifiability check:** perturb starting points / inspect the likelihood surface; if many
   parameter sets fit equally, add priors or pool across learners (hierarchical).
4. **Predictive check:** on held-out responses compare predicted vs. observed correctness (AUC,
   calibration plot). Poor calibration ⇒ revisit the evidence model or skill granularity.
5. Recommend item-level actions for low-information items (high guess/slip).

## Output
Per-skill fitted parameters, degeneracy/identifiability/calibration verdicts, and item-revision
recommendations. Saved to `outputs/bkt-calibration-<topic>.md`.
