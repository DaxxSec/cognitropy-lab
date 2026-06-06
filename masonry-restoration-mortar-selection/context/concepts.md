# Masonry Restoration Mortar Selection — Core Concepts

Background the agent reads before identifying a mortar, designing a repair mix, surveying colonisation, or forecasting maintenance. Optimised for fast recall, not exhaustive theory. The organising idea: **identify the mortar like a mycologist identifies a fungus, then select by compatibility, then schedule by predicted decay.**

## The lime cycle (why mortars differ)

```
CaCO3  --calcination ~900°C-->  CaO (quicklime) + CO2
CaO    --slaking + H2O------->  Ca(OH)2 (slaked / hydrated lime)
Ca(OH)2 --carbonation + CO2-->  CaCO3 (the set; slow, needs air + moisture)
```

- **Air (non-hydraulic) lime** sets *only* by carbonation — slow, soft, highly vapour-open, self-healing of fine cracks, fully re-workable. Fat lime (high-calcium CL 90), or dolomitic.
- **Hydraulic lime** additionally sets by **hydration** of reactive belite (C₂S) and aluminate phases formed during calcination of argillaceous (clay-bearing) limestones — sets underwater, harder, faster, less vapour-open as hydraulicity rises.
- **Pozzolanic reaction** — amorphous silica/alumina (pozzolan) + Ca(OH)₂ + H₂O → calcium-silicate/aluminate-hydrates (C-S-H / C-A-H). Turns an air lime "feebly hydraulic" without firing clay. Roman *opus caementicium* used volcanic ash (pozzolana from Pozzuoli).
- **Portland cement** — fired at ~1450°C, alite (C₃S) dominant; very strong, low permeability. The modern incompatibility hazard for soft historic fabric.

## Binder taxonomy (the "phyla → genera → species" of mortar)

A working hierarchy from most vapour-open/soft to most closed/hard — this *is* the binder phylogeny used by `/binder-phylogeny`:

1. **Air limes** — CL 90 / CL 80 / CL 70 (calcium); DL (dolomitic). Hydraulic Index (HI) < ~0.10.
2. **Feebly hydraulic / pozzolan-gauged limes** — air lime + brick dust (cocciopesto), trass, metakaolin. HI ~0.10–0.16.
3. **Moderately hydraulic limes** — NHL 2 → NHL 3.5. HI ~0.16–0.31.
4. **Eminently hydraulic limes** — NHL 5. HI ~0.31–0.42.
5. **Natural cements (Roman cement) & hydraulic-lime/cement gauges** — fast-set, harder; HI/cementation index higher.
6. **Portland-cement mortars** — Types M/S (high cement). The *distant clade*; rarely compatible with historic units.

**Hydraulic Index (Vicat/Boynton):** `HI = (SiO₂ + Al₂O₃ + Fe₂O₃) / (CaO + MgO)` from oxide analysis. The single most useful chemical "character" separating clades.

**NHL classes (EN 459-1):** the number is the minimum 28-day compressive strength in MPa, with a banded range: **NHL 2** (2–7 MPa), **NHL 3.5** (3.5–10 MPa), **NHL 5** (5–15 MPa). Strength climbs and permeability falls up the series — choose the *lowest* class compatible with exposure and substrate.

## The cardinal selection rule — compatibility, not strength

The repair mortar must be **weaker, more porous, and more vapour-permeable than the masonry units and the original mortar.** It is *sacrificial*: salts and moisture should concentrate and decay in the joint (cheap, renewable) rather than in the unit (irreplaceable). Consequences:

- **Strength.** Match or undershoot the original; never overshoot. A too-hard mortar transfers stress to the unit arris → spalling.
- **Vapour permeability.** Water-vapour resistance factor **μ** (dimensionless) and **Sd = μ × thickness (m)**; repair must have ≤ the unit's resistance so the wall can dry through the joint.
- **Capillarity / porosity.** Higher, well-connected porosity in the joint lets it act as the evaporation/wicking path. Capillary absorption coefficient (kg/m²·min^0.5 or per √h, EN 1015-18).
- **Thermal & moisture movement.** Coefficients of thermal expansion and moisture movement should be close to the unit's; mismatches crack the bond.
- **Pore-size distribution** (MIP) matters more than total porosity for frost and salt resistance — many small pores plus some coarse "reservoir/air" pores resist freeze-thaw.

## Mortar characters (the identification "characters")

Like taxonomic characters, split into **morphological** (petrographic) and **chemical ("barcode")**:

- **Morphological / petrographic (thin-section, PLM):** binder character (carbonated lime, lime lumps, hydraulic phases), aggregate mineralogy and provenance, grain shape/roundness, **grading** (sieve curve), void/pore structure, lime lumps, shrinkage cracks, relict fuel ash. Point-counting gives the binder:aggregate ratio by volume.
- **Chemical "barcode":** **acid digestion** (dilute HCl) dissolves the carbonate binder; the insoluble residue is weighed and sieved → **binder:aggregate ratio** and aggregate grading (⚠ confounded by carbonate aggregate — limestone sand dissolves too; always pair with petrography). **Oxide analysis** (SEM-EDS / XRF) → hydraulic index. **XRD** → mineral phases (calcite, portlandite, ettringite, gypsum, hydraulic C-S-H). **TGA** → bound water, portlandite, CaCO₃ (mass loss steps ~ 100–200 / 400–550 / 600–800 °C).

