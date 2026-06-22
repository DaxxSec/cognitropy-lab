# Upholstery Frame Restoration — Reference Tables

Compact lookup data for tasks. Defer to upstream standards for full detail.

## Control-chart constants (subgroup size n)

| n | A₂ (X̄) | D₃ (R LCL) | D₄ (R UCL) | d₂ (σ̂ = R̄/d₂) |
|---|---|---|---|---|
| 2 | 1.880 | 0 | 3.267 | 1.128 |
| 3 | 1.023 | 0 | 2.574 | 1.693 |
| 4 | 0.729 | 0 | 2.282 | 2.059 |
| 5 | 0.577 | 0 | 2.114 | 2.326 |

**Individuals (I-MR), n=1 — the default for restoration:**
- I chart limits: `X̄ ± 2.66·M̄R`  (2.66 = 3/d₂ for n=2 moving range)
- MR chart: `UCL = 3.267·M̄R`, `LCL = 0`
- σ̂ = M̄R / 1.128

## Western Electric / Nelson out-of-control rules

| Rule | Signal |
|---|---|
| 1 | 1 point beyond 3σ (UCL/LCL) — gross shift |
| 2 | 2 of 3 consecutive points beyond 2σ (same side) |
| 3 | 4 of 5 consecutive points beyond 1σ (same side) |
| 4 | 8 (Nelson) / 9 consecutive points on one side of center — sustained shift |
| 5 | 6 points steadily increasing or decreasing — trend |
| 6 | 14 points alternating up/down — over-control/tampering |
| 7 | 15 points within 1σ — stratification / wrong limits |

## Capability interpretation (Cpk, in-control process)

| Cpk | Verdict | ~ defects (centered) |
|---|---|---|
| < 1.00 | Incapable | > 2700 ppm |
| 1.00–1.33 | Marginal | 64–2700 ppm |
| 1.33–1.67 | Capable | ~0.6–64 ppm |
| ≥ 1.67 | High capability | < 0.6 ppm |

Cp = (USL−LSL)/6σ; Cpk = min[(USL−X̄),(X̄−LSL)]/3σ. Use σ̂ from the in-control chart.

## Gage R&R acceptance (AIAG MSA)

| %GRR (study var.) | ndc | Verdict |
|---|---|---|
| < 10% | ≥ 5 | Acceptable |
| 10–30% | ≥ 5 | Conditional (cost/criticality) |
| > 30% | < 5 | Unacceptable — fix method |

Gauge resolution rule (10:1 / "rule of tens"): instrument discrimination ≤ 1/10 of the tolerance band.

## ANSI/ASQ Z1.4 — single sampling, General Inspection Level II (excerpt)

| Lot size | Code | Sample n | AQL 1.0 (Ac, Re) | AQL 2.5 (Ac, Re) |
|---|---|---|---|---|
| 2–8 | A/B | 2–3 | 0,1 | 0,1 |
| 9–15 | C | 5 | 0,1 | 0,1 |
| 16–25 | D | 8 | 0,1 | 0,1 |
| 26–50 | E | 13 | 0,1 | 1,2 |
| 51–90 | F | 20 | 0,1 | 1,2 |
| 91–150 | G | 32 | 1,2 | 2,3 |
| 151–280 | H | 50 | 1,2 | 3,4 |
| 281–500 | J | 80 | 2,3 | 5,6 |

(Antique/irreplaceable pieces: do not sample — inspect 100%.)

## Wood equilibrium moisture content (EMC, %) by ambient RH at ~21 °C

| RH | 30% | 40% | 50% | 60% | 70% | 80% |
|---|---|---|---|---|---|---|
| EMC | 6.2 | 7.7 | 9.2 | 11.0 | 13.1 | 16.0 |

- Target service MC: **6–9%** (most interiors). Glue-up window: mating surfaces within ~2% of service EMC; avoid > ~12% MC.

## Common frame joints → first-line repair

| Joint | Failure | First-line repair |
|---|---|---|
| Mortise & tenon | glue-line open, shoulder gap | clean & re-glue (hide); shim/oversize tenon if loose |
| Dowel | rocking, sheared dowel | drill out, re-dowel with fluted dowels + PVA/hide |
| Corner block | detached/split | re-glue + screw new hardwood block; never just staple |
| Lap/bridle | split along grain | glue + clamp; reinforce with hidden spline if structural |
| Rail crack | seasonal split | inject hide/PVA, clamp; butterfly key only if reversible-documented |

## Adhesive cheat-sheet

| Adhesive | Reversible | Open time | Clamp/cure | Use |
|---|---|---|---|---|
| Hot hide glue | Yes (heat+moisture) | short (~1–2 min) | overnight | conservation-grade; antique frames |
| Liquid hide glue | Yes | long | 24 h | longer assemblies, still reversible |
| PVA (yellow/Type II) | No (practically) | ~5–10 min | clamp 30–60 min, full 24 h | utility/modern frames |
| Epoxy | No | varies | per product | last-resort structural gap-fill; non-conservation |

## Upstream catalogues & standards

- **AIC — Code of Ethics & Guidelines for Practice** — https://www.culturalheritage.org/about-conservation/code-of-ethics — conservation ethics binding the disposition.
- **ANSI/ASQ Z1.4-2003 (R2018)** — https://asq.org/quality-resources/z14-z19 — acceptance sampling for attributes (successor to MIL-STD-105E).
- **ISO 7870 series** — https://www.iso.org/standard/40174.html — control charts (general + specific chart types).
- **AIAG MSA Reference Manual (4th ed.)** — https://www.aiag.org/ — gage R&R methodology.
- **NIST/SEMATECH e-Handbook of Statistical Methods** — https://www.itl.nist.gov/div898/handbook/ — free reference for control charts, capability, sampling.
- **Forest Products Laboratory, *Wood Handbook* (FPL-GTR-282)** — https://www.fpl.fs.usda.gov/products/publications/ — EMC, shrinkage, wood movement data.
- **ASTM E2554 / ASQ tables** — control-chart constants and capability conventions.
