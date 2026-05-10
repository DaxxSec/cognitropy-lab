# Soil Microbiome Management — Working Concepts

Background the agent should read before acting on monitoring, trend, or recommendation tasks. Optimised for fast recall, not exhaustive theory.

## What the soil microbiome actually is

A community of microorganisms living in soil that together drive nutrient cycling, plant health, disease suppression, and carbon turnover. Coarse breakdown:

- **Bacteria & archaea** — the bulk of cell counts; carry out N cycling (nitrification, denitrification, fixation), C oxidation, sulfur and iron cycling.
- **Fungi** — decomposers (saprotrophs), root symbionts (arbuscular mycorrhizal, ectomycorrhizal), and pathogens. Carry C-rich, lignin-degrading capacity bacteria largely lack.
- **Protists** — top-down regulators of bacterial communities; underrated.
- **Nematodes** — bacterivores, fungivores, herbivores, predators; classic indicators of soil food-web maturity.
- **Viruses** — recently appreciated; turn over a substantial fraction of microbial biomass daily.

Functional outcomes the agronomist actually cares about: nitrogen availability, phosphorus solubilisation, disease suppression, aggregate stability, water-holding capacity, soil organic carbon, greenhouse gas (N2O, CH4) flux.

## Diversity metrics

### Alpha (within-sample)
- **Observed richness** — number of distinct ASVs/OTUs.
- **Shannon index** — accounts for evenness; sensitive to rare taxa.
- **Simpson / Inverse Simpson** — emphasises dominant taxa.
- **Faith's PD** — phylogenetic diversity; preferred for ecological inference.
- **Pielou's evenness** — separates evenness from richness.

### Beta (between-sample)
- **Bray-Curtis** — count-based dissimilarity; classic but not phylogeny-aware.
- **Weighted / unweighted UniFrac** — phylogenetically informed.
- **Aitchison distance** — Euclidean on CLR-transformed counts; the right choice for compositional data.
- **PERMANOVA** to test group differences; **dispersion** test (`betadisper`) to confirm spread differences are not driving the result.

## Compositionality — the constant trap

Sequencing returns relative abundances, not absolutes. A taxon "increasing" can simply mean another decreased. Mitigations the agent should default to:

- **CLR (centered log-ratio)** transform before linear modelling.
- **ILR (isometric log-ratio)** when balances between known groups matter.
- **Rarefaction** to even depth as a robustness check, not a primary fix.
- Compositional-aware tools: **ALDEx2**, **ANCOM-BC**, **MaAsLin2** (with arc-sine sqrt or CLR), **gneiss** (balances).
- Where possible, anchor with an absolute method: **qPCR** of total 16S, **flow cytometry** counts, or **spike-in** standards. Then re-scale relative abundances to absolute.

## Functional capacity (when taxonomy is not enough)

- **Functional-gene qPCR** — `nifH` (N fixation), `amoA` (ammonia oxidation, AOA vs AOB), `nirK`/`nirS`/`nosZ` (denitrification stages), `phoD` (alkaline phosphatase), `chiA` (chitinase).
- **Shotgun metagenomics** with HUMAnN / KEGG / CAZy mappings — pathway-level abundance.
- **Metatranscriptomics** — what's actually being expressed, not just present.
- **PICRUSt2** — predicted functions from 16S; OK for hypothesis generation, weak for quantitative claims.
- **PLFA / NLFA** — biomass and broad group ratios (fungal:bacterial, AMF marker 16:1ω5).
- **Soil enzyme assays** — beta-glucosidase, urease, alkaline phosphatase, dehydrogenase; inexpensive and complementary to sequencing.

## Time-series methods that actually fit microbiome data

### Trend tests (non-parametric)
- **Mann-Kendall** — tests for monotonic trend; tolerant of non-normality.
- **Seasonal Mann-Kendall** — handles seasonal autocorrelation.
- **Theil-Sen slope** — robust median-based slope estimator; pair with MK for magnitude.
- Apply to alpha-diversity series, CLR-transformed taxa, and qPCR copy numbers — not raw relative abundances.

