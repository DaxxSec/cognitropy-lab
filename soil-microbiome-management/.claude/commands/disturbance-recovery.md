# /disturbance-recovery

Quantify the recovery trajectory after a defined disturbance event (tillage, fumigation, drought, fire).

## Inputs

- Path to a longitudinal sample series spanning pre-disturbance + post-disturbance time points.
- Disturbance type and date.
- Pre-disturbance baseline window definition (≥3 samples before the event).
- Recovery threshold (default: 75% or 90% return to baseline).

## Steps

1. Read `context/workflows.md` "Disturbance Recovery Quantification".
2. Verify the baseline window has ≥3 samples; flag if not.
3. Compute Aitchison distance from each post-disturbance sample to the baseline centroid.
4. Plot distance vs. time-since-disturbance.
5. Fit a recovery curve:
   - Saturating exponential: `D(t) = D_∞ + (D_0 - D_∞) · exp(-t/τ)`
   - Pure exponential decay: `D(t) = D_0 · exp(-t/τ)`
   - Choose by AIC or eyeball; saturating is the default for ecological recovery.
6. Compute time-to-X% recovery (default X = 75%, 90%) and asymptote D_∞.
7. Bootstrap 95% CI on τ, X% recovery time, and D_∞.
8. Compare across treatments / sites if multiple are present: parallel curves with shared asymptote vs. divergent trajectories.

## Output

A markdown file `outputs/recovery-<event>-YYYY-MM-DD.md` containing: disturbance summary, baseline window, distance-vs-time plot description, fitted curve parameters with 95% CI, X% recovery time, asymptote interpretation (full recovery vs. regime shift), and any cross-treatment comparisons.

## Notes

- Curve doesn't saturate within the observation window → either extend sampling or report a linear segment with explicit caveats; do not extrapolate beyond observed range.
- Asymptote ≠ baseline → the system has shifted to a new stable state ("regime shift"); quantify the shift, do not call it incomplete recovery.
- Recovery faster than the sampling cadence → cadence was too sparse for this disturbance class (see `context/concepts.md` for typical recovery time-scales by disturbance type).
- Per `context/concepts.md`: drought rewetting recovery is fast (Birch effect, days); fumigation recovery is slow (months); tillage homogenisation recovery is intermediate (weeks-months) but AMF recovery is years.
