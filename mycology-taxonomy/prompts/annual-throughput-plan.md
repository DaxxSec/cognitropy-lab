# Annual Throughput Plan

## Purpose

Use this prompt to build a year-ahead capacity and throughput plan for a fungarium — typically under a digitization grant or institutional target — sizing curator hours, sequencing cadence, and budget against a determination quota and a deadline.

## Prompt Template

```
You are a fungarium operations planner. Build an annual throughput plan to hit our determination target.

Planning inputs:

- **Target:** [N specimens determined by DATE, e.g. 1,200 in 9 months]
- **Backlog at start:** [count, by difficulty tier if known]
- **Expected arrivals:** [λ per month, seasonality if any]
- **Curator capacity:** [roster, hours/week, group expertise]
- **Sequencing:** [Sanger/Illumina, plate format, per-run cost, runs/month feasible]
- **Budget:** [reagent + labour envelope]
- **Tier mix:** [rough % routine / moderate / hard]

Please:
1. Compute the required takt (available time ÷ target) and the throughput each stage must sustain.
2. Identify which stage is the binding constraint at that throughput and by how much.
3. Size curator allocation (difficulty-weighted) and sequencing cadence/batch size to meet takt with a safety buffer.
4. Project the monthly backlog burn-down and flag months where the plan slips.
5. Estimate cost (sequencing runs × cost + labour) and check it against budget; show the cost/turnaround tradeoff of batch choices.
6. List the top risks (variability, key-reviewer dependency, hard-taxon surge) and a mitigation for each.
```

## Expected Output

- Required takt and per-stage throughput targets.
- The binding constraint and the staffing/sequencing plan that relieves it (with safety buffer).
- A month-by-month backlog burn-down projection and slip flags.
- A budget estimate vs envelope, with the batch-size cost/turnaround tradeoff made explicit.
- A ranked risk list with mitigations.
