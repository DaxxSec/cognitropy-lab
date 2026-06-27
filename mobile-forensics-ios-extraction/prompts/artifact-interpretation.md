# Artifact Interpretation

## Purpose

Interpret a single iOS artifact (a SQLite row, a KnowledgeC event, a carved fragment) with proper provenance, timestamp conversion, and reliability caveats — so it can enter the ACH matrix at the right weight rather than as an assumed fact.

## Prompt Template

```
You are interpreting one iOS artifact for an examination. Be precise about provenance and uncertainty.

- **Artifact / source DB:** [e.g. sms.db message table, row id 4412]
- **Raw values:** [FIELD: VALUE pairs, including raw timestamp]
- **How obtained:** [live table / WAL / freelist / unallocated carve]
- **Tool + version:** [VALUE]
- **Question it bears on:** [VALUE]

Please:
1. Convert any timestamps to UTC, stating the epoch used (Unix / Mac-absolute 2001 / Mach-continuous).
2. Explain what the artifact does and does NOT establish (e.g. presence of a row ≠ user authored it).
3. Rate reliability given how it was obtained (live vs carved) and whether it is corroborated.
4. State which hypotheses it is consistent and inconsistent with, and its diagnosticity.
```

## Expected Output

- A normalised, UTC-converted interpretation with the epoch noted.
- An explicit "establishes / does not establish" statement.
- A reliability rating and the artifact's diagnosticity for the open hypotheses.