## Mycology-method → mortar-method mapping (the fusion)

| Mycology taxonomy technique | Applied to mortar selection |
|---|---|
| Dichotomous identification key | `/mortar-key` — couplets on field + lab characters → binder class |
| Two-track ID: morphology + ITS barcode | Petrography ("morphology") + acid-digestion/oxide chemistry ("barcode") |
| Binomial nomenclature (*Genus species*) | Systematic mix name, e.g. *Calx aerius 1:3 (fine siliceous)* |
| Holotype + fungarium deposit | `/specimen-accession` — type specimen in the reference collection |
| Phylogeny / clades / relatedness | `/binder-phylogeny` — compatibility = closeness to original's clade |
| Species delimitation / cryptic species | `/delimit-mix` — one mortar taxon vs several mixes/phases |
| Index Fungorum / MycoBank registration | The accession register; one name = one type specimen |
| Indicator species / bioindication | `/biodeteriogen-survey` — colonisers indicate the moisture regime |
| Lichenometry growth curves (dating by thallus size) | Colonisation growth as a *clock* feeding `/maintenance-forecast` |

The fusion is more than metaphor: masonry **is** colonised by fungi/lichens, so literal mycological identification is part of condition assessment — and the *bioreceptivity* of a fresh lime mortar (high pH, smooth, low initial porosity) genuinely differs from a weathered one.

## Decay mechanisms (what the maintenance schedule is racing)

- **Salt crystallisation** — the dominant decay driver. **Subflorescence** (crystals growing *within* pores) generates pressure → spalling; **efflorescence** (surface bloom) is mostly cosmetic. Worst offenders: sodium sulfate (thenardite ↔ mirabilite hydration cycling), magnesium sulfate, chlorides, nitrates. Salt source: groundwater rising damp, de-icing salts, cement (alkalis), birds/agriculture (nitrates).
- **Freeze-thaw** — water in saturated pores expands ~9% on freezing; repeated cycles disrupt poorly-air-entrained, fine-pored mortars. Driven by saturation × cycle count.
- **Sulfate attack / ettringite** — sulfates + cementitious aluminates → expansive ettringite. Another reason cement near gypsum plasters/soils is risky.
- **Erosion / joint recession** — wind-driven rain and abrasion wear soft joints back from the face; recession depth is a primary monitoring indicator.
- **Biodeterioration** — biofilms retain moisture, secrete chelating/acidic metabolites (oxalic acid → calcium oxalate), and physically penetrate (endolithic lichens, fungal hyphae). Net effect is usually moisture-retention + slow biochemical etching.

## Biodeteriogens and bioreceptivity

- **Algae** — green (*Chlorella*, *Klebsormidium*) and orange filamentous **Trentepohlia** (carotenoid-rich; classic damp/N-facing indicator).
- **Cyanobacteria** — pioneer crusts on damp masonry; some endolithic.
- **Lichens** — symbiotic mycobiont + photobiont; crustose genera on stone: *Verrucaria*, *Lecanora*, *Caloplaca*, *Aspicilia*, *Rhizocarpon* (the lichenometry workhorse). Endolithic forms bore into calcareous stone.
- **Microcolonial / meristematic black fungi (MCF)** — *Knufia petricola*, *Sarcinomyces*, *Coniosporium*; extremophile black yeasts, severe biodeteriogens on stone.
- **Bioreceptivity** (Guillitte 1995): the material's *aptitude* to be colonised — primary (intrinsic: porosity, roughness, mineralogy, pH), secondary (after weathering), tertiary (after anthropogenic change). Fresh high-pH lime resists colonisation initially; this matters when timing repointing vs biocide.

## Predictive-maintenance concepts

- **Maintenance regimes:** run-to-failure → preventive (calendar) → **condition-based** → **predictive (PdM)**. This workspace targets condition-based/predictive.
- **P-F interval** — time from a *detectable* potential failure (rising capillarity, biofilm bloom, accelerating recession) to functional failure (joint loss, unit spalling). Inspection cadence must fit inside it.
- **Remaining Useful Life (RUL)** — extrapolate a decay indicator's trajectory to a failure threshold; report with a confidence band, never a point.
- **Decay indicators (monitored series):** joint recession depth (mm), scratch/drilling-resistance hardness, capillary absorption (Karsten tube mL/min), soluble-salt content (% by ion), biofilm coverage (%), surface moisture, crack width.
- **Exposure ranking:** driving-rain index / orientation prioritise elevations (SW worst in NW Europe).
- **Curing constraint on scheduling:** lime mortars need slow carbonation — protect from frost, rapid drying and heavy rain for weeks; schedule lime work to ~5–25 °C windows, not late autumn.

## Pitfalls the agent should call out by default

- Specifying by *strength class* alone without checking it is **softer than the substrate**.
- Acid-digestion binder:aggregate ratios when the aggregate is calcareous (it dissolves → overstated binder).
- Reading relative-abundance-style mineralogy (XRD peak heights) as quantitative without Rietveld/standards.
- Calling a building "one mortar" before delimiting phases/campaigns (`/delimit-mix`).
- Treating efflorescence and subflorescence as the same problem.
- Killing biofilm without fixing the moisture cause — it returns, and the wall is now also bleached.
- A two-point "recession trend" is not a trend; require ≥3–4 monitoring epochs before forecasting.
- Scheduling lime repointing into a frost window.
