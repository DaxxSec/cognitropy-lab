# /checksum-seal

Recompute and correct the calibration/module checksums and CVN after edits so the flash is accepted and durable — the conservator's "sealing and finishing" step that makes the mount hold. An unsealed cal is rejected or flagged as tampered.

## Inputs

- The edited calibration image (post `/calibration-mount`, post any legal corrections)
- The platform's checksum/CVN scheme (tool-integrated or platform routine)
- The original specimen for before/after comparison

## Steps

1. **Identify the integrity scheme.** Which regions carry checksums, and how CVN is computed for this platform.
2. **Diff against the specimen.** Confirm *only* the intended tables changed (no stray edits) by comparing to the archived stock image.
3. **Recompute checksums** for every affected region.
4. **Recompute / update the CVN** so it is valid for the new cal.
5. **Verify.** Re-validate the whole image's integrity values; confirm the bootloader/OS will accept it.

## Output

A sealed, flash-ready image written to `outputs/` with a `seal-report.md`: the regions changed, old vs new checksum/CVN values, and a clean/again-sealed confirmation.

## Notes

- **Do this last**, after every cal edit — an unsealed image either won't flash or runs in a fault/limp mode.
- The diff-against-specimen step catches accidental edits before they reach the module.
- A correct CVN is required for `/emissions-legality-gate` and for honest provenance — it is not a way to disguise an emissions edit (the gate runs separately and independently).
