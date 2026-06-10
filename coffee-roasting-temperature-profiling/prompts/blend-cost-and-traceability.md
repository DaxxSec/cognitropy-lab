# Blend Cost & Traceability

## Purpose

Use to compose and cost a blend on roasted weight and produce its full per-component traceability/certification statement. Pairs with `/build-blend-recipe` and `/track-green-lot`.

## Prompt Template

```
You are a blend-costing agent in the coffee-roasting-temperature-profiling workspace.
Read context/concepts.md ("Roasted costing", "Inventory & supply-chain model") first.

Compose, cost, and document this blend:

- **Blend SKU & target ratio:** [e.g. House Espresso, 60/30/10]
- **Roast model:** [pre-blend (each to own profile) | co-roasted (one profile)]
- **Components (per lot):** [lot ID, origin chain, landed green cost, measured yield, roast level, on-hand qty, crop year, certs]
- **Target output (roasted):** [qty]
- **Batch size:** [VALUE]

Please:
1. Convert the roasted target to green needed per component (÷ each yield).
2. Cost each component on roasted weight; give the blended cost/kg and the gap vs a naive green-price estimate.
3. Check feasibility against on-hand; identify the binding component (first to reorder/stale).
4. Produce the per-component traceability statement and the defensible certification claim (or why a claim can't be made).
5. Show the inventory drawdown per component.
```

## Expected Output

- Per-component green-needed and roasted cost, plus blended cost/kg and the vs-naive gap.
- A feasibility verdict and the binding component.
- A complete per-lot genealogy and the substantiable certification claim (with mass-balance note).
- The inventory drawdown and a re-balance flag if a component is near exhaustion.
