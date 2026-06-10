# /forecast-roast-schedule

Turn a roasted-SKU demand forecast into a green-consumption plan and a batch-by-batch roast schedule, drawing green inventory down FIFO.

## Inputs

- Roasted-SKU demand for the horizon (sales history or forecast), including blend SKUs (with recipes from `/build-blend-recipe`).
- Per-SKU yield (from `/calc-roast-loss`) to convert roasted demand to green.
- Roaster capacity: batch size, batches/day, operating days; profile per SKU (group same-profile batches).
- Current green on-hand by lot with crop year and arrival date (from `/track-green-lot`), for FIFO ordering.

## Steps

1. Read `context/workflows.md` (Workflow C) and `context/references.md` ("green needed = roasted demand ÷ yield").
2. Explode blend SKUs into component green demand via their recipes; sum green demand per lot/origin.
3. Convert roasted demand to **green needed** per SKU/component (÷ yield). Aggregate the green requirement over the horizon.
4. Allocate green to demand **FIFO** (oldest in-spec, in-crop first); note where a lot will be exhausted mid-horizon and the next lot takes over.
5. Lay batches onto the calendar within roaster capacity, sequenced by profile (minimize re-dialing) and by FIFO; count batches/day vs capacity.
6. Hand the per-lot green requirement and exhaustion dates to `/plan-green-reorder`; save the schedule.

## Output

`outputs/schedules/roast-schedule-<period>.md` — roasted demand → green needed per lot, the FIFO allocation with lot-exhaustion dates, the batch-by-batch calendar within capacity, and the green-requirement handoff to reorder planning.

## Notes

- Always gross roasted demand up by 1/yield — scheduling on roasted weight under-buys green by the roast-loss %.
- FIFO must respect *spec*, not just date: skip a stale/off-aw lot even if it's oldest, and flag it for disposition.
- If capacity can't meet the schedule, surface the shortfall early (add days, larger batches, or trim/sequence SKUs) rather than silently slipping.
