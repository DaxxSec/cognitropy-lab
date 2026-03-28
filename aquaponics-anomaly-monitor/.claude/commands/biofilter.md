# /biofilter — Biofilter Health Assessment

Evaluate nitrifying bacteria health, nitrogen cycle efficiency, and biofilter capacity.

## Input Required
- NH3, NO2, NO3 readings (current and ideally a 48-hour trend)
- Biofilter type and age
- Media volume
- Recent disturbances (cleaning, medications, temperature drops)
- Feed rate (g/day)

## Nitrogen Cycle Efficiency Score
Calculate Stage 1 (NH3→NO2) and Stage 2 (NO2→NO3) efficiency.

Reference: A healthy, mature biofilter should process incoming ammonia to nitrate with both stages > 90% efficient, resulting in NH3 and NO2 both < 0.1 ppm in a properly loaded system.

## Bioload Assessment
Estimate theoretical ammonia production:
- Fish produce ~1% of body weight in ammonia-N per day (rough estimate)
- 10 kg of fish × 0.01 = 100g NH3-N/day
- Compare to biofilter conversion capacity based on media volume

## Output
```
BIOFILTER HEALTH ASSESSMENT

System: [biofilter type, age]
Bioload: ~[X] kg fish

NITROGEN CYCLE EFFICIENCY:
  Stage 1 (NH3 → NO2): [%] — [OK/DEGRADED/FAILED]
  Stage 2 (NO2 → NO3): [%] — [OK/DEGRADED/FAILED]
  Overall N-cycle Score: [0-100]

HEALTH INDICATORS:
  [list of positive/negative indicators]

ASSESSMENT: [Healthy / Stressed / Failing / Crashed]

RECOMMENDATIONS:
  [prioritized actions]

IF RECOVERY NEEDED:
  [Day-by-day recovery protocol]
```
