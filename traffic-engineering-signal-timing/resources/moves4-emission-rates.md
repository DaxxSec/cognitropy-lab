# EPA MOVES4 — Aggregated Emission Rates Quick Reference

> Source: EPA MOVES4 (2024 release). These are aggregated/representative defaults for first-cut estimating. **For SIP/CMAQ submittals, always run MOVES4 directly** — these are not a substitute for an actual project-level run.

## Light-Duty Vehicle (LDV) — Gasoline, MY 2020 fleet average, 75°F

| Drive condition | CO (g/mi) | NOx (g/mi) | VOC (g/mi) | PM2.5 (g/mi) | CO2 (g/mi) | Fuel (gal/mi) |
|-----------------|-----------|------------|------------|---------------|------------|----------------|
| Idle (per hr) | 8.5 g/hr | 0.42 g/hr | 0.65 g/hr | 0.012 g/hr | 1450 g/hr | 0.16 gal/hr |
| 5 mph | 12.0 | 0.95 | 0.85 | 0.020 | 580 | 0.065 |
| 15 mph | 4.8 | 0.55 | 0.40 | 0.012 | 380 | 0.043 |
| 25 mph | 2.9 | 0.40 | 0.25 | 0.009 | 320 | 0.036 |
| 35 mph | 2.2 | 0.36 | 0.18 | 0.008 | 295 | 0.033 |
| 45 mph | 1.9 | 0.38 | 0.15 | 0.008 | 290 | 0.033 |
| 55 mph | 1.8 | 0.45 | 0.13 | 0.009 | 305 | 0.034 |
| 65 mph | 2.0 | 0.62 | 0.13 | 0.011 | 360 | 0.040 |

## Light-Duty Truck (LDT, includes pickups, SUVs, minivans) — MY 2020, 75°F

Multiply LDV rates by approximately:
- CO: 1.4×
- NOx: 1.5×
- VOC: 1.3×
- PM2.5: 1.4×
- CO2: 1.45×
- Fuel: 1.45×

## Single-Unit Truck (SU) — Diesel, MY 2020, 75°F

| Drive condition | CO (g/mi) | NOx (g/mi) | VOC (g/mi) | PM2.5 (g/mi) | CO2 (g/mi) |
|-----------------|-----------|------------|------------|---------------|------------|
| Idle (per hr) | 25 g/hr | 18 g/hr | 4.5 g/hr | 0.45 g/hr | 5800 g/hr |
| 25 mph | 2.5 | 8.5 | 0.45 | 0.085 | 1100 |
| 45 mph | 1.8 | 7.2 | 0.30 | 0.060 | 950 |
| 55 mph | 1.7 | 7.8 | 0.28 | 0.060 | 1050 |

## Combination Truck (CT) — Diesel, MY 2020, 75°F

Multiply SU rates by approximately 1.6× across all pollutants.

## Transit Bus (Diesel 40-ft, MY 2018+) — 75°F

| Drive condition | CO (g/mi) | NOx (g/mi) | PM2.5 (g/mi) | CO2 (g/mi) |
|-----------------|-----------|------------|---------------|------------|
| Idle (per hr) | 35 g/hr | 22 g/hr | 0.55 g/hr | 6800 g/hr |
| 15 mph (urban) | 5.0 | 14 | 0.18 | 2400 |
| 35 mph | 3.5 | 11 | 0.13 | 1900 |

## Temperature & Humidity Adjustment

NOx is highly temperature-sensitive (Arrhenius-style):
- < 50 °F: multiply NOx by 1.10
- 50–75 °F: multiply NOx by 1.00 (baseline)
- 75–95 °F: multiply NOx by 0.95
- > 95 °F: multiply NOx by 0.90

CO is cold-start sensitive: < 50 °F multiply CO by 1.20.

## Fleet Aging

Per-mile rates drop ~3–5%/yr as MY mix advances; default MOVES4 release uses HPMS-projected fleet aging through 2050.

## Equivalents (EPA 2024)

- 1 metric ton CO2-eq ≈ **0.22** average passenger vehicles' annual emissions
- 1 gallon gasoline burned ≈ **8.89 kg** CO2
- 1 gallon diesel burned ≈ **10.21 kg** CO2

## Citation
EPA Office of Transportation and Air Quality, "MOVES4 (2024) Technical Guidance."
For project-level conformity: EPA, "Project-Level Conformity and Hot-Spot Analyses" (latest revision).
