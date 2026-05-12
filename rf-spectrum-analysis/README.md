# RF Spectrum Analysis Workspace

> Treat the radio spectrum like a chronic patient: grade the symptoms, chart the vitals, escalate proportionately, follow up for life.

## What This Workspace Does

This workspace fuses three traditions that rarely talk to each other: **RF spectrum analysis** (the engineering practice of mapping what's on the air), **statistical process control** (the manufacturing practice of distinguishing common-cause from special-cause variation), and the **palliative-care assessment framework** (the medical practice of grading multidimensional symptoms and matching intervention intensity to symptom severity rather than to disease label).

The output is an agent that helps an RF analyst run a *spectrum care plan* rather than a one-off survey: establish a baseline, grade observed symptoms on a 0–10 multidimensional scale, build SPC control charts that distinguish "the noise floor is wobbling within natural variation" from "something material has changed", apply a proportionate intervention ladder (re-aim antenna → reassign channel → schedule a deeper investigation → escalate to facilities or compliance), and re-assess on a defined cadence.

The defining technique today is **quality-control statistical methods** — X-bar/R, EWMA and CUSUM charts, Western Electric run rules, and Cp/Cpk/Ppk capability indices. The defining cross-domain borrow is the palliative-care multidisciplinary review: a structured handoff format that lets RF analysts, security engineers, and facilities owners share a single severity-graded view of the spectrum instead of arguing past each other in escalation tickets.

## Why This Workspace Exists

Most spectrum surveys produce one waterfall PNG and a paragraph of prose. Six months later nobody knows whether the 433 MHz noise floor is up because something new is leaking or because it's just a noisy afternoon. SPC was invented for exactly this confusion — separate signal from noise so you only escalate when the data demands it. Palliative care contributed the second missing piece: a clinically rigorous severity rubric that gets a multidisciplinary team to agree on what to do next.

## Getting Started

### Prerequisites

- An SDR — HackRF One, RTL-SDR Blog v4, USRP B-series, or an Airspy / KrakenSDR. Vendor-class spectrum analysers (Tek RSA, R&S FSV, Keysight N9020) also work.
- A receive antenna appropriate to the band(s) of interest (discone, log-periodic, mag-mount whip, etc.).
- Python 3.11+ with `numpy`, `scipy`, `pandas`, `matplotlib`. Optional: `scikit-rf`, `gnuradio`, `hackrf_sweep` / `rtl_power` CLI binaries.
- A consistent measurement location and antenna placement — control charts are only valid under stable measurement conditions.
- Authorisation from the site/facility owner, and awareness of local regulator rules (FCC, Ofcom, BNetzA, ACMA).

### Quick Start

1. Clone this workspace into your project tree.
2. Park your SDR at a fixed measurement location and run `/spectrum-baseline-survey` for at least 24 hours (48–168 hours preferred for sites with diurnal/weekly cycles).
3. Run `/control-chart-build` on the resulting CSV to compute X-bar/R or EWMA limits for the bands you care about.
4. As issues arise, run `/symptom-assess` to grade them on the multi-axis rubric, then `/intervention-ladder` to decide what (if anything) to do.
5. Schedule a recurring `/longitudinal-track` (weekly or monthly) and a quarterly `/process-capability-report`. Use `/spectrum-mdt-handoff` whenever ownership needs to cross teams.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/spectrum-baseline-survey` | Sets the 24h+ baseline and computes SPC limits per channel/sub-band. | First contact with a site, or after a deliberate environmental change (new tenant, antenna move, building work). |
| `/symptom-assess` | Multi-axis severity grade (intensity / frequency / distress / trend) on a 0–10 scale. | When a new emitter, drift, or complaint is reported. |
| `/control-chart-build` | Builds X-bar/R, EWMA, or CUSUM and applies Western Electric run rules. | When you have ≥25 baseline subgroups and need to detect special-cause variation. |
| `/intervention-ladder` | Maps the severity grade to a proportionate intervention step. | After every `/symptom-assess`, before any field action. |
| `/longitudinal-track` | Refreshes the symptom trajectory and intervention markers. | Weekly or monthly. |
| `/process-capability-report` | Computes Cp / Cpk / Ppk against SLA or regulatory limits. | Quarterly, or before/after a major change. |
| `/spectrum-mdt-handoff` | Produces an MDT-style structured handoff. | When ownership crosses RF / SecOps / facilities boundaries. |

## Directory Structure

```
rf-spectrum-analysis/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # Bespoke domain commands
├── context/
│   ├── concepts.md           # SPC primitives, palliative→spectrum analogy, RF basics
│   ├── workflows.md          # Baseline → assess → chart → intervene → reassess loop
│   └── references.md         # Western Electric rules, ITU/FCC bands, ESAS rubric, tool refs
├── prompts/                  # Reusable prompt templates
└── outputs/                  # Generated baselines, charts, trajectories, MDT briefs
```

## Example Use Cases

### Hospital biomedical telemetry site survey
The ward reports intermittent ECG telemetry drops on the WMTS band. Baseline first; symptom-assess any candidates; build an EWMA chart on telemetry packet-loss rate; ladder-up only if the trend chart and severity grading agree.

### Multi-tenant office building noise floor
A new tenant moved in and the existing tenant is now seeing Wi-Fi retries climb. The workspace lets you separate "natural diurnal variation" (common cause) from "new emitter, intervene" (special cause) without a political fight.

### Industrial 900 MHz ISM congestion
A factory floor's 900 MHz mesh telemetry is occasionally losing nodes. Capability indices (Cpk) against the application's link-budget spec say whether the channel is *capable* of the SLA or whether the mesh needs to migrate.

### Pre-broadcast event sweep with longitudinal record
For recurring events at the same venue, the workspace builds a multi-year symptom trajectory so each sweep starts with prior knowledge instead of a blank sheet.

### Compliance posture before a regulatory audit
Process-capability + longitudinal trajectory + MDT handoff together make a defensible "we knew, we measured, we acted" record for an FCC/Ofcom enquiry.

## Recommended MCP Servers

- **Filesystem** — Read/write CSV captures, chart PNGs, and MDT briefs in `outputs/` without re-pasting.
- **Python (Jupyter or scratchpad)** — Run pandas/scipy/matplotlib to compute control limits and render charts directly.
- **GitHub** — Pull RF-baseline reference datasets or push the longitudinal record to a shared repo for audit.
- **A web/search MCP** — Cross-reference unknown frequencies against the [Sigidwiki](https://www.sigidwiki.com/) signal identification catalogue.

## Legal & Ethical Considerations

- **Receive-only by default.** Passive observation of the spectrum is generally lawful; intentional radiation is not. Do not transmit on licensed bands without the appropriate licence (FCC Part 5/15 experimental, Ofcom test licence, etc.).
- **Don't decode protected communications.** In most jurisdictions, listening to certain bands (cellular, public-safety encrypted, satellite uplinks) is restricted even if technically receivable. Consult the regulator before publishing decodes.
- **Site permission matters.** Get written authorisation from a building/facility owner before deploying a long-term receiver. Spectrum surveys are non-invasive but legal exposure exists if the activity is misread.
- **Document the chain of custody for measurements** that may feed into a regulatory complaint or insurance claim.

## Technical References

- [AIAG SPC Reference Manual (4th ed.)](https://www.aiag.org/store/publications/details?ProductCode=SPC-3) — the canonical industrial reference for control charts and capability indices.
- [ISO 22514-2 Process capability statistics](https://www.iso.org/standard/77727.html) — the international standard for Cp/Cpk reporting.
- [NIST/SEMATECH e-Handbook of Statistical Methods, Ch. 6 (Process Monitoring & Control)](https://www.itl.nist.gov/div898/handbook/pmc/pmc.htm) — free deep dive into SPC.
- [ITU Radio Regulations](https://www.itu.int/pub/R-REG-RR) — global allocation reference.
- [FCC Online Table of Frequency Allocations](https://www.fcc.gov/oet/spectrum/table) — US allocations.
- [Sigidwiki — Signal Identification Guide](https://www.sigidwiki.com/) — community catalogue of known emission types.
- [Edmonton Symptom Assessment System (ESAS-r)](https://www.albertahealthservices.ca/assets/info/peolc/if-peolc-ed-esas-r-administration-manual.pdf) — the 0–10 multidimensional symptom rubric this workspace's severity scale is modelled on.
- [WHO Analgesic Ladder](https://www.who.int/publications/i/item/9789241550390) — the proportionate-intervention pattern adapted in `/intervention-ladder`.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
