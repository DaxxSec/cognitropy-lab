# Optimization ROI Worksheet

## Purpose

Force a measured, honest ROI decision on a specific proposed optimization before any engineering time is spent — the antidote to premature optimization.

## Prompt Template

```
You are deciding whether a firmware optimization is worth doing, using measured numbers.

I have a proposed optimization:

- **What it changes:** [DESCRIBE THE OPTIMIZATION]
- **Budget it relieves + current headroom:** [FLASH/RAM/CYCLES/µA, and how much free]
- **Measured saving (from .map / profiler / ammeter):** [VALUE]
- **Estimated cost:** [DEV-HOURS, COMPLEXITY, MAINTAINABILITY HIT]
- **Regression risk / code path criticality:** [VALUE, e.g. safety path?]

Please:
1. State whether the relevant budget is actually tight; if not, recommend reject/defer and stop.
2. Quantify the saving and the cost on comparable terms.
3. Compute the ROI and give a do-now / defer-as-debt / reject verdict.
4. If do-now, specify the post-change measurement that confirms the saving and the tests that cover the risk.
```

## Expected Output

- A tight-budget yes/no gate (and an early exit if there's headroom)
- The saving and cost quantified
- An ROI verdict with reasoning
- The confirming re-measurement and required tests if proceeding
