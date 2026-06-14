# /calibration-mount

Verify that a candidate calibration fits the vehicle's exact mechanical **"form"** — injectors, sensors, turbo, transmission — the way a mount is fitted to the specific animal's anatomy. A cal that flashes cleanly but doesn't fit the form is the classic source of phantom faults.

## Inputs

- Candidate cal file (selected via `/region-cal-map` + `/reference-collection`)
- The vehicle's **hardware inventory:** injector flow rate, MAF/MAP range, turbo/supercharger spec, transmission model, displacement, cam/VVT hardware
- The cal's hardware assumptions (definition metadata / scaling constants)

## Steps

1. **Inventory the form.** Confirm the actual installed hardware (don't assume the cal's defaults).
2. **Extract the cal's assumptions.** Injector slope/offset, MAF transfer function, boost hardware, trans model the cal was built around.
3. **Compare axis by axis.** Flag every mismatch between cal-assumed and installed hardware.
4. **Classify each mismatch:** benign (within range), correctable (legal, non-emissions scaling), or disqualifying (wrong injectors/trans → wrong cal).
5. **Verdict.** FIT / FIT-WITH-CORRECTIONS / DOES-NOT-FIT, with the specific axes and required corrections listed.

## Output

A `outputs/fitment-<vin>.md` report: hardware inventory, cal assumptions, per-axis comparison, and a clear fitment verdict that gates `/flash-session`.

## Notes

- **Injector and MAF mismatches are the #1 "chasing a lean code for a week" trap** — never flash past a disqualifying scaling mismatch.
- A transmission-model mismatch invalidates the shift/line-pressure tables → it is the wrong cal, not a tuning problem.
- Corrections here stay within legitimate, non-emissions scope; emissions tables route to `/emissions-legality-gate`.
