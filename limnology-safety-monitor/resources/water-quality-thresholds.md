# Water Quality Threshold Quick Reference

## EPA National Recommended Water Quality Criteria (Freshwater)

### Recreational Water Quality
| Parameter | Statistical Threshold Value (STV) | Geometric Mean | Notes |
|---|---|---|---|
| E. coli | 410 CFU/100mL | 126 CFU/100mL | Based on 30-day geometric mean |
| Enterococci | 130 CFU/100mL | 35 CFU/100mL | Less commonly used for freshwater |

### Cyanotoxin Recreational Advisories (EPA 2019)
| Toxin | Advisory Level | Do-Not-Swim Level |
|---|---|---|
| Microcystins | 8 μg/L | 20 μg/L |
| Cylindrospermopsin | 15 μg/L | 40 μg/L |

### Drinking Water Health Advisories (10-day, children)
| Toxin | Health Advisory |
|---|---|
| Microcystins | 0.3 μg/L |
| Cylindrospermopsin | 0.7 μg/L |

### Dissolved Oxygen
| Use Category | Acute (mg/L) | Chronic (mg/L) |
|---|---|---|
| Warmwater aquatic life | 5.0 | 6.0 |
| Coldwater aquatic life | 6.0 | 7.0 |
| Early life stages (coldwater) | — | 9.5 |

### pH
| Use Category | Range |
|---|---|
| Aquatic life (general) | 6.5 – 9.0 |

### Nutrients (EPA Ecoregion Reference Conditions)
These vary significantly by ecoregion. Representative ranges:

| Parameter | Oligotrophic | Mesotrophic | Eutrophic | Hypereutrophic |
|---|---|---|---|---|
| Total Phosphorus (μg/L) | <10 | 10-30 | 30-100 | >100 |
| Total Nitrogen (mg/L) | <0.35 | 0.35-0.75 | 0.75-1.5 | >1.5 |
| Chlorophyll-a (μg/L) | <2 | 2-8 | 8-25 | >25 |
| Secchi Depth (m) | >6 | 3-6 | 1-3 | <1 |

### Temperature
| Species Category | Upper Limit | Notes |
|---|---|---|
| Coldwater (trout, salmon) | Species-specific, typically 18-22°C | Check state-specific criteria |
| Warmwater (bass, bluegill) | Species-specific, typically 28-32°C | Check state-specific criteria |

### Ammonia (Total Ammonia Nitrogen)
pH and temperature dependent. At pH 7.0, 20°C:
| Duration | Criterion (mg/L TAN) |
|---|---|
| Acute (1-hour) | 24.1 |
| Chronic (30-day) | 3.09 |

*Note: Ammonia toxicity increases dramatically with pH and temperature. Always use the EPA ammonia criteria calculator for site-specific values.*

### Common Metals (Hardness-Dependent, at 100 mg/L CaCO₃)
| Metal | Acute (μg/L) | Chronic (μg/L) |
|---|---|---|
| Copper | 13.4 | 8.96 |
| Lead | 65.0 | 2.53 |
| Zinc | 120 | 120 |
| Cadmium | 1.79 | 0.25 |

*Note: Actual criteria depend on site-specific hardness. Use EPA metals criteria calculator.*

---

## Carlson's Trophic State Index Formulas

```
TSI(SD)  = 60 - 14.41 × ln(Secchi depth in meters)
TSI(CHL) = 9.81 × ln(Chlorophyll-a in μg/L) + 30.6
TSI(TP)  = 14.42 × ln(Total Phosphorus in μg/L) + 4.15
```

| TSI Range | Classification |
|---|---|
| <30 | Oligotrophic |
| 30-50 | Mesotrophic |
| 50-70 | Eutrophic |
| >70 | Hypereutrophic |

---

## Sample Holding Times (Common Parameters)

| Parameter | Container | Preservation | Max Holding Time |
|---|---|---|---|
| Temperature | — | Field measurement | Immediate |
| pH | — | Field measurement | Immediate (or 15 min) |
| Dissolved Oxygen | — | Field measurement | Immediate |
| Conductivity | P or G | Cool to 4°C | 28 days |
| Turbidity | P or G | Cool to 4°C | 48 hours |
| Total Phosphorus | P or G | H₂SO₄ to pH<2, cool to 4°C | 28 days |
| Total Nitrogen (TKN) | P or G | H₂SO₄ to pH<2, cool to 4°C | 28 days |
| Nitrate + Nitrite | P or G | H₂SO₄ to pH<2, cool to 4°C | 28 days |
| Chlorophyll-a | G (amber) | Filter in field, freeze | 28 days (frozen) |
| E. coli | Sterile P or G | Na₂S₂O₃, cool to 4°C | 8 hours (24 max) |
| Metals (dissolved) | P (acid-washed) | Field filter, HNO₃ to pH<2 | 6 months |
| Metals (total) | P (acid-washed) | HNO₃ to pH<2 | 6 months |
| Microcystin | G or P | Cool to 4°C (or freeze) | 14 days (4°C) |

P = Polyethylene/plastic, G = Glass
