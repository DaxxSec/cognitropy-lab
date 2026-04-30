# Macroeconomics GDP Modeling Workspace

> An agent workspace for building, estimating, and publishing GDP forecasts under a forensic chain-of-custody regime — every vintage, transformation, and model fit is sealed as evidence so that any quarterly forecast can be rebuilt bit-for-bit from raw inputs.

## What This Workspace Does

This workspace turns a GDP modeling pipeline into something closer to an ML training lab with a crime-scene log book attached. It guides you through:

- Pulling **real-time vintages** of expenditure, production, and income series from FRED ALFRED, OECD MEI, Eurostat, BEA NIPA, and national statistics offices.
- Sealing every retrieved series as immutable **evidence** with hash, timestamp, source URL, and license.
- Estimating the standard family of GDP models — **bridge equations, dynamic factor models (DFM), MIDAS regressions, BVAR, and small DSGE** — and treating each fit as a reproducible **training run** with pinned seeds and archived hyperparameters.
- Reconciling **vintage revisions** against priors so the agent can explain why this quarter's print differs from the advance estimate.
- Releasing forecast packages with a full **custody manifest** — the published number is always reconstructable.

## Why This Workspace Exists

GDP forecasting has a reproducibility problem. Forecasters routinely report numbers without recording which vintage of which series they used, with what seasonal adjustment, against which code revision. When the official print revises, the post-mortem becomes an archaeological dig instead of a structured comparison. Meanwhile, the ML community has solved most of these problems already — pinned seeds, MLflow-style run tracking, hashed artifacts, deterministic preprocessing. The forensic community has solved the rest — chain of custody, evidence sealing, tamper-evident manifests.

This workspace fuses both. Every model fit is a tagged training run. Every series snapshot is a sealed evidence item. Every published forecast carries the custody trail of the inputs that produced it.

## Getting Started

### Prerequisites

- Python 3.10+ with `pandas`, `numpy`, `statsmodels`, `scikit-learn`, `arch`, optionally `pymc`, `dynamax`, `linearmodels`
- An API key for at least one real-time source (FRED is the typical baseline; ALFRED is free and provides vintages)
- Access to a clean git repository for the lineage commits — every model fit pins to a commit hash
- (Optional) `gpg` for signing release manifests
- (Optional) `duckdb` for local OLAP over sealed vintage parquet files

### Quick Start

