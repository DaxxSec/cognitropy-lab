# /identify-device

Fingerprint the iOS device — model, SoC generation, and iOS version — and map those facts to the extraction methods that are actually viable. This is the first technical step after isolation.

## Inputs

- Model identifier or markings (e.g. `iPhone12,1`, model number `A2111`, "iPhone 11").
- iOS/iPadOS version if visible or recoverable (Settings, or `ideviceinfo`).
- Whether a forensic host with `libimobiledevice` / commercial tooling is available.
- Any reachable identifiers (UDID, serial, ECID) — record a hash, not the raw value, in committed notes.

## Steps

1. Resolve the marketing name and **SoC generation** from the model identifier (see `context/references.md` SoC table).
2. Decide **checkm8 eligibility** — A5–A11 yes, A12+ no — and note the consequence for method choice.
3. Pin the **iOS version**; flag whether known commercial exploit chains cover it (note unknowns rather than guessing).
4. From SoC + iOS, list the **candidate methods** (logical / FFS / agent / checkm8) and strike out the impossible ones.
5. Cross-check against the current lock state (defer hard ceiling to `/assess-lock-state`).

## Output

`outputs/device-profile-YYYY-MM-DD.md`: marketing name, model id, SoC, iOS version, checkm8 eligibility (Y/N), candidate methods (with eliminated ones and why), and a UDID **hash** for case linkage.

## Notes

- A model number can map to multiple SoCs across regions — confirm the SoC, not just the name.
- Do not power-cycle to read a version string on an AFU device; use a wired query that doesn't reboot.
