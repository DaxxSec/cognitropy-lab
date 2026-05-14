# /banking-curvature-tune

Loop the `B-*` tuning workflow (`context/workflows.md` §5) to bring lateral-g back into envelope by adjusting bank-angle and curvature, without sacrificing the element's speed budget.

## Inputs

- `failing_segment` — the segment that failed `F-3` in `/force-envelope-check`.
- `centerline_csv` — `s, x, y, z, bank` plus a `kappa(s)` field if available; otherwise compute κ from the centerline.
- `velocity_profile` — `v(s)` table.
- `alpha` — relaxation factor for the tune loop, default 0.55. Range [0.4, 0.7].
- `clearance_map` — optional table of support-column proximities to the track to gate B-4.

## Steps

1. `B-0` intake. Confirm the failure is lateral-axis (this command does not address vertical exceedances).
2. Compute `θ_ideal(s) = atan(v(s)² · κ(s) / g)` (`B-1`).
3. Compute `Δθ(s) = θ_ideal(s) - θ(s)` (`B-2`).
4. Identify `s` with `|Δθ| > 30°` and STOP if any (`B-2-a`): a 30°+ correction is no longer a tune.
5. Build `θ'(s) = θ(s) + α · Δθ(s)` (`B-3`).
6. Check secondary effects (`B-4`): does `θ'` change the height profile? Does it move the train into a support column?
7. If clean, emit the proposed banking profile and a linear-approximation estimate of post-change lateral-g (`B-5`).
8. Persist to `outputs/banking-tunes/<segment>-iter<n>-<YYYYMMDD>.md`.
9. Recommend re-running `/heartline-analysis` + `/force-envelope-check` against the new profile. If still failing, increment iteration and repeat with `alpha` toward the top of the range.

## Output

Markdown plus optional centerline CSV with the tuned `bank` column:
- Iteration number, `alpha` used.
- Pre / post bank profile plot (or table).
- Predicted post-tune lateral-g (linear approx).
- Flag for re-survey / structural review if B-4 fired.

## Notes

- The loop is **deliberately conservative** — 0.55 default `alpha` prevents over-correction that would over-shoot into the opposite-direction lateral exceedance.
- The linear approximation is for triage only. Final acceptance always requires full re-simulation.
- A successful B-5 does not authorise retracking; it authorises **proposing** the retrack to engineering. The PE-of-record retains acceptance authority.
- If iteration 3 still fails with `alpha = 0.7`, the geometry of the element is the problem (radius too small for the speed). Recommend speed reduction (lift-hill height trim) or full element redesign.
