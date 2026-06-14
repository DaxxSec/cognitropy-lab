# /emissions-legality-gate

A **hard gate** that must pass before any flash: block changes to emissions-critical tables and OBD monitors for on-road vehicles, and confirm the jurisdictional legality of the intended calibration. This is the workspace's ethical and legal backstop.

## Inputs

- The proposed (sealed) calibration vs. the archived stock specimen (the diff)
- The vehicle's use case: **on-road** vs. **off-road / motorsport / closed-course / bench-research**
- The operating jurisdiction (from `/region-cal-map`)

## Steps

1. **Classify the use case.** On-road road-registered vehicle → strict gate. Documented dedicated off-road/motorsport/closed-course/bench → research scope (still documented, never sold as a road part).
2. **Diff for emissions-critical edits.** Compare proposed vs. stock for changes to: EGR, DPF/SCR/AdBlue, catalytic-converter & O2-sensor monitors, evap, readiness/OBD-monitor logic, defeat-style switches.
3. **Block on tamper.** For an on-road vehicle, **fail the gate** on any emissions-critical or monitor-defeat change. State exactly which table/monitor and why.
4. **Check jurisdictional legality.** Confirm the cal is appropriate and legal for the operating regime; flag CARB EO requirements for aftermarket parts where relevant.
5. **Record the verdict.** PASS (legitimate recalibration / replacement / restoration) or BLOCK, with the specific basis.

## Output

A `outputs/legality-<vin>.md` gate record: use-case classification, the emissions-critical diff, the jurisdiction check, and a PASS/BLOCK verdict. `/flash-session` refuses to run on a BLOCK.

## Notes

- **This gate is non-negotiable for road vehicles.** Disabling emissions controls or readiness reporting on a road car is illegal (Clean Air Act §203, CARB, and international equivalents) and out of scope for this workspace.
- A BLOCK is a correct outcome, not a failure of the run — surface the legal alternative (correct OEM cal, EO-approved part).
- Legitimate flashes still pass freely: TSB recalibration, replacement-module programming, and bricked-module restoration to stock are the normal PASS cases.
