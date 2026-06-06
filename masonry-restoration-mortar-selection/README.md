# Masonry Restoration Mortar Selection Workspace

> A Claude Code workspace that picks compatible repair mortars for historic masonry by borrowing the **methodology of mycology taxonomy** — keys, type specimens, binomial naming, two-track identification and phylogenetic reasoning — and schedules the work with **predictive maintenance**.

## What This Workspace Does

Choosing a repair mortar for an old wall is, underneath, an *identification* problem followed by a *selection* problem. You cannot specify a compatible repointing mortar until you know what the original binder actually is — air lime, a feebly or eminently hydraulic lime, a pozzolan-gauged lime, or (the modern mistake) a cement-rich mix — together with its aggregate and its hydraulicity. This workspace treats that identification the way a mycologist treats an unknown fungus.

A historic mortar sample is a **specimen**. The agent runs it down a **dichotomous key** to a binder class, then confirms with a two-track identification that mirrors fungal taxonomy: **petrographic "morphology"** (thin-section under a polarising-light microscope — binder character, aggregate mineralogy, grading, voids) paired with a chemical **"barcode"** (acid-digestion binder:aggregate ratio, hydraulic index, and where available SEM-EDS, XRD, TGA). Each characterised mortar gets a **binomial name** and is deposited as a **type specimen** in a reference "fungarium," so the next building can be matched against the collection. Mortars are placed on a **binder phylogeny** where compatibility is read by *relatedness* — the conservation rule that a repair must be softer, more porous and more vapour-open than the masonry becomes "stay near the original's clade; never graft on the distant Portland-cement clade."

The fusion also runs literally: masonry is colonised by lichens, microcolonial fungi, algae and cyanobacteria, and the agent **taxonomically identifies** them as **bioindicators** of the wall's moisture regime — orange *Trentepohlia* and crustose lichens tell you something about water dwell that a moisture meter alone does not. All of this feeds a **predictive-maintenance schedule**: monitored decay indicators and colonisation growth curves estimate the remaining useful life of the pointing and time the next intervention, so repointing is planned against degradation, not triggered by visible failure.

## Why This Workspace Exists

The single most destructive thing done to historic buildings in the 20th century was repointing soft lime-bonded masonry with hard Portland cement. Cement is stronger and far less permeable than the brick or stone around it, so moisture and dissolved salts are driven *through the units* instead of evaporating from the sacrificial joint — and the face of the masonry spalls off. Compatible mortar selection is therefore not a matter of taste; it is the difference between conserving a wall and quietly demolishing it over two decades. This workspace codifies a discipline: every repair recipe traces back to a *characterised* original (named, typed, archived), a stated compatibility rationale (softer / more porous / more vapour-open), and a monitoring baseline that says when to come back. Mycology's identification rigour is borrowed because taxonomy is the mature science of "what is this, exactly, and what is it most closely related to?" — which is the question mortar selection keeps failing to ask.

## Getting Started

### Prerequisites

- Physical mortar samples (loose fragments from a raked joint, not the masonry units) and, ideally, access to a petrographic lab for thin-sections.
- Basic lab capability or a partner lab: dilute-HCl acid digestion, balance, sieve stack; bonus: PLM, SEM-EDS, XRD, TGA.
- Field tools: Karsten tube / RILEM tube for capillary absorption, scratch-hardness picks or a drilling-resistance device, salt test strips or IC access, camera + scale bar.
- Conservation literacy: the lime cycle, ICOMOS / SPAB minimal-intervention ethics, and the softer-than-substrate principle.
- A qualified conservator and (for protected structures) the relevant consenting authority in the loop.

### Quick Start

