# Biomechanical Engineering — Prosthetics Workspace

> A Claude Code workspace for biomechanical prosthetics engineering — lower-limb and upper-limb fittings — framed throughout as **statistical process control**. Every decision about socket fit, gait kinematics, component fatigue, and patient-reported outcomes is treated as a measured process with characteristic variation, control limits, and capability indices.

## What This Workspace Does

This workspace turns a prosthetics-and-orthotics (P&O) practice's fitting + follow-up data — pressure-mapping scans, 3D socket scans, force-plate gait recordings, fatigue-test rigs, encounter PROMs — into structured Statistical Process Control (SPC) outputs. Rather than chart-by-chart visual review, it applies the methods refined in manufacturing QC: I-MR and X-bar-R control charts on pressure distributions, Gauge R&R on scanner repeatability, Cp / Cpk on socket-lamination tolerances, paired-sample asymmetry detection on gait kinematics, DMAIC for clinic-wide fit-improvement programmes.

The agent guides the full cycle: baseline establishment, control chart deployment, assignable-cause investigation, fatigue testing against ISO 22675 / ISO 10328, outcome-measure trend analysis against MCID thresholds, recall screening, and Six Sigma–style continuous improvement.

## Why This Workspace Exists

P&O practices generate measurement data continuously — every cast, every alignment session, every gait-lab recording, every follow-up PROM — but most of it dies in the patient chart as a single point. Statistical methods that catch process drift early are well-developed in manufacturing but rarely transferred to fittings. Socket-fit complaints that show up in PEQ scores 90 days post-fit are often visible as control-chart signals at 30 days. Component fatigue failures that surface in MAUDE reports months later are often catchable in early ISO 22675 cycle excursions. This workspace codifies the discipline: each clinical signal pairs with a documented prior, a statistical test, and a credible interval — not just an "impression."

## Getting Started

### Prerequisites

- **Data sources** — pressure mapping (Tekscan F-Scan, Novel pedar-X, FSA), 3D socket scans (Rodin4D, BioSculptor, Omega), force plates (AMTI, Bertec, Kistler) and motion capture (Vicon, Qualisys), encounter PROMs (PEQ, AMP-PRO, PROMIS-PF, Houghton Scale of Use).
- **Statistical environment** — R (with `qcc`, `SixSigma`, `lme4`), Python (with `pyspc`, `statsmodels`, `pingouin`), or Minitab. Excel acceptable for control charts only — not for Gauge R&R or capability studies.
- **Regulatory familiarity** — ISO 10328 (lower-limb structural testing), ISO 22675 (foot/ankle cyclic testing), ISO 14971 (risk management), FDA 21 CFR 820 (QSR) if US-based; ANSI/RESNA standards for upper-limb. EU MDR if EU.
- **Clinical workflow integration** — read access to your practice management system or EHR (or structured export) for encounter-level data.

### Quick Start

