# /fuse-trip-prior — Build a Route-Aware Power-Demand Prior

Construct a fused probabilistic prior for power demand along a planned route by combining navigation, traffic, elevation, weather, and driver-style sources into a single time-indexed `{mean, lower, upper}` curve over the prediction horizon.

## Inputs

- **Route definition** — GPX, encoded polyline, or `(start, end, waypoints)` resolved via routing API.
- **Vehicle parameter sheet** — mass, frontal area, drag coefficient, rolling resistance, drivetrain efficiency map.
- **Available sources** (any subset; at minimum nav + elevation): nav route, OSM/HD-map elevation, traffic feed (live or historical), weather (wind vector, ambient temp, precipitation), driver-style profile (aggressive/normal/eco prior or per-driver fingerprint), V2X feeds if reachable.
- **Trust weights** (optional) — last `/audit-fusion-trust` output for this vehicle + region, defaults to uniform with a stale-source decay.
- **Horizon length** — distance- or time-based (default: 30 km or 20 min, whichever is shorter).

## Steps

### 1. Time-Align Sources
- Convert every source to a common spatial index (cumulative distance s along the route, with timestamps when available).
- Apply per-source latency compensation (V2X SPaT timestamps are usually 100–500 ms stale; cloud traffic feeds 30–120 s).
- Flag any source older than its TTL — see `context/references.md` for per-source TTLs.

### 2. Per-Source Power Decomposition
Decompose road-load power along the route from each source independently:

- `P_aero(s) = 0.5 · ρ_air(weather) · C_d · A · (v(s) + headwind(s))^2 · v(s)`
- `P_roll(s) = C_rr · m · g · cos(slope(s)) · v(s)`
- `P_grade(s) = m · g · sin(slope(s)) · v(s)`
- `P_accel(s) = m · v(s) · dv/ds · v(s)` — speed profile from traffic + driver model
- `P_aux(s)` — HVAC + accessories, weather-driven for cabin conditioning, vehicle-specific for everything else

Use elevation from HD-map (primary) and OSM SRTM (fallback) — see `context/workflows.md` for the elevation-conflict rules.

### 3. Speed-Profile Fusion
- Combine traffic-derived speed (mean, percentile bands) with driver-style scaling (aggressive drivers run ~10–25% over traffic mean on free-flow segments; eco drivers ~5–15% under).
- Constrain by posted speed and curvature limits.
- Emit a `v(s)` distribution rather than a point estimate.

### 4. Source Weighting and Combination
- Compute per-source predictive variance from historical residuals (or default `context/references.md` table).
- Inverse-variance weight where sources agree; switch to **robust fusion** (Huber, M-estimator, or Mahalanobis-gated) where any pair disagrees beyond χ² threshold — log the gating event for `/source-conflict`.
- Propagate variance through the decomposition (linearise around the fused speed/elevation profile) to emit credible bands.

### 5. Emit and Persist
- Write the fused prior to `outputs/priors/<vehicle>-<route-hash>-<timestamp>.json` with schema:
  `[ { s, t, P_mean, P_lower, P_upper, dominant_uncertainty, source_provenance: [...] } ]`
- Render a quick-look plot (mean ± credible band) for visual sanity check.

## Output

JSON prior file in `outputs/priors/` plus a PNG plot of the predicted power-demand curve with credible bands and a stacked-area decomposition (aero / rolling / grade / accel / aux). Every sample carries its source provenance list.

## Notes

- **Don't average elevation sources.** If HD-map and OSM disagree by >5 m on a segment, prefer HD-map and log the divergence — averaging hides systematic biases (e.g. SRTM canopy artefacts).
- **Driver-style fingerprints are sticky.** A single anomalous drive shouldn't shift the fingerprint; use exponentially-weighted updates with a half-life of 5–10 drives.
- **Don't fuse without the trust audit.** If `/audit-fusion-trust` hasn't run for the current vehicle + region, default to nav + elevation only and emit a warning. Bringing in unaudited sources silently is the failure mode.
