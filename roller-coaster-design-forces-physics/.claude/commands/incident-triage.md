# /incident-triage

Walk an inbound rider complaint or sensor event through the `I-*` decision tree (`context/workflows.md` §4) and bin it as NUISANCE / MONITOR / HOLD / PULL_FROM_SERVICE.

## Inputs

- `ride_name`, `element_id` (best guess if rider can't name it).
- `complaint_type` — `head-bang | lateral-strike | restraint-bruise | vestibular | eject-event | hardware`.
- `rider_position` — `front | mid | back | unspecified`.
- `injury_reported` — boolean (medical attention requested OR visible injury).
- `sensor_window` — `(t_start, t_end)` or null.
- `event_count_this_week` — running count of matching events on this element.

## Steps

1. Run `I-0` intake. De-identify any PII / PHI in the complaint text **before** writing anything to `outputs/`.
2. Apply `I-1` injury gate. If injured, bin = HOLD and proceed straight to `I-5` (skip sensor work; that's for the post-hold root-cause).
3. Apply `I-2`. If hardware-related, route to maintenance queue; bin = HOLD until cleared.
4. Apply `I-3`. If sensor data is available for the window, invoke `/force-envelope-check` and `/jerk-budget-audit` and use their verdicts to set the bin.
5. If no sensor data, apply `I-4` pattern match against this week's event count.
6. Emit `I-5` — bin + reasoning trail + recommended next action.
7. Persist to `outputs/incidents/<ride>-<YYYYMMDD-HHMM>-<bin>.md`.

## Output

Markdown file containing:
- Anonymised complaint summary.
- Path through I-tree with node ids.
- Bin verdict + recommended next action (instrument sensor, escalate to maintenance, monitor frequency, pull from service).
- Cross-reference to `/force-envelope-check` and `/jerk-budget-audit` walks if invoked.

## Notes

- The injury gate (`I-1`) is **always first**. Bin overrides cannot waive it.
- "5 events" in `I-4` is the typical industry threshold; operator policy may differ. Make the threshold a per-ride config knob, not a hard-coded constant.
- Back-car / front-car distinction at `I-0` matters because envelope-check is usually run on the train's average-position trace; back-car negative-g can exceed mid-car by ~30%.
- The output of this command becomes part of the operator's incident log. Treat it as evidentiary, not internal-only.
