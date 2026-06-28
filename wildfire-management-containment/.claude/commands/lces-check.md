# /lces-check — LCES & Go/No-Go Safety Gate

Build and verify the LCES package — Lookouts, Communications, Escape Routes, Safety Zones — for a division/assignment and run the go/no-go gate before any crew commits. This command is a hard stop, not a checklist for the record.

## Inputs

- The division/assignment and the resources about to be committed
- Current and forecast fire behavior (flame length, ROS, spotting, wind shift timing)
- Terrain and fuels around the assignment; available roads/black/openings
- Radio plan / frequencies in use

## Steps

1. **Lookout(s):** identify a posted lookout with a clear view of the fire and the crew, briefed on trigger points. If none can be posted → fail.
2. **Communications:** confirm the radio frequency, that all resources can hear/be heard, and the check-in cadence. Untested comms → fail.
3. **Escape Routes:** identify at least one (prefer two) escape route to the safety zone; **time** the walk under fatigue/uphill and re-time as behavior changes. Escape time must beat fire arrival with margin.
4. **Safety Zones:** verify a safety zone sized for the flame length (separation distance scales with flame height; the black or a large opening). Inadequate size → fail.
5. Run the **go/no-go** tree (Decision Tree 3): 10 Orders followed? Any Watch Outs unmitigated? LCES set & communicated? Instructions understood?
6. Output **GO** (with mitigations) or **NO-GO** with the specific failed element and what would have to change.

## Output

A go/no-go record to `outputs/lces-<division>-<date>.md`: the four LCES elements with concrete details (who/where/frequency/timed route/zone size), the go/no-go determination, and any required mitigations. A NO-GO names the exact failure.

## Notes

- "We'll watch it" is not a mitigation. A named lookout, a tested frequency, a timed route, and a measured zone are.
- Re-run on any material change in fire behavior — LCES is dynamic; escape times shrink as ROS climbs.
- A single unmitigated NO is a stop. Defending property never overrides this gate.
