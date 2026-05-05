# Dataset Index — Where to Get Mars Terrain Data

A planning-oriented index of the public datasets used by `/terrain-assess` and the look-ahead workflow. Each entry includes how to access, typical resolution, and what it's good for.

---

## HiRISE — High Resolution Imaging Science Experiment

- **Spacecraft:** Mars Reconnaissance Orbiter (MRO)
- **Resolution:** 25–60 cm/px (orthoimage); 1 m posting (DEM) in the typical Digital Terrain Model release
- **Coverage:** ~3% of Mars surface (targeted, not global)
- **Browse:** https://www.uahirise.org/
- **Targeting requests:** https://www.uahirise.org/hiwish/  (HiWish — public can request targets)
- **PDS releases:** https://pds-imaging.jpl.nasa.gov/volumes/mro.html
- **Best for:** Tactical sol planning, pre-landing site selection, single-target follow-up imagery
- **Notes:** DEM products are released for selected sites only; check the DTM index. Per-pixel elevation accuracy is typically ±0.25–1 m vertical.

## CTX — Context Camera

- **Spacecraft:** MRO
- **Resolution:** ~6 m/px
- **Coverage:** Global
- **Browse:** https://www.uahirise.org/ctx/
- **PDS releases:** Via PDS Imaging Node
- **Best for:** Strategic look-ahead, regional context, locating HiRISE target candidates
- **Notes:** CTX-derived DEMs (CTX-DEM, CaSSIS-comparable products) are produced by external groups (e.g., Murray Lab CTX mosaic at https://murray-lab.caltech.edu/CTX/) and provide near-global ~6 m posting.

## HRSC — High Resolution Stereo Camera

- **Spacecraft:** Mars Express (ESA)
- **Resolution:** 12.5 m/px nadir; 50 m DEM posting
- **Coverage:** Global, multi-band
- **PDS releases:** Via ESA PSA archive
- **Best for:** Wide-area regional DEMs, geological context
- **Notes:** Often used in concert with MOLA for elevation tie-down.

## MOLA — Mars Orbiter Laser Altimeter

- **Spacecraft:** Mars Global Surveyor (MGS)
- **Resolution:** 463 m grid (gridded altimetry product); track spacing variable
- **Coverage:** Global
- **PDS releases:** https://pds-geosciences.wustl.edu/missions/mgs/mola.html
- **Best for:** Global topography baseline, vertical reference for higher-res DEMs
- **Notes:** The authoritative global elevation reference. All other DEMs should be tied to MOLA.

## CaSSIS — Colour and Stereo Surface Imaging System

- **Spacecraft:** ExoMars Trace Gas Orbiter (TGO)
- **Resolution:** ~4.6 m/px
- **Coverage:** Targeted, growing
- **Browse:** https://wiki.cassis.unibe.ch/cassis/web/
- **Best for:** Color context where HiRISE not available; complementary stereo DEMs

## THEMIS — Thermal Emission Imaging System

- **Spacecraft:** 2001 Mars Odyssey
- **Resolution:** 18 m/px (VIS), 100 m/px (IR)
- **PDS releases:** Via PDS Imaging Node
- **Best for:** Thermal inertia (loose vs consolidated terrain inference), day/night contrast, regional mosaic
- **Notes:** Thermal inertia is a useful prior for terrain class (high TI → bedrock; low TI → fines).

## CRISM — Compact Reconnaissance Imaging Spectrometer for Mars

- **Spacecraft:** MRO
- **Resolution:** 18 m/px (full-resolution targeted)
- **Best for:** Mineralogy overlay (clays, sulfates, hydrated minerals — drives strategic targets, not tactical planning)

## MARCI — Mars Color Imager

- **Spacecraft:** MRO
- **Resolution:** ~1 km/px
- **Best for:** Daily weather (dust storm avoidance — affects solar rovers)
- **Browse:** Mars Weather Reports (MARCI weekly)

---

## Derived Products (Community / Lab)

- **Murray Lab CTX Global Mosaic:** https://murray-lab.caltech.edu/CTX/  — Near-global 6 m mosaic; tactical look-ahead.
- **NASA Trek (Mars):** https://trek.nasa.gov/mars/  — Web-based viewer over many of the above datasets.
- **Mars QuickMap:** https://mars.quickmap.io/  — Fast browsing; layers HiRISE, CTX, MOLA, mineralogy.
- **JMARS:** https://jmars.asu.edu/  — Free desktop tool; many overlays; planning-friendly.

---

## Per-Site Recommendations

| Site | Primary tactical dataset | Look-ahead dataset | Notes |
|------|--------------------------|---------------------|-------|
| Jezero Crater (Perseverance) | HiRISE DTMs of delta front | CTX (Murray Lab mosaic) | Project-internal HiRISE products may exist; check mission archive |
| Gale Crater (Curiosity) | HiRISE DTMs along route | CTX | Long mission archive — many sols of context |
| Meridiani Planum (Opportunity) | HiRISE | CTX | Historical reference |
| Gusev Crater (Spirit) | HiRISE | CTX | Historical reference |
| Utopia Planitia (Zhurong) | HiRISE / CaSSIS | CTX | Limited DEM coverage at HiRISE resolution |
| Oxia Planum (Rosalind Franklin) | HiRISE / CaSSIS | CTX | Pre-landing characterization extensive |

---

## What to Cache Locally

- Always cache the HiRISE DEM and orthoimage for the current planning AOI plus a 500 m buffer.
- Always cache the CTX coverage of the strategic horizon (next 5–10 sols of look-ahead).
- Cache MOLA for the broader region as elevation reference.
- Don't cache CRISM unless the strategic team is using it actively — large file size, infrequent use.
