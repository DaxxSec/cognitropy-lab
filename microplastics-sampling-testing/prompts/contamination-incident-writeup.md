# Prompt — Contamination Incident Write-up

## Purpose

Document a blank-failure or anomalous-result incident with a root-cause analysis — like an incident report. Turns a quarantined batch into a traceable record and a maintenance/process action, so the same contamination doesn't recur silently.

## Prompt Template

```
Write a contamination incident report.

Trigger: {blank-audit failure | anomaly escalation | recovery collapse}
Batch / sample IDs affected: {ids}
Observed signal: {e.g. polyester fiber blank load 8x baseline; PET recovery 22%}
Timeline: {when first seen, what runs are in scope}
Environment at the time: {enclosure/HEPA state, reagent lots, recent gear changes}

Produce:
1. Impact scope: which results are quarantined / not reportable, and which
   prior batches share the suspected cause and need re-examination.
2. Root-cause analysis: rank candidate causes (HEPA cartridge end-of-life,
   synthetic clothing, reagent contamination, worn sieve, light density medium),
   with the evidence for/against each.
3. Containment: immediate quarantine + which checkpoint to take out of service.
4. Corrective action: the maintenance order (link to instrument-maintenance-forecast)
   and the process fix.
5. Verification: the check standard / recovery spike that must pass before
   resuming reportable runs.
```

## Expected Output

An incident record: impact scope (incl. retrospective batches at risk), a ranked root-cause analysis with evidence, the containment and corrective actions tied to a maintenance order, and the explicit re-verification gate before reportable work resumes.
