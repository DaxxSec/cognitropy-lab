# Significance-vs-Cost Matrix

## Purpose

Plot a set of sites (or recovery units) on a significance-vs-cost matrix to triage a portfolio under a shared budget — which to excavate, which to preserve in situ, which to evaluate further. Use when allocating across multiple candidates.

## Prompt Template

```
You are triaging a portfolio of submerged sites (or recovery units) under a shared budget using
a multi-criteria cost-benefit framework. Significance is the benefit axis; full lifecycle cost is the cost axis.

Candidates (repeat per item):
- **ID:** [VALUE]
- **Significance (weighted score + tier):** [VALUE]
- **Lifecycle cost (PV, incl. conservation/curation):** [VALUE]
- **Threat / urgency:** [VALUE]
- **Special-status flags (war grave, sovereign, human remains):** [VALUE]

Shared constraints:
- **Total budget:** [VALUE]
- **Conservation capacity:** [VALUE]
- **Discount rate:** [VALUE]

Please:
1. Place each candidate in a significance × cost quadrant (high-sig/low-cost = excavate first; high-sig/high-cost = sample or in-situ; low-sig = record/preserve).
2. Overlay urgency: at-risk high-significance items rise in priority.
3. Recommend an allocation that respects budget AND conservation capacity (whichever binds first).
4. Mark the in-situ-preserve and record-only remainder.
5. Note any candidate where a legal/ethical flag overrides the matrix.
```

## Expected Output

- A quadrant placement for every candidate.
- A budget- and capacity-respecting allocation.
- The preserve-in-situ / record-only remainder.
- Any override flags called out.
