# CMEM Modal Fuel & Emission Rates — Aggregated Reference

> Source: Comprehensive Modal Emissions Model, UC Riverside, Barth et al. (2000) with subsequent updates. These coefficients support second-by-second per-link estimation by mode (idle, accel, cruise, decel) and are intended for the inner-loop Pareto search; finalists should be verified with MOVES4.

## Modal Definitions
- **Idle:** vehicle stopped, engine running. Time fraction: time at v ≤ 0.5 mph.
- **Accel:** acceleration > 1 ft/s² and v > 0.5 mph.
- **Cruise:** |accel| ≤ 1 ft/s² and v > 0.5 mph.
- **Decel:** acceleration < −1 ft/s² and v > 0.5 mph (engine braking; negligible fuel for modern engines with deceleration fuel cut-off).

## LDV (Tier 3 / LEV III, MY 2018+, gasoline) — per second of mode time

| Mode | Fuel (g/s) | CO (mg/s) | NOx (mg/s) | HC (mg/s) | CO2 (g/s) |
|------|------------|-----------|------------|-----------|------------|
| Idle | 0.30 | 2.4 | 0.12 | 0.18 | 0.95 |
| Cruise (35 mph, level) | 0.85 | 4.5 | 0.55 | 0.20 | 2.65 |
| Accel (0.6 g, 35 mph target) | 4.50 | 22 | 4.8 | 1.4 | 14.0 |
| Decel (DFCO active) | 0.05 | 0.6 | 0.05 | 0.05 | 0.15 |

## LDT (MY 2018+, gasoline) — per second of mode time

| Mode | Fuel (g/s) | CO (mg/s) | NOx (mg/s) | HC (mg/s) | CO2 (g/s) |
|------|------------|-----------|------------|-----------|------------|
| Idle | 0.42 | 3.4 | 0.18 | 0.24 | 1.32 |
| Cruise (35 mph) | 1.18 | 6.2 | 0.78 | 0.28 | 3.70 |
| Accel | 6.20 | 32 | 6.8 | 2.0 | 19.4 |
| Decel | 0.08 | 0.9 | 0.07 | 0.07 | 0.24 |

## Single-Unit Truck (diesel, MY 2018+) — per second of mode time

| Mode | Fuel (g/s) | CO (mg/s) | NOx (mg/s) | HC (mg/s) | PM2.5 (mg/s) | CO2 (g/s) |
|------|------------|-----------|------------|-----------|---------------|------------|
| Idle | 1.4 | 8 | 28 | 4.0 | 0.7 | 4.4 |
| Cruise (35 mph) | 4.5 | 18 | 95 | 9.0 | 1.4 | 14.2 |
| Accel | 24 | 95 | 480 | 45 | 7.5 | 76 |
| Decel | 0.4 | 3 | 14 | 1.5 | 0.4 | 1.3 |

## Combination Truck (diesel, MY 2018+) — per second

Multiply SU values by approximately:
- Fuel / CO2: 1.6×
- NOx: 1.7×
- PM2.5: 1.8×
- CO / HC: 1.5×

## Transit Bus (diesel 40-ft, MY 2018+) — per second

| Mode | Fuel (g/s) | NOx (mg/s) | PM2.5 (mg/s) | CO2 (g/s) |
|------|------------|------------|---------------|------------|
| Idle | 1.8 | 32 | 0.9 | 5.7 |
| Cruise (15 mph urban) | 5.5 | 110 | 1.7 | 17.4 |
| Accel | 28 | 540 | 8.5 | 88 |
| Decel | 0.6 | 16 | 0.5 | 1.9 |

## Per-Stop Marginal Cost

A "stop" = decel from cruise speed to idle, hold, then accel back to cruise. Approximate marginal cost beyond the cruise baseline:

| Vehicle | ΔCO2 / stop (kg) | ΔNOx / stop (g) | ΔPM2.5 / stop (g) | ΔFuel / stop (gal) |
|---------|-------------------|------------------|---------------------|---------------------|
| LDV (LDV+LDT mix, 25 mph approach) | 0.045 | 0.060 | 0.0008 | 0.0050 |
| LDV, 45 mph approach | 0.085 | 0.110 | 0.0014 | 0.0095 |
| SU truck, 25 mph | 0.32 | 5.4 | 0.085 | 0.038 |
| Combo truck, 35 mph | 0.78 | 12.8 | 0.205 | 0.092 |
| Bus, 25 mph | 0.42 | 7.2 | 0.108 | 0.050 |

Use these for fast "saved emissions per saved stop" arithmetic in the Pareto search.

## Coefficient Sensitivity

- Aggressive accel (> 0.8 g vs. 0.6 g default): NOx scales ~1.4×, fuel ~1.25×.
- Cold ambient (< 50 °F): cruise NOx ~1.10×, idle CO ~1.20× (cold catalyst).
- High humidity: NOx ~0.92× (NOx-suppressing effect of water in combustion).

## Fleet-Weighted Aggregation

For a fleet with composition `w = [w_LDV, w_LDT, w_SU, w_CT, w_Bus, w_MC]`:
```
E_p_link = sum_j w_j * (
    t_idle_j * r_idle_p_j +
    t_cruise_j * r_cruise_p_j +
    t_accel_j * r_accel_p_j +
    t_decel_j * r_decel_p_j
) * vehicles_link
```

## Citation
Barth, M., An, F., Younglove, T., Scora, G., Levine, C., Ross, M., Wenzel, T. (2000). "Comprehensive Modal Emissions Model (CMEM), Version 2.0 User's Guide." UC Riverside CE-CERT.
Update reference: Scora, G. and Barth, M. (2006). "Comprehensive Modal Emissions Model (CMEM), Version 3.01 User's Guide."
