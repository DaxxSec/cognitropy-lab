# Extraction Method Selection

## Purpose

Given a device fingerprint, lock state, and legal authority, recommend the extraction method with explicit trade-offs and a "do-not" list. Use after `/identify-device` and `/assess-lock-state`, before acquiring.

## Prompt Template

```
You are planning an iOS acquisition. Recommend the least-invasive method that answers the question.

- **Device / SoC:** [e.g. iPhone 11 / A13]
- **iOS version:** [VALUE]
- **Lock state:** [BFU / AFU]
- **Passcode:** [known / unknown / none]
- **Data of interest:** [Messages / app sandbox / Health / deleted records / etc.]
- **Legal scope:** [WHAT THE AUTHORITY COVERS]
- **Tooling available:** [open / commercial list]

Please:
1. Eliminate methods the SoC/iOS/lock-state forbid, with reasons.
2. Among feasible methods, identify which actually yield the data class of interest (note logical vs encrypted-backup vs FFS coverage).
3. Recommend the least-invasive sufficient method and justify it.
4. List the operational do-NOTs (e.g. do not reboot an AFU device) and expected Data Protection class coverage for verification.
```

## Expected Output

- A ranked feasibility list with eliminations explained.
- A single recommended method with rationale and trade-offs.
- An expected class-coverage target and an explicit do-not list.
