# /weather-hold — Weather Go/No-Go Decision

Evaluate current and forecast weather conditions against field safety thresholds for a go/no-go decision.

## Procedure

1. Ask the user to provide:
   - Site location
   - Planned field window (start time, duration)
   - Activity type (boat-based, shore-based, wading, ice operations)
   - Watercraft type and size (if applicable)

2. Ask the user for current/forecast conditions (or help them identify sources):
   - Air temperature (current and forecast high/low)
   - Wind speed and direction (sustained and gusts)
   - Precipitation probability and type
   - Lightning/thunderstorm probability
   - Visibility
   - Wave height (for large lakes/reservoirs — NOAA marine forecast)
   - Water temperature (if known)

3. Evaluate against hard no-go thresholds:

| Condition | Threshold | Decision |
|---|---|---|
| Lightning | Within 10 miles or 30-minute forecast | **NO-GO** |
| Sustained wind | >20 knots (small craft) / >30 knots (large craft) | **NO-GO** |
| Gusts | >30 knots (any craft) | **NO-GO** |
| Visibility | <0.5 miles (fog, rain, snow) | **NO-GO** |
| Wave height | >3 ft (small craft) / >5 ft (large craft) | **NO-GO** |
| Air temp + wind chill | <-20°C without cold weather protocol | **NO-GO** |
| Water temp | <4°C without immersion suits | **NO-GO** |
| Active tornado/severe thunderstorm watch | Any | **NO-GO** |

4. Evaluate soft hold conditions (require mitigation):

| Condition | Threshold | Action |
|---|---|---|
| Wind | 15-20 knots (small craft) | **HOLD** — Shorten window, stay near shore |
| Rain | Steady rain forecast | **HOLD** — Assess equipment protection, footing risk |
| Heat index | >105°F | **HOLD** — Shorten exposure, mandatory hydration breaks |
| UV index | >8 | **CAUTION** — Enhanced sun protection, shade breaks |
| Fog | 0.5-1 mile visibility | **HOLD** — Delay departure, monitor for clearing |

5. Issue one of four decisions:
   - **GO** — Conditions within all thresholds, proceed with standard precautions
   - **CONDITIONAL GO** — Soft holds present, proceed with specific mitigations documented
   - **HOLD** — Conditions marginal, delay departure and re-evaluate at specified time
   - **NO-GO** — Hard threshold exceeded, abort and reschedule

6. Document the decision with:
   - Specific conditions evaluated and values
   - Decision rationale
   - If HOLD: re-evaluation time and conditions that would change the decision
   - If CONDITIONAL GO: specific mitigations required

7. Save to `work-log/weather-hold-[DATE]-[TIME].md`
