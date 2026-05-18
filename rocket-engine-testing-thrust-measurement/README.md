# Rocket Engine Testing Thrust Measurement Workspace

> A ground-test propulsion workspace for hot-fire risk planning and thrust-stand uncertainty work — every failure mode lands on a MIL-STD-882E likelihood × severity matrix before the propellant valves crack open.

## What This Workspace Does

Liquid rocket engine ground testing is where propellants meet metal at chamber pressures of 30–250 bar and exhaust temperatures north of 3,000 K, while a calibrated load cell quietly tries to measure thrust to a fraction of a percent. The combinatorics are unforgiving: a chug-mode combustion instability, a hung start, a deadweight calibration eight months past expiration, or a fragment containment wall that wasn't sized for the worst-credible chamber breach can each turn a successful campaign into an incident report. This workspace gives a test engineer (or a range-safety reviewer reading the test card) a deterministic, **likelihood × severity matrix-driven** way to score every identified hazard and measurement-credibility threat:

- **Pre-fire test-readiness matrix** — every failure mode in the test card binned into the MIL-STD-882E 5×5 with named mitigation, ALARP justification, and explicit residual-risk acceptance lines.
- **Redline matrix** — runtime abort thresholds for chamber P, manifold P, pump speed, bearing temperatures, vibration, gimbal actuator load — each line carries its own likelihood × severity score so the redline density reflects the actual risk surface, not abort-button enthusiasm.
- **Thrust uncertainty budget** — the JCGM-100 "Guide to the Expression of Uncertainty in Measurement" pipeline for the load-cell chain: transducer linearity, amplifier noise, alignment tilt, thermal coefficient, tare drift. The output is a combined and expanded uncertainty mapped to the measurement objective (development burn vs. flight-qualification fire).
- **Anomaly-risk matrix** — post-test, any flagged anomaly (instability tone, leak, thermocouple dropout, slow valve actuation) is scored for *next-test* impact: PROCEED, PROCEED_WITH_MITIGATION, HOLD, or SCRUB.

The "using risk scoring matrices" technique is what shapes this workspace: instead of one omnibus "is this test safe?" command, every analytical command produces a *scored matrix cell* tied to a named failure mode, with a likelihood basis and a severity basis. The verdict is always **explainable and auditable** — you can read backwards from any GO/NO-GO to the cells that justified it.

## Why This Workspace Exists

Ground-test propulsion programs sit at the intersection of three risk universes that usually live in different binders: classical reliability engineering (MIL-STD-882E, FMEA, FMECA), metrology (JCGM 100, ASTM E74, NIST traceability), and range safety (AFSPCMAN 91-710, NFPA 55, KSC-DE-512). Each binder has its own scoring vocabulary, and an engineer trying to assemble a single test-readiness review usually ends up cutting and pasting between five different spreadsheets and three different rating scales.

This workspace codifies a single 5×5 matrix that all three universes feed into. Severity is MIL-STD-882E categories I–IV plus a measurement-objective category for metrology-only hazards; likelihood is the same A–E frequency banding across all sources. Every command produces matrix cells in this single grid, so a chug-mode hazard (development reliability), a 0.4% load-cell drift (metrology), and a 30 m fragmentation footprint (range safety) can be compared on the same axes without translation loss. That's the invariant. The workspace deliberately fits the entropy of the daily-build series: rocket engine ground-test vocabulary (hard-start, chug, hung start, autogenous pressurization, k=2 expanded uncertainty, AFSPCMAN tables) doesn't translate to any other domain, which is exactly the point.

## Getting Started

### Prerequisites

- A test card or test-readiness review (TRR) draft with engine specs, propellants, propellant inventories, expected chamber pressure, planned burn time, and personnel positions.
- Load-cell datasheet(s) and the most recent NIST-traceable calibration certificate per ASTM E74. Calibration date and stated uncertainty are mandatory; vendor model number alone is not enough.
- Test-stand mechanical specs: load-cell mount geometry (axial column or thrust-block), expected tare load, thermal environment, alignment tolerance, side-load cells if present.
- For redline work: data-acquisition channel list with sample rate, transducer ranges, and abort-actuation latency (valve-close time + controller cycle).
- Familiarity with MIL-STD-882E severity definitions (Catastrophic / Critical / Marginal / Negligible) and JCGM 100 uncertainty type-A vs. type-B distinction. References live in `context/concepts.md` for re-reading.

### Quick Start

