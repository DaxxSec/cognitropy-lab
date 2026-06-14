# Specimen Intake Report

## Purpose

Produce the archival accession record for a factory calibration *before any edit*. Use at the start of every job, right after reading the module, to lock in provenance and prove the original was preserved.

## Prompt Template

```
You are a PCM calibration conservator. I have just read a module and need a complete intake/accession record.

- **VIN:** [VALUE]
- **Module type / part number:** [PCM/ECM/TCM + HW/SW #]
- **CAL-ID (Mode 09/04):** [VALUE]
- **CVN (Mode 09/06):** [VALUE]
- **Read coverage:** [FULL (bootloader+OS+cal+VIN) | PARTIAL — list what was unreadable]
- **Image hash (SHA-256):** [VALUE]
- **Supply voltage during read / tool:** [VALUE]
- **Context:** [why this module is on the bench — TSB, replacement, restoration, diagnostics]

Please:
1. Produce an accession.md with all identifiers and a COMPLETE/PARTIAL flag.
2. Decode the VIN to make/model/year/plant/market and infer the cal's intended emissions regime + fuel grade.
3. State the restoration risk level given the read coverage.
4. List exactly what must be true before any flash may proceed (the gate checklist).
```

## Expected Output

- A clean `accession.md` for `outputs/specimens/<vin>-<date>/`
- Decoded VIN + inferred origin geography
- A COMPLETE/PARTIAL verdict with restoration-risk note
- The pre-flash gate checklist
