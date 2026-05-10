# Soil Microbiome Management — References

Lookup data the agent reaches for during pipeline selection, dataset triage, and method choice. Compact by design — defer to upstream sources for fuller specs.

## Sequencing pipelines

| Tool | Scope | Notes |
|------|-------|-------|
| QIIME 2 | End-to-end amplicon | Plugin ecosystem; reproducible provenance |
| DADA2 | ASV inference | Replaces OTU clustering; preferred for new work |
| mothur | OTU pipeline | Older; still in use for legacy comparability |
| Kraken2 + Bracken | Shotgun taxonomy | Fast k-mer; pair with abundance correction |
| MetaPhlAn 4 | Shotgun taxonomy | Marker-gene based; species-level resolution |
| HUMAnN 3 / 4 | Functional profiling | UniRef + MetaCyc pathways |
| PICRUSt2 | Predicted function from 16S | Hypothesis generation only |
| FunGuild | Fungal trait assignment | Taxonomy -> guild (saprotroph, pathogen, AMF) |

## Primer regions in routine use

| Region | Primer pair | Target | Notes |
|--------|-------------|--------|-------|
| 16S V4 | 515F (Parada) / 806R (Apprill) | Bacteria + archaea | Earth Microbiome Project standard |
| 16S V3-V4 | 341F / 805R | Bacteria | Higher resolution, longer reads |
| ITS1 | ITS1F / ITS2 | Fungi | Length variation across phyla |
| ITS2 | ITS86F / ITS4 | Fungi | More even amplification across taxa |
| 18S V9 | 1391f / EukBr | Eukaryotes (incl. protists) | Earth Microbiome eukaryote standard |

## Time-series and statistics packages

### R
- `phyloseq` — data container + diversity analyses.
- `vegan` — diversity, ordination, PERMANOVA.
- `microbiome` — tidy microbiome helpers.
- `MaAsLin2` — multivariate associations with random effects (longitudinal).
- `ALDEx2`, `ANCOMBC` — compositional differential abundance.
- `forecast`, `fable` — ARIMA / state-space.
- `changepoint`, `bcp` — change-point detection.
- `Kendall`, `trend` — Mann-Kendall, Sen's slope.
- `lme4`, `glmmTMB` — mixed-effects.

### Python
- `scikit-bio` — diversity, ordination.
- `statsmodels` — SARIMAX, STL, state-space.
- `ruptures` — change-point detection.
- `pymc` / `numpyro` — Bayesian state-space, BCPD.
- `gneiss` — phylogenetic balances.

## Public datasets and catalogues

- **Earth Microbiome Project** — https://earthmicrobiome.org/ — global 16S/18S/ITS reference, EMP protocols.
- **MGnify (EBI)** — https://www.ebi.ac.uk/metagenomics/ — 500k+ public metagenomes.
- **Qiita** — https://qiita.ucsd.edu/ — 16S/ITS/18S studies with QIIME 2 provenance.
- **NCBI SRA / BioProject** — primary sequence archive.
- **USDA NRCS Soil Health Initiative** — https://www.nrcs.usda.gov/conservation-basics/natural-resource-concerns/soil/soil-health — methods + interpretation.
- **LTAR (Long-Term Agroecosystem Research) Network** — https://ltar.ars.usda.gov/ — multi-decade US ag plots.
- **NEON Soil Microbe Group** — https://www.neonscience.org/ — continental-scale time-series.
- **TerraGenome / Earth BioGenome** — broader context for reference genomes.

## Standards and methods

- **Soil sampling — ISO 10381** (series) — sampling guidance.
- **DNA extraction — ISO 11063** — direct extraction from soil for molecular methods.
- **Soil enzyme assays — Tabatabai / Sinsabaugh standard methods** — colorimetric and fluorometric.
- **Carbon / nitrogen — Walkley-Black, dry combustion (Dumas)** — for SOC and total N covariates.
- **Soil respiration — closed-chamber, IRGA** — for CO2 flux time-series.

## Canonical literature (starter list)

- Fierer 2017, *Nat Rev Microbiol* — embracing the unknown: understanding soil microbial communities.
- Schimel & Schaeffer 2012, *Front Microbiol* — microbial control over biogeochemistry.
- Wallenstein & Hall 2012 — trait-based community ecology of soil microbes.
- Faust & Raes 2012, *Nat Rev Microbiol* — microbial interactions, network analysis.
- Allison et al. 2010, *Nature Geoscience* — trait-based modelling of decomposition.
- Bahram et al. 2018, *Nature* — global topsoil microbiome structure.
- Crowther et al. 2019, *Nature Climate Change* — soil C response to warming.
- Trivedi et al. 2020, *Nat Rev Microbiol* — plant-microbiome interactions: from community assembly to plant health.
- Dini-Andreote et al. 2015, *PNAS* — assembly mechanisms during succession.

## Useful threshold heuristics

- **Read depth** — 10k reads/sample for 16S diversity; 50k+ for rare taxa; 5–10 M reads/sample for shotgun.
- **Detection** — taxon present in >=20% of samples and mean abundance >0.01% before including in trend tests.
- **Replication** — n=3 minimum for any treatment claim; n=4–6 for trend with FDR control.
- **Time points** — n>=4 for any "trend"; n>=8 for SARIMA / decomposition; n>=20 for reliable change-point.
