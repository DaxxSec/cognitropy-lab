# /magnet-ramp-schedule

Lay out a magnet-utilisation calendar that respects training, persistent-mode dwell, controlled ramp-down, and quench-recovery buffers. Returns a per-magnet weekly schedule with explicit slack and a feasibility verdict.

## Inputs

- Magnet inventory: per magnet — Bmax (T), bore Ø (mm), home temperature (K), maximum safe ramp rate (T/s up, T/s down), training history (number of quenches, last quench date, current "trained" plateau)
- Planned high-field runs from `/sample-queue-plan`: per run — target field (T), dwell duration (h), required temperature, allowable angle/sweep policy
- Quench-recovery time per magnet (typical 24–72 h to retrain to design field plus a low-rate ramp policy for the next week)
- Calendar constraints (operator availability, helium-fill schedule, public-holiday blackouts)

## Steps

1. For each magnet, compute the *effective* maximum ramp rate as min(spec rate, training-derated rate). A magnet that quenched at 12 T while specced for 14 T must train back through 12 T at a reduced rate (typical 0.3 × spec) before resuming spec ramps.
2. Decompose each planned run into ramp-up + dwell + ramp-down windows; round up to the next 15-min slot.
3. Insert a fixed 4 h transfer/standby buffer between ramps on the same magnet to allow LHe top-up and operator handoff.
4. Insert a 60-min training-pulse window on Monday morning after any weekend that included a quench event.
5. Lay the windows onto a per-magnet weekly grid; resolve conflicts by priority (P0 > P1 > P2). Run a sanity pass: no two ramps overlap, no ramp ends after operator coverage stops.
6. Compute slack: hours of unscheduled magnet time per week. Aim for ≥15 % slack to absorb a single quench; flag the week if slack < 10 %.
7. Emit the schedule, a slack-vs-week chart, and the contingency plan for the most-loaded magnet (which runs to defer if it quenches).

## Output

Markdown report and a Mermaid Gantt diagram at `outputs/magnet-ramp-schedule-<YYYY-MM-DD>.md`:
- Per-magnet weekly window list with ramp class, dwell, and operator
- Total magnet hours used / available / slack
- Contingency plan: "if magnet X quenches on day Y, defer these runs in this order"
- Inputs forwarded to `/lhe-budget` (high-field hours drive dynamic burn)

## Notes

- Persistent-mode magnets dwell with zero ramping cost but the ramp-up + ramp-down still bookend the run; budget them.
- "Training" is real: the first ramp after a quench has a high quench probability *near the previous quench field*. De-rate by 5–10 % on the first ramp, then re-approach.
- Magnet ramp rate is field-dependent (slower near Hc2 of the wire); use the vendor curve, not a single number.
- If two cryostats share a magnet, the magnet is the constrained server in `/sample-queue-plan`; flag this explicitly.
