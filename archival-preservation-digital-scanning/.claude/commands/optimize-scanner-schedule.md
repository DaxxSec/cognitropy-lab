# /optimize-scanner-schedule — Allocate jobs across capture stations

Assign the queued lots to the lab's heterogeneous capture stations over a planning window to minimize makespan (time to clear the batch) while respecting equipment and handling constraints.

## Inputs

- The sequenced queue from `/plan-digitization-queue` (or any lot list with image counts and material types).
- Station roster: each station's supported material types, max document size, throughput (images/hour) by material, and available hours per day.
- Constraints: lots that must stay on one station (color-managed set), operator certifications, and any fixed deadlines.

## Steps

1. **Build the compatibility matrix.** For each (lot, station) pair, mark feasible/infeasible from material type, max size, and operator certification. An overhead/planetary scanner handles bound volumes; a flatbed/copy stand handles loose sheets; a film/transparency scanner handles negatives — never cross these.
2. **Compute per-station job durations.** `duration = images / station_throughput_for_material`. Fragile lots inherit the handling multiplier from `context/references.md`.
3. **Schedule.** Model as unrelated-parallel-machines makespan minimization (R||Cmax). Use Longest-Processing-Time-first (LPT) as the baseline heuristic, then improve with local search (move/swap jobs that reduce the max-loaded station). For small instances note that this is NP-hard and LPT gives a bounded approximation.
4. **Honor pins and deadlines.** Keep color-managed sets on a single station; place deadline lots first and verify they finish in time — if not, surface the conflict rather than silently slipping.
5. **Level the load.** Report per-station utilization; flag any station > 90% (bottleneck) or < 50% (idle) and suggest one rebalancing move.
6. **Insert QA and maintenance windows.** Reserve target-chart shots at shift start and a calibration/maintenance block per station per day so the schedule is executable, not just theoretical.

## Output

`outputs/scanner-schedule-<window>.md`: a per-station, per-day assignment table; the makespan and per-station utilization; the heuristic used and its approximation note; deadline-conflict warnings; and the recommended rebalancing move. Optionally emit a CSV the lab can paste into its tracking sheet.

## Notes

- Throughput numbers are estimates — capture the *actual* images/hour after the first day and re-run; the schedule converges as real rates replace estimates.
- A single fragile, oversized, color-critical lot can dominate the makespan. If one job is the bottleneck, the fix is often splitting or outsourcing it, not reshuffling everything else.
- Don't optimize the operators into a treadmill. Sustainable pace beats a schedule that looks efficient and burns the team out — the schedule is input to a human plan, not a mandate.
