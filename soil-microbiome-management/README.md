# Soil Microbiome Management Workspace

> A Claude Code workspace for longitudinal management of agricultural soil microbiomes — built around **time-series trend analysis** of community composition, functional-gene abundance, and soil-health proxies across cropping cycles, amendments, and disturbances.

## What This Workspace Does

This workspace turns a stream of soil samples — 16S/ITS amplicon counts, shotgun metagenomic taxonomies, qPCR functional-gene copy numbers, soil-health sensor traces — into a structured, season-aware view of how the microbiome is moving over time. Instead of treating each lab report as a one-shot snapshot, it pairs the data with classical trend tests (Mann-Kendall, Theil-Sen slope, STL decomposition, SARIMA) and ecology-aware methods (ALDEx2 / MaAsLin2 with random effects, change-point detection on Aitchison distances, generalized Lotka-Volterra) so the agronomist can separate management signal from rotation noise.

The agent guides the full longitudinal-monitoring cycle: sampling design, batch-effect-aware ingestion, compositional normalisation, alpha and beta diversity tracking, monotonic and seasonal trend testing, change-point detection on community shifts, post-disturbance recovery quantification, and treatment vs. control comparisons under a mixed-effects model.

## Why This Workspace Exists

Most "soil health is improving" claims rest on two soil tests in the same season — useless for distinguishing rotation effects from amendment effects from inter-annual climate variation. This workspace codifies a discipline: every claim about the microbiome ties back to a documented sampling cadence, a compositionality-aware analysis pipeline, and a trend test with a stated confidence interval. Time-series framing makes seasonality visible, which is what makes management effects defensible.

## Getting Started

### Prerequisites

- A sequencing or qPCR data source — your own runs, a contracted lab (e.g. Microbiome Insights, RTL Genomics), or public archives (Earth Microbiome Project, NCBI SRA).
- Sample metadata: site, plot, depth, date, primary covariates (temperature, moisture, pH, EC, total C/N), management history.
- Analysis environment: R with `phyloseq`, `vegan`, `MaAsLin2`, `ALDEx2`, `Kendall`, `changepoint`, `forecast`; or Python with `scikit-bio`, `statsmodels`, `ruptures`, `arviz`.
- Compositional-data-analysis literacy (Aitchison geometry, CLR, log-ratios) — the workspace assumes the analyst will not interpret raw relative abundances as biology.

### Quick Start

