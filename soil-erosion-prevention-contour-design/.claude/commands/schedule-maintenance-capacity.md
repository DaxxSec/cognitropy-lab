# /schedule-maintenance-capacity

Turn time-varying capacity loss into an operable maintenance calendar — basin cleanout, channel re-grading, revegetation — driven by each structure's remaining capacity, not the calendar alone.

## Inputs

- The designed structures with their storage/conveyance capacities and drawdown rates (sediment accumulation from `/plan-sediment-basin`, cover/vegetation degradation, channel sedimentation).
- Utilization-threshold triggers (e.g. clean basin at 50–60% storage filled; re-vegetate when cover drops below the C assumed in design).
- Inspection frequency and any seasonal constraints (planting/harvest, freeze, wet season).
- Budget/labor constraints on intervention cadence.

## Steps

1. Read `context/concepts.md` "The capacity-planning analogy" (capacity drawdown / refresh) and `context/workflows.md` Phase 8.
2. For each structure, model remaining capacity over time from its drawdown rate; mark the time it hits its **trigger utilization**.
3. Convert triggers into scheduled actions: basin cleanout (restores live storage), terrace channel re-grading (restores grade/conveyance), waterway revegetation (restores permissible velocity / Manning n), check-dam sediment removal.
4. Set **inspection** checkpoints ahead of each trigger and after every storm above a threshold return period (condition-based, not just time-based).
5. Sequence the calendar around seasonal constraints; flag where two refresh actions collide and should be batched.
6. State the consequence of a missed refresh per structure (e.g. trap-efficiency collapse, scour, breach) so deferral is an informed decision.

## Output

`outputs/maintenance/capacity-schedule-<system>-YYYY-MM-DD.md` — per-structure remaining-capacity timeline, trigger dates/utilizations, the action calendar with inspection checkpoints, seasonal sequencing, and missed-refresh consequences.

## Notes

- Maintenance is condition-based first, calendar-based second — a post-storm inspection can move a trigger forward; don't wait for the date.
- An unfunded cleanout cadence means the design's real capacity is whatever it silts to — surface that explicitly to the owner.
- Re-run after any `/stress-test-design-storm` change, since reinforcing the bottleneck shifts which structure drives the schedule.
