# References — Microplastics Sampling & Testing

Compact lookup data. Cite, don't paraphrase from memory.

## Polymer densities & separation media

| Polymer | Density (g/cm³) | Floats in… |
|---|---|---|
| PP | 0.90–0.92 | water (≥1.0) |
| PE (LDPE/HDPE) | 0.91–0.97 | water |
| EPS foam | 0.01–1.05 | water |
| PS | 1.04–1.07 | NaCl |
| PA (nylon) | 1.12–1.15 | ZnCl₂/NaI |
| PMMA | 1.17–1.20 | ZnCl₂/NaI |
| PC | 1.20–1.22 | ZnCl₂/NaI |
| PVC | 1.16–1.45 | NaI/SPT |
| PET | 1.37–1.45 | NaI/SPT |
| PTFE | 2.1–2.3 | SPT |

**Density media (approx. achievable density):**

| Medium | Density (g/cm³) | Note |
|---|---|---|
| NaCl (saturated) | ~1.2 | Cheap, non-toxic; misses PET/PVC/PA |
| ZnCl₂ | ~1.5–1.7 | Recovers most common polymers; corrosive, waste handling |
| NaI | ~1.6–1.8 | Effective; expensive, oxidizes |
| Sodium polytungstate (SPT) | up to ~3.1 | Recovers all incl. PTFE; costly, reusable |

## Characteristic spectral bands (diagnostic, cm⁻¹)

| Polymer | FTIR diagnostic bands | Raman notes |
|---|---|---|
| PE | 2915 & 2848 (C–H), 1463, **718/730 doublet** | strong 1063, 1128, 1295, 1440 |
| PP | 2950, 2917, 2838, 1456, 1377, 997, 973, 841 | 809, 841, 1152, 1458 |
| PS | 3025 (aromatic C–H), 1601, 1493, 1452, 757, **697**, 540 | 1001 (ring breathing) sharp |
| PET | **1715 (C=O)**, 1240, 1095, 720 | 1614, 1728, 1096 |
| PVC | 1426, 1331, 1255, 960, 690, **615 (C–Cl)** | 638, 695, 2912 |
| PA (nylon) | 3300 (N–H), 1635 (amide I), 1540 (amide II) | 1634, 1280, 1440 |
| PMMA | **1730 (C=O)**, 1240, 1190, 1148 | 812, 1450, 1730 |

- **Hit-Quality Index threshold:** ~0.70 working default for FTIR library correlation; require runner-up margin ≥ ~0.05. Weight backbone bands over fluorescence/weathering artifacts.

## Size classes (working convention)

| Class | Range |
|---|---|
| Large microplastic | 1–5 mm |
| Small microplastic | 1 µm – 1 mm |
| Nanoplastic | < 1 µm |
| Standard neuston/manta mesh | 333 µm |
| Common cascade pore sizes | 500, 300, 100, 20, 10, 5, 0.45 µm |

## Counting uncertainty (Poisson)

For a raw count *n*, the relative standard error ≈ 1/√n. Sample enough volume that *n* clears your target precision:

| Target rel. error | Min count n |
|---|---|
| 50% | 4 |
| 30% | ~11 |
| 20% | 25 |
| 10% | 100 |

Report a Poisson confidence interval; do not report a 3-particle result as a precise concentration.

## Concentration units

- Water: **particles/L** or **particles/m³**; mass **µg/L**.
- Sediment / biota: **particles/kg dry weight** (always dry-weight normalize).
- State blank-corrected, recovery-corrected, and the size reporting floor alongside every figure.

## Instrument / sampler service intervals (starting points — tune to vendor specs)

| Asset | Watch metric | Typical action trigger |
|---|---|---|
| Neuston/manta net | tow distance, mesh integrity | inspect aperture each campaign; replace on wear |
| Sieve stack | sample count | aperture-gauge check; replace on out-of-tolerance |
| Sampling pump | run hours, flow-cal drift | re-cal flow each campaign; tubing/diaphragm on schedule |
| ATR-FTIR | IR source hours, crystal | source ~ vendor-rated hours; crystal inspect/clean routinely |
| µ-FTIR FPA detector | LN₂/MCT checks | per-session cooldown check; desiccant when saturated |
| Raman | laser diode hours, baseline creep | laser ~ rated hours; recal grating on drift |
| Py-GC/MS | injections, source cleaning | liner/septum by cycle; MS source per drift |

## Standards & methods

- **NOAA** Laboratory Methods for the Analysis of Microplastics in the Marine Environment — Masura et al. 2015, NOS-OR&R-48 (WPO + density separation reference method).
- **GESAMP** 2019, Reports & Studies No. 99 — monitoring & assessment of plastic litter in the ocean.
- **ISO 24187:2023** — principles for analysis of microplastics in the environment.
- **ISO/TR 21960:2020** — plastics in the environment, terminology & test methods overview.
- **ASTM D8332** — standard practice for collection of water samples for MP analysis.
- **ASTM D8333** — standard practice for preparation of water samples (digestion).
- **JRC / MSFD TG10** — EU marine-litter monitoring guidance (microplastics).
- **SCCWRP** interlaboratory method-evaluation studies (matrix/recovery comparability).

## Open tools & libraries

- **Open Specy** — open spectral library + matching (FTIR/Raman) for polymer ID.
- **siMPle** (systematic identification of MicroPlastics) — FTIR/Raman matching tool.
- **Nile Red protocols** — Maes et al. 2017 and successors (rapid fluorescence screening).
