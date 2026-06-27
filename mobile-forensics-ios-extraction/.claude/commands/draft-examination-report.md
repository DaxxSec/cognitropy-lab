# /draft-examination-report

Produce a court-ready examination report that states findings with calibrated confidence, the competing hypotheses considered and refuted, the methodology, and the chain of custody — the deliverable of the whole pipeline.

## Inputs

- The scored ACH matrix and surviving hypothesis (`/build-diagnosticity-matrix`).
- The acquisition plan, verification results, timeline, and carve outputs.
- Custody log (isolation, identification, acquisition timestamps, hashes).
- The audience (court, counsel, internal) and required format.

## Steps

1. **State the question and authority** — the investigative question and the legal basis for the examination.
2. **Methodology** — devices, tools + versions, acquisition method, hashes; reference the seizure-to-report lifecycle followed.
3. **Findings with confidence** — for each finding, give the surviving hypothesis, a calibrated confidence level, and the *evidence that supports and the evidence that constrains* it.
4. **Alternatives considered** — list the competing hypotheses and the specific evidence that **refuted** each; this is what makes the report defensible.
5. **Limitations** — what was sealed/unacquired, single-source findings, and any sensitivity dependencies that could change the conclusion.
6. **Chain of custody** — the full handling record with timestamps and hashes.

## Output

`outputs/examination-report-YYYY-MM-DD.md`: a structured report (Question/Authority → Methodology → Findings+Confidence → Alternatives Refuted → Limitations → Chain of Custody) suitable for review or disclosure, with no real PII (synthesised/redacted).

## Notes

- Report confidence and the alternatives you ruled out — a single-narrative report that hides the competing hypotheses invites impeachment.
- Every number (timestamp, count, hash) traces to a pinned source + tool version, or it doesn't go in.
