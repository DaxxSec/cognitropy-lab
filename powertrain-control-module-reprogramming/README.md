# Powertrain Control Module Reprogramming Workspace

> Reprogram PCMs the way a conservator handles a specimen — archive the original before you touch it, fit the calibration to the vehicle's exact form, and map every variant to the geography it was built for.

## What This Workspace Does

Flashing a powertrain control module (PCM / ECM / engine ECU) is a high-stakes, mostly-irreversible-if-you're-careless operation: a single interrupted write can **brick** a module, and the factory calibration that came on it is frequently the *only copy that will ever exist* for that specific vehicle. This workspace reframes reprogramming as a **conservation discipline**, borrowing the working method of a taxidermist preserving an irreplaceable specimen: you **read and archive the stock image first** (the "study skin"), you **fit the calibration to the exact mechanical form** of the vehicle, you keep a **reference collection** of known-good calibrations, you document **provenance**, and you can **restore a damaged module** from your archive.

The organising technique here is **geographic / spatial analysis**. A calibration is not a universal artifact — it is a *regional* one. The same engine gets materially different fueling, spark, EGR, and OBD-monitor calibrations depending on its **emissions regime** (EPA Tier 3 vs CARB LEV III vs Euro 6/7 vs China 6), its **fuel grade** (87 AKI vs 95 RON vs E85-capable), its **altitude band** (sea-level vs high-altitude barometric compensation), and its **climate** (cold-start enrichment, thermal management). This workspace ships commands that map cal variants to markets and elevations, so the calibration you mount is the one that belongs to the vehicle's actual operating geography — not just any cal that happens to flash without an error.

It is intended for **legitimate** reprogramming only: factory recalibration and TSB reflashes, programming a replacement module, restoring a bricked unit, diagnostics, and off-road / motorsport / closed-course / bench-research work. It is **not** a tool for producing emissions-defeat calibrations on road vehicles — a hard legality gate enforces that.

## Why This Workspace Exists

The expensive lesson every calibration shop eventually learns is the same one a museum learns: **you cannot un-destroy an original.** Techs brick modules by flashing with a low battery, mount a calibration meant for a different hardware revision and chase a phantom lean code for a week, or grab a "stage 1" file from a forum that turns out to be a European-market cal that fails U.S. OBD readiness monitors. Each of those is a *preservation failure* — the original specimen wasn't archived, the form wasn't verified, or the geography wasn't mapped. This workspace codifies the conservator's discipline (archive-first, fit-the-form, keep-a-reference-collection, document-provenance, restore-when-damaged) into reusable commands so a single engineer — or an agent — works methodically instead of hopefully.

## Getting Started

### Prerequisites

- A **J2534-2 pass-thru interface** (e.g. a compliant VCI) or the OEM-specified reprogramming tool, plus the OEM reprogramming software / NASTF-licensed access where required.
- A **stable power supply / battery maintainer** (13.0–13.5 V, sufficient amperage) — under-voltage during a flash is the #1 cause of bricked modules.
- A binary/hex editor or calibration tool capable of reading the module, and (ideally) a **definition / XDF / damos** for the target so tables are human-readable.
- A way to compute checksums / CVN for the platform (tool-integrated or scripted).
- The vehicle's **VIN** and access to the module's **CAL-ID and CVN** (OBD-II Mode 09, PIDs 04/06).

### Quick Start

