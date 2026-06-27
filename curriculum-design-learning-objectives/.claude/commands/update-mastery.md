# /update-mastery

Given a learner's responses, update the posterior mastery probability for each objective and
return the met / re-teach / advance decision using a credible-interval rule.

## Inputs
- Learner response log (item, correct/incorrect, ordered if sequential).
- The priors (`/elicit-prior`) and evidence model (`/map-evidence`).
- Decision rule (threshold + credible-interval floor; default 0.95 mean, 80% CI lower ≥ 0.80).

## Steps
1. Choose the model: **BKT** when responses span instruction (learning between attempts),
   **Beta–Bernoulli closed form** for a single fixed-mastery checkpoint.
2. BKT path: apply the per-response condition-then-learn update (see `context/concepts.md` §4 and
   the worked example in `context/workflows.md`) using `p-init, p-transit, p-slip, p-guess`.
3. Beta path: posterior `Beta(α₀+k, β₀+n−k)`; read the mean and the central credible interval off
   the Beta quantiles.
4. Apply the decision tree: MET only if the mean clears the threshold *and* the CI lower bound
   clears the floor; otherwise re-teach (route backward) or give more practice.
5. Never threshold on the mean alone — a wide posterior that trips the rule on luck must be caught.

## Output
Per objective: posterior `P(mastery)`, credible interval, evidence count used, and the decision
(MET / MORE-PRACTICE / NOT-MET → prerequisite). Saved to `outputs/mastery-<learner>.md`.
