# /plan-green-reorder

Compute par levels, reorder points, and lead-time demand for each green lot/origin from the roast schedule, and flag lots projected to stock out or cross into past-crop before they are consumed.

## Inputs

- Green demand per lot/origin (from `/forecast-roast-schedule`, grossed up by 1/yield).
- Supplier lead times and their variability; demand variability (σ) per origin.
- On-hand quantity, crop year, and arrival date per lot (from `/track-green-lot`).
- Service-level target (→ z for safety stock); holding and order-cost estimates if sizing EOQ.

## Steps

1. Read `context/concepts.md` ("Inventory control") and `context/references.md` (ROP / safety-stock / EOQ formulas).
2. For each lot/origin: compute **lead-time demand** = avg demand × lead time, **safety stock** = z·σ over lead time, and **ROP** = lead-time demand + safety stock.
3. Project on-hand forward against the schedule; find the stock-out date and compare to lead time → reorder-now vs later.
4. Overlay the **crop-year clock**: will the lot cross into past-crop before it's consumed? Flag staleness risk independent of stock-out.
5. For reorders, note the procurement path (spot vs forward) and how current C-market + differential moves landed cost; size the order (EOQ or par top-up).
6. Produce a prioritized action list: reorder now / monitor / draw down faster / push to blend.

## Output

`outputs/inventory/reorder-plan-YYYY-MM-DD.md` — per-lot ROP, par, safety stock, projected stock-out date, crop-year staleness flag, recommended action and order size, and the procurement note (spot/forward, cost basis). Re-run weekly.

## Notes

- Green has a freshness clock, so "more safety stock" isn't free — balance stock-out risk against staleness/holding cost.
- A lot can be over-stocked *and* at risk: plenty on hand but aging past-crop. Surface both, not just the stock-out.
- Substituting a comparable green to dodge a stock-out invalidates the existing golden profile — re-validate via Workflow A / `/match-profile-batch`.
