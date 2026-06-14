# /specimen-intake

Read, hash, and archive the factory calibration **before any edit** — the conservator's "study skin." This is the mandatory first step; no flash may proceed without a verified specimen on file.

## Inputs

- Connected module (J2534 VCI or bench rig) and a **stable 13.0–13.5 V supply**
- Read access (security access where required, licensed)
- (Optional) tool that can reach all flash regions vs. calibration region only

## Steps

1. **Pre-check power.** Confirm supply voltage 13.0–13.5 V; abort if marginal — under-voltage reads/flashes are how modules die.
2. **Capture identifiers.** Record VIN, CAL-ID (Mode 09 PID 04), CVN (Mode 09 PID 06), ECU HW/SW numbers, and read date/tool.
3. **Full read.** Read the module image — all regions if possible (bootloader/OS/cal/VIN), at minimum the full calibration region. Note what was *not* readable.
4. **Hash it.** Compute SHA-256 (or platform standard) of the image file.
5. **Accession.** Write image + hash + identifiers + read notes to `outputs/specimens/<vin-or-serial>-<date>/`, then **re-hash the saved file and confirm the match** before declaring the specimen archived.

## Output

An accession folder in `outputs/specimens/` containing the raw image, its hash, an `accession.md` with all identifiers and read coverage, and a clear `COMPLETE` / `PARTIAL` flag. This is the artifact `/module-restoration` and `/flash-session` depend on.

## Notes

- A `PARTIAL` read (bootloader unreachable) is still worth archiving — but mark restoration risk as elevated.
- If the module won't communicate at all, you may already have a damaged specimen → go to `/module-restoration`.
- Never overwrite an existing specimen file; archive every read as a new dated accession.
