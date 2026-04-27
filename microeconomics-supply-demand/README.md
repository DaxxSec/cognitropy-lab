# Microeconomics Supply & Demand — Risk Scoring Matrix Workspace

> A Claude Agent Workspace that turns supply-and-demand analysis into defensible, audit-ready risk scores. Bring a market, a product, or a SKU portfolio; leave with an ISO 31000–aligned risk register backed by elasticity estimates, equilibrium stress tests, and calibrated likelihood × impact matrices.

## What This Workspace Does

This workspace bridges two worlds that usually don't talk to each other:

- **Microeconomics** — partial-equilibrium supply/demand models, elasticity, surplus analysis, comparative statics.
- **Operational risk management** — IEC 31010 risk matrices, ISO 31000 risk registers, COSO ERM heat maps, FMEA/RPN scoring.

It treats every market force (a supply disruption, a demand shock, a substitute entry, a regulation) as a *risk event* and scores it on a calibrated likelihood × impact matrix that an executive, a buyer, or a portfolio manager can act on. The economics anchors the score; the matrix communicates it.

## Why This Domain × Technique Pairing Matters

Supply/demand analysis traditionally produces *narratives* ("oil is volatile"), *plots* (a curve shift), or *point estimates* (Δprice = 8%). None of those slot cleanly into an enterprise risk framework. Risk matrices, conversely, are widely understood and integrated with existing GRC tooling — but when they're populated by gut feel, they produce risk theater.

The pairing solves both problems:

- The **risk-scoring matrix** gives the analyst a discipline (decompose the event into likelihood and impact, anchor each axis to a calibration scale, repeat).
- The **microeconomic model** provides the *evidence* for each axis — elasticity ranges are likelihoods of large quantity responses; surplus deltas are impact magnitudes; structural-vs-parametric distinctions prevent double counting.

The result is a risk register where every row says, in effect, "we expect X to happen with probability anchored to historical base rate Y, the consequence is bounded by elasticity ε with CI Z, and the cell is therefore (L=3, I=4) → score 12 → amber tier."

## Getting Started

### Prerequisites

- Some understanding of supply-and-demand basics (curves, elasticity, equilibrium). The workspace teaches the rest as you go.
- A market or product portfolio you want to assess.
- Optional: time-series price/quantity data (CSV/Parquet) for empirical elasticity estimation; otherwise the workspace will use literature priors.
- Python 3.10+ with `numpy`, `pandas`, `statsmodels`, `matplotlib`, `seaborn` (for `/equilibrium-stress-test` and `/elasticity-risk-matrix` plotting). All optional — the agent can work in qualitative mode without them.

### Quick Start

1. Clone or open this workspace.
2. Run `/onboard` — the agent interviews you about market scope, products, time horizon, scoring scale (3×3 / 5×5 / 7×7), risk appetite, and data availability.
3. Drop any reference data (price series, sales history, regulatory texts) into a folder of your choice and tell the agent the path.
4. Run `/calibrate-scale` to anchor the 1–5 likelihood and impact tiers to *your* business's units (revenue, margin, units, downtime hours).
5. Run `/score-supply-shock` or `/score-demand-shock` for each named scenario in your watchlist.
6. Run `/elasticity-risk-matrix` once you have ε estimates per SKU/segment to produce a portfolio-wide heat map.
7. Run `/draft-risk-register` to consolidate everything into `outputs/risk-register-<date>.md` for stakeholder distribution.

## Command Reference

| Command | Description | Inputs | Outputs |
|---|---|---|---|
| `/onboard` | Interview-driven workspace initialization | User responses to 8–12 questions | Populated `context/project.md`, `context/role.md`, `context/constraints.md` |
| `/calibrate-scale` | Anchor the L/I axes to user's business metrics | Revenue, margin, headcount thresholds; risk appetite statement | Updated `context/constraints.md`, calibration log in `work-log/` |
| `/score-supply-shock` | Score a named supply-side disruption | Scenario name, suspected cause, affected inputs, expected duration, supply elasticity (est.) | Scenario card in `outputs/`, register entry, matrix coordinates (L, I, RPN) |
| `/score-demand-shock` | Score a named demand-side disruption | Scenario name, driver (income, taste, regulation, substitute), affected segments, demand elasticity (est.) | Scenario card in `outputs/`, register entry, matrix coordinates |
| `/elasticity-risk-matrix` | Build a 2D matrix across SKUs/segments | Elasticity estimates with CIs, axis selection (own-price × income, own × cross, etc.) | `outputs/elasticity-matrix-<date>.md` with PNG heat map |
| `/equilibrium-stress-test` | Comparative statics under a named scenario | Initial S/D parameters, perturbation (curve shift type and magnitude), surplus baseline | `outputs/stress-<scenario>.md` with ΔP*, ΔQ*, ΔCS, ΔPS, deadweight loss, composite RPN |
| `/cross-elasticity-screen` | Substitute/complement screening across a basket | Product list, observed cross-elasticities or qualitative substitution claims | `outputs/cross-elasticity-<date>.md` heat map + ranked substitution risks |
| `/draft-risk-register` | Consolidate scenario cards into ISO 31000 register | All scenario cards in `outputs/` | `outputs/risk-register-<date>.md` with cause → event → consequence → score → treatment columns |

## Directory Structure

