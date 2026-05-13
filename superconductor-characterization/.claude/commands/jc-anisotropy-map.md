# /jc-anisotropy-map

Plan a field-angle Jc(θ, B, T) anisotropy map for an HTS coated conductor or anisotropic LTS sample. Returns a sweep matrix, ramp policy, expected total measurement time, and the queue impact for `/sample-queue-plan`.

## Inputs

- Sample ID, conductor type (REBCO coated, Bi-2212 round wire, Bi-2223 tape, MgB2 wire, Nb3Sn ITER-style strand), critical width (mm), tap separation L_tap (mm)
- Target field set B = {B_1, B_2, …} (T) and temperature set T = {T_1, T_2, …} (K)
- Angle set θ = {0°, 15°, 30°, 45°, 60°, 75°, 90°} (H‖c at 0°, H‖ab at 90°; refine near minima)
- Ic definition: 1 µV/cm (default) or 0.1 µV/cm for high-precision binning
- Quench-protection current limit (A) on the sample stage
- Available rotator (Andeen-Hagerling, in-house): step accuracy and angular settling time

## Steps

1. Build the sweep matrix: |B| × |T| × |θ| points. Estimate per-point time = current ramp (V-I) + dwell + reset = typically 60–180 s.
2. Identify expected anisotropy peaks: for REBCO, sharp Jc maximum at H‖ab (intrinsic pinning); for Bi-2223 multifilamentary tape, broad H‖ab peak and steep drop H‖c. Densify θ-sampling within ±15° of expected peaks (2.5° step) and use coarser 15° steps in flat regions.
3. Define a quench-protection policy: current source compliance, V-trip threshold (typically 100 µV across the tap pair), trip latency (≤10 ms). Recheck the quench-current calculation per (T, B) point.
4. Order the matrix to minimise magnet ramps: fix B, sweep T from highest → lowest; at each T, rotate θ from 0° → 90° (or reverse); only then change B. Rotating under field is much faster than ramping B.
5. Compute total measurement time and helium burn; feed to `/lhe-budget` and `/sample-queue-plan` as a single "high-load" job.
6. Specify reporting: Jc(θ) at each (B, T) plus the angular FWHM of the H‖ab peak; an Ic_min map for engineering use.
7. Cross-reference IEC 61788-4 / 61788-22 (HTS strand and bulk Jc measurement) for reporting compliance.

## Output

Markdown plan at `outputs/jc-anisotropy-plan-<sample-id>-<YYYY-MM-DD>.md`:
- Sweep matrix table with per-point timing
- Expected anisotropy shape and dense-sample regions
- Quench-protection settings
- Total magnet hours, LHe cost, queue impact
- Stretch: a placeholder plot specification (`Jc_vs_theta_byB.png`) the runtime can populate

## Notes

- Current-source compliance must exceed the expected V-trip × cable resistance margin or the trip won't engage.
- For REBCO, a 1° miscalibration of θ near H‖ab can halve the measured Jc — verify rotator zero with a Hall probe on the sample stage before the run.
- Long V-tap separations smooth out local defects (good for engineering Jc) but blur intrinsic Jc; report both if material physics is the question.
- Heating-induced Jc collapse at high field is irreversible if the sample is damaged; if a point trips the V-threshold, halve the ramp rate at the next point, not just at the failed one.
