# Longitudinal Microbiome Trend Assessment

## Purpose
Use this prompt when you have repeated soil samples from the same plots/fields across at least four time points and want a defensible read on whether anything is actually changing.

## Prompt Template

I have a longitudinal soil microbiome dataset with the following characteristics:

- **Sites/plots:** [count and design — e.g., 6 plots, 3 treatments, 2 reps]
- **Time points:** [list dates or cadence — e.g., monthly Apr–Oct 2024–2025]
- **Sequencing layer:** [16S V4 / ITS2 / shotgun / qPCR / multiple]
- **Read depth (median):** [e.g., 32k 16S reads/sample after DADA2]
- **Pipeline:** [e.g., QIIME 2 + DADA2 with SILVA 138]
- **Covariates available:** [e.g., soil moisture, T, pH, prior management, weather]
- **Management context:** [e.g., transition to no-till started 2024-04, cover crop mix interseeded]
- **Files:** [paths to ASV table, taxonomy, sample metadata, tree if present]

Please produce a longitudinal trend assessment by:
1. Recommending a normalisation strategy (CLR vs rarefaction vs absolute via spike-in/qPCR) given depth distribution and the question.
2. Picking the right alpha and beta metrics (justify each — phylogeny-aware vs not, compositional vs not).
3. Running per-plot trend tests on alpha diversity (Mann-Kendall + Sen's slope) and on the top 30 CLR-transformed taxa (FDR-controlled).
4. Decomposing community-level Aitchison distance to a baseline window using STL or seasonal trend test; surface the seasonal vs trend split.
5. Flagging any change points and aligning them with management or weather covariates.
6. Writing a defensible "what changed, what didn't, what's still ambiguous" summary, with explicit caveats on power.

## Expected Output
- Trend table per plot per metric with p-values and effect size (Sen's slope, log fold change).
- Decomposition plot (trend / seasonal / remainder) for community distance.
- Annotated change-point timeline overlaid with covariate events.
- Caveat list (batch effects, missing covariates, unbalanced design).
- Concrete next-sample recommendations (cadence, depth, additional assays).
