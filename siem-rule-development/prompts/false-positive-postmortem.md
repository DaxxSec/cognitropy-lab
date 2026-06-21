# False-Positive Postmortem

## Purpose

Diagnose a confirmed false positive by identifying which propagation factor failed — noise-floor shift, missing diurnal baseline, threshold below the LUF, or a space-weather disturbance — and prescribe the specific fix. Use after triage closes an alert as benign.

## Prompt Template

```
You are diagnosing a false positive on a production detection rule, using the
LUF/MUF/FOT and noise-floor model in context/concepts.md.

- **Rule:** [NAME / ID + current FOT threshold]
- **The false alert:** [WHAT FIRED, ENTITY, TIMESTAMP]
- **What it actually was:** [BENIGN ROOT CAUSE]
- **Noise floor at fire time:** [VALUE / "unknown"]
- **Diurnal baseline for that hour bucket:** [VALUE / "none exists"]
- **Recent environment changes:** [DEPLOYS / INCIDENTS / NEW LOG SOURCES]

Please:
1. Classify the failure: floor risen (below LUF), no diurnal baseline (tuned to
   the mean), threshold set too loose, or a space-weather disturbance.
2. Identify which lifecycle phase was skipped or is now stale.
3. Prescribe the exact fix (re-characterize floor / build diurnal baseline /
   retune to FOT / freeze-and-wait), and which command runs it.
4. State whether this is a one-off transient (Sporadic-E — do not retune) or a
   persistent drift (retune warranted).
```

## Expected Output

- A named failure class tied to the propagation model.
- The stale/skipped phase.
- A concrete fix mapped to a command (`/noise-floor`, `/diurnal-baseline`, `/tune-rule`…).
- A transient-vs-persistent verdict so the team doesn't retune on noise.
