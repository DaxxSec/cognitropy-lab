# /heartline-analysis

Project a track-frame force trace into the **heartline frame** so the verdict reflects what the rider's chest feels, not what the chassis feels.

## Inputs

- `centerline_csv` — `s, x, y, z, bank` columns (arc length, position, bank angle in degrees). Required.
- `force_csv` — `t, ax, ay, az` in track frame.
- `velocity` — either a `v(s)` profile or a constant; required to map `t` to `s`.
- `heartline_offset` — height above wheel plane in meters. Default 1.10 m. Use 1.05 m for EN 13814 alignment.

## Steps

1. Resample the centerline so its `s` aligns with the force trace's `t` via the velocity profile (`s(t) = ∫ v dt`).
2. For each sample, compute the local body-axes rotation matrix from `bank(s)` and the centerline tangent.
3. Add the heartline-offset moment: the heartline is at `+ heartline_offset` along the local body-z (rider stands up in the seat). Account for the angular velocity ω = v · κ when computing the heartline-felt acceleration: `a_heart = a_chassis + ω × (ω × r) + α × r`, where `r` is the offset vector and `α = dω/dt`.
4. Rotate the resulting vector into the heartline body frame.
5. Emit a new CSV in heartline frame, plus a side-by-side delta plot script (write to `outputs/heartline/<ride>/`).
6. Note any segment where the track-frame → heartline-frame delta exceeds 0.3g in any axis — this is where peak-chasing on the chassis trace would have been wrong.

## Output

- `outputs/heartline/<ride>/<segment>-heartline.csv` — heartline-frame trace.
- `outputs/heartline/<ride>/<segment>-delta.md` — per-axis delta summary, callouts where it matters.

## Notes

- This command is **pre-processor** to `/force-envelope-check`. Run it when the source data is track-frame and any element is banked > 20°.
- `α × r` term is small but real on rapid bank-rate changes (e.g. entry to cobra roll). Don't drop it without justification.
- If centerline data has gaps, interpolate with a cubic spline along `s`, NOT `t`. The two are different because `v(s)` is not constant.
- The heartline offset is operator policy. 1.10 m is a common ASTM convention; 1.05 m is EN. Document which used.
