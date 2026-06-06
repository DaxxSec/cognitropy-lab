# Repointing Maintenance Plan

## Purpose

Use when monitoring data exists and you need to turn it into a predictive-maintenance schedule — remaining-useful-life estimates, a priority ranking, and intervention windows that respect lime curing.

## Prompt Template

```
You are planning predictive maintenance for historic masonry pointing. Forecast remaining useful life from monitored decay, then schedule — inside the P-F interval and a lime-curing weather window.

I have monitoring and context:

- **Monitoring series:** [per zone: indicator, readings, dates — recession, capillarity, salts, biofilm %, hardness, crack width]
- **Epochs available:** [count per zone]
- **Failure thresholds:** [tuned values per indicator]
- **Exposure ranking:** [orientation / driving-rain per elevation]
- **Consequence:** [visible / structural per zone]
- **Climate constraints:** [frost windows, drying conditions, access seasons]

Please:
1. Fit a decay trajectory per indicator per zone (respect any change-point; don't extrapolate across breaks).
2. Estimate RUL per zone with a confidence band; name the governing indicator.
3. Rank zones by RUL × exposure × consequence.
4. Schedule interventions inside the P-F interval and a lime-curing window; sequence repointing, cause-first biocide, and detailing fixes.
5. Set the next inspection date and flag zones where you'd monitor rather than intervene.
```

## Expected Output

- Per-zone RUL with confidence bands and the governing indicator.
- Priority ranking (RUL × exposure × consequence).
- Scheduled intervention windows + sequence, honouring curing constraints.
- "Monitor vs intervene" calls for wide-band zones.
- Next inspection date and cadence justification.
