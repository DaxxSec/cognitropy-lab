# spec-traceability-audit

## Purpose

Walk a drafted spec end-to-end and confirm every operation / schema / response carries a usable `x-provenance` chain. Used during pre-publication review and during quarterly hygiene to catch tooling that silently strips extensions.

## Prompt Template

```
I need a traceability audit of the OpenAPI spec at [SPEC_PATH].

- **Spec file or directory:** [PATH, e.g. outputs/spec/orders-v3.yaml or outputs/spec/]
- **Sample size:** [PERCENT_OR_ALL, default 100% for single file, 10% sample for directory hygiene]
- **Source dossier for the surface:** [PATH, e.g. outputs/sources/payments-api-2026-05-01.md]
- **Adjudication directory:** outputs/adjudication/
- **Report destination:** outputs/traces/[SPEC_SLUG]-audit-[DATE].md

Please:
1. For every operation in scope, run /trace-provenance on the operation, on each non-trivial parameter, on each response, and on each $ref'd schema.
2. Aggregate the per-element results into a single audit report.
3. Flag elements with missing or incomplete provenance under a "Gaps" section.
4. Flag elements whose most-specific provenance contradicts the ancestor's under a "Contradictions" section.
5. Flag any provenance referencing a source class no longer in the current dossier (source class was retired or never re-elicited).
6. Summarise the audit at the top: total elements checked, gaps, contradictions, stale source references.
```

## Expected Output

- A single audit report at `outputs/traces/[SPEC_SLUG]-audit-[DATE].md` with:
  - Header summary (elements / gaps / contradictions / stale).
  - "Gaps" section: elements with no provenance — most likely a tooling strip; flag the pipeline.
  - "Contradictions" section: most-specific provenance disagreeing with ancestor.
  - "Stale source references" section: provenance citing source classes not in the current dossier.
  - A remediation list ranked by severity: tooling fixes first (gaps), adjudication needed second (contradictions), re-elicit third (stale).
