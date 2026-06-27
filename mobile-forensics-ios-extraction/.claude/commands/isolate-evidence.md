# /isolate-evidence

Execute the seizure-time isolation protocol: cut RF, keep power, and capture any reachable pairing/lockdown record before the device leaves the scene. Time-critical — run this first.

## Inputs

- Physical custody of the device and its as-seized state (screen on/off, locked/unlocked).
- Availability of a Faraday bag/enclosure and an in-bag power source.
- Any seized paired host (laptop/desktop) that may hold a lockdown/pairing record.
- Scene constraints (can power be maintained? is a shielded room available?).

## Steps

1. **Cut RF** — place the device in a Faraday bag/enclosure to prevent remote wipe and network-driven state change. If isolation is impossible, document why and enable Airplane Mode as a last resort (note that this requires interaction).
2. **Maintain power** — connect a charger inside the isolation; an AFU device that dies drops to BFU.
3. **Capture pairing/lockdown records** — from any seized paired host, preserve the lockdown record (escrow keybag) that can bypass USB Restricted Mode and unlock encrypted backups. Hash and log it.
4. **Document as-seized state** — photograph the screen, record lock state, time, and battery level into the custody log *before* any change.
5. **Hand off** to `/identify-device` and `/assess-lock-state` without rebooting.

## Output

`outputs/isolation-log-YYYY-MM-DD.md`: isolation method, power status, as-seized state (with timestamp), pairing-record capture result (hash), and any deviations (e.g. Airplane Mode used) with justification.

## Notes

- A lockdown record is perishable leverage — expires/rotates; capture it early.
- Never connect the device to a network "just to back it up to iCloud"; that risks remote wipe and out-of-scope data.
