# /use-phase-energy-balance

Compare the use-phase energy of an SMA device against its conventional alternative, and find the environmental payback point — does the actuation-phase story redeem (or worsen) the high embodied energy?

## Inputs

- The SMA device function and duty cycle: actuations per day, stroke, work per actuation, on-time, and the heating method (Joule heating current/voltage or ambient thermal).
- The conventional baseline it replaces (solenoid, DC motor + gearbox, wax actuator, bimetal) with its energy draw and mass.
- Service lifetime (years and cycles) and the grid carbon intensity of the use location.

## Steps

1. Read `context/concepts.md` on SMA actuation thermodynamics: the transformation is driven by latent heat, so electrical-to-mechanical efficiency is **low (a few percent)**, but work density and part count are excellent.
2. Estimate per-actuation energy: Joule heating energy to raise the element through Af plus the latent heat, divided by the duty cycle; account for cooling time limiting bandwidth.
3. Compute lifetime use-phase energy and GWP for both the SMA device and the baseline, using the location's grid intensity.
4. Pull the cradle-to-gate burden from `/lca-cradle-to-gate` for both, and compute the **net** cradle-to-gate-plus-use comparison.
5. Find the **break-even**: at what cycle count (if ever) does the SMA device's total footprint fall below the baseline's — i.e., does part-count/weight reduction or use-phase savings repay the embodied-energy premium?
6. State the verdict honestly: SMA can win on compactness, silence, and reliability, but a frequently-Joule-heated actuator may *never* beat an efficient motor on energy alone. Say so when that's the answer.

## Output

`outputs/use-phase-balance-<device>-YYYY-MM-DD.md`: per-actuation energy, lifetime use-phase energy/GWP for both options, the combined cradle-to-gate-plus-use comparison, the break-even cycle count (or "no break-even"), and the qualitative trade-offs (mass, NVH, reliability).

## Notes

- Low actuation efficiency is intrinsic — don't hide it. The honest case for SMA is usually system-level (fewer parts, less weight, no gearbox), not raw energy efficiency.
- Cooling is the bandwidth bottleneck and can dominate cycle time and parasitic power for forced-cooling designs — include it.
- Use the actual use-location grid intensity; a clean grid changes the verdict.