```
microeconomics-supply-demand/
├── CLAUDE.md                      # Agent role and operating rules
├── README.md                      # This file
├── CREATION_REPORT.md             # Why this workspace exists
├── context/
│   ├── project.md                 # Market, products, horizon (populated by /onboard)
│   ├── role.md                    # Your role, decision rights, audience
│   ├── constraints.md             # Calibrated L/I scales, risk appetite, ethical bounds
│   └── for-agent/
│       ├── domain-knowledge.md    # Microeconomics + risk-matrix reference
│       ├── workflows.md           # Step-by-step scoring workflows w/ decision trees
│       ├── environment.md         # Data sources, file conventions, Python env
│       └── tools.md               # Statsmodels, scipy, IEC 31010 mapping
├── .claude/commands/              # Slash commands above
├── prompts/                       # Reusable prompt templates
│   ├── commodity-supply-chain-screen.md
│   ├── consumer-demand-shift-analysis.md
│   └── pricing-power-vulnerability.md
├── resources/                     # Reference materials
│   ├── risk-matrix-templates.md   # 3x3, 5x5, 7x7 templates with calibration guidance
│   ├── elasticity-reference.md    # Common elasticity values by category, interpretation guide
│   └── iso-31000-mapping.md       # How matrix scores map to ISO 31000 register fields
├── planning/
│   └── plan.md                    # Active assessment plan
├── outputs/                       # Scenario cards, registers, heat maps
├── user-docs/
│   └── getting-started.md         # User-facing introduction
└── work-log/                      # Dated session logs
    └── 2026-04-27.md              # Day 1: workspace built
```

## Example Use Cases

### 1. Commodity Buyer Hedging Decision

A procurement lead at a food manufacturer needs to decide whether to hedge wheat exposure for the next 6 months. They run `/score-supply-shock` for ("Black Sea export disruption", "drought in major producer", "import quota change"), then `/score-demand-shock` for ("recession demand drop", "competing-substitute crop pricing"). The resulting register tells them which scenarios sit in the red zone (L=4, I=5) and informs hedge ratio sizing — without pretending to forecast prices.

### 2. SaaS Pricing Committee Vulnerability Review

A product team is considering a 12% price increase across a 40-SKU catalog. They run `/elasticity-risk-matrix` with own-price × cross-price elasticity per SKU. SKUs with εd more negative than −2.0 *and* high cross-elasticity to a free competitor end up in the red cell — concrete candidates for grandfathering or smaller increases.

### 3. Regulatory Change Impact Assessment

A device maker faces a possible new compliance mandate (e.g., EU CSRD, USP <800>) that increases marginal cost by an estimated 4–9%. They run `/equilibrium-stress-test` with a leftward supply shift scenario, and the workspace returns ΔP*, ΔQ*, deadweight loss, and a composite RPN — feeding the mandatory regulatory impact assessment workpaper.

### 4. Portfolio Substitution Screen

A consumer-goods analyst wants to know which of their 60 products are most vulnerable to a private-label entrant. `/cross-elasticity-screen` ranks products by estimated cross-elasticity to the entrant's likely price point and surfaces a top-10 watchlist with calibrated scores.

## Recommended MCP Servers and External Tools

- **filesystem MCP** — for reading price/quantity CSVs, writing scorecards and registers.
- **shell MCP** — for invoking Python (`statsmodels` log-log regression, `scipy.optimize.curve_fit` for nonlinear demand) when empirical elasticity estimation is needed.
- **fetch / web MCP** — for pulling literature elasticity priors (e.g., Goolsbee & Petrin for cable, Hausman for consumer goods) when no in-house data exists.
- **A risk register or GRC system** (Archer, ServiceNow IRM, Resolver) — the workspace exports markdown that is straightforward to convert into the register's import schema.

## Ethical and Legal Considerations

This workspace produces analytical artifacts only. Specifically:

- **Not investment or trading advice.** Risk scores are decision *inputs*, not recommendations to buy, sell, or hedge any security or commodity.
- **Not pricing collusion-safe by default.** Cross-firm pricing analyses must respect antitrust law (Sherman Act §1, EU Article 101, equivalent regimes). The workspace will refuse to coordinate pricing across firms or share competitively sensitive forecasts.
- **Not consumer welfare claims.** Producer/consumer surplus deltas are model outputs; presenting them as societal welfare claims requires a much richer model than partial equilibrium.
- **Calibration is the analyst's responsibility.** A 5×5 cell is only as good as the calibration anchors; mis-anchored matrices give false confidence. The workspace forces calibration documentation but cannot vouch for its alignment with reality.

## Methodology Anchors and Citations

This workspace is built on widely accepted standards and texts. When the agent cites methodology, it should reference these directly:

- **ISO 31000:2018** — *Risk management — Guidelines.* Defines risk register structure (event, cause, consequence, control, treatment).
- **IEC 31010:2019** — *Risk management — Risk assessment techniques.* Section B.29 covers risk matrices specifically; sections B.7–B.10 cover scenario analysis and Bow-tie.
- **COSO ERM Framework (2017)** — *Enterprise Risk Management — Integrating with Strategy and Performance.* Heat-map and risk-appetite vocabulary.
- **NIST SP 800-30 Rev. 1** — Risk assessment guide; the L × I scoring approach is adapted from §3.2 (qualitative tier) and Appendix I (semi-quantitative).
- **Marshall (1890)** — *Principles of Economics.* Original partial-equilibrium S/D framework.
- **Hicks (1939); Slutsky (1915)** — Income/substitution decomposition; basis for own × income elasticity matrix.
- **Tirole (1988)** — *The Theory of Industrial Organization.* Cross-elasticity and substitute analysis grounded here.
- **Varian (current ed.)** — *Microeconomic Analysis.* Standard reference for elasticity formulas and surplus calculations the workspace uses.

## A Note on Limits

Partial-equilibrium analysis ignores feedback loops between markets. For multi-market or general-equilibrium questions (a tax that affects both labor and capital, climate transition risk across an economy), this workspace will give you the right *vocabulary* but the wrong *boundary*. Pair it with a CGE or multi-sector model in those cases — and document the limitation in the register's "model risk" column.
