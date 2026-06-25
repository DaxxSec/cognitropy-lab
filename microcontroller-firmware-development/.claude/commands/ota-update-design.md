# /ota-update-design

Design the field-update path — bootloader, OTA, or USB DFU — trading flash footprint and complexity against robustness and security, with authentication treated as non-negotiable rather than a cost to cut.

## Inputs

- Update channel (wired DFU, BLE/Wi-Fi OTA, gateway), update frequency, and field accessibility
- Flash budget for bootloader + dual-bank/staging, and the security requirement
- Failure tolerance (can a bad update brick the device?)

## Steps

1. Choose the **topology**: single-bank with a bootloader (cheap flash, riskier) vs **dual-bank/A-B** (safe rollback, ~2× app flash).
2. Size the **bootloader + staging** against the flash budget; this is the footprint cost of updatability.
3. Specify **authentication**: signature verification of every image (and encryption if the firmware is confidential) — this is required, not optional.
4. Design **power-fail safety**: an interrupted update must leave a bootable image (staging + verify-before-swap).
5. Decide the trade and record it; if flash is too tight for safe dual-bank, resolve via budget (`/budget-flash-ram`) — never by dropping verification.

## Output

`outputs/projects/<name>/ota-design.md` — the chosen topology, flash footprint, the authentication/encryption scheme, the power-fail-safe flow, and the cost trade behind the choice.

## Notes

- **Skipping signature verification to save flash is a vulnerability, not an optimization** — it is off the table.
- Single-bank saves flash but risks a brick on a failed update; price that risk honestly against the dual-bank footprint.
