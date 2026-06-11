# References — Lookup Tables and Links

Compact lookup data. Numbers are typical/illustrative and **dataset-dependent**; always reconcile against the cited primary source or your own LCA database before quoting.

---

## Transformation properties — typical binary NiTi

| Property | Typical value | Note |
|----------|---------------|------|
| Af tuning range | ~ −50 to +110 °C | by Ni:Ti ratio + ternary additions |
| Thermal hysteresis | ~20–40 °C | R-phase only ~1–5 °C |
| Transformation enthalpy ΔH | ~20–32 J/g | DSC peak integral |
| Clausius–Clapeyron slope dσ/dT | ~5–8 MPa/°C | superelastic regime |
| One-way SME recoverable strain | ~6–8 % | |
| Two-way SME strain | ~2–5 % | trained; fades with cycling |
| Superelastic recoverable strain | up to ~8 % | with stress plateau |
| Ni-rich composition sensitivity | ≈ −10 °C per +0.1 at% Ni | above 50 at% Ni |
| Superelastic plateau stress | ~300–600 MPa (loading) | composition/temperature dependent |

## Alloy family quick-compare

| Family | Max Af | Strain | Cost | Watch-outs |
|--------|--------|--------|------|------------|
| NiTi | ~110 °C | high | high | Ni-tuning tolerance; Ni release |
| NiTiHf / NiTiZr | ~300–500 °C | moderate | high | embrittlement, processing |
| NiTiPd / NiTiPt | ~300–500 °C | moderate | very high | embodied carbon + supply risk |
| CuAlNi / CuZnAl | ~100–200 °C | low–moderate | low | brittle, grain-boundary fracture, aging |
| FeMnSi | one-way | low | low | large civil parts, small strain |

## Embodied energy & GWP — order-of-magnitude (RECONCILE before use)

> These vary widely by ore type (sulfidic vs. lateritic Ni), process route, and grid mix. Treat as ranges and verify against ecoinvent / GaBi-Sphera / GREET for the actual supply chain.

| Material | Cumulative energy demand | GWP (cradle-to-gate) | Driver |
|----------|--------------------------|----------------------|--------|
| Primary nickel | ~ 100–150 MJ/kg | ~ 6–13+ kg CO₂e/kg (much higher for lateritic/HPAL) | ore type, smelting energy |
| Titanium (sponge / mill) | very high (Kroll); ~ tens of MJ/kg sponge, more for mill product | ~ 8–35+ kg CO₂e/kg | Kroll process energy intensity |
| Platinum / palladium additions | very high | very high | extraction + supply risk; avoid unless required |

The **scrap / buy-to-fly ratio** frequently dominates the part footprint more than the material choice — minimize machining waste (near-net shape) first.

## Standards

| Standard | Scope |
|----------|-------|
| ASTM F2004 | DSC transformation-temperature measurement (NiTi) |
| ASTM F2005 | Standard terminology for NiTi shape memory alloys |
| ASTM F2063 | Wrought NiTi for medical devices and surgical implants |
| ASTM F2082 | Af by bend-and-free-recovery |
| ASTM F2516 | Tension testing of superelastic NiTi |
| ISO 14040 / 14044 | Life-cycle assessment — principles, framework, requirements |
| ISO 10993 | Biological evaluation of medical devices (biocompatibility) |
| EU REACH Annex XVII (entry 27) | Nickel-release limits for prolonged skin contact |
| RoHS (2011/65/EU) | Restricts Pb, Cd, Hg, Cr⁶⁺, etc. (not Ni directly) |

## LCA impact methods

- **ReCiPe** — midpoint + endpoint characterization.
- **TRACI** — US EPA characterization method.
- **CML** — midpoint method (Leiden).
- **Cumulative Energy Demand (CED)** — total primary energy across the life cycle.

## Links (verify currency)

- ASM / Nitinol overview — https://www.asminternational.org
- ASTM SMA standards index — https://www.astm.org (search F2004, F2063, F2516)
- ISO 14040/14044 — https://www.iso.org
- ecoinvent LCI database — https://ecoinvent.org
- GREET model (Argonne) — https://greet.es.anl.gov
- EU REACH legislation — https://echa.europa.eu
- "Engineering Aspects of Shape Memory Alloys" (Duerig et al.) — foundational reference text
- "Shape Memory Materials" (Otsuka & Wayman, eds.) — transformation crystallography reference
