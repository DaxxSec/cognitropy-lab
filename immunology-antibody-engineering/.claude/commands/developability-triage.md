# /developability-triage

Run a developability profile on a candidate — biophysical risk (thermostability, aggregation, viscosity, self-association, poly-reactivity) plus in-silico structural flags — and rank candidates for the lead/backup decision.

## Inputs

- Candidate VH/VL (and ideally an Fv homology model) for the in-silico arm.
- Any measured biophysics: Tm/Tonset (nanoDSF), %monomer (SEC), Tagg (DLS), HIC retention, AC-SINS red-shift, PSR/poly-reactivity score, high-concentration viscosity.
- The target product profile: dose, concentration (subcutaneous high-conc vs IV), and route.
- The clinical-stage reference distribution to score against (TAP-style metrics).

## Steps

1. Read `context/concepts.md` "Developability" and `context/references.md` "Developability thresholds".
2. Compute/collect the in-silico structural metrics — TAP-style flags: total CDR length, patches of surface hydrophobicity (PSH), patches of positive/negative charge (PPC/PNC), and Fv charge-symmetry (SFvCSP); compute theoretical pI.
3. Fold in measured biophysics where available; convert each metric to Green/Amber/Red against the thresholds and the clinical-stage distribution.
4. Identify the dominant risk axis (thermal vs colloidal/aggregation vs charge/viscosity vs poly-reactivity) — candidates usually fail for *one* reason; name it.
5. Reconcile with `/sequence-liability-scan` so chemical and colloidal risks are presented as one risk picture; rank candidates and recommend lead + backups.

## Output

- `outputs/developability/<candidate>-developability-<date>.md` — per-metric Green/Amber/Red table, dominant risk axis, candidate ranking, and go/remediate/kill recommendation per candidate.
- Demonstrates competency: **developability triage**.

## Notes

- In-silico flags are early-warning, not destiny — confirm Amber/Red with wet-lab biophysics before killing a candidate.
- High subcutaneous concentration (≥100 mg/mL) makes viscosity and self-association first-class risks; for IV-only programs the bar is lower.
- A candidate that is best-in-class on affinity but Red on developability is usually the wrong lead — developability failures surface late and expensively.
