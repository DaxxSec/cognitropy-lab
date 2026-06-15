# Unidentified Emitter Intake

## Purpose

Turn a raw, unexplained detection into a structured candidate KB entry and a concrete identification plan — used when a sweep surfaces a signal you can't yet name and you want it captured (with provenance) before it's forgotten.

## Prompt Template

```
You are the RF spectrum knowledge engineer for this workspace. I have an unidentified detection to triage into a candidate KB entry.

Detection:
- **Center frequency:** [e.g. 868.30 MHz]
- **Occupied bandwidth:** [e.g. ~125 kHz]
- **Power / level:** [e.g. -78 dBm peak, floor at -110 dBm]
- **Temporal behavior:** [continuous / bursty / hopping; duty cycle if known]
- **Waterfall fingerprint:** [what it looks like — rails / chirp / OFDM block / noise-like]
- **Capture settings (provenance):** [hardware, sample rate, gain, antenna, location, timestamp]
- **Region:** [ITU region + country]

Please:
1. Rule out receiver artifacts first (image, harmonic, intermod, spur) and say how confident you are it's a real emitter.
2. Use band-plan allocation + fingerprint to propose ranked candidate identities, each with the evidence for/against and a confidence (`probable`/`unidentified`).
3. Draft a schema-compliant candidate entry (per context/references.md), leaving `identification` honest about uncertainty.
4. Give a concrete next-step ID plan: what single capture or decode would most cheaply raise confidence.
```

## Expected Output

- An artifact-vs-real verdict with reasoning
- A ranked candidate-identity list with per-candidate evidence and confidence
- A draft entry ready for `/emitter-entry-author` review (saved under `outputs/kb/_drafts/`)
- A prioritized identification plan (the cheapest experiment that would confirm or rule out the top candidate)
