# /epitope-binning

Design and interpret an epitope-binning / competition experiment to cluster a panel of antibodies into epitope bins, and plan follow-on fine epitope mapping for the bins that matter.

## Inputs

- The antibody panel (clones) and the antigen.
- Binning format available: classical sandwich, premix (in-solution competition), or tandem (sequential) on SPR/BLI.
- The goal: epitope diversity for lead selection, a blocking-vs-non-blocking question, or a bispecific pairing decision.
- Optional: structural data (HDX-MS, crystallography, cryo-EM, AlphaFold-Multimer) for the bins you want resolved.

## Steps

1. Read `context/concepts.md` "Epitope mapping" and choose the binning format for the panel size and throughput.
2. Build the competition matrix (every clone vs every clone as saturating and as analyte); include self-blocking controls and an isotype/irrelevant control.
3. Run/score the matrix into a blocking heatmap; cluster antibodies into bins where mutual blocking is symmetric, and flag asymmetric (one-way) blocking as allosteric or steric-overlap signal.
4. Relate bins to function: which bins are ligand-blocking, which are non-blocking; for bispecifics, identify bin pairs that bind simultaneously.
5. Recommend which bins to take to fine mapping (HDX-MS / structure) and which clones best represent each bin for the lead panel.

## Output

- `outputs/epitopes/<panel>-binning-<date>.md` — competition matrix, bin assignments, blocking-vs-non-blocking annotation, simultaneous-binding pairs, and a fine-mapping recommendation.
- Demonstrates competency: **epitope mapping**.

## Notes

- Binning gives *relative* epitope relationships, not coordinates — two clones in one bin can still touch different residues; only structural mapping resolves that.
- Asymmetric blocking is information, not noise: it often means conformational/allosteric effects rather than direct overlap.
- Antigen valency and avidity confound premix binning; monomeric antigen and proper saturation controls are non-negotiable.
