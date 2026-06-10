# /calibrate-roaster

Calibrate the bean-probe against environmental temperature, characterize probe lag, and establish reference points so profiles are reproducible batch-to-batch and comparable machine-to-machine.

## Inputs

- Machine make/model, probe type/diameter and placement, datalogger/software.
- Reference checks: ice-point (0 °C) and boiling-point (~100 °C, altitude-adjusted) probe readings; local altitude.
- A reference roast log on this machine (to characterize TP timing and RoR responsiveness).
- The date of last calibration, if any.

## Steps

1. Read `context/concepts.md` ("Temperature measurement, RoR") and `context/references.md` (cheat-sheet: ice/boiling references).
2. Verify the BT probe at ice point and boiling point; record offset/drift. Compute the altitude-adjusted boiling point.
3. Note probe lag: a heavier/recessed probe reads slower — describe how it shifts apparent marker temps and RoR.
4. Run/inspect a reference roast; record this machine's *characteristic* charge, TP, dry-end, FC, and drop BT for a known coffee — these become the local reference, not absolute truth.
5. Document the calibration (date, offsets, probe spec) and stamp it onto profiles roasted afterward.
6. If comparing to another machine, build an offset note (this machine's FC vs the reference machine's FC) so profiles can be translated.

## Output

`outputs/calibration/<machine>-YYYY-MM-DD.md` — probe offsets, altitude-adjusted boiling reference, characteristic markers for a reference coffee, probe-lag note, and any cross-machine offset. Referenced by every profile/batch from this machine.

## Notes

- Without this, "FC at 198 °C" is not portable; reproducibility is defined *relative to a calibrated reference*, never as absolute °C.
- Re-calibrate after a probe change, repair, or relocation — these are the usual causes of sudden batch drift in `/match-profile-batch`.
- Calibration is about *comparability*, not making your numbers match someone else's machine.
