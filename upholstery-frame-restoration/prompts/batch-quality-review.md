# Batch Quality Review

## Purpose

Use at the close of a batch (a week's frames, a supplier lot, a production run of re-glued joints) to summarize quality: control state, capability, Pareto of causes, and the next improvement action. The shop-level retrospective that turns per-frame data into process learning.

## Prompt Template

```
You are the quality-engineering agent for an upholstery frame restoration bench.
Produce a batch quality review.

I have a completed batch:

- **Batch scope:** [date range, number of frames, restorers, piece types]
- **Tracked characteristics + data:** [series per characteristic, with metadata]
- **Defect log:** [occurrences by cause category, with rework time/cost if available]
- **Tolerances / specs in force:** [VALUE]
- **Gage R&R status of the gauges used:** [VALUE]

Please:
1. For each characteristic, state the control state (in control / signals) and, if in control, the capability (Cp/Cpk, class).
2. Build a Pareto of defect causes (by count and by cost if available) and name the vital few.
3. Flag any characteristic where capability is being quoted on an unstable chart (and discount it).
4. Identify whether measurement-system variation is masking or inflating any result.
5. Recommend ONE or TWO targeted improvement actions for next batch, aimed only at the vital few, and the metric that will show whether they worked.
```

## Expected Output

- Per-characteristic control-state + capability summary.
- A Pareto with the vital-few causes (count and cost).
- Explicit discounting of any capability quoted on an out-of-control process.
- A measurement-system caveat where relevant.
- One or two prioritized actions with the success metric to recheck next batch.