1. Clone this workspace.
2. Drop ASV/OTU tables, qPCR exports, sample metadata into `context/` (or `outputs/raw/` for large derived data).
3. Run `/sample-design` to plan or audit the sampling cadence and replication for your study question.
4. Run `/clr-transform` on raw count tables — every downstream analysis assumes CLR or compositional-aware input.
5. Run `/trend-test` on alpha-diversity and key functional-gene series to surface monotonic trends with magnitude estimates.
6. Run `/seasonal-decompose` to separate trend from rotation/seasonal cycles.
7. Run `/changepoint-detect` on Aitchison-distance-from-baseline to identify community shifts; pair with covariate timeline.
8. Iterate: `/treatment-compare` for replicated trials, `/disturbance-recovery` after specific events.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/sample-design` | Plan replication, cadence, depth, compositing, storage | Before kicking off a new monitoring program |
| `/clr-transform` | CLR/ILR-normalise relative-abundance tables; flag low-prevalence taxa | Always, before linear time-series modelling |
| `/trend-test` | Mann-Kendall + Theil-Sen on a time series, with seasonal variant | Looking for monotonic shifts in diversity / functional genes |
| `/seasonal-decompose` | STL decomposition to isolate trend from seasonal cycle | When data spans full seasons / annual cycles |
| `/changepoint-detect` | PELT or Bayesian online change-point detection on Aitchison distance | Identifying when "the community shifted" |
| `/disturbance-recovery` | Quantify time-to-recovery after tillage / fumigation / drought | Studies with planned or unplanned disturbances |
| `/treatment-compare` | Mixed-effects model: `time × treatment + (1\|plot)` | Replicated plot trials over multiple time points |

## Directory Structure

```
soil-microbiome-management/
├── CLAUDE.md                                # Agent role, context refs, command list
├── README.md                                # This file
├── .claude/commands/
│   ├── sample-design.md
│   ├── clr-transform.md
│   ├── trend-test.md
│   ├── seasonal-decompose.md
│   ├── changepoint-detect.md
│   ├── disturbance-recovery.md
│   └── treatment-compare.md
├── context/
│   ├── concepts.md                          # Microbiome composition, diversity metrics, compositionality, time-series methods, disturbance patterns
│   ├── workflows.md                         # Step-by-step procedures tied to today's time-series technique
│   └── references.md                        # Primer sets, reference databases, tools, public catalogues
├── prompts/
│   ├── disturbance-recovery-curve.md
│   ├── longitudinal-trend-assessment.md
│   └── seasonal-decomposition.md
└── outputs/                                 # Trend reports, change-point summaries, recovery indices, recommendations
```

## Example Use Cases

### Multi-year cover-crop trial monitoring
Quarterly 16S + qPCR sampling across treated and control plots; track alpha diversity, AMF abundance (16:1ω5 NLFA + glomeromycete-specific qPCR), and N-cycling gene abundance. Mixed-effects models with `time × treatment` quantify the management effect against rotation noise.

### Post-fumigation recovery in protected cropping
Dense sampling (week 1, 2, 4, 8, 12) after a soil fumigation event. Aitchison-distance-from-pre-disturbance baseline plotted over time with change-point detection identifying the "recovery point."

### Drought-resilience benchmarking across irrigation regimes
Compare community trajectories under standard vs. deficit irrigation across a season. STL decomposition separates seasonal moisture-cycle effect from irrigation-treatment effect; rising autocorrelation in resilient series is an early-warning indicator of drought-induced regime shift in the susceptible series.

### Long-term carbon-sequestration claim verification
Annual sampling over 5+ years of a no-till + cover-crop programme; track soil organic carbon proxies (β-glucosidase activity, fungal:bacterial ratio, bulk-soil C). Mann-Kendall on standardised trajectories with FDR-controlled multiple comparisons across plots.

### Inoculant-persistence audit
Pre-/post-inoculation sampling with strain-specific qPCR markers; time-series trend test on copy numbers tells you whether the inoculant established or washed out by week 4.

## Recommended MCP Servers

- **filesystem** — for reading sample manifests, ASV tables (often large CSVs), qPCR exports, and writing trend reports.
- **shell** — for invoking R / Python pipelines (`Rscript trend.R`, `python ruptures-changepoint.py`).
- **python** — for compositional-data analysis (`scikit-bio`), change-point detection (`ruptures`), Bayesian models (`pymc`, `numpyro`).
- **R** (via shell or dedicated MCP) — for `phyloseq`, `vegan`, `MaAsLin2`, `ALDEx2`, `Kendall`, `changepoint`.
- **sqlite** or **duckdb** — for joining sample metadata with sequencing run metadata across years.

## Legal & Ethical Considerations

- **Land-tenure and consent.** Microbiome data tied to farmer fields can carry IP and privacy implications (cropping practices, yield outcomes). Confirm consent and data-sharing agreements before publication.
- **Indigenous Data Sovereignty.** If sampling on indigenous-stewarded land, follow CARE principles (Collective benefit, Authority to control, Responsibility, Ethics) alongside FAIR.
- **Public-database submissions** (NCBI SRA, MG-RAST, EMP) — check that metadata you upload doesn't identify individual landowners or operations without consent.

## Technical References

- [Earth Microbiome Project Standard Protocols](https://earthmicrobiome.org/protocols-and-standards/) — canonical 16S/ITS sampling and sequencing standards.
- [SILVA 138 reference database](https://www.arb-silva.de/) — primary 16S taxonomy reference.
- [UNITE](https://unite.ut.ee/) — fungal ITS taxonomy reference.
- [QIIME 2](https://qiime2.org/) — full amplicon-analysis pipeline.
- [DADA2](https://benjjneb.github.io/dada2/) — exact amplicon-sequence-variant inference.
- [MaAsLin2](https://huttenhower.sph.harvard.edu/maaslin/) — multivariable association in microbial communities (mixed-effects ready).
- [ALDEx2](https://bioconductor.org/packages/release/bioc/html/ALDEx2.html) — compositional differential abundance.
- [Gloor et al., *Microbiome Datasets Are Compositional* (2017)](https://doi.org/10.3389/fmicb.2017.02224) — the canonical compositionality argument.
- [Faust & Raes, *Microbial interactions: from networks to models* (2012)](https://doi.org/10.1038/nrmicro2832) — community-dynamics modelling.
- [`changepoint` R package](https://cran.r-project.org/package=changepoint) and [`ruptures` Python](https://centre-borelli.github.io/ruptures-docs/) — change-point detection.
- [Soil Health Institute's measurement standards](https://soilhealthinstitute.org/) — practical context for biology + chemistry + physics integration.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available. The workspace is self-contained without it.
