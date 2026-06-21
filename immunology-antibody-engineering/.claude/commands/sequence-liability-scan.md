# /sequence-liability-scan

Scan an antibody VH/VL pair for sequence-level developability liabilities — deamidation, isomerization, oxidation, glycosylation sequons, free cysteines, and fragmentation sites — and rank them by CDR exposure.

## Inputs

- VH and VL amino-acid sequences (FASTA or plain text); optionally the full IgG with constant regions.
- Numbering scheme to apply (Kabat / Chothia / IMGT / Martin) — default IMGT via ANARCI.
- Antibody format and intended route (the same NG in a framework is lower-risk than one in CDR-H2).
- Optional: a structural model (ABodyBuilder2 / ImmuneBuilder) for solvent-accessibility weighting.

## Steps

1. Number the sequences (ANARCI or AbNum) and annotate CDR vs framework per `context/references.md` "Numbering & CDR definitions".
2. Flag chemical-degradation motifs from `context/references.md` "Liability motif table": deamidation (NG, NS, NH, NT), isomerization (DG, DS, DT, DH), oxidation (exposed Met, Trp), N-glycosylation sequons (N-X-S/T, X≠P), unpaired/odd cysteines, and Asp-Pro fragmentation.
3. Weight each hit by location (CDR > Vernier/framework > constant) and, if a model is supplied, by relative solvent accessibility — buried motifs are usually benign.
4. Classify each liability as Red (CDR, high-rate motif, exposed), Amber (borderline location/rate), or Green (buried/framework, low-rate) and note the canonical remediation (conservative substitution that preserves the canonical residue's role).
5. Cross-check against `/developability-triage` biophysical flags so sequence and structural risk are reconciled, not double-counted.

## Output

- `outputs/liabilities/<candidate>-liability-scan-<date>.md` — annotated sequence, ranked liability table (motif, position, region, Red/Amber/Green, suggested remediation), and a one-line developability-risk verdict.
- Demonstrates competency: **sequence-liability assessment**.

## Notes

- A motif is a *hypothesis* of risk, not a confirmed degradation site — confirm rates with forced-degradation (stress) studies before remediating away binding.
- Never silently mutate a CDR residue to remove a liability; flag the affinity/specificity trade-off for `/affinity-maturation-plan`.
- Methionine in the Fc (M252, M428 region) affects FcRn binding and half-life — treat constant-region Met oxidation separately from CDR liabilities.
