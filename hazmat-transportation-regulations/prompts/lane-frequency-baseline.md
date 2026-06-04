# Lane Frequency Baseline

## Purpose

Build or refresh a frequency baseline for a shipper or shipping lane and rank shipments by deviation, so inspection effort goes to the statistically unusual few. Use when triaging a corpus of manifests rather than a single shipment.

## Prompt Template

```
You are the dangerous-goods documentation agent. Build a frequency baseline and surface outliers for the corpus below.

- **Grouping:** [SHIPPER | LANE (origin→destination) | FLEET]
- **Group identity:** [e.g. "ACME Logistics", "Rotterdam→Newark"]
- **Mode:** [ROAD | RAIL | SEA | AIR]
- **Codebook edition:** [VALUE]
- **Manifest corpus:** [PASTE OR ATTACH THE BATCH OF MANIFESTS]
- **Prior baseline (optional):** [PASTE OR REFERENCE outputs/baselines/...]

Please:
1. Decode each manifest's UN numbers, classes, and packing groups.
2. Build frequency histograms (UN, class, PG) for the group and note the sample size.
3. Establish the "normal" profile; if a prior baseline is given, update it.
4. Score each shipment for deviation (rare/never-seen class, class atypical for this lane, sudden volume shift).
5. Output a ranked outlier list with a one-line rationale each, and persist the updated baseline.
```

## Expected Output

- Frequency histograms with sample size noted.
- The baseline "normal" profile for the group.
- A ranked outlier list with rationale, ready to feed into `/decode-manifest`.
- An updated baseline saved to `outputs/baselines/`.
