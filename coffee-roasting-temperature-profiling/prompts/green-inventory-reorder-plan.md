# Green Inventory Reorder Plan

## Purpose

Use to turn a roast forecast and current green on-hand into a reorder plan with par levels, reorder points, and crop-year staleness flags. Pairs with `/plan-green-reorder` and `/forecast-roast-schedule`.

## Prompt Template

```
You are a green-inventory planning agent in the coffee-roasting-temperature-profiling workspace.
Read context/concepts.md ("Inventory control", "Green coffee") and context/workflows.md (Workflow C) first.

Build a reorder plan from this data:

- **Horizon:** [e.g. next 8 weeks]
- **Roasted-SKU demand / forecast:** [per SKU; include blends]
- **Per-SKU yield:** [or "use measured yields in outputs"]
- **Green on-hand by lot:** [lot ID, qty, crop year, arrival date]
- **Supplier lead times & variability:** [per origin]
- **Service level:** [e.g. 95% → z]
- **Market context:** [current C-price / differential notes, if relevant]

Please:
1. Convert roasted demand to green needed per lot (÷ yield).
2. Compute lead-time demand, safety stock, reorder point, and par per lot.
3. Project on-hand forward; give each lot's stock-out date and reorder-now vs later.
4. Flag lots crossing into past-crop before consumption (staleness, independent of stock-out).
5. Recommend order sizes and procurement path (spot vs forward) with the cost basis.
```

## Expected Output

- Per-lot ROP / par / safety stock and projected stock-out date.
- Crop-year staleness flags separate from stock-out risk.
- A prioritized action list (reorder now / monitor / draw down faster / push to blend) with order sizes.
- A procurement note (spot vs forward, C-market + differential) per reorder.
