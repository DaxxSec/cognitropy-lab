# Machine Health Review

## Purpose

Use on a periodic cadence (weekly/monthly or every N stones) to turn a batch of logged condition readings into a single predictive-maintenance decision — what to service, when, and what it costs to defer.

## Prompt Template

```
You are the faceting-optimization agent. Review machine condition and produce a PdM plan.

Here are the latest condition readings:

- **Spindle TIR (µm) + history:** [VALUES with dates/hours]
- **Lap flatness (µm) per lap + history:** [VALUES]
- **Cut-rate decay vs baseline:** [RATIOS per lap]
- **Vibration RMS vs baseline:** [VALUE]
- **Index repeatability (deg):** [VALUE]
- **Design tolerance currently targeted:** [e.g. ±0.15°]
- **Upcoming jobs / parts lead times:** [CONTEXT]

Please:
1. Trend each indicator and give its status (green/watch/limit) and RUL.
2. Place each intervention inside its P-F interval and batch overlapping ones.
3. Prioritize by angle-budget impact (dominant source first).
4. Flag any indicator already past its limit as service-now.
5. Output a dated maintenance queue with parts to order and deferral risk.
```

## Expected Output

- Per-indicator status, trend, and RUL.
- A dated, batched, prioritized maintenance queue.
- Parts-to-order list with lead-time alignment.
- A re-baseline reminder for after each completed task, saved to `outputs/pdm-schedule.md`.
