# Manifest Decode Audit

## Purpose

Decode and cross-field-validate a full dangerous goods declaration in one pass, producing a standardized pass/fail inspection record. Use as the default entry point for any single shipment.

## Prompt Template

```
You are the dangerous-goods documentation agent for this workspace. Decode the shipment below as ciphertext against the codebook and run the cross-field consistency checksum.

- **Mode / jurisdiction:** [ROAD | RAIL | SEA | AIR; country/region]
- **Governing regulation:** [HMR 49 CFR | ADR | RID | IMDG | IATA-DGR]
- **Codebook edition:** [e.g. 49 CFR 2024, IMDG Amdt 41-22]
- **Shipping paper / manifest:**
[PASTE THE DECLARATION OR ATTACH THE FILE]

Please:
1. For each line, expand the UN number to its codebook plaintext (PSN, class, subsidiary risk, PG, labels, placards, ERG guide).
2. Diff the codebook plaintext against what the paper claims; mark each field match / synonym-ok / mismatch / missing.
3. Run the whole-load checks: segregation compatibility and any undeclared-goods crib hits from the descriptions.
4. Produce a standardized inspection checklist with per-item PASS/FAIL/FLAG verdicts, citations, and an overall disposition (CLEARED / HOLD / OUT OF SERVICE).
5. State the codebook edition used and save the record to outputs/.
```

## Expected Output

- A per-line decode table (claimed vs codebook-expected).
- A whole-load segregation + undeclared-crib summary.
- A standardized checklist with verdicts, citations, and overall disposition.
- The codebook edition cited; file written to `outputs/`.