### Decomposition
- **STL (Seasonal-Trend decomposition using LOESS)** — separates trend / seasonal / remainder; works with irregular gaps via interpolation.
- **X-13 ARIMA-SEATS** — overkill for ecology but useful when monthly cadence is clean.

### Forecasting / structural models
- **ARIMA / SARIMA** — for evenly-spaced univariate (e.g. monthly soil respiration).
- **State-space (Kalman) models** — handle missing time points cleanly.
- **gLV (generalized Lotka-Volterra)** — community dynamics as ODEs; needs dense sampling and is identifiability-fragile.
- **Mixed-effects** with `time` as fixed and `plot` as random — workhorse for replicated plot trials (`MaAsLin2`, `lme4`, `glmmTMB`).

### Change-point detection
- **PELT / `changepoint` (R)** — efficient for multiple change points in mean/variance.
- **`ruptures` (Python)** — flexible cost functions including non-parametric.
- **Bayesian Online Change-Point Detection** — for streaming sensor data (CO2 flux, EC).
- Apply to Aitchison distance from a baseline window when looking for "the community shifted".

### Early-warning indicators (resilience)
- Rising **autocorrelation** and **variance** in a noisy series can precede regime shifts (the critical-slowing-down literature). Use cautiously — false positives are common in ecology.

## Disturbance and recovery

Common disturbances and their typical microbiome signatures:

- **Tillage** — short-term homogenisation; depresses fungi (especially AMF, slow regrowth), favours r-strategists.
- **Fumigation / sterilisation** — collapse + rebound; recovery trajectory is the actual signal of interest.
- **Synthetic N (high)** — selects copiotrophs, suppresses oligotrophs and AMF; nitrifier abundance climbs.
- **Pesticides / fungicides** — non-target effects; track over multiple seasons.
- **Drought** — reduces bacterial richness, favours actinobacteria and fungi; fast recovery on rewetting (Birch effect on C flush).
- **Fire** — sterilises top horizons; pyrogenic carbon shifts long-term community.

Recovery quantification: time to return within X% of pre-disturbance Aitchison distance, or PERMANOVA p > 0.05 vs control.

## Beneficial inputs the agent will be asked about

- **Compost** — broad biodiversity boost; effect persists 2–5+ years.
- **Biochar** — habitat for microbes; long-lived; alters bulk density and pH.
- **Cover crops** — root exudates feed rhizosphere; legumes add N-fixers.
- **Reduced / no-till** — favours fungi, increases AMF colonisation and aggregate stability over years.
- **Microbial inoculants** — establishment is generally poor; demand evidence (qPCR of strain marker over time) before claiming impact.
- **Biofertilisers** — same caveat as inoculants; persistence is the question.

## Sampling design for time-series work

- **Replication** — minimum 3 plots per treatment, ideally 4–6.
- **Cadence** — match the question. Seasonal cycle: monthly. Disturbance recovery: dense early (week 1, 2, 4), then taper. Long-term trend: quarterly to annually.
- **Depth** — segregate 0–10 cm vs 10–30 cm minimum; deeper if subsoil microbiome matters.
- **Compositing** — combine 5–10 cores per plot to dampen within-plot heterogeneity.
- **Storage** — flash-freeze in liquid N or store at -80 C; at minimum, dry ice in the field. Anything warmer biases the result.
- **Metadata** — temperature, moisture, pH, EC, total C/N, prior management — capture every time. Without covariates, trends are uninterpretable.

## Pitfalls the agent should call out by default

- Comparing across primer sets, sequencing runs, or pipelines without batch correction.
- Treating relative abundance shifts as absolute biology.
- Reading too much into a 2-time-point "trend".
- Ignoring spatial structure: nearby plots are not independent.
- Over-fitting differential abundance with thousands of taxa and no FDR control.
- Confounding seasonal weather with treatment effect when treatments are not blocked across seasons.
