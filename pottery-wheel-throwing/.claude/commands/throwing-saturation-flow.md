# /throwing-saturation-flow

Estimate the saturation flow rate (max sustainable pieces/hour) of each studio stage and find the practical bottleneck — the first diagnostic for any flow problem.

## Inputs

- Stage inventory: number of wheels, drying capacity (pieces it holds + dry time), trimming benches, kiln(s) with pieces-per-firing and cycle hours.
- Measured or logged per-stage durations for the representative form(s).
- The studio's actual demand (pieces wanted per week) for comparison.

## Steps

1. For each **serial** stage (wheel, trimming): `s = 60 / active_minutes_per_piece` pieces/hour, times the number of stations.
2. For each **passive** stage (drying): effective rate `s = capacity / dry_time` — a rack holding 40 pieces that dry in 12 h passes ~3.3 pieces/h.
3. For each **batch** stage (kiln): `s = pieces_per_firing / cycle_hours` (load + ramp + soak + cool + unload). This is usually the lowest number.
4. Compute degree of saturation `X = demand / capacity` per stage; rank. The highest X (and any X > 1) is the bottleneck.
5. Sanity-check against observed reality — where does greenware actually pile up? The math should agree with the physical queue.

## Output

`outputs/saturation-flow-YYYY-MM-DD.md`: a per-stage table (saturation flow, capacity, X), the identified bottleneck, and a one-line recommendation routing to `/kiln-load-density` (if kiln-bound) or the appropriate stage fix.

## Notes

- Measured saturation flow beats textbook — log three real sessions before trusting a number.
- The kiln being the bottleneck is the expected, not the surprising, result; the value is quantifying *by how much* so the capacity decision is grounded.
