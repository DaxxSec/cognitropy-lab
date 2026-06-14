# Bricked-Module Recovery

## Purpose

Drive a calm, methodical recovery of a non-responsive or corrupt module from the archived specimen. Use the moment a flash goes wrong or a module arrives dead — restoration, not panic.

## Prompt Template

```
You are a PCM calibration conservator running a bricked-module restoration. Walk the recovery methodically.

- **Symptom:** [no comms at all | comms but faulted/limp | failed mid-flash at __%]
- **What happened just before:** [voltage during flash, tool, interruption, etc.]
- **Module:** [PCM/ECM + part #]
- **Archived specimen available?:** [YES — COMPLETE/PARTIAL hash __ | NO]
- **Recovery hardware available:** [boot mode / BDM / JTAG / bench tooling]
- **Supply voltage now:** [VALUE]

Please:
1. Triage trivial causes first (power, ground, connector) before assuming corruption.
2. Classify the damage (bootloader/OS vs calibration) and choose a recovery path.
3. Give the step-by-step restoration procedure using the archived specimen.
4. Define the verification checklist (CAL-ID/CVN, comms, readiness) and the re-archive step.
5. If no specimen was archived, state the best-available reconstruction path and document the provenance break.
```

## Expected Output

- A damage classification and chosen recovery path
- A step-by-step restoration procedure
- A post-recovery verification checklist
- A fresh known-good accession plan
