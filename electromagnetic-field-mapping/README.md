# Electromagnetic Field Mapping Workspace

> A decision-tree-driven Claude agent workspace for planning, executing, and interpreting EM field surveys — from substations to server rooms to TSCM sweeps.

## What This Workspace Does

Electromagnetic field mapping is the practice of measuring electric, magnetic, and electromagnetic field intensities across space and frequency, then turning those samples into a defensible picture: where the field is strong, what is emitting it, whether it exceeds an exposure or compatibility limit, and how confidently we know. The discipline spans three loosely related sub-fields — low-frequency power-frequency assessments (50/60 Hz E and H near power lines and transformers), broadband RF safety surveys (commercial transmitters, cellular sites, broadcast towers), and EMC/EMI investigations (a device that fails its emissions test or interferes with a neighbour) — that share probes, jargon, and pitfalls.

This workspace organises field-mapping work around **decision-tree triage workflows**. Every measurement is interpreted by walking down a structured tree: is the source intentional or unintentional, near-field or far-field, narrowband or broadband, continuous or pulsed, polarized or isotropic? Each branch routes to a specific measurement protocol (e.g. probe choice, RBW, dwell time, polarization sweep, averaging) and to a specific limit standard (ICNIRP 2020, IEEE C95.1-2019, FCC OET-65, IEC 62232, CISPR 32, IEC 61786). The agent gates each next action on what the previous reading actually showed, not on a fixed checklist.

The workspace is also fully self-contained: clone it, point it at your spectrum analyser or broadband field meter, and the bespoke `/survey-plan`, `/triage-source`, `/map-near-field`, `/check-exposure-compliance`, `/interpolate-isofield`, and `/isolate-emi-culprit` commands will carry the methodology end-to-end.

## Why This Workspace Exists

Field mapping fails in predictable ways: the wrong probe (E-field probe in a near-field magnetic zone), wrong detector (peak instead of RMS for an exposure assessment, average instead of quasi-peak for a CISPR compliance check), missing antenna factor, polarisation mismatch on a 5G band where the cross-pol component dominates, or a "we measured fine here" conclusion drawn from one spot reading when the lobe was 2 m to the left. The cost of these mistakes is anything from a re-test bill to a real exposure overrun. A formal decision tree closes the gap between the engineer's intuition and the methodology that the limit standard actually requires.

## Getting Started

### Prerequisites

- A broadband EMF meter (e.g. Narda NBM-550, Wandel & Goltermann EFA-300) **or** a calibrated spectrum analyser with isotropic / log-periodic / horn antennas
- Up-to-date probe calibration certificates (within 12 months for most occupational programs)
- For LF / power-frequency work: a 3-axis ELF magnetic probe (e.g. Narda ELT-400)
- A site plan or floor layout to register measurement points against
- Python 3.10+ with `numpy`, `scipy`, `matplotlib`, `pykrige` if you intend to use `/interpolate-isofield`
- For TSCM / counter-surveillance use: a written authorisation from the property owner and awareness of local intercept law

### Quick Start

