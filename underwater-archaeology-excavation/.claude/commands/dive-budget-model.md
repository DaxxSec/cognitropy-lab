# /dive-budget-model

Convert a fieldwork plan into a costed estimate, accounting for the decompression overhead that makes underwater excavation expensive.

## Inputs

- Target site depth and water temperature.
- Total productive bottom-time required (person-hours of excavation/recording).
- Team size, dive mode (SCUBA / surface-supplied / mixed gas / ROV), and shift pattern.
- Day-rates: vessel, dive team, equipment; mobilisation/demobilisation cost.
- Weather/sea-state downtime allowance (fraction of days lost).

## Steps

1. Read `context/references.md` ("Diving Access vs. Cost Multiplier") to fix the access mode and its cost multiplier for the site depth.
2. Compute **effective bottom time per diver per day**: no-decompression limit (or planned-deco profile) at depth, number of dives/day, minus descent/ascent/deco overhead. This is the productivity, not the clock.
3. Divide required productive bottom-time by effective per-diver-day productivity × team size → **diver-days**.
4. Convert diver-days to **calendar days** by adding weather downtime and surface logistics; round up to charter blocks.
5. Cost it: calendar days × (vessel + team + equipment day-rates) + mobilisation/demobilisation.
6. If depth forces ROV/AUV mode, re-base the model on vehicle/vessel-days instead of diver-days and note the productivity change.
7. Carry the result forward as the *fieldwork* line of the lifecycle CBA — explicitly not the whole cost.

## Output

`outputs/dive-budget-<site>-YYYY-MM-DD.md`: a table of bottom-time assumptions, derived diver-days and calendar days, the cost build-up, and a sensitivity note on the two biggest drivers (usually depth/deco overhead and weather downtime).

## Notes

- Decompression overhead is non-linear in depth — a 45 m site can have a fraction of a 25 m site's productive bottom time per dive.
- Weather downtime dominates open-water budgets; model it as a probability, not a point estimate.
- Productive bottom time, not gross dive time, is the unit that does archaeological work — never cost the latter.
