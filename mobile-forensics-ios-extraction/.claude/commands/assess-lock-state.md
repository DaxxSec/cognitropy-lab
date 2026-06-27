# /assess-lock-state

Determine whether the device is **Before First Unlock (BFU)** or **After First Unlock (AFU)**, and enumerate exactly what is decryptable in the current state. This sets the ceiling for everything downstream.

## Inputs

- Observed device state: powered on/off as seized; was it ever unlocked since boot in your custody?
- Passcode condition: known / unknown / none / biometric-only.
- Time since last unlock (for USB Restricted Mode estimation).
- Output of `/identify-device`.

## Steps

1. Classify state: if unlocked at least once since boot → **AFU**; if only powered on, never unlocked → **BFU**.
2. Map state to **Data Protection reachability** — AFU exposes Class C (most user data); BFU exposes Class D only (see `context/references.md`).
3. Estimate **USB Restricted Mode** status (≈1 hour locked) and whether a pairing/lockdown record could restore data access.
4. Mark the state as **perishable**: state the events (reboot, power loss, prolonged idle) that would drop AFU → BFU and what data each would forfeit.
5. Recommend the urgency tier and the immediate next action (acquire now vs. hold + isolate).

## Output

`outputs/lock-state-YYYY-MM-DD.md`: BFU/AFU determination with justification, decryptable-class summary, USB-Restricted-Mode estimate, perishability warning, and urgency tier (High/Hold).

## Notes

- AFU is a melting ice cube — never recommend a reboot "to check" anything.
- "Locked screen" ≠ BFU. A locked-but-previously-unlocked device is still AFU and still rich.