1. Clone this workspace.
2. Drop encounter exports, pressure-map files, force-plate traces, and component lot data into `context/` (or `outputs/raw/` for large derived data).
3. Run `/gait-lab-spc-baseline` on at least 20 sessions of an established patient to lock baseline kinematic / kinetic distributions.
4. Run `/fitting-gauge-rr` once for each measurement system before treating its data as SPC input — measurement noise needs to be characterised before process noise can be.
5. Run `/socket-fit-control-chart` on follow-up pressure data; investigate any out-of-control signals as assignable causes.
6. Iterate: `/proms-trend-analysis` for cohort-level outcome trends; `/dmaic-fit-improvement` when a fit-quality programme spans multiple patients.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/gait-lab-spc-baseline` | Establish SPC baselines from gait-lab kinematics/kinetics | First 20+ sessions of an established patient or as periodic recalibration |
| `/socket-fit-control-chart` | I-MR / X-bar-R control charts on socket pressure mapping | Every follow-up visit with pressure data; weekly or monthly review |
| `/iso-22675-cycle-plan` | Plan ISO 22675 cyclic fatigue testing protocol | Before product acceptance testing; when new foot/ankle component is being qualified |
| `/proms-trend-analysis` | Statistical trend on PEQ / AMP-PRO / PROMIS / Houghton across encounters | Quarterly cohort review; pre-MDT meeting; outcomes reporting |
| `/fitting-gauge-rr` | Gauge R&R study on a measurement system | Onboarding a new scanner / pressure mat; quarterly re-validation |
| `/manufacturing-cpk-audit` | Cp / Cpk on socket manufacturing tolerances vs. spec | Each batch of in-house laminations; vendor incoming QC |
| `/gait-asymmetry-detect` | Statistical detection of prosthetic-vs-sound-side asymmetry | After every gait-lab session post-fit; at 30/60/90/180-day milestones |
| `/component-recall-screen` | Screen patient cohort against component recall notices | Whenever FDA MAUDE / manufacturer field action posts; monthly proactive sweep |
| `/dmaic-fit-improvement` | Six Sigma DMAIC cycle for clinic-wide fit-improvement programme | When socket-fit refit-rate exceeds baseline; quality committee initiative |

## Directory Structure

```
biomechanical-engineering-prosthetics/
├── CLAUDE.md                                # Agent role, available commands, foundational instructions
├── README.md                                # This file
├── .claude/commands/                        # 9 bespoke domain commands
│   ├── gait-lab-spc-baseline.md
│   ├── socket-fit-control-chart.md
│   ├── iso-22675-cycle-plan.md
│   ├── proms-trend-analysis.md
│   ├── fitting-gauge-rr.md
│   ├── manufacturing-cpk-audit.md
│   ├── gait-asymmetry-detect.md
│   ├── component-recall-screen.md
│   └── dmaic-fit-improvement.md
├── context/
│   ├── concepts.md                          # Prosthetic taxonomy, gait fundamentals, QC stats, standards, outcome measures
│   ├── workflows.md                         # Fitting, gait-lab SPC, ISO testing, gauge R&R, recall screening, DMAIC
│   └── references.md                        # ISO/ANSI table, PROMs scoring, K-level lookup, regulatory framework
├── prompts/                                 # 4 reusable prompts
│   ├── new-patient-fitting-intake.md
│   ├── component-selection-decision.md
│   ├── gait-deviation-differential.md
│   └── quality-complaint-root-cause.md
└── outputs/                                 # Control charts, capability reports, DMAIC charters, trend memos
```

## Example Use Cases

### Quarterly cohort PROM review for a TT amputee clinic
Pull all PEQ-MS and AMP-PRO scores from the last 90 days for K2/K3 transtibial patients. Run `/proms-trend-analysis` to detect significant trends after FDR adjustment. Pair any declines with `/socket-fit-control-chart` outputs from the same patients to triangulate whether the trend is fit-related, activity-related, or comorbidity-related.

### New foot/ankle component qualification
A new dynamic-response foot enters the formulary. Run `/iso-22675-cycle-plan` to design the acceptance-testing protocol — load profile, cycle count, instrumentation, accept/reject criteria. Run the test, then `/manufacturing-cpk-audit` on the as-manufactured tolerances to confirm vendor capability before fitting the first patient.

### MAUDE recall response
A manufacturer issues a field-action notice for a specific knee-component lot range. Run `/component-recall-screen` against your patient cohort with active components from that vendor; generates a prioritised action list (immediate refit needed / next-scheduled-visit triage / no-action), tracks acknowledgement, and produces an audit-ready compliance memo.

### DMAIC programme on a refit-rate problem
Clinic-wide socket refit rate at 90 days has crept from 12% to 19% over six months. Run `/dmaic-fit-improvement` to charter a Six Sigma project — Define the problem operationally, Measure baseline (refit rate, Cp/Cpk on lamination thickness, gauge R&R on scanner), Analyze for assignable causes (vendor change? new fitter? new pressure-mapping system?), Improve, then institute Control to lock in the gain.

### Gait-lab measurement-system validation
A new motion-capture system replaces an aging one. Before any gait data from the new system enters the SPC baseline, run `/fitting-gauge-rr` (or its kinematic equivalent) — repeated measurements of the same patient by the same operator and across operators. Establishes whether the system contributes <10% (acceptable), 10-30% (marginal), or >30% (unusable) of total observed variation.

## Recommended MCP Servers / Tools

- **filesystem** — for reading large pressure-map files, force-plate CSVs, scanner exports, encounter data dumps.
- **shell** — for invoking statistical pipelines (`Rscript`, `python -m pyspc`, `minitab` if local), 3D socket-scan processors.
- **python** — for custom statistical analyses (`statsmodels`, `pingouin`, `pyspc`, `pymc`), Gauge R&R calculations, control chart generation.
- **R** (via shell or dedicated MCP) — for `qcc`, `SixSigma`, `lme4`, `psych` — many specialist P&O statistics live in R packages.
- **sqlite** or **duckdb** — for joining encounter metadata with measurement data across visits.

## Legal & Ethical Considerations

- **Patient safety is sovereign.** Statistical methods flag concerns; clinical decisions belong to the licensed prosthetist (CPO/CO) and the prescribing physician. Never propose a fit-change that bypasses CPO sign-off.
- **HIPAA / GDPR.** All patient data referenced in this workspace must be either pseudonymised on entry or stored only in environments meeting your jurisdiction's PHI handling requirements. Never paste raw identifiers into the agent context.
- **Regulatory framework.** US fittings fall under FDA 21 CFR 820 (QSR) for the device side; clinic side under state P&O licensure. EU fittings under MDR 2017/745. Testing references must cite the current revision (ISO 22675:2016, ISO 10328:2016, etc.).
- **Component recall obligations.** When `/component-recall-screen` flags affected patients, the practice has documented duties to notify under FDA 21 CFR 806 (Medical Device Reporting) for US, MDR Article 87 for EU.

## Technical References

- [ISO 22675:2016 — Prosthetics — Testing of ankle-foot devices and foot units](https://www.iso.org/standard/70203.html) — cyclic fatigue testing standard.
- [ISO 10328:2016 — Prosthetics — Structural testing of lower-limb prostheses](https://www.iso.org/standard/70205.html) — structural strength testing.
- [ANSI/RESNA WC-1, WC-2, WC-3](https://www.resna.org/) — Rehabilitation Engineering and Assistive Technology Society standards.
- [Prosthetics and Orthotics International — Journal](https://journals.lww.com/poijournal/Pages/default.aspx) — peer-reviewed outcomes research.
- [Prosthesis Evaluation Questionnaire (PEQ)](https://www.amputee-coalition.org/wp-content/uploads/2015/05/PEQ-original.pdf) — Legro et al. 1998, the workhorse PROM for prosthesis users.
- [AMPnoPRO / AMPPRO scoring](https://onlinelibrary.wiley.com/doi/10.1002/pmrj.2007.07.041) — Amputee Mobility Predictor.
- [PROMIS Physical Function](https://www.healthmeasures.net/explore-measurement-systems/promis) — NIH-developed item bank.
- [FDA MAUDE database](https://www.fda.gov/medical-devices/medical-device-recalls) — Medical Device Recalls and adverse-event reporting.
- [Montgomery — Introduction to Statistical Quality Control (8th ed.)](https://www.wiley.com/en-us/Introduction+to+Statistical+Quality+Control%2C+8th+Edition-p-9781119723097) — canonical SPC textbook.
- [AIAG MSA Manual (4th ed.)](https://www.aiag.org/quality/automotive-core-tools/measurement-systems-analysis) — Gauge R&R reference.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available. The workspace is self-contained without it.