1. Drop the test card, propellant safety data sheets, and load-cell cal cert into `outputs/inbox/<test-id>/`.
2. Run `/load-cell-calibration-check test-id=<id> cell=<serial>` to verify the calibration is current and traceable. If it fails, **stop here** — the rest of the matrix depends on credible thrust data.
3. Run `/thrust-uncertainty-budget test-id=<id>` to compute the combined and expanded uncertainty for the planned thrust readings. Compare the expanded uncertainty against the measurement objective tolerance in the test card.
4. Run `/test-readiness-risk test-id=<id>` to walk the test-card failure-mode list through the `T-*` tree and produce the 5×5 matrix.
5. Run `/redline-set test-id=<id>` to define and score abort thresholds; the redline table is part of the GO/NO-GO package.
6. Run `/range-safety-matrix test-id=<id> personnel-positions=<file>` to confirm fragmentation, overpressure, fire-spread, and plume hazards against established standoffs.
7. If a post-test anomaly appears, run `/anomaly-risk-score` instead of restarting at readiness — anomaly triage routes back into readiness only when the next-test posture demands it.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/test-readiness-risk` | Builds the pre-fire 5×5 LxS matrix across all identified failure modes. | First pass for every new test card; re-pass after any engine, plumbing, or propellant change. |
| `/redline-set` | Designs the runtime abort-threshold table with per-line LxS scoring. | After `/test-readiness-risk`; before the TRR; re-checked after any DAQ or controller change. |
| `/thrust-uncertainty-budget` | Propagates load-cell-chain uncertainties to combined / expanded values (JCGM 100). | Before any test where thrust will be reported; after any transducer swap or alignment adjustment. |
| `/load-cell-calibration-check` | Validates NIST-traceable calibration (ASTM E74) is current, in-tolerance, and within hysteresis spec. | Mandatory pre-fire; on any new cell; if a cell saw an overload event. |
| `/anomaly-risk-score` | Bins a post-test anomaly into PROCEED / PROCEED_WITH_MITIGATION / HOLD / SCRUB. | First response to any flagged anomaly; before the post-fire review meeting. |
| `/range-safety-matrix` | Scores proximity hazards against AFSPCMAN 91-710 / NFPA 55 standoffs. | Before the TRR; on any change to personnel positions, propellant inventory, or stand layout. |

## Directory Structure

```
rocket-engine-testing-thrust-measurement/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # Six bespoke commands for hot-fire risk scoring
├── context/
│   ├── concepts.md           # Thrust stands, load cells, MIL-STD-882E, propellant hazards
│   ├── workflows.md          # The T-, R-, U-, A-, S- decision trees
│   └── references.md         # Risk matrix tables, standards index, transducer specs
├── prompts/                  # Pre-fire readiness review, anomaly recovery plan, uncertainty buildup
└── outputs/                  # Risk matrices, redline tables, uncertainty budgets, anomaly walks
```

## Example Use Cases

### Pre-fire readiness review for a new LOX/methalox upper-stage engine

The test card calls for a 200-second burn at 60 bar chamber pressure with autogenous pressurization. Walk the engine through `/test-readiness-risk` — combustion instability (chug + screech), hard-start at sub-second ignition delay, cooling-jacket burn-through near the throat, hung start with valve-sequencing failure all land on the matrix. `/redline-set` produces chamber-P-rise-rate, manifold-ΔP, and bearing-temperature redlines. `/range-safety-matrix` confirms the 50 m blast standoff against propellant TNT-equivalent.

### Load-cell swap after an overload event

A side-load excursion during a gimbal sweep flexed the axial load cell beyond its 150% safe-overload limit. Run `/load-cell-calibration-check` against the post-event cal — span shift exceeds the 0.1% recheck threshold. The cell is pulled, replaced, and re-characterized; `/thrust-uncertainty-budget` is re-run with the new transducer specs, and the expanded uncertainty is compared back to the test-card objective before fire authorization.

### Anomaly post-fire — chug-mode tone observed at 230 Hz

The chamber-pressure FFT shows a 230 Hz tone at +4% of mean chamber pressure, marginal against the typical 5% chug threshold. `/anomaly-risk-score` walks `A-*` — severity II (mission degradation), likelihood B (chug is a known mode for this injector geometry) — score `2B` lands in the HIGH band. Disposition: HOLD pending injector pattern review and a low-pressure cold-flow re-check, with a re-fire only after `PROCEED_WITH_MITIGATION` is justified by injector data.

### Range-safety re-baseline after a propellant inventory upgrade

The propellant farm gets a 40% LOX volume increase. `/range-safety-matrix` re-runs the fragmentation, overpressure, fire-spread, and plume distance against new TNT-equivalent. The control room standoff that was acceptable at the prior inventory now scores `4C` SERIOUS — the matrix is the artifact the range-safety officer signs off on for the new operating envelope.

### Flight-qualification fire with 0.5% thrust uncertainty target

The customer specifies a flight-qual thrust value with ≤ 0.5% expanded uncertainty (k=2). `/thrust-uncertainty-budget` aggregates load cell (0.10%), amplifier noise (0.05%), alignment tilt budget (0.15%), thermal sensitivity (0.20%), and tare drift (0.10%) into a combined standard uncertainty; with k=2 the expanded value is ~0.6%. The result drives a mitigation plan — better thermal compensation or a tighter alignment spec — *before* the test, not after the data is reviewed.

## Recommended MCP Servers

- **filesystem MCP** — pull TDMS/CSV thrust traces and DAQ exports from `outputs/inbox/`; push risk matrices and uncertainty budgets back into `outputs/`.
- **python-exec MCP** (or any sandboxed numeric runner) — `/thrust-uncertainty-budget` benefits from a numeric propagation pass; per-input partial-derivative arithmetic done by hand in a markdown table is error-prone for complex chains.
- **pdf MCP / docx MCP** — calibration certificates and propellant SDS arrive as PDF; extraction into structured cal records helps `/load-cell-calibration-check` operate without manual transcription.

## Legal & Ethical Considerations

- **Advisory, not approval.** This workspace produces analyses and risk matrices; the formal Test Readiness Review (TRR), GO/NO-GO authority, and abort responsibility belong to the licensed test conductor and range-safety officer per the site's range operations manual. Outputs are decision support, not decisions.
- **Export control.** Liquid rocket engine designs, performance, and detailed test data are typically ITAR-controlled (USML Category IV) in the United States. Do not place ITAR-controlled data in this workspace if it is hosted on an uncontrolled platform; consult your export-control officer on segregation.
- **Personnel safety overrides program schedule.** If a hazard scores HIGH or SERIOUS and a documented mitigation is not in place, the matrix's correct output is NO-GO regardless of program-schedule pressure. The workspace exists to make schedule pressure visible against fixed safety thresholds, not to soften the thresholds.
- **Calibration claims must be traceable.** Reporting a thrust value without a valid NIST-traceable calibration is a measurement-integrity failure. Old, in-house "we re-zeroed it" tare adjustments are *not* a substitute for an ASTM E74 calibration.
- **Anomaly data is sensitive.** Combustion instability traces, hard-start postmortems, and incident logs contain information that has competitive, regulatory, and (for some programs) classified implications. Apply the site's data-handling rules before placing artifacts in shared storage.

## Technical References

- [MIL-STD-882E — System Safety](https://www.dau.edu/cop/armyesoh/DAU%20Sponsored%20Documents/MIL-STD-882E.pdf) — DoD canonical risk-matrix definitions (Severity I–IV, Probability A–F, residual-risk acceptance authorities).
- [JCGM 100:2008 — Guide to the Expression of Uncertainty in Measurement (GUM)](https://www.bipm.org/en/publications/guides) — type-A / type-B / combined / expanded uncertainty methodology.
- [ASTM E74 — Standard Practices for Calibration and Verification for Force-Measuring Instruments](https://www.astm.org/e0074-18.html) — primary force-cell calibration practice (paywalled).
- [AIAA G-145-2019 — Guide to the Assessment of Test Uncertainty for Aerospace Ground-Test Facilities](https://www.aiaa.org/publications/standards) — aerospace adaptation of GUM.
- [NFPA 55 — Compressed Gases and Cryogenic Fluids Code](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=55) — propellant storage and proximity standards.
- [AFMAN 91-710 — Range Safety User Requirements](https://www.faa.gov/space/additional_information/launch_safety) — flight & ground test range-safety baseline.
- [NASA-STD-5018 — Strength Design and Verification Criteria for Glass, Ceramics, and Windows in Human Space Flight](https://standards.nasa.gov) — NASA technical standards portal (broader NASA-STD-50xx propulsion suite linked from this hub).
- [NIST SP 250-39 — Force Calibration Service](https://www.nist.gov/calibrations) — NIST primary force-calibration program reference (top of the traceability chain).

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
