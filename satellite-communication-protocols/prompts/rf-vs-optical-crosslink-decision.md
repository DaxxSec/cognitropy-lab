# RF-vs-Optical Crosslink Decision

## Purpose

Structure the choice between an RF link and a free-space optical link for a given hop — the point where satellite comms and optics literally become the same engineering problem. Use when sizing inter-satellite links or feeder links where optical might dominate.

## Prompt Template

```
You are choosing RF vs free-space optical (or hybrid) for one hop. The optical beam has enormous diffraction-limited gain but a µrad beamwidth and a heavy pointing burden; weigh benefit against cost honestly.

Hop:
- **Type:** [inter-satellite (vacuum) | space-to-ground (atmosphere)]
- **Range:** [km]
- **Optical option:** [wavelength, aperture D, Tx power, PAT capability]
- **RF alternative:** [band, antenna sizes, power, current budget margin]
- **Constraints:** [SWaP budget, latency need, availability target, $ per terminal]

Please:
1. Build both link budgets in the same cascade form (for optical: antenna gain (πD/λ)², free-space (λ/4πR)², detector photons/bit).
2. Quantify the optical pointing (PAT) cost and risk, and the weather/cloud availability hit for space-to-ground.
3. Compare capacity gained vs SWaP/$ spent vs availability and licensing delta (optical needs no ITU frequency coordination; credit any LPI/LPD benefit).
4. Recommend RF, optical, or hybrid, naming the single dominant deciding factor.
```

## Expected Output

- Side-by-side RF and optical link budgets
- A PAT cost/risk assessment and a weather-availability comparison
- A clear RF / optical / hybrid recommendation with the deciding factor named
