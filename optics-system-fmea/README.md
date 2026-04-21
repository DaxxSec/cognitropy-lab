# optics-system-fmea

> A Claude Agent Workspace for **designing and de-risking optical systems using Failure Mode and Effects Analysis (FMEA).**
>
> Part of the [Cognitropy Lab](https://github.com/DaxxSec/cognitropy-lab) — Day 27, Physical Sciences.

## What This Workspace Is

This workspace turns Claude into a specialist collaborator for optical engineers, physics grads, and imaging-system builders who need to go from a requirements blurb to a layout + tolerance budget + **structured FMEA** with RPN (Risk Priority Number) scoring.

It pairs first-principles optics (ray + wave, Gaussian beams, Fourier optics, radiometry) with the reliability-engineering rigor of FMEA so that every design candidate is accompanied by **at least three candidate failure modes**, root causes, detection methods, and mitigations before the user spends a dollar on glass or a hour in Zemax/OpticStudio.

## Why FMEA-First Optics?

Most optical failures in the field are not optical — they're **mechanical, thermal, contamination, assembly, or documentation** failures that manifest as optical degradation. A conventional "design then sanity-check" flow buries these modes. An FMEA-first flow surfaces them while parameters are still soft, which is where 80% of lifecycle cost gets locked in.

Standards this workspace leans on:
- **ISO 10110** — Optical elements and systems: preparation of drawings
- **MIL-STD-1472H** — Human-engineering design criteria
- **IEC 60825** — Laser product safety
- **SAE J1739 / AIAG-VDA FMEA Handbook** — FMEA methodology
- **ISO 9022** — Environmental test methods for optics

## Getting Started

1. Clone the workspace into your projects directory:
   ```bash
   git clone https://github.com/DaxxSec/cognitropy-lab.git
   cd cognitropy-lab/optics-system-fmea
   claude
   ```
2. On first session, run `/onboard`. Claude will interview you about:
   - System type (imaging, illumination, spectrometer, laser, fiber, free-space link, metrology, etc.)
   - Waveband, FOV, f/#, etendue, detector or source
   - Environment (thermal range, vibration, shock, vacuum, humidity)
   - Budget, schedule, regulatory posture
3. After onboarding, invoke any domain command below.

## Command Reference

| Command | Purpose |
|---|---|
| `/onboard` | Interview the user and populate `context/project.md`, `role.md`, `constraints.md`, `for-agent/environment.md` |
| `/design-optical-system` | First-pass paraxial + real-ray layout with parameter sweep table |
| `/run-fmea` | Structured Design FMEA pass with Severity × Occurrence × Detection = RPN scoring |
| `/tolerance-analysis` | Monte Carlo tolerancing and sensitivity ranking, outputs CSV + report |
| `/stray-light-audit` | Ghost, scatter, and baffle analysis with APART/FRED-style checklist |
| `/thermal-vibration-review` | Athermalization and modal failure checks — bond-line, barrel CTE, mount stiffness |

## Directory Layout

```
optics-system-fmea/
├── CLAUDE.md                   # Lightweight agent brief (loaded every prompt)
├── README.md                   # This file
├── CREATION_REPORT.md          # Why this workspace, technique used, rationale
├── context/
│   ├── project.md              # Populated by /onboard
│   ├── role.md                 # Populated by /onboard
│   ├── constraints.md          # Populated by /onboard
│   └── for-agent/
│       ├── domain-knowledge.md # Optics + FMEA theory (read on demand)
│       ├── workflows.md        # Step-by-step procedures
│       ├── environment.md      # User's tooling
│       └── tools.md            # Libraries and solvers
├── .claude/commands/           # Slash commands (6 total)
├── prompts/                    # Reusable prompt templates (4)
├── planning/                   # plan.md — active plan + pivots/
├── resources/                  # Checklists, standards refs, RPN worksheets
├── user-docs/                  # Polished deliverables for the user
├── work-log/                   # Dated session logs
└── outputs/                    # Generated artifacts (Zemax .ZMX, CSV, PDFs)
```

## Example Use Cases

### 1. Miniature LWIR imager for a UAV payload
Claude drives you from "detect a human at 500 m in a 30° FOV with a 17 µm pitch µbolometer" to a candidate f/1.0 Germanium doublet, a thermal-vibration FMEA flagging bond-line stress at −40 °C, and a baffle recommendation to kill the 10.6 µm ghost off the window.

### 2. Raman spectrometer for field chemistry ID
Claude sets up a 785 nm laser, notch filter, and f/2.0 transmissive spectrograph; FMEA surfaces fluorescence-swamping from sample variability, detector ADC-bit starvation at low signal, and misalignment of the input fiber as top-3 RPN items.

### 3. Fiber-coupled pump laser diode for medical use
IEC 60825 hazard classification, thermal runaway failure mode, connector-end-face contamination analysis, and a patient-safety FMEA with interlocks mapped to each Severity-10 entry.

## Recommended MCP Servers

- **Filesystem MCP** — Read/write Zemax `.ZMX`, Code V `.len`, CSV tolerance tables
- **GitHub MCP** — Version the workspace and pull standards PDFs you've committed
- **Python execution MCP** — Run POPPY, prysm, rayopt, or opticspy scripts for quick sanity checks

## Python Libraries Worth Installing

```
pip install prysm rayopt opticspy poppy numpy scipy matplotlib pandas
```

| Library | Use |
|---|---|
| `prysm` | Wavefront propagation, MTF, PSF, Zernike tools |
| `rayopt` | Paraxial + real-ray tracing, optimization |
| `poppy` | Physical optics propagation (astronomy heritage) |
| `opticspy` | Interferogram analysis, aberration fits |

## Ethical & Safety Considerations

- **Laser safety (IEC 60825)** — Any workspace session involving Class 3B or Class 4 lasers must generate a hazard analysis and enclose interlock recommendations. Claude will refuse to optimize a retinal-hazard design without an explicit safety paragraph in `context/constraints.md`.
- **Export control (ITAR/EAR)** — Imaging below 400 nm, above 1.1 µm (thermal), or MWIR/LWIR systems may be export-controlled. Claude flags this but you are responsible for compliance.
- **Human factors** — Any HMI or eyepiece design will reference MIL-STD-1472 accommodation limits.

## FMEA Scoring Convention

| Scale | Severity (S) | Occurrence (O) | Detection (D) |
|---|---|---|---|
| 10 | Catastrophic / safety | Near-certain | Undetectable |
| 7–9 | Major performance loss | Frequent | Hard to detect |
| 4–6 | Noticeable | Occasional | Detectable with effort |
| 1–3 | Minor / cosmetic | Rare | Easily detected |

**RPN = S × O × D** (max 1000). Any RPN ≥ 100 is actioned. Any Severity = 10 is actioned regardless of RPN (per AIAG-VDA handbook guidance).

## Contribution & Feedback

This is a Cognitropy Lab workspace — built autonomously by a Claude agent on 2026-04-21. Issues, PRs, and suggestions welcome at the root repo.

## License

MIT. Use it, fork it, break it, improve it.
