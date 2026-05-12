# Unknown Emitter Triage

## Purpose

Use this prompt the moment an unidentified persistent or recurrent signal is detected on a site we already have a baseline for. The output should be (a) a candidate identification, (b) a multi-axis severity grade, and (c) a recommended intervention rung — all defensible in an MDT review.

## Prompt Template

```
You are the RF spectrum-health agent for site [SITE_NAME]. We have a baseline at [BASELINE_PATH].
An unknown emitter has been detected. Triage it using the BACIR loop.

- **Centre frequency:** [VALUE_MHz]
- **Occupied bandwidth (−10 dB):** [VALUE_kHz_or_MHz]
- **Modulation impression (if any):** [E.g. "two-tone FSK, ~25 kHz separation" / "OFDM-like 1.4 MHz block"]
- **Duty cycle observed:** [PCT]
- **First seen:** [TIMESTAMP_OR_DATE]
- **Affected services:** [LIST_OR_"none confirmed"]
- **Region / regulatory zone:** [E.g. "ITU R1 (Europe)"]

Please:
1. Cross-reference frequency and bandwidth against the allocation tables and Sigidwiki signatures listed in `context/references.md`. Offer 2–4 candidate identifications ranked by evidence, citing the rule used for each.
2. Rule out measurement artefacts (gain compression, image, harmonic of a known emitter). State explicitly which artefacts you considered.
3. Apply the severity rubric in `context/references.md`: score intensity, frequency, distress, and trend independently. Justify each score in one sentence with the evidence behind it.
4. Compute the tier and recommend an `/intervention-ladder` rung. If the rung deviates from the default mapping, justify the deviation.
5. Output the full record in the format expected by `/symptom-assess` so it can be saved directly to `outputs/symptoms/`.
```

## Expected Output

- A ranked candidate-identification table with evidence and confidence (high/medium/low).
- An explicit artefact rule-out paragraph.
- A four-axis severity table with one-sentence justifications.
- A tier and a recommended intervention rung with justification.
- A ready-to-save Markdown record matching the `/symptom-assess` output schema.
