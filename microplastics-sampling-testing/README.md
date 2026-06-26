# Microplastics Sampling & Testing

> A Claude Agent workspace for running an environmental microplastics monitoring program like a layered border-screening operation — risk-targeted sampling, primary→secondary analytical screening, legal-grade chain of custody, and predictive maintenance that keeps the detection network honest.

Microplastics monitoring has a dirty secret: the hardest part isn't finding plastic, it's proving the plastic you found wasn't shed by your own coat, sieve, or air handler. This workspace treats the whole program as a **screening operation under contamination pressure**. It imports three ideas that frontier inspection agencies have spent decades refining — *risk-based targeting*, *layered primary/secondary inspection*, and *unbroken custody of evidence* — and applies them to particle counts and infrared spectra. A **predictive-maintenance** layer keeps every "checkpoint" (each sampler and each spectrometer) in calibration so the screen never quietly goes blind.

## Who this is for

- Environmental monitoring labs running routine surface-water, sediment, biota, or atmospheric-deposition microplastics surveillance.
- Researchers who need defensible, blank-corrected concentrations with documented method provenance.
- Utility / wastewater / drinking-water programs screening influent and effluent.
- Anyone doing source-attribution work where a number may end up in a regulatory filing or litigation and therefore needs an intact chain of custody.

## Why the border-screening framing

| Border-inspection idea | Microplastics analogue |
|---|---|
| Intelligence-led, risk-based targeting | Prioritize sites near outfalls, urban runoff, river mouths, aquaculture, gyres — sample where the load is, don't sample uniformly with finite capacity |
| Primary inspection (fast, high-throughput) | Rapid screen: visual sort + Nile Red fluorescence; counts candidate particles cheaply |
| Secondary inspection (definitive, slow) | µ-FTIR / Raman polymer confirmation only on referred particles |
| Watchlist / signature match | Polymer & additive watchlist — tire-wear particles, banned microbeads, signature copolymers |
| Anomaly escalation | Count/composition deviating from a site baseline raises an alert |
| Sensor fusion | Combine staining + vibrational spectroscopy + Py-GC/MS to cut false positives and negatives |
| Sealed evidence & custody transfer | Tamper-evident sample sealing and a signed custody log from collection to archive |

The fusion is not cosmetic: it changes *where* you sample, *what* you confirm, and *what you can defend*.

## Getting started

**Prerequisites**

