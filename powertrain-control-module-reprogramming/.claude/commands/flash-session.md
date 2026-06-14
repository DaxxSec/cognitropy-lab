# /flash-session

Execute the controlled write — the actual "mounting" of the calibration onto the module — with a rollback plan armed and a verification gate at the end. The one irreversible-if-careless moment, performed with full preservation discipline.

## Inputs

- A **sealed** image (`/checksum-seal` PASS) that **fits the form** (`/calibration-mount` FIT) and **cleared legality** (`/emissions-legality-gate` PASS)
- A verified archived specimen on file (`/specimen-intake` COMPLETE preferred)
- Stable **13.0–13.5 V** supply; correct J2534 VCI / OEM tool; security access (licensed)

## Steps

1. **Pre-flight gate.** Refuse to proceed unless specimen archived, fitment FIT, legality PASS, image sealed, and voltage stable. Abort and name the missing gate otherwise.
2. **Arm rollback.** Confirm the exact stock specimen is ready to re-flash, and `/module-restoration` is understood as the recovery path.
3. **Establish session.** UDS programming session (0x10), security access (0x27), erase (RoutineControl 0x31), RequestDownload (0x34).
4. **Write.** Stream the image (TransferData 0x36), RequestTransferExit (0x37); **do not interrupt** — hold power steady throughout.
5. **Reset & verify.** ECUReset (0x11); re-read CAL-ID/CVN to confirm the new image took; confirm comms and no new hard faults.
6. **Drive/verify readiness.** Begin OBD readiness-monitor verification; log the event.

## Output

A `outputs/flash-log-<vin>-<date>.md`: pre-flight gate results, before/after CAL-ID & CVN, tool/voltage, write result, and readiness-verification status. The new known-good state is then filed via `/reference-collection`.

## Notes

- **If voltage drops or the write is interrupted → stop and go straight to `/module-restoration`.** This is exactly the scenario archive-first protects against.
- Verify CVN/CAL-ID actually changed — a "successful" tool message without an identifier change means the write didn't land.
- Never flash on a failed gate; the gates exist because this step is the dangerous one.
