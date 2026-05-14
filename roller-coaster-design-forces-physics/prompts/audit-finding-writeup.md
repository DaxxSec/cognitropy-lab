# Audit Finding Writeup

## Purpose

Use when one or more `/force-envelope-check` or `/jerk-budget-audit` walks have produced REWORK / REJECT verdicts and you need to package them into a single audit finding that the operator and AHJ can act on. Follows an ASTM F2974-style audit narrative structure.

## Prompt Template

```
A force review has produced one or more decision-tree verdicts that need to be written
up as a formal audit finding. Compose the finding so a manufacturer, operator, and AHJ
can act on it without re-walking the underlying data.

Finding context:
- **Ride name:** [name]
- **Standard / framework:** [F2291 | EN13814 | in-house]
- **Reviewer:** [your name / org]
- **Date:** [YYYY-MM-DD]
- **Affected segments / elements:** [list]
- **Walks to package:** [paths to /force-envelope-check, /jerk-budget-audit walks]
- **Severity hint:** [PASS_WITH_NOTE | REWORK | REJECT — derived from highest severity in walks]
- **Context:** [scheduled audit | post-incident | post-modification | other]

Please:
1. Open with a one-paragraph executive summary keyed to the severity hint.
2. List each underlying decision-tree node verdict in a finding table: element, axis, measured value, limit, node id, frame, sample rate.
3. For every REJECT / REWORK row, state the impact on operations: continue / restricted operation / hold.
4. Recommend a remediation pathway: tune via /banking-curvature-tune, redesign element, swap train, instrument sensors, re-survey.
5. Close with a sign-off block: reviewer attestation that the finding is advisory only and that PE-of-record / AHJ retain authority.
```

## Expected Output

- Markdown audit finding (suitable for PDF export).
- Executive summary, severity, finding table, remediation, sign-off block.
- Cross-references to all source decision-tree walks in `outputs/walks/`.
- Reproducibility footer: list of input file hashes and workspace git SHA.
