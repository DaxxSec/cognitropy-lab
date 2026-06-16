# Fuel-Trim Consensus Readout

## Purpose

Turn a set of fuel-trim and sensor readings into a structured "node report" — classifying each sensor as faithful / suspect / Byzantine and naming the implied lean/rich condition — before any root cause is proposed.

## Prompt Template

```
You are an emissions root-cause adjudicator. Treat each sensor as a node that may be faithful, crashed, or Byzantine (lying). Do not name a root cause yet.

I have these readings:

- **Vehicle:** [YEAR/MAKE/MODEL/ENGINE]
- **STFT / LTFT (per bank):** [e.g. B1 STFT +6%, LTFT +18%; B2 ...]
- **Condition:** [idle / steady cruise / WOT; warm/cold]
- **O₂ / wideband (upstream & downstream):** [VALUES]
- **MAF (g/s) and MAP (kPa) at this RPM/load:** [VALUES]
- **Other:** [fuel pressure, IAT/ECT, etc.]
- **Context:** [DTCs present, complaint]

Please:
1. Cross-check MAF against MAP+RPM-implied airflow and flag if MAF is reading high/low (Byzantine).
2. Cross-check the upstream O₂ against the commanded λ; note slow/skewed switching.
3. Classify each sensor: faithful / crashed / Byzantine, with the cross-check that decided it.
4. State the trim-implied condition (lean/rich) and where it localizes by the trim-vs-load pattern — without yet committing a root cause.
```

## Expected Output

- A per-sensor trust classification with the deciding cross-check
- The lean/rich verdict and its localization (idle-only vs all-load, one bank vs both)
- A shortlist of candidate root causes to take into `/build-quorum` — explicitly *not* a committed diagnosis
