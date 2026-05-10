# Disturbance-Recovery Curve

## Purpose
Use this prompt after a defined disturbance (tillage, fumigation, fire, fungicide application, fertiliser pulse, drought) to quantify the community response and the return-to-baseline trajectory.

## Prompt Template

I want to characterise the soil microbiome's recovery from a disturbance event:

- **Disturbance type:** [e.g., chisel-tillage / fumigation with metam sodium / accidental flooding]
- **Disturbance date:** [e.g., 2025-06-12]
- **Pre-disturbance baseline window:** [e.g., 2025-04-01 to 2025-06-10, 3 sample dates]
- **Post-disturbance sampling cadence:** [e.g., +1 day, +1 week, +1 mo, +3 mo, +6 mo]
- **Control plots:** [yes/no — describe]
- **Sequencing layer & primer:** [e.g., 16S V4 515F/806R, ITS2 ITS86F/ITS4]
- **Functional assays available:** [e.g., qPCR nifH, amoA, nirS; soil enzymes; respiration]
- **Files:** [ASV table, taxonomy, sample metadata, qPCR exports]

Please construct a recovery analysis by:
1. Defining a baseline distribution from pre-disturbance samples (Aitchison centroid + dispersion).
2. Computing post-disturbance distance-to-baseline at each time point, per plot, with confidence bands.
3. Fitting a recovery curve (exponential decay or piecewise) and reporting the half-recovery time and asymptotic offset.
4. Identifying taxa / functional genes with the largest displacement and their individual recovery times (some don't recover — call those out).
5. Comparing disturbed vs control trajectories with a mixed-effects model (random plot, fixed time x treatment).
6. Producing a short narrative: what bounced back, what didn't, what shifted to a new equilibrium.

## Expected Output
- Distance-to-baseline plot (disturbed vs control) with fitted recovery curve.
- Half-recovery time and asymptotic offset, with CIs.
- Top displaced taxa / genes and their per-taxon recovery profile.
- Functional vs taxonomic recovery comparison (functions often return before composition).
- Recommended monitoring extension if the curve has not asymptoted.
