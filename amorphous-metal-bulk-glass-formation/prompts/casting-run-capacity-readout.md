# casting-run-capacity-readout

## Purpose

Summarize a completed casting run's capacity outcome — planned vs actual yield, the binding constraint, and OEE — so the next run's plan is grounded in what actually happened. Use at run close-out or shift handoff.

## Prompt Template

```
You are a BMG foundry process engineer writing a capacity readout for a completed run.

Run data:

- **Alloy / product / section (mm):** [VALUE]
- **Planned yield vs actual yield:** [VALUE]
- **Per-station cycle times & counts:** [VALUE]
- **Amorphicity QA results (pass/scrap, where crystallinity appeared):** [VALUE]
- **Context:** [any process excursions, feedstock change, mold condition]

Please:
1. Compute actual bottleneck throughput, OEE (with Quality = amorphous yield), and capacity cushion vs target.
2. Compare planned vs actual yield; attribute the gap (cooling margin, oxygen/nucleation, TPF over-dwell, geometry).
3. Identify the binding constraint this run (machine vs crystallization clock) and whether it matched the plan.
4. Recommend the highest-leverage change for the next run (TOC: exploit/subordinate/elevate).
5. Note where the bottleneck is likely to migrate if the recommendation is applied.
```

## Expected Output

- Actual bottleneck rate, OEE, and capacity cushion.
- Planned-vs-actual yield with a root-cause attribution.
- The binding constraint named and the prioritised next-run action.
- A prediction of the next bottleneck.
