# Hybrid EMS — Multi-Source Intelligence Fusion Workspace

> An agent workspace for hybrid-vehicle energy management that fuses navigation, traffic, weather, V2X, driver, and powertrain telemetry into a single look-ahead picture — and turns that picture into torque-split and SOC-trajectory decisions you can defend to a calibration engineer.

## What This Workspace Does

Modern hybrid energy-management strategies (ECMS, A-ECMS, MPC, RL, rule-based with adaptive parameters) all share a problem: their performance is bounded by how well the controller knows what the next 1–30 km of driving will look like. A perfect optimiser on a perfect cycle still loses to a mediocre optimiser with an accurate **route prior**. The bottleneck is upstream of the controller — it is intelligence fusion.

This workspace codifies that upstream layer. It treats the EMS controller as a downstream consumer of a probabilistic trip forecast and focuses on **how** that forecast is constructed: which sources to ingest, how to time-align them, how to detect when they disagree, how to weight trust per source, and how to propagate uncertainty all the way through to the credible bands the controller sees. The technique lens for this build — *multi-source intelligence fusion* — frames every input as a partially-reliable witness and every decision as a fused posterior with a paper trail.

The workspace is opinionated about three things: every source has an explicit trust weight (no silent equal-vote averaging), every fused estimate emits a credible band (no point estimates without uncertainty), and every recommendation cites the sources that produced it (no black-box outputs).

## Why This Workspace Exists

Hybrid powertrain calibration teams routinely have V2X, ADAS look-ahead, cloud-routed traffic, weather APIs, and high-resolution elevation data available, but production EMS strategies often consume only one or two of these — usually because integrating more sources without an arbitration framework introduces more noise than signal. The shortcut is to fall back on rule-based heuristics or a single high-confidence source (typically nav-route + elevation) and accept the cost.

The workspace exists to make the next step affordable: fuse the rest, but do it carefully. It captures the fusion patterns, sensor-fault handling, and ablation methodology that distinguishes a serious EMS-with-fusion project from a demo that works on one curated drive and falls over the moment a V2X message is stale.

## Getting Started

### Prerequisites

- Vehicle parameter sheet (mass, frontal area, drag coefficient, rolling resistance, gear ratios, motor/engine maps, battery pack capacity & internal resistance).
- A drive-cycle library: at minimum WLTP class 3b and one RDE route GPX; ideally CLTC-P and EPA FTP-75 for cross-region comparison.
- A simulator with hybrid powertrain models — Autonomie, AMESim, GT-SUITE, Simulink with the Powertrain Blockset, or an in-house equivalent.
- A fusion / state-estimation toolchain — Python (`filterpy`, `pgmpy`, `pyro`/`pymc`) or MATLAB (Sensor Fusion and Tracking Toolbox, Stateflow).
- Optional but recommended: a CAN log decoder (`cantools` + DBC files), a V2X parser (J2735/SAE), an OpenStreetMap elevation + traffic data source.

### Quick Start

