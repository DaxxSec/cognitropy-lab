# /clay-reclaim-balance

Model the studio's clay mass balance — trimmings, slurry, and failed pieces in vs. reclaimed clay out — to quantify the reclaim rate and the clay/water waste it eliminates.

## Inputs

- Clay purchased per period (kg).
- Estimated or measured loss streams: trimming shavings (% of thrown mass), throwing slurry, failed/recycled greenware, and bone-dry scrap.
- Whether a reclaim workflow exists (slaking buckets, plaster bats, pugmill) and its throughput.

## Steps

1. Tally inputs: clay in = purchased + reclaimed.
2. Tally loss streams: trimming typically removes ~10–30% of thrown mass depending on form; add slurry and fails. Classify each as **recoverable** (trimmings, slurry, unfired scrap — all reclaimable) vs. **unrecoverable** (bisque-fired rejects — cannot return to plastic clay).
3. Compute reclaim rate = recovered ÷ recoverable. A studio with no reclaim workflow sends recoverable clay to landfill — flag the gap.
4. Account water: reclaim re-wets dry scrap; estimate the water and the labor/energy (plaster drying, pugmill) the reclaim loop costs, so the net footprint benefit is honest.
5. Recommend the reclaim path sized to the recoverable stream (bucket-slake for small studios, pugmill above a throughput threshold).

## Output

`outputs/clay-balance-YYYY-MM-DD.md`: the mass-balance table (in, recoverable, recovered, landfilled), the reclaim rate, water accounting, and a sized reclaim-workflow recommendation.

## Notes

- Bisque-fired rejects are unrecoverable as clay — the lesson is to catch fails at the greenware stage, before the kiln's energy is spent on them.
- Reclaim is not free: it costs water, labor, and (with a pugmill) energy. Net it out rather than assuming reclaim is automatically greener.
