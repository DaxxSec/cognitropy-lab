# /crystallization-yield

Model the crystallized volume fraction along a real (non-isothermal) thermal path using JMAK, then convert it into a first-pass yield — the quality term in yield-adjusted capacity.

## Inputs

- Kinetic model: Ea, n, K₀ (from `/kissinger-kinetics`).
- The actual **thermal path** at the critical location: a cooling curve (T vs t) from `/cooling-budget`/simulation, or an isothermal hold (T, dwell time) for a TPF step.
- The amorphicity acceptance spec (max allowable crystalline fraction, e.g. X ≤ 2 vol% to pass).
- Lot/run size and gross production rate, if you want the capacity figure.

## Steps

1. Read `context/concepts.md` §4 (JMAK + additivity) and `references.md` for the equations.
2. For an **isothermal** path: X = 1 − exp[−(K(T)·t)ⁿ] directly.
3. For a **cooling/variable** path: apply the additivity (Scheil) rule — integrate the incremental crystallization over the temperature–time history, stepping through the TTT field, accumulating extended volume fraction.
4. Evaluate X at the **slowest-cooling / hottest-dwell location** (worst case) and compare to the acceptance spec → pass/scrap for that part.
5. Translate to **first-pass yield**: estimate the fraction of parts whose worst-case location stays under spec, given process variation (cooling-rate spread, oxygen-driven nucleation-density spread).
6. Compute **yield-adjusted capacity**: good-parts/hr = gross-rate × first-pass-yield. Note the dominant yield-loss driver.

## Output

`outputs/cryst-yield-<alloy>-<process>-YYYY-MM-DD.md`: predicted crystalline fraction at the critical location, pass/scrap verdict vs spec, first-pass yield estimate with its variance driver, and the yield-adjusted good-parts/hr. Cross-link to `/line-throughput` and `/amorphicity-qa`.

## Notes

- The model is only as good as the kinetics — extrapolating K(T) far outside the Kissinger fit range is the most common error. State the valid range.
- Heterogeneous nucleation (oxygen, inclusions) effectively raises the nucleation rate beyond the homogeneous JMAK fit — when oxygen is the driver, treat the kinetic constants as optimistic and route to `/melt-flux-spec`.
- "Surface glassy, core crystalline" means your critical location is the centre — make sure the thermal path is for the centre, not the skin.
