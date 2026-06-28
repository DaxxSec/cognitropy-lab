# /red-flag-readiness — Fire-Weather Risk & Operational Posture

Read the day's fire-weather risk — red-flag status, Haines Index, ERC, fuel moisture, wind shift timing — and set the operational posture and staffing level for the period.

## Inputs

- Today's/tomorrow's fire-weather forecast (NWS fire weather / spot forecast, RAWS)
- Wind forecast (speed, direction, gust, and the timing of any shift)
- RH and temperature trend; dead/live fuel moisture; ERC or fuel-moisture percentile
- Haines Index; any red-flag warning or fire-weather watch in effect

## Steps

1. Pull the metrics; note source and valid time for each.
2. Score each against the thresholds in `context/references.md`: RH crossover, 1-hr fuel moisture band, Haines 5–6, high ERC.
3. Identify the **critical window** — the hours of peak risk (often early afternoon to evening burning period, or the wind-shift hour).
4. Set an **operational posture**: routine / elevated / critical — and translate to staffing, pre-positioning, patrol frequency, and whether to pre-stage structure-protection resources.
5. List the specific hazards to brief (e.g. "frontal passage ~1600 swings wind NW→SW; right flank becomes the head").
6. Recommend go/no-go implications for planned line work and burnout during the critical window.

## Output

A readiness brief to `outputs/red-flag-readiness-<date>.md`: metric-by-metric read with thresholds, the critical window, the posture call with staffing/pre-positioning, the hazards to brief, and burnout/line-work implications.

## Notes

- The forecast **wind shift** is the most important line in the brief — call out the hour and which flank it endangers.
- Red flag = posture up *before* the window, not during. Pre-position; don't react.
- This sets posture; per-assignment commitment still runs through `/lces-check`.