1. Clone this workspace.
2. Drop sample photographs, lab reports, and elevation drawings into `context/` (large raw data into `outputs/raw/`).
3. Run `/mortar-key` on each original sample to get a provisional binder class from field + simple-lab characters.
4. Run `/characterize-historic-mortar` to confirm with the two-track (petrographic + chemical) identification and assign a binomial name.
5. Run `/specimen-accession` to archive the named mortar as a type specimen in the reference collection.
6. Run `/match-compatible-mortar` to design the repair mix, checking it against `/binder-phylogeny` for relatedness/compatibility.
7. Run `/biodeteriogen-survey` and `/decay-monitor` to baseline biological colonisation and decay indicators.
8. Run `/maintenance-forecast` to turn the baseline into a remaining-useful-life estimate and a scheduled intervention window.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/characterize-historic-mortar` | Two-track ID (petrographic "morphology" + chemical "barcode") → binomial name | After provisional keying, to confirm the original mortar |
| `/mortar-key` | Dichotomous key to binder class from field + lab characters | First pass on any unknown sample |
| `/specimen-accession` | Archive a characterised mortar as a type specimen with holotype data | Once a mortar is named, before reuse on other buildings |
| `/match-compatible-mortar` | Design a softer, vapour-open, salt/frost-aware repair mix | The core deliverable — specifying the repointing mortar |
| `/binder-phylogeny` | Place mortars on the binder tree; compatibility by relatedness | Sanity-checking a proposed mix against the original |
| `/delimit-mix` | Decide one mortar taxon vs several distinct mixes/phases | When samples across the building disagree |
| `/biodeteriogen-survey` | Identify lichen/fungal/algal/cyanobacterial colonisers as bioindicators | Condition assessment; reading the moisture regime |
| `/decay-monitor` | Log a time-series of decay indicators as a baseline | Establishing or updating the monitoring record |
| `/maintenance-forecast` | RUL estimate + scheduled intervention window | Planning the repointing/biocide/sheltering campaign |

## Directory Structure

```
masonry-restoration-mortar-selection/
├── CLAUDE.md                              # Agent role, context refs, command list
├── README.md                              # This file
├── .claude/commands/
│   ├── characterize-historic-mortar.md
│   ├── mortar-key.md
│   ├── specimen-accession.md
│   ├── match-compatible-mortar.md
│   ├── binder-phylogeny.md
│   ├── delimit-mix.md
│   ├── biodeteriogen-survey.md
│   ├── decay-monitor.md
│   └── maintenance-forecast.md
├── context/
│   ├── concepts.md                        # Binder taxonomy & phylogeny, compatibility, mycology mapping, decay indicators
│   ├── workflows.md                       # Keying-out, two-track ID, accession, mix design, survey, monitor→forecast
│   └── references.md                      # Binder/NHL/hydraulic-index tables, standards, mix ratios, biodeteriogen genera, links
├── prompts/
│   ├── mortar-identification-report.md
│   ├── repair-mortar-specification.md
│   ├── biodeterioration-assessment.md
│   └── repointing-maintenance-plan.md
└── outputs/                               # Identification reports, mix specs, survey records, forecasts
```

## Example Use Cases

### Repointing a Victorian soft-red-brick terrace
Provisional `/mortar-key` reads "air lime, fine sand"; thin-section and acid digestion confirm a 1:3 fat-lime:sand mortar (hydraulic index < 0.10). `/match-compatible-mortar` rejects the contractor's NHL 5 proposal as far too hard and specifies a hot-mixed or CL 90s lime mortar, putty-to-sand 1:2.5 with matched aggregate grading.

### Differentiating original fabric from later patch repairs on a parish church
Samples from buttress, plinth and nave disagree. `/delimit-mix` treats it as a species-delimitation problem: thin-section + hydraulic index resolve three "taxa" — a medieval hot-lime original, a 1900s gauged-lime campaign, and a 1970s cement patch — each needing its own repair recipe and its own removal decision.

### Reading a damp north elevation through its colonisers
`/biodeteriogen-survey` identifies *Trentepohlia* (orange filamentous alga), *Verrucaria* and *Lecanora* crustose lichens, and black microcolonial fungi. Their distribution maps the persistent-wetting zone; combined with `/decay-monitor` capillarity readings it localises a failed throating/drip detail driving the decay.

### Scheduling a cathedral repointing campaign by exposure
`/decay-monitor` baselines joint recession and friability across elevations; `/maintenance-forecast` ranks the SW (driving-rain) elevation as shortest remaining useful life and schedules it first, with lime-curing windows chosen to avoid frost.

### Building a regional reference collection
Over many jobs, `/characterize-historic-mortar` + `/specimen-accession` accumulate a typed catalogue of local historic mortars, so future identifications match against known regional "species" rather than starting cold.

## Recommended MCP Servers

- **filesystem** — read lab PDFs, sieve-analysis CSVs, elevation drawings; write identification reports and mix specs.
- **python** — grading curves, hydraulic-index arithmetic, recovery/decay-curve fits, lichenometry growth models (`numpy`, `scipy`, `pandas`, `matplotlib`).
- **sqlite** / **duckdb** — back the type-specimen "fungarium" and the multi-building decay-indicator time-series.
- **image / vision** — triage thin-section and colonisation photographs, estimate biofilm coverage %.
- **shell** — invoke lab pipeline scripts and generate the scheduled-maintenance calendar.

## Legal & Ethical Considerations

- **Heritage consent.** Listed buildings, scheduled monuments and conservation areas require consent before intervention (e.g. Listed Building Consent in the UK). Sampling itself may need permission. This workspace is advisory; a qualified conservator and the consenting authority decide.
- **Minimal intervention & reversibility.** Follow the ICOMOS Venice Charter and SPAB approach — repair, don't restore-away; match like-for-like; prefer the least, most reversible action.
- **Worker safety.** Lime is strongly caustic (pH ~12.5; alkali burns and eye damage — slaking quicklime is exothermic and hazardous). Cutting, raking and sieving generate **respirable crystalline silica**; biocides for biodeteriogen control are regulated pesticides. Record PPE, exposure controls and product approvals.
- **Biocide and ecology.** Lichens may be slow-growing and locally protected; biofilm removal can damage friable surfaces. Treat biocide use as a last resort after addressing the moisture cause.

## Technical References

- [Building Limes Forum](https://www.buildinglimesforum.org.uk/) — practitioner authority on lime mortars, hot-mixing and repointing.
- [Historic England — Practical Building Conservation: Mortars, Renders & Plasters](https://historicengland.org.uk/advice/technical-advice/buildings/) — canonical UK conservation guidance.
- [RILEM TC 203-RHM — Repair Mortars for Historic Masonry](https://www.rilem.net/) — testing and requirements for compatible repair mortars.
- [ASTM C270 — Mortar for Unit Masonry](https://www.astm.org/c0270-19a.html) — types M/S/N/O (and historic Type K) by proportion and property.
- [EN 459-1 Building lime](https://www.cen.eu/) and [EN 998-2 Masonry mortar](https://www.cen.eu/) — European lime and mortar classifications (CL/NHL, M-classes).
- [EN 1015 series](https://www.cen.eu/) — mortar test methods (1015-11 strength, 1015-18 capillary water absorption, 1015-19 vapour permeability).
- [ICOMOS Venice Charter (1964)](https://www.icomos.org/en/participer/179-articles-en-francais/ressources/charters-and-standards/157-the-venice-charter) — conservation ethics.
- [Index Fungorum](https://www.indexfungorum.org/) and [MycoBank](https://www.mycobank.org/) — fungal nomenclature and name registration (the type-specimen discipline borrowed here).
- [UNITE](https://unite.ut.ee/) — the ITS reference database; the "molecular barcode" model for the chemical-barcode analogy.
- [Warscheid & Braams 2000, *Biodeterioration of stone: a review* (Int. Biodeterioration & Biodegradation)](https://doi.org/10.1016/S0964-8305(00)00109-8) — microbial colonisation of masonry.
- [Guillitte 1995, *Bioreceptivity: a new concept for building ecology studies* (Sci. Total Environ.)](https://doi.org/10.1016/0048-9697(95)04528-5) — material aptitude for colonisation.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace is self-contained without it.
