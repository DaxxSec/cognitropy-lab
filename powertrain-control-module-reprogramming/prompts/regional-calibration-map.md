# Regional Calibration Map

## Purpose

Select the correct, legal calibration variant for a vehicle's operating geography — jurisdiction, fuel grade, altitude, climate. Use when choosing between regional cals or triaging a gray-market mismatch. This is the geographic/spatial-analysis prompt.

## Prompt Template

```
You are a PCM calibration conservator performing a spatial calibration analysis. Map the right legal cal for this vehicle's geography.

- **Vehicle:** [make/model/year/engine]
- **Registration / operating jurisdiction(s):** [e.g. California USA; or fleet across CO + UT]
- **Cal origin market (from provenance):** [e.g. EU-market ECU]
- **Fuel grade available/used:** [AKI/RON, ethanol %]
- **Elevation band:** [min–max metres]
- **Climate:** [cold-region / temperate / hot]
- **Candidate cals available:** [list CAL-IDs + their origin markets]
- **Context:** [on-road | off-road/motorsport/closed-course/bench]

Please:
1. Resolve the governing emissions regime from jurisdiction.
2. Score each candidate cal for regime-fit, fuel-fit, climate-fit, and altitude coverage.
3. Recommend the best-fitting LEGAL variant; flag any gray-market mismatch and the readiness-monitor failures it predicts.
4. State whether this passes a preliminary emissions-legality check or must route to the legality gate.
```

## Expected Output

- The resolved regime + a scored variant-fit table
- A recommended legal calibration
- Gray-market / readiness-monitor warnings
- A preliminary legality note (PASS / route-to-gate)