1. Clone this workspace into your forecasting project directory.
2. Run `/onboard` to record country/region, target GDP series (e.g. `GDPC1` quarterly chained 2017 USD), modeling approach (top-down expenditure / DFM nowcast / BVAR), and vintage retention policy.
3. Run `/ingest-vintage` to pull today's vintages and seal them. Re-run on every release day; the sealed snapshots accumulate as `outputs/vintages/<source>/<series>/v<YYYY-MM-DD>.parquet` plus a manifest.
4. Run `/build-nowcast` to spin up a current-quarter nowcast — typically a DFM or bridge equation — fed from the sealed vintages.
5. Run `/estimate-model` to fit a horizon-extending model (BVAR / DSGE / gradient-boosted regressor) and tag the artifact.
6. After each official release, run `/audit-revision` to reconcile the new print and decompose the revision into (a) data revision, (b) model drift, (c) realised innovations.
7. When ready to publish, run `/release-forecast` — the agent assembles the forecast package with its custody manifest and (optionally) GPG signs it.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/onboard` | Configure target country, series, modeling approach, custody policy | First time setup |
| `/ingest-vintage` | Retrieve and seal today's vintages of a configured series set | Every release day, or before a forecast run |
| `/build-nowcast` | Construct/refresh a current-quarter nowcast (bridge / DFM / MIDAS) | Mid-quarter, after monthly indicators land |
| `/estimate-model` | Fit a horizon-extending GDP model with full training-run lineage | When a new model is needed or the validation cadence triggers a refit |
| `/audit-revision` | Reconcile a new official print against the prior vintage and decompose the delta | Within 24h of a BEA / Eurostat / national release |
| `/compare-forecasts` | Score competing forecasts (own vs. consensus vs. SPF) using realised vintages | Quarterly, after final prints settle |
| `/release-forecast` | Build a sealed, signed forecast package with its custody manifest | Before any external publication of a forecast number |

## Directory Structure

```
macroeconomics-gdp-modeling/
├── CLAUDE.md                              # Lightweight role and command index
├── README.md                              # This file
├── CREATION_REPORT.md                     # Why this workspace exists
├── context/
│   ├── project.md                         # Target country, series, policy
│   ├── role.md                            # User's role (forecaster, researcher, sovereign analyst)
│   ├── constraints.md                     # Embargoes, data licenses, publication rules
│   └── for-agent/
│       ├── domain-knowledge.md            # GDP measurement, vintages, methodology, custody primer
│       ├── workflows.md                   # End-to-end forecasting workflows
│       ├── environment.md                 # Python env, API keys, GPG setup
│       └── tools.md                       # FRED/ALFRED/OECD/Eurostat clients, statsmodels recipes
├── .claude/commands/
│   ├── onboard.md
│   ├── ingest-vintage.md
│   ├── build-nowcast.md
│   ├── estimate-model.md
│   ├── audit-revision.md
│   ├── compare-forecasts.md
│   └── release-forecast.md
├── prompts/
│   ├── vintage-evidence-sealing.md        # Template prompt for evidence seal step
│   ├── revision-postmortem.md             # Template for explaining a revision
│   └── nowcast-decision-note.md           # Template for current-quarter decision write-up
├── resources/
│   ├── gdp-identities-cheatsheet.md       # Y = C + I + G + (X-M); production / income approach
│   ├── series-catalog.md                  # FRED / ALFRED / OECD / Eurostat series IDs
│   └── custody-manifest-schema.md         # JSON schema for evidence and run manifests
├── planning/                              # Active model design notes, plan.md
├── outputs/
│   ├── vintages/                          # Sealed real-time data snapshots
│   ├── models/                            # Tagged model artifacts (joblib, json metadata)
│   ├── forecasts/                         # Forecast bundles
│   └── manifests/                         # Custody manifests (one per release)
├── user-docs/
│   ├── getting-started.md                 # Quick start
│   └── report.md                          # Stakeholder-facing report template
└── work-log/                              # Dated session logs
    └── session-log.md
