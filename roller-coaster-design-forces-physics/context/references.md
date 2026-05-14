# Roller Coaster Forces — Reference Tables

Compact lookup data. Defer to ASTM F2291, EN 13814, and IAAPA guidance for binding values.

## Approximate ASTM F2291 §6.4 Limit Curves

Mnemonic peaks vs. sustained. Always confirm against the standard.

| Axis | Peak (≤ 0.2 s) | Sustained (≥ 2 s) | Failure mode if exceeded |
|------|----------------|--------------------|---------------------------|
| `+z` (eyeballs-down)     | ~6.0 g  | ~3.0 g  | Spinal compression, greyout |
| `-z` (eyeballs-up, airtime) | ~-2.0 g | ~-1.0 g | Eject from seat |
| `+y` / `-y` (lateral)    | ~2.0 g  | ~1.5 g  | Head against restraint, neck strain |
| `+x` (eyeballs-back, launch) | ~5.0 g  | ~2.5 g  | Neck strain, restraint bruising |
| `-x` (eyeballs-forward, brake) | ~-3.5 g | ~-2.0 g | Forward whiplash, restraint bruising |
| Combined vector          | ~6.0 g  | —       | Cumulative |

## EN 13814 Annex G — Reference Points

- Limit envelope expressed as zones (A, B, C) by acceleration and duration.
- Zone A: routine; Zone B: requires justification; Zone C: prohibited absent specific medical / engineering rationale.
- Heartline reference height fixed at 1.05 m for ride-design purposes in EN; ASTM allows 1.0–1.2 m.

## Jerk In-House Conventions

| Axis | Peak (g/s) | Sustained 0.3 s (g/s) |
|------|------------|------------------------|
| Lateral (`d(ay)/dt`)  | 1.5 | 1.0 |
| Vertical (`d(az)/dt`) | 5.0 | 2.0 |
| Longitudinal (`d(ax)/dt`) | 3.0 | 2.0 |

These are common industry rules of thumb, not standards values. Operator in-house limits override.

## Restraint Class Lookup

| Class | -z floor (g) | Inversions | Lateral peak (g) | Typical example |
|-------|---------------|------------|-------------------|------------------|
| None / wrist tether | ≥ 0.0  | No | ≤ 0.5 | Kiddie / family coaster |
| Lap-bar single      | ≥ -0.5 | No | ≤ 1.0 | Wooden family coaster |
| Lap-bar ind. ratchet| ≥ -1.0 | No | ≤ 1.5 | Hyper-coaster (B&M / Intamin Mega-Lite) |
| OTSR fixed yoke     | < -0.5 or yes | Yes | ≤ 1.2 | Mid-90s loopers |
| Soft-vest OTSR      | < -1.0 or yes | Yes | > 1.2 | Modern inverters (B&M Wing, Mack Mega-Coaster) |
| Individual hydraulic| any    | Any | any | Launch coasters (Intamin Accelerator) |

## Simulator Output Column Map

| Source | Time | ax | ay | az | Frame |
|--------|------|----|----|----|-------|
| NoLimits 2 telemetry CSV | `t` | `ax` | `ay` | `az` | "Physics" = track, `+z` = down. |
| NoLimits 2 biomechanics CSV | `t` | `accelLong` | `accelLat` | `accelVert` | Heartline-style, `+z` = up. |
| Newton 2 export | `T` | `LongG` | `LatG` | `VertG` | Track frame, configurable. |
| RideTracker (sensor pack) | `t` | `ax` | `ay` | `az` | Body-fixed at sensor; track-frame approximation. |
| Custom MATLAB / Python | varies | varies | varies | varies | Always confirm. |

## Quick Geometry Formulas

- **Centripetal acceleration:** `a_c = v² · κ`, where `κ = 1/R` is local curvature.
- **Ideal bank for zero lateral-g:** `θ_ideal = atan(v² · κ / g)`.
- **Heartline force vector:** rotate track-frame `(ax, ay, az)` by the local bank `θ` around the local longitudinal axis. Add the heartline-offset moment if heartline ≠ wheel plane along the body-z.

## Standards & Catalogues

- **ASTM F2291 — Design of Amusement Rides and Devices** — https://www.astm.org/f2291-23.html — primary force envelope source (paywalled).
- **EN 13814 — Safety of amusement rides and devices** — https://standards.iteh.ai/catalog/standards/cen/65a6c39d-7f64-470a-86fb-c00d4b1da9d3/en-13814-1-2019 — European framework.
- **ASTM F770 — Ownership / operation of amusement rides** — https://www.astm.org/f0770-23.html — operations lifecycle.
- **ASTM F893 — Modifications to amusement rides** — https://www.astm.org/f0893-22.html — modification governance.
- **ASTM F2974 — Auditing of amusement rides** — https://www.astm.org/f2974-22.html — audit procedure.
- **IAAPA Safety & Standards Hub** — https://www.iaapa.org/safety-and-standards/safety-resources — global guidance index.

## Element Catalogue (for naming consistency)

| Element | Typical force signature |
|---------|--------------------------|
| Lift hill | Sustained +0.1 to +0.3 g longitudinal (chain), gentle |
| Drop | -1.0 to -1.2 g airtime at crest, +3 to +5 g pullout |
| Vertical loop | +4 to +5 g at base, +0 to +0.5 g at apex |
| Cobra roll | Two inversions, oscillating lateral |
| Zero-g roll | -0.2 to +0.2 g vertical at heartline; rolling without g-change |
| Heartline cam roll | Same as zero-g; heartline-aligned axis |
| Airtime hill (camelback) | -0.8 to -1.5 g at crest |
| Stengel dive | Banked lateral transition pre-loop |
| Helix | Sustained +1.5 to +2.5 g vertical, can exceed lateral limits if bank wrong |
| Brake run | -1.0 to -3.0 g longitudinal, short |
| Launch (LIM/LSM) | +1.5 to +5 g longitudinal, ~2–4 s |
| Block brake mid-course | -0.5 to -1.5 g longitudinal |
