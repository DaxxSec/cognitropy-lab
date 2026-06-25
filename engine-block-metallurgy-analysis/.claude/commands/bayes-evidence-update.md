# /bayes-evidence-update

Update the root-cause posterior with a new lab finding by applying its likelihood ratio in odds (log-odds) form.

## Inputs

- The current prior/posterior ledger from `/failure-hypothesis-rank` (hypotheses + current probabilities)
- The new finding (e.g. "nodularity 42% in a part specified ≥85%", "fatigue striations from a single bore-bridge origin")
- The standard/source the finding came from (A247, SEM fractography, OES) and its confidence

## Steps

1. Restate the finding precisely and identify which hypotheses it bears on.
2. Estimate the likelihood ratio: `LR = P(finding | H₁) / P(finding | H₀)` for each affected hypothesis pair, using the LR scale in `context/references.md`. Justify the number in one sentence.
3. **Independence check** — confirm this finding is not a restatement of evidence already counted (two measures of the same thermal event are one LR, not two). If correlated, combine or down-weight.
4. Convert current odds to log-odds, add `log(LR)`, convert back; renormalize the full hypothesis set to probabilities summing to 1.
5. Append the step to the ledger (finding, LR, log-LR contribution, new posterior) and note whether the leader changed.

## Output

An updated `outputs/<case-id>/posterior-ledger.md` with the running table and the current posterior distribution. Each row is auditable: anyone can see which finding moved the verdict and by how much.

## Notes

- A finding "consistent with" a cause but equally consistent with its rival has LR ≈ 1 — record it, but it must not move the posterior.
- Keep contributions in log-odds so each finding's weight is additive and visible; a single LR > 100 dominating the result should be scrutinized, not trusted blindly.
