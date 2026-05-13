# Superconductor Characterization Workspace

> Run the cryogenic measurement lab like a constrained service system — qualify Tc, Jc, Hc2, and Rs on LTS and HTS samples while keeping liquid-helium burn, magnet hours, and queue length inside planned headroom.

## What This Workspace Does

This workspace equips an agent to operate a superconductor characterization facility end-to-end: transport (four-probe R(T), V(I), n-value), magnetic (SQUID/VSM M(T), M(H), AC χ′/χ″), microwave surface-resistance (cavity Q), and supporting calorimetry — across LTS materials (NbTi, Nb3Sn), HTS coated and BSCCO conductors (REBCO, Bi-2212, Bi-2223), MgB2, and emerging unconventional candidates. Every measurement is anchored to the relevant IEC 61788 part so results are inter-laboratory comparable.

The twist for this build is **capacity planning**. A characterization lab is a small queueing network: samples queue for a cryostat, cryostats queue for a magnet's ramp window, magnets queue for the helium that survived the recovery plant. Today's technique applies operations-research models — Little's Law, M/G/1 utilisation, batch-service throughput, and Holt-Winters demand forecasting — to size the queue, forecast LHe burn, set ramp-window policy, and reserve safety headroom against quenches. The result is a measurement plan a lead can defend against both physics constraints (don't rush a field ramp) and operations constraints (don't run dry by Friday).

## Why This Workspace Exists

Characterization throughput is the bottleneck for almost every applied-superconductor programme: tokamak conductor qualification (ITER/SPARC), MRI magnet vendor acceptance, accelerator-cavity Rs screening, HTS-power-cable Jc binning, and university PhD pipelines all share the same scarce resources. Most labs run those resources informally — "we'll fit it in next week" — and pay for it in helium emergencies, missed deadlines, and quench-driven schedule resets. This workspace codifies the lab as a measurable, plannable service: cryogen as inventory, magnet hours as a server, samples as jobs, ramp policy as queue discipline. The benefit is twofold: a forecast you can show a sponsor, and a queue that survives a quench without a blame-storm.

## Getting Started

### Prerequisites

- A cryogenic measurement platform — at minimum a He-bath or closed-cycle cryostat (4 K-class), or a dilution insert for sub-1 K work
- A superconducting magnet or normal-conducting electromagnet appropriate to the target Hc2 / Jc range (commonly 9 T, 14 T, or 16 T solenoids; split-pair for angle-resolved work)
- Standard transport and magnetic instruments: nanovoltmeter (Keithley 2182A / NPLC ≥5), current source (6221, 2400), lock-in amplifier (SR830/860), VSM or SQUID magnetometer (MPMS3 / PPMS DynaCool), optional microwave VNA (R&S ZNA / Keysight PNA) for cavity Q
- LHe / LN2 supply with metered draws, recovery line, and a cryogen inventory log
- Python 3.10+ with NumPy / SciPy / pandas for capacity-planning calculations; optional `simpy` for queue simulation
- Calibrated thermometry traceable to ITS-90 (Cernox + CCS, RhFe, or RuO2)

### Quick Start

1. Clone this workspace into your lab notebook tree (`outputs/` is where measurement summaries and capacity reports will land).
2. Run `/lhe-budget` first — feed it the next two weeks of planned measurements; it returns burn-rate, time-to-empty, and required recovery throughput.
3. Run `/sample-queue-plan` against the same horizon to size the cryostat queue and lead-time (Little's Law) with explicit utilisation ρ.
4. For each priority sample, invoke `/tc-sweep-protocol` (or `/jc-anisotropy-map`, `/microwave-q-screen` depending on the question) to generate the measurement procedure and per-sample capacity cost.
5. Hold a weekly review using `prompts/weekly-throughput-review.md` to compare planned vs. actual; adjust headroom and ramp policy before the next intake.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/lhe-budget` | Forecast LHe burn against tank inventory; recommend a recovery throughput target and procurement trigger. | Start of any planning horizon, after a quench, or when intake adds a high-field run. |
| `/sample-queue-plan` | Size the queue with Little's Law + M/G/1; flag samples that push ρ over 0.85. | When intake changes, when a cryostat goes down, when a deadline appears. |
| `/magnet-ramp-schedule` | Lay out magnet windows including training, persistent-mode dwell, controlled ramp-down, and quench-recovery slack. | Before any week with multiple high-field measurements or a fresh magnet. |
| `/tc-sweep-protocol` | Write the four-probe Tc-sweep procedure with measurement uncertainty and capacity cost. | New sample, screening pass, or anytime Tc is the primary disposition criterion. |
| `/jc-anisotropy-map` | Plan Jc(θ, B, T) mapping across H‖c and H‖ab including step density and queue impact. | HTS coated-conductor binning, tape qualification, or anisotropy R&D. |
| `/microwave-q-screen` | Screen surface resistance Rs via cavity Q at cryogenic T; check mode purity and coupling. | Accelerator-cavity material screening, RF-loss studies, niobium qualification. |

## Directory Structure

```
superconductor-characterization/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # Bespoke domain commands
├── context/
│   ├── concepts.md           # Superconductivity + capacity-planning primitives
│   ├── workflows.md          # Sample pipeline, capacity loop, Tc/Jc/Hc decision tree
│   └── references.md         # Material tables, IEC 61788 index, M/G/1 formulas, facilities
├── prompts/                  # Sample intake, weekly throughput review, incident debrief
└── outputs/                  # Measurement summaries, capacity reports, IEC test reports
```

## Example Use Cases

### Conductor qualification campaign for a fusion magnet vendor
A vendor delivers thirty REBCO short samples that need Ic(B, T, θ) binning under a deadline. Use `/sample-queue-plan` to size the queue, `/magnet-ramp-schedule` to allocate the 14 T solenoid windows, and `/jc-anisotropy-map` per sample. The capacity report tells the vendor whether the deadline is real or aspirational *before* the first sample is mounted.

### Accelerator cavity material screening
Three coupons of high-purity Nb (RRR 300+) need Rs(T) screening at 1.3 GHz before bulk-cavity fabrication. Use `/microwave-q-screen` to plan the cavity test sequence; `/lhe-budget` confirms the 1.8 K superfluid runs fit the helium plan; results are reported per IEC 61788-19 conventions.

### PhD timeline rescue after a quench
A 9 T magnet quenched on Monday and lost three samples' worth of measurement time. Re-run `/lhe-budget` (helium loss plus warm-up), `/magnet-ramp-schedule` (training pulses + reduced-rate ramps for a week), and `/sample-queue-plan` (with the down-week excluded) to produce a defensible revised timeline for the thesis committee.

## Recommended MCP Servers

- **Filesystem MCP** — to ingest CSV/HDF5 measurement files from the cryostat PC and write structured reports into `outputs/`.
- **Sequential-thinking / Code-execution MCP** — for running NumPy/SciPy capacity-model calculations (Little's Law, M/G/1, Erlang-C, Holt-Winters) reproducibly alongside text reasoning.
- **Time / Calendar MCP** — to materialise the ramp schedule onto a real calendar with quench-recovery windows.

## Legal & Ethical Considerations

- **High magnetic-field safety.** Field exposure above 0.5 mT can interfere with implanted medical devices; the 5-gauss line must be marked. Verify all personnel screening before allowing a ramp.
- **Cryogenic asphyxiation hazard.** LHe and LN2 displace oxygen. Confirm room O2 monitoring and ventilation interlocks before initiating a transfer.
- **Magnet quench energy.** A persistent-mode magnet stores tens of MJ. Quench-protection circuits and dump-resistor sizing are safety-critical, not optional.
- **Export-controlled materials and cryocoolers.** Some Nb3Sn and REBCO conductors, dilution refrigerators, and high-field magnets are dual-use items subject to ECCN review. Verify export compliance before sample exchange across borders.
- **Data provenance.** Every reported Jc, Hc2, or Rs must be traceable to instrument-level metadata. Honour IEC 61788 reporting requirements rather than headlining a single best-day number.

## Technical References

- [IEC 61788 series](https://webstore.iec.ch/) — Superconductivity measurement standards (Jc on Nb–Ti, Nb3Sn, Ag-sheathed Bi-based and RE-Ba-Cu-O; Tc, n-value, hysteresis loss, surface resistance, mechanical and electrical characterisation).
- [NHMFL — National High Magnetic Field Laboratory](https://nationalmaglab.org/) — Reference facility for high-field characterization (DC ≥ 45 T, pulsed > 100 T).
- [Superconductivity News Forum (SNF)](https://snf.ieeecsc.org/) — Curated standards, tutorials, and the "Wires & Tapes" benchmark archive for HTS conductors.
- [Tinkham, *Introduction to Superconductivity* (2nd ed.)](https://store.doverpublications.com/) — Canonical reference for Type-II superconductivity, Hc2, λ, ξ, and surface-impedance theory.
- [Kleinrock, *Queueing Systems* Vol. I](https://www.lk.cs.ucla.edu/) — Foundational reference for M/M/1, M/G/1, and capacity utilisation models used in `/sample-queue-plan`.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
