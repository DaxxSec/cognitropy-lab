# /size-grassed-waterway

Size a vegetated waterway so its conveyance capacity carries the design peak runoff with freeboard while keeping mean velocity below the permissible (non-erosive) limit.

## Inputs

- Peak design runoff Qₚ (from `/forecast-runoff-capacity`) and its return period.
- Channel longitudinal grade (%) along the drainageway.
- Vegetation/lining type → Manning's **n** and permissible velocity (`context/references.md`).
- Cross-section preference (parabolic for natural waterways, trapezoidal if constructed).
- Freeboard requirement (default 0.15–0.3 m or per standard).

## Steps

1. Read `context/concepts.md` "Hydraulic capacity fundamentals".
2. Pick a trial cross-section geometry (bottom width / top width / depth) and compute flow area A and hydraulic radius R.
3. Compute conveyance capacity `Q_cap = (k/n)·A·R^(2/3)·S^(1/2)` (k = 1.49 US / 1.0 SI).
4. **Utilization check:** Qₚ/Q_cap must be ≤ 1.0 with the chosen freeboard depth above the design water surface. Iterate geometry until it passes.
5. **Velocity check (governs):** compute mean V = Qₚ/A_flow at design depth; require V ≤ permissible for the vegetation/soil. If V too high, widen/flatten the section or add stepped grade control — do not just deepen.
6. Cross-check with tractive shear `τ = γ·R·S` against permissible shear for vegetated channels (more rigorous than velocity alone).
7. Specify establishment: lining/sod, temporary protection until vegetation establishes, and the retardance class assumed.

## Output

`outputs/waterways/grassed-waterway-<reach>-YYYY-MM-DD.md` — final cross-section, Q_cap, Qₚ/Q_cap utilization, freeboard, mean velocity vs permissible, shear check, and vegetation-establishment notes.

## Notes

- Area capacity can pass while velocity fails — the velocity/shear check, not Q alone, usually governs the width.
- Newly seeded waterways are most vulnerable before vegetation establishes; assume bare-soil permissible velocity for the establishment period or use a temporary blanket.
- Parabolic sections self-form toward stability and pass farm machinery better than trapezoidal.
