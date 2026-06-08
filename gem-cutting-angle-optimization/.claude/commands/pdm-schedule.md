# /pdm-schedule — Build the Predictive-Maintenance Plan

Consolidate all condition trends (spindle runout, lap wear, vibration, index repeatability) into one dated, prioritized maintenance queue that keeps the machine permanently inside the angle tolerance the optimization assumes.

## Inputs

- Latest trend outputs: `/spindle-runout-trend`, `/lap-wear-forecast`, plus any vibration RMS and index-repeatability readings.
- The machine baseline and the design tolerance currently being targeted.
- Calendar constraints (upcoming jobs, parts lead times).

## Steps

1. Gather each indicator's current status, RUL, and P-point from its trend file.
2. For each, place the intervention **inside the P-F interval** — late enough not to waste life, early enough to act before functional failure.
3. **Batch** interventions whose windows overlap (e.g. dress lap + service spindle in one teardown) to minimize machine downtime.
4. Prioritize by angle-budget impact: the dominant tolerance-budget source (from `/tolerance-budget`) is serviced first.
5. Account for parts lead time — order bearings/laps so they arrive before the scheduled date.
6. Produce a dated queue with each task, trigger, target date/hours, and the budget consequence of deferring it.
7. After any completed work, prompt a re-baseline so trends reset against a known-good machine.

## Output

A maintenance schedule table: task, triggering indicator, P-point, target date/hours, priority, parts needed, and deferral risk. Save to `outputs/pdm-schedule.md` and update after each service.

## Notes

- This is predictive, not preventive: tasks are triggered by *trends crossing thresholds*, not by the calendar. A flat, well-under-threshold indicator should push its interval out, not trigger needless work.
- Re-baseline after every intervention — a schedule built on stale baselines drifts into reactive maintenance.
- The whole point: no stone is ever cut on a machine that has silently left the tolerance band its design requires.
