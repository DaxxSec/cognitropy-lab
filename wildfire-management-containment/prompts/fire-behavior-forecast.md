# Fire Behavior Forecast

## Purpose

Produce a fire-behavior forecast narrative for an operational period from weather, fuels, and topography inputs — the kind a Fire Behavior Analyst (FBAN) would brief. Use at period start, on a weather change, or to underwrite a `/spread-projection`.

## Prompt Template

```
You are a fire-behavior analysis assistant. Produce a fire-behavior forecast for the operational period. State your assumptions (fuel model, weather source + valid time, slope, aspect). Treat BehavePlus/FSPro-class tools as the authoritative model and note where you're estimating.

Inputs:

- **Period / valid time:** [VALUE]
- **Fuel model (Anderson 13 / Scott & Burgan 40):** [VALUE]
- **Topography (slope %, aspect, terrain features — chimneys, drainages):** [VALUE]
- **Weather (wind speed/direction/gust, shift timing, RH, temp):** [VALUE]
- **Fuel moisture (1-hr / 10-hr / live):** [VALUE]
- **Indices (Haines, ERC, red-flag status):** [VALUE]
- **Current observed behavior (flame length, ROS, spotting):** [VALUE]

Please:
1. Forecast rate of spread and flame length for the head and flanks, with the band interpretation.
2. Assess crowning / torching / spotting potential and likely spotting distance.
3. Identify the critical burning window and the wind-shift effect (which flank becomes the head).
4. Translate behavior into suppression capability (what can hold the line where).
5. State the dominant uncertainty and how the forecast changes if it breaks the wrong way.
```

## Expected Output

- Head/flank ROS + flame length with band interpretation
- Crowning / torching / spotting assessment with spotting distance
- The critical window and the wind-shift effect
- A suppression-capability translation per flank
- The dominant uncertainty and its sensitivity