1. Clone this workspace alongside your survey notes.
2. Run `/survey-plan` with the site description, frequency range of interest, and standard you must meet — it produces a measurement grid, a probe / detector / RBW table, and a budget of dwell time per point.
3. Capture readings into `outputs/raw/`. Stick to one row per measurement (timestamp, position, probe, frequency, magnitude, polarization, notes).
4. For anomalous readings invoke `/triage-source` — it walks the decision tree until the source is classified and located.
5. Once the grid is captured, run `/interpolate-isofield` to produce the spatial map, and `/check-exposure-compliance` to generate the compliance comparison against the chosen standard.
6. If the project is an EMC chase rather than a safety survey, replace step 5 with `/isolate-emi-culprit` to walk the bisection.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/survey-plan` | Builds a frequency-aware grid, probe table, and dwell budget. | Start of any survey. |
| `/triage-source` | Walks the decision tree on an unknown / anomalous reading. | Mid-survey, when a value surprises you. |
| `/map-near-field` | Executes a structured near-field scan over a device-under-test. | Bench EMC, PCB hot-spot work, antenna near-field. |
| `/check-exposure-compliance` | Compares measurements against ICNIRP / IEEE / FCC limits with the right averaging. | End of an occupational or general-public survey. |
| `/interpolate-isofield` | Builds isofield contours from spot data (kriging / IDW). | Once the grid is complete and you need a map artefact. |
| `/isolate-emi-culprit` | Bisects a multi-emitter environment to find the offending device. | EMC pre-compliance failure, neighbour interference. |

## Directory Structure

```
electromagnetic-field-mapping/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # /survey-plan, /triage-source, /map-near-field,
│                             # /check-exposure-compliance, /interpolate-isofield,
│                             # /isolate-emi-culprit
├── context/
│   ├── concepts.md           # NF/FF, probe types, exposure limits, EMC concepts
│   ├── workflows.md          # Decision-tree triage methodology and survey phases
│   └── references.md         # Standards table, ISM bands, probe catalogue, formulas
├── prompts/                  # Reusable templates: survey brief, compliance narrative, EMC postmortem
└── outputs/                  # Generated grids, isofield plots, compliance reports
```

## Example Use Cases

### Cellular rooftop RF safety survey
A property manager wants to lease rooftop space to a new mobile operator and needs a baseline RF safety survey against FCC OET-65 / ICNIRP general-public limits before workers are sent up. `/survey-plan` produces the 1 m grid and the 100 kHz – 6 GHz sweep schedule; `/check-exposure-compliance` produces the final exposure-quotient map.

### EMC pre-compliance pre-screen
A startup's IoT device is about to enter the CISPR 32 chamber and they want to find emissions hot-spots first. `/map-near-field` runs a 5 cm grid over the PCB with an H-field probe; `/isolate-emi-culprit` walks the swap-out tree across cables, switchers, and clock harmonics.

### Substation transformer ELF survey
An occupational hygienist must document worker exposure to 50 Hz magnetic field around a distribution transformer. The agent uses the LF branch: 3-axis ELF probe, IEEE C95.1 time-averaged limits, isofield contours plotted on a CAD overlay.

### TSCM RF sweep of a conference room
A corporate security team is sweeping a board-room before a sensitive meeting. The decision tree branches into "intentional emitter" mode: spectrum-analyser dwell-time scheduling, polarization sweeps, and proximity bisection via `/triage-source`.

### Hospital MRI fringe field
Map the 0.5 mT and 5 G isocontours around an MRI suite to validate signage placement under IEC 60601-2-33. ELF/static-field probe; `/interpolate-isofield` generates the floor-plan overlay.

## Recommended MCP Servers

- **Filesystem / Drive** — for ingesting site plans (PDF / DWG / PNG) and writing isofield map outputs.
- **Python execution** — to run interpolation and limit-checking calculations directly (the kriging step is far cheaper to delegate than to describe).
- **Spreadsheet (xlsx)** — for organising raw readings and the final compliance comparison table.

## Legal & Ethical Considerations

- **Authorization.** Only conduct field surveys on premises the user owns or has written authorization to assess. RF-safety surveys at telecoms sites typically require operator coordination.
- **Local RF intercept law.** Distinguishing TSCM/counter-surveillance work from unlawful interception varies by jurisdiction (US: 18 USC §2511; UK: IPA 2016; EU: ePrivacy Directive transpositions). Document scope and consent in writing.
- **Reporting obligations.** Where a survey reveals an exposure overrun for workers or the public, occupational safety reporting law (OSHA, UK HSE, equivalent) may require notification.
- **No medical advice.** Where survey subjects ask about health effects, route them to ICNIRP / WHO summaries; do not opine clinically.

## Technical References

- [ICNIRP RF Exposure Guidelines 2020](https://www.icnirp.org/en/publications/article/rf-guidelines-2020.html) — 100 kHz – 300 GHz general-public and occupational limits.
- [IEEE Std C95.1-2019](https://standards.ieee.org/ieee/C95.1/4940/) — IEEE safety levels for human exposure to RF EM fields, 0 Hz – 300 GHz.
- [FCC OET Bulletin 65](https://www.fcc.gov/general/oet-bulletins-line) — Evaluating compliance with FCC guidelines for human exposure.
- [IEC 62232](https://webstore.iec.ch/publication/63990) — Determination of RF field strength, power density and SAR in the vicinity of base stations.
- [IEC 61786-1 / -2](https://webstore.iec.ch/publication/22751) — Measurement of DC and low-frequency magnetic and electric fields.
- [CISPR 32](https://webstore.iec.ch/publication/28144) — Multimedia equipment EMC emission requirements.
- [NIST Tech Note 1297](https://www.nist.gov/pml/nist-technical-note-1297) — Guidelines for evaluating expressing uncertainty of NIST measurement results.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