```

## Core Concepts

### 1. Vintages, not series

A GDP series is not a single time series — it is a *family* of time series indexed by retrieval date. The 2024Q1 advance print on 2024-04-25 is a different observation from the 2024Q1 third estimate on 2024-06-27. Honest forecast evaluation requires the vintage available *at decision time*, not the latest revised series. This workspace stores every retrieved vintage as `outputs/vintages/<source>/<series>/v<YYYY-MM-DD>.parquet`.

### 2. Evidence sealing

Every retrieved vintage is hashed (SHA-256) and recorded in a custody manifest with: source URL, retrieval timestamp UTC, vintage date as reported by source, license, and the agent identity that fetched it. Sealed evidence is **append-only** — a re-pull of the same vintage on a later date is a separate evidence item, never an overwrite.

### 3. Models as training runs

Every model fit produces a tagged artifact (`outputs/models/<model>__<config>__<git_sha>.joblib`) plus a JSON sidecar recording: input vintage hashes, hyperparameters, random seeds, library versions, validation metrics (RMSFE, MAE, log score), and the code git SHA. The fit is reproducible bit-for-bit if the same inputs are replayed.

### 4. Revision decomposition

When an official print is revised, the workspace decomposes the delta into:
- **Data revision component:** Δ from the source statistics office's revisions to component series.
- **Model drift component:** Δ from refitting the model on the new vintage.
- **Innovation component:** the genuine forecast error that remains after the first two are removed.

This is the discipline that separates a forecaster's skill score from the noise of revisions.

### 5. Custody manifest at publication

A released forecast carries a manifest containing every input vintage hash, every model artifact hash, every code commit, and a signed digest. Anyone given the workspace and the manifest can reproduce the published number.

## Example Use Cases

### Sovereign Analyst Quarterly Note
A sell-side macro analyst publishes a quarterly GDP nowcast. Before publication, `/release-forecast` produces a sealed bundle. After the official print, `/audit-revision` decomposes the surprise into model error vs. data revision and feeds the `work-log/` post-mortem.

### Central Bank Research Replication
A research team needs to reproduce a 2018 BVAR forecast as part of a methodology paper. They check out the relevant git tag, replay the sealed 2018 vintages, and rebuild the forecast bit-for-bit — the manifest tells them exactly which vintages and parameters to use.

### Real-Time Recession Tracker
An analyst maintains a Sahm-rule and DFM-based recession probability. Every monthly release, `/ingest-vintage` seals the new unemployment, payrolls, and IP series; `/build-nowcast` updates the probability; the work-log captures the day's signal.

### ML Forecaster Evaluation
A team tests a gradient-boosted regressor against a Federal Reserve BVAR. `/compare-forecasts` runs both against the same sealed real-time vintages and produces a Diebold–Mariano test, RMSFE table, and bias decomposition.

### Methodology Audit Trail for Regulators
A statistical office or sovereign issuer needs an audit trail showing that published GDP forecasts have not been retro-fit. The custody manifests are the audit trail; every published number can be tied back to inputs available at decision time.

## Recommended MCP Servers

- **filesystem** — Read/write sealed vintage parquet files and model artifacts.
- **shell** — Drive `git`, `gpg --detach-sign`, and CLI tools for FRED/ALFRED retrieval.
- **python** — Run `statsmodels`, `arch`, `pymc`, `scikit-learn` for fits and tests.
- **fetch** / **http** — Retrieve series from public APIs (FRED/ALFRED, OECD SDMX, Eurostat SDMX).

## Legal & Ethical Considerations

- **Embargoes.** Many statistical releases are under press embargo until a stated UTC time. Never publish a forecast that depends on embargoed data before the embargo lifts. The workspace records the embargo timestamp on each vintage.
- **Licensing.** FRED/ALFRED is public; OECD/Eurostat content is licensed under specific reuse terms; some private vintages (Bloomberg, Refinitiv) are not redistributable. The custody manifest records the license per series.
- **Disclosure of methodology.** Published forecasts should disclose the model class, vintage cutoff, and any judgmental adjustments. The release manifest captures this.
- **Conflicts of interest.** A forecaster publishing GDP estimates that affect markets they trade should disclose accordingly; this workspace does not police that, but it produces the auditable trail that regulators expect.
- **No fabrication of revisions.** The append-only custody policy exists to prevent post-hoc rewriting of "what we thought at the time." Do not delete or overwrite a sealed vintage.

## Technical References

- [FRED ALFRED — Real-Time Vintages](https://alfred.stlouisfed.org/)
- [BEA NIPA Methodology](https://www.bea.gov/resources/methodologies/concepts-methods-us-national-income-and-product-accounts)
- [OECD Main Economic Indicators (MEI)](https://www.oecd.org/sdd/oecdmaineconomicindicatorsmei.htm)
- [Eurostat SDMX API](https://wikis.ec.europa.eu/display/EUROSTATHELP/API+-+Statistics+-+SDMX+2.1)
- [Stock & Watson — Dynamic Factor Models](https://www.princeton.edu/~mwatson/papers/Stock_Watson_HOM_DFM.pdf)
- [Ghysels, Sinko & Valkanov — MIDAS Regressions](https://www.tandfonline.com/doi/abs/10.1080/07474930600972467)
- [Giannone, Reichlin, Small — Nowcasting (NY Fed)](https://www.newyorkfed.org/research/policy/nowcast)
- [Diebold–Mariano Test for Forecast Accuracy](https://www.tandfonline.com/doi/abs/10.1080/07350015.1995.10524599)
- [NIST SP 800-86 — Guide to Integrating Forensic Techniques (chain-of-custody primer)](https://csrc.nist.gov/publications/detail/sp/800-86/final)
- [MLflow — Tracking Methodology Reference](https://mlflow.org/docs/latest/tracking.html)
