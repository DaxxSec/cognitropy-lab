# Hydraulic Engineering Fluid Dynamics Workspace

A Claude agent workspace for hydraulic engineering analysis with Bayesian probability methods. This workspace combines classical fluid dynamics with modern probabilistic reasoning to handle the uncertainty inherent in real-world hydraulic systems — from pipe network design to flood risk assessment.

## Why This Workspace Exists

Hydraulic engineering decisions carry enormous consequences: undersized culverts cause flooding, over-designed systems waste millions, and aging infrastructure fails in ways that deterministic models don't predict. Traditional hydraulic analysis relies on safety factors and worst-case assumptions. This workspace takes a different approach — using Bayesian probability to quantify what we actually know, what we're uncertain about, and how that uncertainty propagates through design decisions.

The agent applies Bayesian methods to:
- **Flood frequency analysis** — updating return-period estimates as new data arrives
- **Pipe network reliability** — probabilistic capacity assessment under demand uncertainty
- **Model calibration** — fitting hydraulic model parameters (Manning's n, loss coefficients) to field measurements
- **Infrastructure risk scoring** — combining condition data, loading, and consequence into actionable risk rankings
- **Design optimization** — finding cost-optimal designs that meet reliability targets

## Getting Started

### 1. Clone and Initialize
```bash
git clone https://github.com/your-org/hydraulic-engineering-fluid-dynamics.git
cd hydraulic-engineering-fluid-dynamics
```

### 2. Run Onboarding
Use the `/onboard` command to configure the workspace for your specific project:
- What type of hydraulic system you're analyzing (open channel, pressurized, combined)
- Your data sources (USGS gauges, SCADA, field surveys, LiDAR)
- Regulatory framework (FEMA, state dam safety, local stormwater ordinances)
- Computational environment (Python packages, HEC-RAS version, SWMM, EPANET)

### 3. Start Analyzing
Pick a command that matches your task — see the Command Reference below.

## Command Reference

| Command | Description |
|---------|-------------|
| `/onboard` | Initialize workspace with your project context, data sources, and regulatory requirements |
| `/analyze-flow` | Run hydraulic flow analysis (open channel or pressurized) with Bayesian uncertainty bands |
| `/risk-assess` | Probabilistic risk assessment — combines hazard, vulnerability, and consequence |
| `/flood-model` | Flood frequency and inundation modeling using Bayesian return-period estimation |
| `/pipe-network` | Pipe network hydraulics — demand allocation, head loss, reliability under uncertainty |
| `/calibrate` | Bayesian parameter calibration from field observations (Manning's n, C-values, loss coefficients) |

## Directory Structure

```
hydraulic-engineering-fluid-dynamics/
├── CLAUDE.md                     # Agent identity and command registry
├── README.md                     # This file
├── CREATION_REPORT.md            # Build rationale and domain context
├── context/
│   ├── project.md                # Your specific project definition
│   ├── role.md                   # Your role and expertise level
│   ├── constraints.md            # Boundaries, standards, regulations
│   └── for-agent/
│       ├── domain-knowledge.md   # Hydraulic engineering fundamentals + Bayesian methods
│       ├── environment.md        # Software, data sources, compute setup
│       ├── tools.md              # Recommended tools and integrations
│       └── workflows.md         # Step-by-step analysis workflows
├── .claude/commands/             # Slash command definitions
├── prompts/                      # Reusable prompt templates
├── resources/                    # Reference tables, equations, standards
├── outputs/                      # Generated reports, plots, data
├── planning/                     # Active analysis plans
├── user-docs/                    # Agent-written guides for the user
└── work-log/                     # Session logs and analysis history
```

## Example Use Cases

### Municipal Stormwater System Upgrade
You have a 30-year-old storm sewer system serving a growing suburban area. Rainfall patterns are shifting, impervious cover is increasing, and you need to decide which segments to upsize. Use `/risk-assess` to rank pipe segments by failure probability, `/analyze-flow` to model capacity under projected conditions, and `/calibrate` to tune your model using flow monitoring data.

### Dam Safety Probabilistic Risk Assessment
A state dam safety program needs to prioritize inspection and rehabilitation across 200+ dams. Use `/flood-model` to generate inflow design floods with Bayesian return-period estimates, `/risk-assess` to combine structural condition scores with downstream consequence, and produce ranked risk registers with uncertainty bounds.

### Water Distribution Network Reliability
An aging water utility wants to understand where their network is most vulnerable to pressure deficits during peak demand or fire flow events. Use `/pipe-network` with Monte Carlo demand sampling to identify critical pipes, quantify the probability of pressure standard violations, and optimize capital improvement sequencing.

### Stream Restoration Design
A watershed group needs to size rock vein structures for a stream restoration project. Channel geometry is surveyed but roughness and bankfull discharge are uncertain. Use `/calibrate` to fit Manning's n from stage-discharge measurements, then `/analyze-flow` to design structures that perform across the credible parameter range.

## Recommended Tools & Integrations

- **Python**: NumPy, SciPy, PyMC (Bayesian inference), ArviZ (posterior diagnostics)
- **HEC-RAS**: 1D/2D hydraulic modeling (the agent can script HEC-RAS via RASController or HEC-RAS Python API)
- **EPANET / WNTR**: Water distribution network modeling
- **SWMM / PySWMM**: Stormwater and combined sewer modeling
- **QGIS / GeoPandas**: Spatial analysis, watershed delineation, flood mapping
- **USGS dataretrieval**: Pull streamflow and gage data programmatically

## Ethical & Safety Considerations

- **This workspace does not replace licensed professional engineering judgment.** All outputs should be reviewed by a qualified PE before use in design or regulatory submissions.
- Bayesian methods quantify uncertainty — they do not eliminate it. Always communicate uncertainty ranges to stakeholders.
- Flood risk analysis affects public safety. Be conservative with life-safety-related decisions even when probabilistic analysis suggests lower risk.
- Climate non-stationarity means historical data may not represent future conditions. The agent will flag this assumption when relevant.
- Dam and levee analyses may be subject to security restrictions. Do not include sensitive infrastructure data in public repositories.

## Cognitropy Lab

This workspace was generated by the [Cognitropy Lab](https://github.com/DaxxSec/cognitropy-lab) — a daily agent workspace factory that explores diverse domains through the lens of AI-assisted analysis. Day 6 assignment: Engineering & Technical domain, Bayesian probability assessment technique.
