# Seasonal Calibration Reference

## Purpose

Aquaponics parameters shift with seasons. A pH of 7.0 in July and 7.0 in January may represent different system states depending on latitude, species, and system type. This reference provides seasonal baseline adjustment guidance so anomaly detection accounts for natural variation rather than flagging seasonal shifts as false positives.

## Why Seasonal Calibration Matters

- **Water temperature** varies with ambient air temp, especially in greenhouses and outdoor systems
- **Dissolved oxygen** solubility is inversely related to temperature — warmer water holds less DO
- **Biofilter efficiency** varies with temperature — nitrifying bacteria slow below 15C and stall below 10C
- **Fish metabolism** changes with temperature — feeding rates, waste output, and oxygen demand all shift
- **Plant uptake** varies with photoperiod and temperature — nutrient removal rates change seasonally

Without seasonal calibration, a system that is perfectly healthy in winter may trigger anomaly alerts simply because "normal" was baselined during summer.

## Seasonal Adjustment Tables

### Water Temperature Norms by System Type

| Season | Outdoor (Temperate) | Greenhouse (Unheated) | Greenhouse (Heated) | Indoor (Climate-Controlled) |
|--------|--------------------|-----------------------|--------------------|-----------------------------|
| Winter (Dec-Feb) | 4-10C | 10-18C | 22-28C | 24-28C |
| Spring (Mar-May) | 10-18C | 16-24C | 24-28C | 24-28C |
| Summer (Jun-Aug) | 22-30C | 24-34C | 26-32C | 24-28C |
| Fall (Sep-Nov) | 12-20C | 14-22C | 22-28C | 24-28C |

**Note:** These ranges are for temperate latitudes (30-50 degrees). Tropical systems (0-23 degrees) have much smaller seasonal variation. Adjust for your latitude.

### Dissolved Oxygen Saturation by Temperature

DO saturation decreases as temperature increases. These are the 100% saturation values at sea level:

| Water Temp (C) | DO Saturation (mg/L) | Practical Minimum for Fish |
|----------------|---------------------|---------------------------|
| 10 | 11.3 | 7.0 |
| 15 | 10.1 | 6.5 |
| 20 | 9.1 | 6.0 |
| 25 | 8.3 | 5.5 |
| 30 | 7.6 | 5.0 |
| 35 | 7.0 | 4.5 |

**Calibration rule:** In summer, a DO of 6.0 mg/L at 30C represents 79% saturation — adequate. In winter, a DO of 6.0 mg/L at 10C represents only 53% saturation — something is consuming oxygen. Same number, different diagnosis.

### Biofilter Efficiency by Temperature

Nitrifying bacteria (Nitrosomonas, Nitrobacter) are temperature-sensitive:

| Water Temp (C) | Relative Nitrification Rate | Practical Impact |
|----------------|----------------------------|------------------|
| <10 | <20% of peak | Biofilter effectively offline. Ammonia will accumulate. |
| 10-15 | 20-50% of peak | Biofilter sluggish. Reduce feeding to match. |
| 15-20 | 50-80% of peak | Biofilter functional but not peak. Monitor NH3/NO2. |
| 20-30 | 80-100% of peak | Optimal range. Full processing capacity. |
| >30 | Declining | Heat stress on bacteria. DO competition increases. |

**Calibration rule:** In spring, an ammonia reading of 0.15 ppm may be normal — the biofilter is still warming up. In summer, the same reading is a warning — the biofilter should be at full capacity.

### Feeding Rate Adjustment by Season

| Season | Feeding Rate (% body weight/day) | Rationale |
|--------|----------------------------------|-----------|
| Winter (<15C) | 0.5-1.0% | Reduced metabolism, slow biofilter |
| Spring (15-20C) | 1.0-2.0% | Increasing metabolism, biofilter warming |
| Summer (20-30C) | 2.0-3.0% | Peak metabolism, full biofilter capacity |
| Fall (20-15C) | 1.5-2.0% | Decreasing metabolism, biofilter cooling |

**Calibration rule:** Nitrogen loading (NH3 + NO2 + NO3 total) should be evaluated relative to feeding rate, not absolute thresholds. A system fed at 3% in summer will naturally have higher nitrogen than the same system fed at 1% in winter.

## How to Apply Seasonal Calibration

### Step 1: Determine Your Season Profile

When running `/onboard` or `/baseline`, record:
- Latitude (for photoperiod and ambient temp range)
- System type (outdoor / greenhouse unheated / greenhouse heated / indoor)
- Species (temperature preferences determine the operating range)
- Current season and month

### Step 2: Adjust Alert Thresholds

The `/scan` command should apply seasonal adjustments:

```
If system_type == "outdoor" AND season == "winter":
    NH3_warning = 0.2 ppm (relaxed from 0.1 — biofilter is slower)
    DO_warning = 8.0 mg/L (tightened — cold water should hold more DO)
    pH range = 6.6-7.6 (slightly wider — less biological buffering)

If system_type == "outdoor" AND season == "summer":
    NH3_warning = 0.1 ppm (standard — biofilter should be at capacity)
    DO_warning = 5.5 mg/L (relaxed — warm water holds less DO)
    pH range = 6.8-7.4 (standard)
```

### Step 3: Document Baseline Shifts

The `/baseline` command should record seasonal baselines separately:
- Winter baseline (Dec-Feb readings)
- Spring baseline (Mar-May readings)
- Summer baseline (Jun-Aug readings)
- Fall baseline (Sep-Nov readings)

Anomaly detection compares current readings to the *seasonal* baseline, not the annual average.

---

## Domain Accuracy Note

The temperature-DO solubility relationship and nitrification rate curves in this document are based on published aquaculture science (Timmons & Ebeling, *Recirculating Aquaculture*, 3rd ed.; Lennard & Leonard, *A Comparison of Three Different Hydroponic Sub-systems*). Feeding rate percentages are general guidelines — actual rates depend on species, life stage, and system design. **This reference should be reviewed by a practicing aquaponics operator before use in production monitoring.** If you identify inaccuracies, please open an issue.
