# /module-restoration

Bring a bricked or corrupt module back to life from the archived specimen — the conservator restoring a damaged mount to its original condition. The payoff of every archive-first discipline upstream.

## Inputs

- The non-responsive / faulted module and a **stable 13.0–13.5 V** supply
- The archived specimen from `/specimen-intake` (the exact original, ideally COMPLETE)
- (If needed) bench/BDM/boot-mode recovery hardware for the platform

## Steps

1. **Triage trivially first.** Check power, grounds, and the connector — rule out a wiring/comms cause before assuming a bad flash.
2. **Classify the damage.** No comms at all (likely bootloader/OS corruption) vs. comms-but-faulted (likely bad cal / checksum).
3. **Enter recovery.** For no-comms: force **boot mode / bootloader entry**, or go bench/BDM/JTAG if the bus path is dead.
4. **Restore the specimen.** Write back the **exact archived original** (not a substitute); re-seal checksums/CVN if the recovery path requires it.
5. **Verify & re-archive.** Confirm comms, CAL-ID/CVN, and readiness; archive the recovered known-good state as a fresh accession.

## Output

A `outputs/restoration-<vin-or-serial>-<date>.md`: damage classification, recovery path used, the specimen restored, and post-recovery verification — plus a fresh known-good accession.

## Notes

- **If the bootloader itself is corrupt**, software recovery may be impossible → bench/BDM hardware recovery, or replace the module then re-marry VIN/immobilizer.
- **If no specimen was ever archived**, you are reconstructing from the reference collection at best — document the (avoidable) provenance break and treat the result as a modified baseline.
- This command is the reason `/specimen-intake` is mandatory: restoration is only as good as the archive it draws from.
