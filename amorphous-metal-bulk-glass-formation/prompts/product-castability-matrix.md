# product-castability-matrix

## Purpose

Build the product × alloy castability matrix that underpins capacity planning: which products can be made amorphous in which alloy, gated by minimum-cooling section vs Dmax. Use at the start of run/quarter planning, before allocating capacity.

## Prompt Template

```
You are a BMG foundry process engineer building a castability matrix for production planning.

Inputs:

- **Products (name, min-cooling section mm, demand/period):** [VALUE]
- **Available alloys (name, Dmax, cost/precious-metal content):** [VALUE]
- **Per-product yield estimates, if known:** [VALUE]
- **Context:** [feedstock/supply constraints, safety constraints e.g. Be]

Please:
1. Build the product × alloy matrix; mark each cell feasible only if min-cooling section < Dmax (with margin).
2. For feasible cells, attach yield and cost; pick the cheapest feasible alloy per product unless flagged.
3. Flag products infeasible in every alloy (section > all Dmax) and propose redesign / higher-GFA alloy / decline.
4. Flag products feasible only in a costly or Be-bearing alloy as cost/safety trade-offs.
5. Summarize total castable demand per alloy to feed capacity allocation.
```

## Expected Output

- A product × alloy castability matrix (feasible/marginal/infeasible).
- Recommended alloy per product with yield and cost.
- Infeasible products with redesign/alloy options.
- Per-alloy castable-demand summary for the capacity step.
