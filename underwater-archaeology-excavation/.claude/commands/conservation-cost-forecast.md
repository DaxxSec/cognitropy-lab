# /conservation-cost-forecast

Forecast the lifetime conservation **and** perpetual curation cost of a proposed recovered assemblage — usually the largest line in the whole CBA.

## Inputs

- Proposed finds inventory by material (waterlogged wood, marine iron, leather, bone, ceramic, copper alloy, glass) and approximate quantity/size.
- Conservation-lab rates or per-object/per-kg estimates, and treatment timescales.
- Curation parameters: storage cost per unit per year, climate-control requirement, expected access/loan activity.
- Discount rate and curation horizon (treat perpetuity as a long horizon, e.g. 50–100 years, discounted).

## Steps

1. Read `context/references.md` ("Conservation Treatment Lookup") and map each material class to its treatment and timescale.
2. Estimate **active conservation cost** per material class (lab-time × rate, scaled by size/fragility); large waterlogged timbers and heavily-concreted iron dominate.
3. Estimate **curation cost** as an annuity: annual storage/documentation cost × the discounted horizon.
4. Sum to **present-value lifetime cost** at the stated discount rate.
5. Compute conservation+curation as a **multiple of the fieldwork (dive-budget) cost** — this ratio is the headline that prevents under-budgeting.
6. Flag any material the available conservation capacity cannot actually treat — those items must not be lifted.
7. Feed the present value into `/insitu-vs-excavate` and `/recovery-prioritization`.

## Output

`outputs/conservation-forecast-<site>-YYYY-MM-DD.md`: per-material cost table, the present-value total, the conservation-to-fieldwork multiple, the discount-rate assumption, and an explicit capacity-vs-demand check.

## Notes

- UNESCO 2001 Annex Rules 9–13 and 25 require conservation/curation funding to be **secured before fieldwork** — model it as a precondition, not a hope.
- Curation is forever; even small annual figures compound into a large discounted liability — never treat it as a one-off.
- "We'll conserve it later" is how conservation backlogs are created. If capacity isn't booked, recommend leaving the material in situ.
