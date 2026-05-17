# Prompt — Exposure Compliance Narrative

## Purpose

Turn a reduced survey dataset into the narrative section of a compliance report. Standard-cited, uncertainty-aware, and reviewable.

## Prompt Template

```
Author the compliance narrative for the attached survey.

SITE: [site name]
SURVEY DATE(S): [yyyy-mm-dd]
STANDARD: [ICNIRP 2020 | IEEE C95.1-2019 | FCC OET-65 | …]
CLASSIFICATION: [general public | occupational | restricted | unrestricted]
INSTRUMENTS USED: [model + serial + last calibration date]
RAW DATA: [path to outputs/raw/<file>.csv]
REDUCED DATA: [path to outputs/compliance/<file>-eq.csv]
HIGHEST EQ ROW(S): [coordinates, frequency, magnitude, EQ]
EXPECTED DOMINANT SOURCES: [from the survey plan]
KNOWN UNCERTAINTIES: [calibration, position, multipath, polarization, …]

Write the narrative in this structure:

1. SCOPE & METHODOLOGY — what was measured, why, against which standard, by which method.
2. INSTRUMENTATION — probes + cal IDs; cite the standard's metrology requirements.
3. RESULTS BY ZONE — table of zone vs. max EQ vs. classification (Compliant / Watch / Non-Compliant). Reference the maps in outputs/maps/.
4. UNCERTAINTY — combined standard uncertainty per IEC 62232 Annex D or NIST TN 1297; whether the uncertainty interval straddles the limit.
5. VERDICT — Compliant / Compliant within uncertainty / Non-Compliant — with the standard cited verbatim (formula + averaging time).
6. ACTIONS — required follow-up (e.g. re-measurement of EQ ≥ 0.8 rows; signage; access controls; mitigations).

Cite limit formulas verbatim from context/references.md — do not paraphrase. The narrative is the artefact a regulator reads; precision matters more than fluency.
```

## Expected Output

A markdown report at `outputs/compliance/<date>-<site>-compliance.md` that is:

- Reviewable by a second engineer without ambiguity.
- Self-contained for sign-off (standard cited, formula verbatim, uncertainty quantified, verdict explicit).
- Cross-referenced to the maps, raw data, and reduction CSV under `outputs/`.
- Followed by a one-line sign-off block: technician + reviewing engineer + safety officer + date.
