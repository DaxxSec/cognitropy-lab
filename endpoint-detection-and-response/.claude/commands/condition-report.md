# /condition-report — Compromise Assessment & Containment

Produce a conservator-style condition report for each affected host — what is intact, what is tampered, what persistence survives — and translate it into containment actions. Modeled on ICOM-CC textile condition-report practice.

## Inputs

- The reconstructed timeline and stratigraphy for the host(s).
- Persistence inventory and the trusted/anachronistic artifact split.
- Business context: host criticality, data sensitivity, operational constraints.

## Steps

1. **Inventory condition** per host: intact components, tampered components (from `/anachronism-sweep`), and confirmed losses/deletions.
2. **Assess persistence**: list every mechanism that survives reboot and the privilege it holds — these define the containment surface.
3. **Estimate exposure**: what data/credentials were accessible or staged; map to `Collection`/`Exfiltration` evidence.
4. **Prescribe interventions** ordered by reversibility and impact: isolate, kill/disable persistence, rotate credentials, reimage — least-destructive-first where safe, but never leaving an active C2 channel.
5. **Note conservation risk**: which containment steps would destroy volatile evidence, and how to preserve it first (memory capture, disk image).

## Output

`outputs/condition-report-<host>-<date>.md`: per-host condition summary (intact / tampered / lost), persistence-and-privilege table, exposure assessment, and a prioritized containment plan with an evidence-preservation note.

## Notes

- Sequence containment to preserve order of volatility — capture before you cleanse where evidence matters.
- The persistence-and-privilege table is the single most important output for responders; lead with it.
