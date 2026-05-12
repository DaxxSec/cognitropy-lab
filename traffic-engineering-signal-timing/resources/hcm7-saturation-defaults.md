# HCM 7 Saturation Flow Defaults & Adjustment Factors

> Source: TRB Highway Capacity Manual, 7th Edition, Chapter 19 (2022).
> Use these only when site-specific saturation flow measurements are unavailable.

## Base Saturation Flow Rate

`s_o = 1900 vphgpl` (vehicles per hour of green per lane) for through movements at signalized intersections (HCM 7 §19, default value).

## Adjusted Saturation Flow

`s = s_o * f_w * f_HV * f_g * f_p * f_bb * f_a * f_LU * f_LT * f_RT * f_Lpb * f_Rpb` (HCM 7 Eq. 19-8)

## Lane Width (f_w)

| Lane width (ft) | f_w |
|-----------------|-----|
| < 10.0 | 0.92 (use with caution) |
| 10.0 | 0.92 |
| 11.0 | 0.96 |
| ≥ 12.0 | 1.00 |

## Heavy Vehicles (f_HV)

`f_HV = 100 / (100 + %HV * (E_T - 1))`

E_T = 2.0 typical; range 1.5–3.0 depending on grade and vehicle composition.

| %HV | f_HV (E_T = 2.0) |
|-----|------------------|
| 0 | 1.00 |
| 2 | 0.98 |
| 5 | 0.95 |
| 10 | 0.91 |
| 15 | 0.87 |
| 20 | 0.83 |

## Approach Grade (f_g)

`f_g = 1 - %grade / 200` (valid for −6% to +10%)

| Grade | f_g |
|-------|-----|
| −4% (downhill) | 1.02 |
| 0 | 1.00 |
| +2% | 0.99 |
| +5% | 0.975 |
| +8% | 0.96 |
| +10% | 0.95 |

## Parking (f_p)

For lane group with adjacent on-street parking:
`f_p = (N - 0.1 - 18 N_m / 3600) / N`

Where N = number of lanes in lane group, N_m = parking maneuvers per hour.

Set f_p = 1.0 for no parking.

## Bus Blockage (f_bb)

`f_bb = (N - 14.4 N_b / 3600) / N`

Where N_b = local buses stopping per hour in lane group.

## Area Type (f_a)

| Area | f_a |
|------|-----|
| CBD (central business district) | 0.90 |
| Other | 1.00 |

## Lane Utilization (f_LU)

| Movement | Default lanes | f_LU |
|----------|---------------|------|
| Through | 1 | 1.000 |
| Through | 2 | 0.952 |
| Through | 3 | 0.908 |
| Through | 4 | 0.865 |
| Exclusive left | 1 | 1.000 |
| Exclusive left | 2 | 0.971 |
| Exclusive right | 1 | 1.000 |
| Exclusive right | 2 | 0.885 |

(HCM 7 Exhibit 19-15. Override with field measurement when available.)

## Left Turn (f_LT)

For exclusive protected left:
`f_LT = 1 / 1.05` ≈ 0.95

For permitted left in shared lane: function of opposing through volume (see HCM 7 Eq. 19-17 et seq.; complex — use HCS or CHARTS).

For permitted left in exclusive lane: similar permitted-flow analysis required.

## Right Turn (f_RT)

For exclusive right turn lane (no peds): `f_RT = 0.85`.
For shared right turn lane: `f_RT = 1 - 0.15 * (P_RT)` where P_RT = right-turn proportion.

## Pedestrian / Bicycle Conflict for Lefts and Rights (f_Lpb, f_Rpb)

Function of conflicting pedestrian volume per cycle and bicycle volume. Compute via HCM 7 Eq. 19-25 et seq. — non-trivial. Default to 1.0 (no adjustment) for ped < 50/hr and bike < 20/hr.

## Common Combined Saturation Examples

| Scenario | s (vphgpl) |
|----------|------------|
| 12-ft through lane, 2% HV, level, suburban | 1900 × 0.98 ≈ **1862** |
| 11-ft through lane, 5% HV, +2% grade, CBD | 1900 × 0.96 × 0.95 × 0.99 × 0.90 ≈ **1545** |
| Exclusive protected left, 12 ft, level | 1900 × 0.95 ≈ **1805** |
| Exclusive right, no peds, 12 ft | 1900 × 0.85 ≈ **1615** |

## Validation
Field-measure saturation flow (5+ saturation cycles) for any high-stakes corridor. Rule of thumb: real-world saturation can vary ±10% from HCM defaults due to driver population, vehicle population, and weather effects.