1. Clone this workspace next to your calibration project.
2. Run `/specimen-intake` **first, every time** — read the stock module, hash it, and archive it to `outputs/specimens/` before anything else.
3. Run `/provenance-trace` to decode the VIN/CAL-ID and establish where this calibration came from and what market it's for.
4. Run `/region-cal-map` and `/altitude-compensation` to confirm (or select) the calibration variant that fits the vehicle's operating geography.
5. Run `/calibration-mount` to verify hardware-form fitment, `/emissions-legality-gate` to clear legality, `/checksum-seal` to finalise, then `/flash-session` to write — with `/module-restoration` standing by if anything goes wrong.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/specimen-intake` | Read + hash + archive the factory image before any edit | **Always first** — before touching any module |
| `/provenance-trace` | Decode VIN/CAL-ID/CVN; reconstruct origin, market, reflash history | When you receive a module or a calibration file of unknown lineage |
| `/reference-collection` | Build/query the known-good cal library by model/year/market | Selecting a baseline, or filing a verified stock cal for reuse |
| `/calibration-mount` | Verify a cal fits the vehicle's exact hardware form | Before flashing any cal onto a specific vehicle |
| `/region-cal-map` | Map cal variants to market/region by emissions regime, fuel, climate | Choosing the correct regional calibration; gray-market imports |
| `/altitude-compensation` | Verify/adjust BARO compensation across an elevation band | High-altitude vehicles, fleets spanning big elevation ranges |
| `/checksum-seal` | Recompute/correct checksums + CVN so the flash is accepted | After any cal edit, before writing |
| `/emissions-legality-gate` | Block emissions-critical edits; check jurisdictional legality | Mandatory gate before every flash |
| `/flash-session` | Controlled J2534 flash with rollback plan + verification | The actual write event |
| `/module-restoration` | Recover a bricked/corrupt module from the archive | After a failed/interrupted flash, or a no-comms module |

## Directory Structure

```
powertrain-control-module-reprogramming/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # Bespoke PCM-conservation commands
├── context/
│   ├── concepts.md           # Module/cal anatomy, identifiers, protocols, conservation taxonomy, spatial dimension
│   ├── workflows.md          # The conservation lifecycle + spatial cal-selection decision trees
│   └── references.md         # Protocol table, identifier glossary, emissions-regime map, altitude bands, tooling
├── prompts/                  # Reusable prompt templates
└── outputs/                  # Specimens (stock reads), modified cals, diffs, flash logs, region maps
```

## Example Use Cases

### Programming a replacement PCM into a fleet truck
A failed module is swapped. `/specimen-intake` archives whatever was readable from the old/new unit, `/provenance-trace` confirms the donor's market, `/region-cal-map` selects the correct U.S. emissions calibration, `/calibration-mount` confirms the hardware part number matches, and `/flash-session` programs VIN + correct cal — with the original preserved in case the swap must be reversed.

### Restoring a module bricked by a low-battery flash
A write was interrupted at 11.4 V and the module no longer responds. `/module-restoration` walks bootloader/boot-mode recovery and restores the exact archived specimen captured by an earlier `/specimen-intake` — proving why archive-first is non-negotiable.

### Selecting the right calibration for a high-altitude vehicle
A truck operating between 1,500 m and 3,500 m has drivability and readiness issues on a sea-level cal. `/altitude-compensation` maps the BARO compensation tables against the elevation band and flags where enrichment/spark/boost need the high-altitude variant.

### Triaging a gray-market import that fails OBD readiness
A Euro-market ECU won't complete U.S. readiness monitors. `/region-cal-map` and `/emissions-legality-gate` identify the regime mismatch and the legal path (correct U.S. cal vs. non-compliance), rather than papering over the codes.

## Recommended MCP Servers

- **Filesystem MCP** — read/write module binaries, definitions, checksums, and the specimen archive directly from the project directory.
- **GitHub MCP** — version the reference collection and cal definitions; correlate a flash event with the definition/commit it used.
- **SQLite / database MCP** — index the known-good calibration library (VIN ↔ CAL-ID ↔ market ↔ hash) for fast `/reference-collection` queries.
- **A mapping / geospatial MCP (or a GIS data source)** — overlay fleet locations, elevation, and emissions-jurisdiction boundaries for `/region-cal-map` and `/altitude-compensation`.

## Legal & Ethical Considerations

- **Emissions tampering is illegal on road vehicles.** In the U.S., the Clean Air Act §203(a)(3) prohibits tampering with emissions controls and the manufacture/sale of defeat devices; CARB enforces in California; the EU (Reg. 715/2007 + UNECE), UK, and others have equivalents. This workspace's `/emissions-legality-gate` blocks edits to emissions-critical tables and monitors for on-road use. Disabling EGR, DPF/SCR, catalytic-converter monitoring, or readiness reporting on a road vehicle is out of scope.
- **Legitimate lanes only:** OEM/TSB recalibration, programming a replacement module, restoring a bricked unit, diagnostics, and dedicated **off-road / motorsport / closed-course / bench-research** vehicles. Document the use case.
- **Safety-critical calibrations.** Torque management, transmission shift, throttle, and thermal protection tables affect vehicle safety and durability — changes here demand the same archive-first, fit-the-form discipline as any other.
- **Warranty & disclosure.** Reflashes can affect warranty (Magnuson-Moss in the U.S. governs how) and must be disclosed to a vehicle's owner/next buyer. Keep honest provenance.
- **Security access is not theft of access.** Use NASTF Secure Data Release, OEM subscriptions, and licensed tooling — not stolen seed-key algorithms or bypassed security gateways.

## Technical References

- [SAE J2534-1/-2 — Pass-Thru Vehicle Programming](https://www.sae.org/standards/content/j2534/1_201712/) — the reprogramming interface standard mandated for emissions-related ECUs.
- [ISO 14229 (UDS) — Unified Diagnostic Services](https://www.iso.org/standard/72439.html) — the diagnostic/programming service layer (incl. security access, request download, transfer data).
- [ISO 15765-2/-4 — Diagnostics over CAN (DoCAN)](https://www.iso.org/standard/66574.html) — OBD-II transport on CAN.
- [SAE J1979 / ISO 15031-5 — OBD-II diagnostic services](https://www.sae.org/standards/content/j1979_201702/) — Mode 09 CAL-ID/CVN, Mode 01 readiness monitors.
- [NASTF — National Automotive Service Task Force](https://wp.nastf.org/) — legitimate OEM reprogramming access & Secure Data Release Model.
- [EPA — Tampering & Aftermarket Defeat Devices policy](https://www.epa.gov/enforcement/air-enforcement) — what crosses the line in the U.S.
- [CARB — Aftermarket Parts / EO program](https://ww2.arb.ca.gov/our-work/programs/aftermarket-performance-parts) — California's emissions-legal-parts framework.
- [NHTSA VIN decoder (vPIC) API](https://vpic.nhtsa.dot.gov/api/) — VIN → make/model/plant/market for `/provenance-trace`.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
