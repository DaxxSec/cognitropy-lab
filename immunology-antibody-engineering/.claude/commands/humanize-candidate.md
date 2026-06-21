# /humanize-candidate

Humanize a murine (or other non-human) antibody by CDR grafting onto a human germline framework, then propose the minimal set of framework back-mutations needed to recover affinity.

## Inputs

- Parental VH/VL sequences (the non-human antibody to humanize).
- Source species and discovery route (hybridoma, immunized mouse, etc.).
- Target: humanness floor (e.g. OASis identity ≥ a threshold) and the acceptable affinity-loss budget vs parental KD.
- Optional: a structural model to identify Vernier-zone and VH/VL-interface residues.

## Steps

1. Number the parental sequences and delineate CDRs (`context/references.md` "Numbering & CDR definitions").
2. Select the closest human germline frameworks (IGHV/IGKV/IGLV) by sequence and canonical-class compatibility — prefer germlines whose canonical CDR conformations match the parent (`context/workflows.md` "Humanization decision tree").
3. Graft the parental CDRs onto the chosen human frameworks; record the straight-graft sequence as the baseline.
4. Identify Vernier-zone residues, canonical-structure-determining residues, and VH/VL interface residues where the human framework differs from the parent — these are the back-mutation candidates.
5. Propose a *ranked, minimal* back-mutation set (most likely to recover affinity first) and an alternative "fewest mutations" set; predict humanness (BioPhi/OASis, Hu-mAb) and re-run `/sequence-liability-scan` on each variant.
6. Hand the variant panel to `/affinity-maturation-plan` if back-mutation alone won't close the affinity gap.

## Output

- `outputs/humanization/<candidate>-humanization-<date>.md` — chosen germlines, straight-graft sequence, ranked back-mutation table (position, parent→human, rationale, expected effect), humanness scores per variant, and a recommended lead + backup.
- Demonstrates competency: **humanization**.

## Notes

- More back-mutations = higher affinity recovery but lower humanness and higher immunogenicity risk; the deliverable is the Pareto front, not a maximal graft.
- Resurfacing/veneering (mutating only exposed framework residues) is an alternative to full CDR grafting for some scaffolds — note it when the parent framework is unusually stable.
- A "fully human via display/transgenic" parent does not need this command; confirm the parent is actually non-human before grafting.
