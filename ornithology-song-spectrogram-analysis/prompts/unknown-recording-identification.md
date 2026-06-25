# Unknown Recording Identification

## Purpose

Drive a from-scratch determination of an unidentified field recording, forcing the systematist's discipline: measure, key by stated characters, rule out the nearest confusable, and stop at the rank the evidence supports.

## Prompt Template

```
You are an avian bioacoustician. Classify this recording by diagnostic characters, not gestalt, and descend the taxonomy only as far as the characters license.

Recording:
- **Spectrogram / measurements:** [PASTE OR DESCRIBE: element types, peak/bandwidth, durations, FM contours, structure]
- **Provenance:** [LOCALITY, DATE, HABITAT, SAMPLE RATE]
- **Quality:** [SNR, attenuation, reverberation]
- **As-recorded guess (if any):** [TREAT AS HYPOTHESIS ONLY]

Please:
1. Place it coarsely (song vs call; trill/warble/whistle; element-type count) using recording-quality-robust structure.
2. Descend a dichotomous key, naming the diagnostic character and value at each split.
3. Give the determination at the lowest rank the characters confidently support — do not force a species.
4. Name the single nearest confusable and the character that rules it out; state confidence and what evidence would change it.
```

## Expected Output

- A coarse placement with its rationale
- A key path with the character cited at each branch
- A determination at the supported rank with confidence
- The nearest confusable and the excluding character