1. Clone this workspace into your project tree (it's self-contained — no global plugin is required).
2. Drop a representative drive log (CAN + GPS + any available V2X traces) into `outputs/raw-traces/<vehicle>-<date>/`. Add the vehicle parameter sheet to `context/` if it's not already there.
3. Run `/audit-fusion-trust` against the recorded drive to score each available input source — this tells you which sources are worth fusing before you spend integration effort.
4. Run `/fuse-trip-prior` for the next planned drive (or replay drive) to produce a route-aware power-demand prior. Inspect the credible bands.
5. Run `/predict-load-envelope` + `/optimize-split` to generate a horizon-aware torque-split and SOC trajectory; commit the resulting policy comparison to `outputs/`.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/fuse-trip-prior` | Construct a fused route-aware power-demand prior. | At trip start, route reroute, or whenever a major upstream source updates (new traffic, weather shift). |
| `/source-conflict` | Detect, classify, and arbitrate inter-source disagreement. | When `/audit-fusion-trust` flags a drop or when controllers report unexpected behaviour mid-drive. |
| `/predict-load-envelope` | Emit a look-ahead power demand distribution over the horizon. | Before invoking the EMS controller for the next planning window. |
| `/optimize-split` | Compute torque-split and SOC reference trajectory over the predicted horizon. | After `/predict-load-envelope`; in offline ablation runs. |
| `/audit-fusion-trust` | Score each source's per-drive reliability and propose trust-weight updates. | At the end of every test drive; weekly for fleet-learning rollups. |
| `/cycle-replay` | Replay a recorded drive against alternative fusion policies for ablation. | When comparing fusion policy candidates or quantifying the value of a candidate new source. |

## Directory Structure

```
hybrid-ems-intelligence-fusion/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # Bespoke EMS-fusion commands
├── context/
│   ├── concepts.md           # Architectures, EMS strategies, fusion algorithms, source taxonomy
│   ├── workflows.md          # Prior building, conflict arbitration, horizon opt, replay ablation
│   └── references.md         # Drive cycles, V2X message formats, fusion toolchains, signal IDs
├── prompts/                  # Reusable EMS-fusion prompt templates
└── outputs/                  # Generated priors, ablations, policy comparisons, audit reports
```

## Example Use Cases

### PHEV — Trip-Aware Charge-Depleting / Charge-Sustaining Switch
Use `/fuse-trip-prior` to predict whether a planned route can finish on remaining battery energy alone. If the credible upper bound exceeds available SOC, schedule a CS segment in the geographically optimal section (typically the lowest-load highway stretch) rather than running CD until depletion and forcing CS in a high-load urban segment.

### HEV — V2X-Assisted Predictive SOC Reference
Use `/predict-load-envelope` with fused signalised-intersection countdown timers (J2735 SPaT) and stop-bar locations to pre-charge before known regen opportunities and pre-discharge before known launch events, smoothing SOC oscillation without rule-based heuristics.

### Fleet — Trust-Weight Learning From Aggregated Drives
Run `/audit-fusion-trust` over a week of fleet drives and roll up per-source reliability across vehicle variants and operating regions. Surface sources that are reliable in city X but unreliable in city Y (typically: cloud traffic feeds in fringe-coverage regions).

### EMC Lab — Sensor-Fault Robustness
Use `/source-conflict` and `/cycle-replay` to inject synthetic sensor faults (frozen V2X feed, drifted IMU, GPS outage in tunnel) and quantify how much the fused EMS policy degrades vs. an unfused baseline. Establishes the **fault degradation budget** for production sign-off.

### Battery Engineering — SOH-Aware Strategy Drift
Combine `/audit-fusion-trust` outputs with battery prognostics signals over months of operation. Detect when the EMS strategy implicitly relies on a battery internal-resistance model that has drifted past its validity envelope — the fusion stack is often the first to surface this because its source-conflict scores degrade before any single subsystem complains.

## Recommended MCP Servers

- **Filesystem (read drive logs, write outputs)** — bulk ingest of CAN/GPS/V2X traces, write of plots and audit reports.
- **Python / Jupyter execution** — running `filterpy`, `pgmpy`, `pyro`/`pymc` fusion and uncertainty propagation routines inline.
- **OpenStreetMap / elevation tiles** — fetching elevation + road-class data for offline route prior construction.
- **Anthropic API for batch ablations** — fanning out `/cycle-replay` runs across drive-cycle library variants when an integrated execution environment is available.

## Legal & Ethical Considerations

- **Driver consent and privacy.** Fused logs typically contain GPS traces, driver-style fingerprints, and behavioural patterns. Strip identifiers before sharing logs externally; comply with applicable data protection regimes (GDPR Art. 4 personal data + Art. 22 automated decision-making, CCPA, KVKK, PIPEDA depending on region).
- **Type approval and emissions certification.** Any EMS change that affects engine on/off scheduling, EAT temperature, or fuel consumption can interact with WLTP/RDE certification. Don't propose calibration changes that haven't been re-certified.
- **Cybersecurity (UN R155 / ISO/SAE 21434).** Fusing V2X and cloud sources introduces remote-attack surface. Treat every external feed as adversarial input by default; assume an intermittently malicious V2X source and design the fusion layer to degrade gracefully.
- **Functional safety (ISO 26262).** EMS decisions can affect drivability (e.g. unexpected mode changes during a passing manoeuvre). Hazard analysis must cover the fusion layer's failure modes, not only the controller's.

## Technical References

- [SAE J2735 (DSRC Message Set Dictionary)](https://www.sae.org/standards/content/j2735_202309/) — V2X message structure (BSM, SPaT, MAP).
- [ISO 23150 (Road vehicles — Data communication between sensors and data fusion unit)](https://www.iso.org/standard/74570.html) — sensor fusion data model for vehicle perception.
- [ISO 26262 (Functional safety — Road vehicles)](https://www.iso.org/standard/68383.html) — hazard analysis and ASIL requirements for EMS function chains.
- [UN R155 (Cybersecurity and CSMS)](https://unece.org/transport/documents/2021/03/standards/un-regulation-no-155-cyber-security-and-cyber-security) — V2X / connected-vehicle threat handling.
- [Argonne Autonomie](https://www.anl.gov/taps/autonomie) — vehicle simulation reference platform widely used for HEV/PHEV powertrain studies.
- [Argonne — A Survey of Hybrid Electric Vehicle Energy Management Strategies](https://publications.anl.gov/) — taxonomy of rule-based, ECMS/A-ECMS, MPC, and RL approaches.
- [filterpy (Kalman / Bayesian filters in Python)](https://github.com/rlabbe/filterpy) — practical reference implementations for state estimation and fusion.
- [WLTP / RDE regulatory texts (UNECE WP.29 GTR 15)](https://unece.org/transport/vehicle-regulations) — drive cycle and real-driving emissions specification.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace is fully usable without it.
