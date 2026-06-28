# /spread-projection — Operational-Period Spread & Values-at-Risk

Project where the fire goes over the next operational period — head, flanks, spotting — and rank the values at risk by projected arrival time, feeding triage and evacuation decisions.

## Inputs

- Current perimeter or point of origin and current ROS/flame length per flank
- Fuel model (Anderson 13 / Scott & Burgan 40), slope %, aspect
- Weather: current + forecast wind (speed/direction/shift timing), RH, temperature, fuel moisture
- Values at risk: structures/zones, critical infrastructure, evacuation routes (with locations)
- Length of the operational period to project

## Steps

1. State inputs and assumptions explicitly (fuel model, weather source + valid time, slope, aspect).
2. Estimate ROS and direction for the **head** (aligned with wind/slope) and **flanks**; note expected flame length band.
3. Estimate **spotting distance** given wind and fuels; mark the area where new heads could form ahead of the main fire.
4. Project the perimeter forward for the period (use BehavePlus/FSPro where available; otherwise a documented hand estimate) and describe the envelope.
5. Compute **arrival time** at each value at risk / protective-action zone.
6. Rank values at risk by arrival time and exposure; hand the arrival times to `/structure-triage` and `/evac-triggers`.
7. Flag the dominant uncertainty (usually the forecast wind shift) and how the projection changes if it occurs early/late.

## Output

A projection memo to `outputs/spread-projection-<date>-<period>.md`: assumptions, head/flank ROS + flame length, spotting envelope, projected perimeter description, a values-at-risk table with arrival times, and the key uncertainty/wind-shift sensitivity.

## Notes

- This is a planning estimate, not a guarantee — treat BehavePlus/FSPro as the authoritative model and say so.
- Arrival time is the currency that drives evacuation lead time; be conservative (assume the faster case) when lives are downstream.
- Re-run on every significant weather change; a forecast wind shift can turn a flank into the head and re-rank everything.
