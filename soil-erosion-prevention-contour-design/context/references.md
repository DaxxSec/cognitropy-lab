# Soil Erosion Prevention (Contour Design) — Reference Tables

Compact lookup data. Defer to RUSLE2, NRCS NEH, and local IDF/soil-survey sources for authoritative values. All factors are order-of-magnitude guidance for first-pass capacity work — verify per site.

## RUSLE K — soil erodibility (US units, t·ac·hr·hundreds⁻¹·ac⁻¹·ft⁻¹·tonf⁻¹·in⁻¹)

| Texture (low OM) | Typical K |
|------------------|-----------|
| Sand | 0.05–0.15 |
| Loamy sand / sandy loam | 0.15–0.30 |
| Loam | 0.25–0.40 |
| Silt loam / silt | 0.35–0.50 (most erodible) |
| Clay loam | 0.20–0.35 |
| Clay | 0.13–0.25 |

(Higher organic matter and better structure/permeability lower K. Pull site K from the NRCS soil survey where possible.)

## RUSLE C — cover-management (0 = full protection, 1 = bare fallow)

| Cover scenario | Typical C |
|----------------|-----------|
| Bare, tilled fallow | 1.0 |
| Conventional-till row crop, residue removed | 0.3–0.5 |
| Reduced-till row crop, 30% residue | 0.10–0.20 |
| No-till, high residue | 0.02–0.08 |
| Established meadow / dense sod | 0.004–0.01 |
| Mature forest / permanent cover | <0.005 |

## RUSLE P — support practice (0 = best, 1 = up-and-down slope)

| Practice | Slope 2–8% | Slope 8–12% | Slope 12–18% |
|----------|-----------|-------------|--------------|
| Up-and-down slope | 1.0 | 1.0 | 1.0 |
| Contour cultivation | 0.50–0.60 | 0.60–0.80 | 0.80–0.90 |
| Contour strip cropping | 0.25–0.30 | 0.30–0.40 | 0.40–0.45 |
| Terracing (+ contour, w/ outlet) | 0.10–0.12 | 0.10–0.16 | 0.16–0.18 |

## Soil-loss tolerance T (capacity budget)

| Soil depth / renewability | T (t/ac/yr) | T (t/ha/yr) |
|---------------------------|-------------|-------------|
| Shallow / non-renewable subsoil | 1–2 | ~2–5 |
| Moderate | 3 | ~7 |
| Deep, favorable, renewable | 4–5 | ~9–11 |

## Manning's n — channel roughness

| Lining | n |
|--------|---|
| Smooth earth, clean | 0.018–0.025 |
| Natural earth, some weeds | 0.025–0.035 |
| Short prairie / mowed grass | 0.03–0.04 |
| Dense tall grass (retardance class) | 0.04–0.15 (flow-depth dependent) |
| Riprap | 0.030–0.045 |
| Concrete | 0.012–0.017 |

## Permissible (non-erosive) mean velocity

| Boundary | Permissible V (m/s) | (ft/s) |
|----------|--------------------|--------|
| Fine sand / silt, bare | 0.3–0.6 | 1.0–2.0 |
| Firm loam, bare | 0.6–0.9 | 2.0–3.0 |
| Stiff clay, bare | 0.9–1.4 | 3.0–4.5 |
| Grass cover (good, erosion-resistant soil) | 1.5–2.4 | 5.0–8.0 |
| Riprap (well-graded) | 2.5–4.5 | 8.0–15 |

## Rational runoff coefficient C (storm-frequency dependent; raise ~10–25% for ≥25-yr)

| Surface | C |
|---------|---|
| Cultivated, flat (0–2%), sandy | 0.10–0.20 |
| Cultivated, rolling (2–7%), loam | 0.20–0.40 |
| Cultivated, steep (>7%), clay | 0.40–0.60 |
| Pasture / grass, average | 0.15–0.35 |
| Woodland | 0.10–0.25 |
| Bare / compacted construction soil | 0.50–0.75 |

## NRCS Curve Number (CN) — antecedent moisture II, by hydrologic soil group

| Cover | A | B | C | D |
|-------|---|---|---|---|
| Row crop, straight row, poor | 72 | 81 | 88 | 91 |
| Row crop, contoured, good | 65 | 75 | 82 | 86 |
| Row crop, contoured + terraced, good | 62 | 71 | 78 | 81 |
| Pasture, good | 39 | 61 | 74 | 80 |
| Woods, good | 30 | 55 | 70 | 77 |

## Design return-period guidance (typical agricultural ESC)

| Structure | Typical design return period |
|-----------|------------------------------|
| Contour cultivation / strip cropping | n/a (agronomic; storm-tolerant up to critical length) |
| Graded terrace channel | 10-yr, 24-hr (commonly) |
| Grassed waterway | 10-yr (peak), vegetated permissible-velocity check |
| Diversion (protecting cropland) | 10-yr; (protecting structures/homes) 25–50-yr |
| Sediment basin (construction) | 2–10-yr storage; principal + emergency spillway sized higher |
| Check dam (temporary) | 2-yr typical; pass larger storms over crest safely |

## Key formulas (quick recall)

- RUSLE: `A = R·K·LS·C·P`  |  Utilization(soil) = `A/T`
- Rational: `Qₚ = C·i·A`  |  CN runoff: `Q=(P−0.2S)²/(P+0.8S)`, `S=1000/CN−10`
- Manning: `Q=(k/n)·A·R^(2/3)·S^(1/2)` (k=1.49 US / 1.0 SI)  |  Utilization(hydraulic)=`Qₚ/Q_cap`
- MUSLE sediment yield: `Y=11.8·(Q·qₚ)^0.56·K·LS·C·P` (t)
- Check-dam spacing: `L ≈ H/(S_existing − S_stable)`
- Horton infiltration: `f(t)=f_c+(f_0−f_c)e^{−kt}`

## Upstream catalogues & standards

- **USDA-ARS RUSLE2** — https://www.ars.usda.gov/southeast-area/oxford-ms/national-sedimentation-laboratory/watershed-physical-processes-research/research/rusle2/ — current process-based soil-loss model + databases.
- **NRCS National Engineering Handbook (NEH)** — https://directives.sc.egov.usda.gov/ — Part 630 (hydrology, CN method), Part 650 (Engineering Field Handbook: terraces, waterways, diversions).
- **NRCS Conservation Practice Standards** — https://www.nrcs.usda.gov/ — e.g. CPS 600 Terrace, 412 Grassed Waterway, 362 Diversion, 350 Sediment Basin.
- **NOAA Atlas 14 (US) Precipitation Frequency** — https://hdsc.nws.noaa.gov/pfds/ — IDF/return-period rainfall depths.
- **NRCS TR-55, Urban Hydrology for Small Watersheds** — peak discharge / hydrograph method for small drainages.
- **FAO Soils Bulletin 70 / land & water** — https://www.fao.org/ — terracing, conservation on slopes (international context).
- **USDA Web Soil Survey** — https://websoilsurvey.nrcs.usda.gov/ — site-specific K, T, hydrologic soil group.
