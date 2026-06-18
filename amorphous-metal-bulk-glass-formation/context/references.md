# Amorphous Metal Bulk Glass Formation — Reference Tables

Compact lookup data. Numbers are representative literature values with real scatter — confirm against your own DSC before quoting a capacity figure. Temperatures in K unless noted.

## GFA Parameters — Formulas & Thresholds

| Parameter | Formula | "Good GFA" | Best correlates with |
|-----------|---------|-----------|----------------------|
| Trg | Tg / Tl | > 0.58–0.60 | castable thickness |
| ΔTx | Tx − Tg | > 40–60 K | supercooled-liquid stability / TPF |
| γ | Tx / (Tg + Tl) | > 0.40 | Rc and Dmax |
| γm | (2Tx − Tg) / Tl | higher | Dmax |
| δ | Tx / (Tl − Tg) | higher | Dmax |
| ω (Long) | Tg/Tx − 2Tg/(Tg+Tl) | lower | Rc |

## Representative BMG Thermal Data (literature, ±)

| Alloy (at%) | Tg (K) | Tx (K) | Tl (K) | ΔTx (K) | Trg | γ | Dmax | Rc (K/s) | Note |
|-------------|--------|--------|--------|---------|-----|------|------|----------|------|
| Pd₄₀Ni₄₀P₂₀ | 590 | 671 | 991 | ~81 | 0.60 | 0.42 | ~7 mm+ | <1 | best GFA, costly |
| Pd₄₀Cu₃₀Ni₁₀P₂₀ | 572 | 670 | 836 | ~98 | 0.68 | 0.476 | ~72 mm | ~0.1 | record thickness |
| Zr₄₁.₂Ti₁₃.₈Cu₁₂.₅Ni₁₀Be₂₂.₅ (Vit1) | 625 | 705 | 996 | ~80 | 0.63 | 0.435 | ~10 mm | ~1 | **Be-bearing** |
| Zr₅₅Cu₃₀Al₁₀Ni₅ | 682 | 767 | 1115 | ~85 | 0.61 | 0.427 | ~10 mm | ~10 | Be-free Zr |
| Cu₄₆Zr₄₂Al₇Y₅ | 695 | 768 | 1166 | ~73 | 0.60 | 0.413 | ~10 mm | — | Cu-based |
| Mg₆₅Cu₂₅Y₁₀ | 425 | 479 | 770 | ~54 | 0.55 | 0.401 | ~7 mm | — | low-Tg, easy TPF |
| Fe-based (Metglas-type) | ~750 | ~820 | — | ~50–70 | — | — | ribbon | ~10⁶ | soft magnetic |

> Values vary by source, purity, and heating rate. Use as anchors, not specs.

## Crystallization Kinetics — Working Equations

- **JMAK (isothermal):** X(t) = 1 − exp[−(K·t)ⁿ];  K = K₀·exp(−Ea/RT);  n = Avrami exponent (1–4).
- **Kissinger:** ln(β / Tp²) = −Ea/(R·Tp) + const → slope −Ea/R over heating rates β.
- **Ozawa / Flynn-Wall-Ozawa:** ln β = −1.052·Ea/(R·Tp) + const.
- **VFT viscosity:** η(T) = η₀·exp[D·T₀/(T − T₀)];  D = fragility (strong ≈ high D).
- **Dmax–Rc (conduction-limited, order-of-magnitude):** Dmax ≈ (a / Rc)^½, a ≈ thermal-diffusivity-scaled constant — calibrate to a known (Dmax, Rc) pair for the family.

## Capacity-Planning Formulas (the technique lens)

| Quantity | Formula |
|----------|---------|
| Little's Law | WIP = Throughput × Flow-time |
| OEE | Availability × Performance × Quality |
| Yield-adjusted capacity | good-parts/hr = gross-rate × first-pass-yield |
| Takt time | available time / demand units |
| Bottleneck throughput | min over stations of (stations × yield / cycle-time) |
| TPF parts-per-heat | floor( t_x(T_form) / cycle-per-part ) |
| Capacity cushion | (capacity − expected demand) / capacity |

## DSC Heating-Scan Cheat-Sheet (order on heating)

1. **Tg** — glass-transition step (endothermic baseline shift). No step → sample may already be crystalline.
2. **Supercooled-liquid region** — flat between Tg and Tx; its width ΔTx is the TPF working zone.
3. **Tx (onset) / Tp (peak)** — crystallization exotherm. Small/absent exotherm in a "glass" → already partly crystallized.
4. **Tm (solidus) / Tl (liquidus)** — melting endotherm(s). Tl is the GFA-parameter input, not Tm.
- Always log heating rate β and sample mass; report onset vs peak convention.

## Upstream Catalogues & Standards

- **ASM Handbook Vol. 1 / metallic-glass entries** — https://www.asminternational.org — alloy data, processing.
- **NIST data & phase references** — https://www.nist.gov — thermophysical properties.
- **ASTM E1356** — Tg by DSC; **ASTM E967/E968** — DSC temperature/heat calibration; **ASTM E698** — Arrhenius kinetics (Kissinger-type) by thermal analysis.
- **Liquidmetal Technologies / Caltech Johnson group** — Vitreloy family origin and TPF processing literature.
- **OSHA 1910.1024** — beryllium standard (PEL 0.2 µg/m³ TWA, 2.0 µg/m³ STEL).

## Quick Sanity Limits

- Fully amorphous XRD = broad halo, no Bragg peaks; XRD detection floor for crystallinity ≈ 2–5 vol% (TEM goes lower).
- If Trg > 0.6 **and** γ > 0.42 → expect cm-scale Dmax (good). If γ < 0.38 → expect mm-scale or worse.
- Oxygen in Zr-based melts: keep < ~few hundred ppm; hundreds of ppm visibly degrade Dmax and yield.
