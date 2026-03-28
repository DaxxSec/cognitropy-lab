# Water Parameter Reference Guide

## Universal Alert Thresholds (Generic — Override with System Baselines)

| Parameter | Ideal | Acceptable | Warning | Critical |
|---|---|---|---|---|
| pH | 6.8–7.2 | 6.5–7.8 | 6.0–6.5 or 7.8–8.5 | <6.0 or >8.5 |
| Temperature (tilapia) | 27–29°C | 24–32°C | 22–24°C or 32–34°C | <20°C or >35°C |
| Temperature (trout) | 13–16°C | 10–18°C | 8–10°C or 18–20°C | <6°C or >22°C |
| NH3 (total ammonia) | <0.05 ppm | <0.1 ppm | 0.1–0.5 ppm | >0.5 ppm |
| NO2- | <0.05 ppm | <0.1 ppm | 0.1–0.5 ppm | >0.5 ppm |
| NO3- | 10–40 ppm | 5–80 ppm | 80–160 ppm | >160 ppm |
| Dissolved Oxygen | >7 mg/L | >6 mg/L | 5–6 mg/L | <5 mg/L |
| EC | 300–800 μS/cm | 200–1500 μS/cm | 1500–2500 μS/cm | >2500 μS/cm |
| KH (alkalinity) | 100–200 ppm | 80–250 ppm | 50–80 ppm | <50 ppm |

## DO Saturation vs. Temperature

Fresh water dissolved oxygen saturation at standard atmospheric pressure:

| Temp (°C) | DO saturation (mg/L) |
|---|---|
| 10 | 11.3 |
| 12 | 10.8 |
| 14 | 10.3 |
| 16 | 9.9 |
| 18 | 9.5 |
| 20 | 9.1 |
| 22 | 8.7 |
| 24 | 8.4 |
| 26 | 8.1 |
| 28 | 7.8 |
| 30 | 7.5 |
| 32 | 7.3 |

Note: As temperature rises, water holds LESS dissolved oxygen. At 30°C your system has a much smaller safety margin than at 20°C.

## Free NH3 Fraction vs. pH and Temperature

Percentage of total ammonia that is the toxic free NH3 form:

| pH | 20°C | 25°C | 28°C | 30°C |
|---|---|---|---|---|
| 6.5 | 0.13% | 0.19% | 0.26% | 0.31% |
| 7.0 | 0.40% | 0.59% | 0.82% | 0.97% |
| 7.2 | 0.63% | 0.93% | 1.29% | 1.54% |
| 7.5 | 1.24% | 1.83% | 2.53% | 3.01% |
| 8.0 | 3.85% | 5.62% | 7.64% | 9.03% |
| 8.5 | 11.2% | 15.7% | 20.7% | 24.1% |

**Key insight:** At pH 8.0 and 28°C, 7.64% of "safe-looking" 0.25 ppm total ammonia is actually 0.019 ppm toxic NH3 — which is fine. But 1.0 ppm total ammonia becomes 0.076 ppm NH3, approaching stress threshold.

## Rate-of-Change Alert Thresholds

| Parameter | Warning Rate | Critical Rate |
|---|---|---|
| pH | ±0.3/hour | ±0.5/hour |
| Temperature | ±1.5°C/hour | ±2.5°C/hour |
| Dissolved Oxygen | -0.5 mg/L/hour | -1.0 mg/L/hour |
| NH3 | +0.1 ppm/hour | +0.2 ppm/hour |
| NO2- | +0.1 ppm/hour | +0.2 ppm/hour |

## Compound Event Trigger Conditions

| Event Name | Trigger Conditions | Severity | Primary Cause |
|---|---|---|---|
| Biofilter Crash | NH3 WARN + NO2 WARN + pH falling | 🔴 CRITICAL | Bacterial die-off |
| Oxygen Crisis | DO CRITICAL + NH3 rising + fish surfacing | 🔴 CRITICAL | O2 depletion |
| Nitrogen Loading | NH3 WARN + NO2 OK + NO3 rising | 🟠 HIGH | Overfeeding/overcrowding |
| Acidification | pH falling rapidly + NH3 OK + DO OK | 🟠 HIGH | CO2/acid buildup |
| Thermal Stress | Temp WARN + DO falling | 🟠 HIGH | Temperature event |
| Mineral Creep | EC rising slow + pH stable | 🟡 MEDIUM | Mineral accumulation |
| N-cycle Lag | NH3 slight↑ + NO2 slight↑ + NO3 stable | 🟡 MEDIUM | Biofilter behind load |
