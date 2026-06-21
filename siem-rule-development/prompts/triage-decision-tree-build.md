# Triage Decision-Tree Build

## Purpose

Author a decision-tree triage runbook for a new alert class — the build's core technique applied to a specific rule. Produces the branching logic an analyst (or an automation) follows to disposition each alert deterministically.

## Prompt Template

```
You are building a decision-tree triage runbook for one alert class, following
the canonical tree in context/workflows.md (Q1 disturbance → Q2 SNR margin →
Q3 corroboration → Q4 criticality).

- **Alert class:** [RULE NAME / WHAT IT FIRES ON]
- **ATT&CK technique:** [ID + likely kill-chain neighbors for Q3 corroboration]
- **Source + diurnal baseline:** [SOURCE; does a baseline exist?]
- **High-criticality entities for this alert:** [crown-jewel hosts / privileged accounts]
- **Known benign causes:** [for the Q2 close-benign branch]

Please:
1. Instantiate the four-node tree for THIS alert: what specifically to check at
   each node (the concrete signals, not the generic question).
2. Define each leaf disposition (defer / close-benign / escalate / enrich-queue)
   and the exact evidence to record for the branch path.
3. Specify the SNR-margin thresholds (MAD multiples) for Q2 at this source.
4. List the corroborating analytics for Q3 (the "second circuit").
5. Note which branches are safe to automate vs which require an analyst.
```

## Expected Output

- A concrete, instantiated four-node decision tree for the alert class.
- Leaf dispositions with required branch-path evidence.
- Source-specific Q2 thresholds and Q3 corroboration sources.
- An automation-vs-human boundary for each branch.
