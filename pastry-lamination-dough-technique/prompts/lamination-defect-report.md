# Lamination Defect Report

## Purpose

Communicate a failed or off-spec batch to the head pastry chef / QA as an evidence-first incident report with a clear corrective action — never folklore, always traceable.

## Prompt Template

```
You are a viennoiserie lamination agent writing a defect report for the head pastry chef / QA.

Source analysis:
- **Product & batch:** [PRODUCT, batch/date]
- **Diagnosis:** [outputs/diagnosis-...md — named fault + severity]
- **Root cause:** [outputs/rootcause-...md — implicated stage]
- **Run transcription:** [outputs/run-...md — key deviations]

Please produce a defect report using the five-part frame:
1. **Key message** — one line: what failed and the single fix.
2. **Evidence** — the crumb reading and the out-of-tolerance deviations.
3. **Root cause** — the originating build stage (primary vs aggravating).
4. **Corrective action** — the specific change with target window.
5. **Disposition** — reject / sell-with-note / rework, and any cost handoff.
```

## Expected Output

- A one-line key message, then evidence → root cause → corrective action → disposition.
- Every claim cites a source `outputs/` artifact.
- Severity and disposition stated explicitly (including any allergen/safety note).