- Field sampling capability matched to your matrix — neuston/manta net (333 µm standard), bulk water grab + filtration cascade, Niskin/Van Dorn bottles, sediment grab/core, or active air pump + filter.
- Wet-lab capability for density separation (NaCl / ZnCl₂ / NaI / sodium polytungstate) and organic-matter digestion (H₂O₂ WPO, Fenton's, or KOH for biota).
- At least one confirmatory instrument: ATR-FTIR or µ-FTIR (FPA imaging), Raman microspectroscopy, or Py-GC/MS. Nile Red staining + epifluorescence is sufficient for the primary screen only.
- A contamination-controlled work area: glass/metal labware, cotton lab coats, laminar-flow or filtered-air enclosure, no synthetic clothing at the bench.

**Quick start**

1. `/risk-target-sites` — rank your candidate sites and pick this quarter's network.
2. `/sampler-deployment-plan` — lay out stations, replicates, depths, and field blanks.
3. For each collected sample: `/custody-log` at the point of collection.
4. After processing: `/blank-audit` first, then `/screen-sample`, then `/polymer-id` on referrals.
5. `/concentration-report` to produce the blank-corrected, recovery-corrected result.
6. Run `/instrument-maintenance-forecast` on a standing schedule so nothing in the network is overdue.

## Command reference

| Command | What it does |
|---|---|
| `/risk-target-sites` | Scores and ranks candidate sampling sites by a weighted contamination-risk model; outputs a targeting list and rationale |
| `/sampler-deployment-plan` | Builds a campaign plan: station layout, replicate count, depth strata, mesh/pore selection, field-blank placement, throughput estimate |
| `/custody-log` | Creates or appends a chain-of-custody record (seal IDs, transfers, signatures, storage conditions) |
| `/screen-sample` | Executes the two-tier screen: primary count via staining/visual, referral rules to secondary spectroscopy |
| `/polymer-id` | Matches a spectrum to a reference library, applies the hit-quality threshold, and adjudicates borderline hits |
| `/blank-audit` | Tallies procedural / field / air blanks, computes the contamination limit of detection, and gates the batch |
| `/qa-recovery-spike` | Computes percent recovery from a reference-particle spike and flags extraction loss by size/polymer |
| `/contamination-anomaly` | Compares a result against the site baseline + watchlist and escalates anomalies with a severity tier |
| `/concentration-report` | Produces the final concentration (particles/L, particles/kg dw, mass) with breakdowns, blank correction, and uncertainty |
| `/instrument-maintenance-forecast` | Tracks usage/condition of samplers and instruments and forecasts the next required service |

## Directory structure

```
microplastics-sampling-testing/
├── CLAUDE.md                 # Agent role, doctrine, command index
├── README.md                 # This file
├── .claude/commands/         # 10 bespoke domain commands
├── context/
│   ├── concepts.md           # Fundamentals + framework mapping + failure modes
│   ├── workflows.md          # Layered screening pipeline, targeting, maintenance loop
│   └── references.md         # Densities, spectral bands, media, standards, intervals
├── prompts/                  # Reusable prompt templates
└── outputs/                  # Baselines, custody logs, reports, instrument logs
```

## Example use cases

1. **Quarterly estuary survey.** Risk-target six of twelve candidate stations, deploy a manta-net campaign with paired field blanks, screen and confirm polymers, and produce a blank-corrected particles/m³ report with a tire-wear-particle watchlist flag.
2. **Drinking-water treatment audit.** Compare microplastic load across influent/effluent of a treatment train, with recovery spikes validating the small-particle (<20 µm) extraction.
3. **Spill source attribution.** Maintain a litigation-grade custody chain on sediment cores while matching a distinctive copolymer signature to a suspected industrial source.
4. **Instrument-uptime defense.** A reviewer asks whether a six-month dataset is comparable; `/instrument-maintenance-forecast` history shows the FTIR stayed within calibration verification limits the whole period.
5. **False-positive incident.** A batch shows an anomalous polyester-fiber spike; `/blank-audit` traces it to a degraded HEPA cartridge, the batch is quarantined, and a maintenance order is raised.

## Recommended tools / MCP servers

- A **filesystem** MCP server for persisting baselines, custody logs, and instrument histories under `outputs/`.
- A **spectral-library** lookup (local reference set of FTIR/Raman polymer spectra) for `/polymer-id`; commercial libraries (e.g., the open siMPle / Open Specy databases) are good public references.
- **Time-series / metrics** tooling for instrument condition monitoring and control charts.

## Legal & ethical notes

- Chain of custody here is about **scientific and legal defensibility**, not surveillance of people. The "border-screening" framing is a methodology metaphor — risk-based targeting, layered inspection, and evidence custody — applied to particles and spectra.
- Report inconclusive batches as inconclusive. Over-reporting microplastics (contamination false positives) and under-reporting (recovery loss, primary-screen false negatives) both mislead policy.
- Respect site-access permissions and sampling permits; some waters, protected areas, and discharge points require authorization.

## Technical references

- NOAA Laboratory Methods for the analysis of microplastics in the marine environment (Masura et al., 2015, NOS-OR&R-48).
- GESAMP (2019), *Guidelines for the monitoring and assessment of plastic litter in the ocean*, Reports & Studies No. 99.
- ISO 24187:2023 — Principles for the analysis of microplastics present in the environment.
- ASTM D8332 / D8333 — sampling and sample preparation for microplastics in waters.
- Open Specy / siMPle — open spectral libraries and matching tools for polymer identification.
- See `context/references.md` for densities, characteristic bands, and the full standards list.
