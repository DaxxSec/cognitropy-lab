# /triage-tree

Generate or execute a decision-tree triage runbook for an alert — this build's core technique. Mirrors a propagation operator's frequency-selection decision tree: check the disturbance, check the SNR margin, confirm with a second circuit, then act.

## Inputs

- The alert (or alert class) to triage.
- Current environment state: noise-floor snapshot + space-weather K-score (`/space-weather`).
- The diurnal baseline for the alert's source (`/diurnal-baseline`).
- ATT&CK context: paired techniques / kill-chain neighbors for the firing rule.

## Steps

1. Load the canonical triage decision tree from `context/workflows.md`.
2. **Q1 — disturbed environment?** If a storm is active (K5+), treat a lone uncorroborated alert as suspected FP-by-conditions: suppress-and-batch, do not re-baseline. Else continue.
3. **Q2 — clears SNR margin for *this* hour bucket?** Compare the observation to the diurnal envelope at the alert's hour-of-day (not the daily mean). Below margin → close-benign + flag for re-baseline. Above → continue.
4. **Q3 — ATT&CK corroboration?** Same entity on a second analytic / a kill-chain neighbor → escalate (high-confidence multi-circuit confirmation).
5. **Q4 — entity criticality?** Crown-jewel asset / privileged account → escalate even without corroboration; else enrich and queue.
6. Record the exact branch path taken — it is feedback for the next `/tune-rule` cycle.

## Output

`outputs/triage-<alert-id>-YYYY-MM-DD.md` — the branch path taken, the disposition (defer / close-benign / escalate / enrich-queue), the rationale at each node, and a tuning-feedback flag for the source rule.

## Notes

- The branch path *is* the audit trail. "Escalated" without the path is unreviewable.
- Mostly-Q2-closes for one rule = it's sitting below its LUF → tighten toward FOT. Never reaching Q3 = possibly above its MUF → check `/coverage-map`.
