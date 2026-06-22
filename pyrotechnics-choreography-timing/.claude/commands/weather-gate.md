# /weather-gate

Build the show-day go/no-go weather decision tree that discharges the `assumed` weather premises in the spec catalog (wind, fallout direction, visibility, lightning).

## Inputs

- The assumptions list from the spec catalog (e.g. `A1: wind ≤ 12 mph SW`).
- Site geometry + the separation/fallout margins from `/separation-proof` (how much wind drift the layout tolerates).
- Permit / NFPA weather limits: max sustained wind, lightning stand-off, visibility/ceiling minimums.
- Max bore in the show (drives apogee/visibility needs).

## Steps

1. Pull each weather assumption from the catalog and the binding regulatory thresholds from `context/references.md` + permit.
2. Translate the separation slack into a **wind envelope**: the max speed and the toward-crowd direction band the discharged FALLOUT proof still holds for.
3. Build the gate tree (see `context/workflows.md` Workflow 5): wind speed cap → wind direction × fallout margin → lightning stand-off → visibility/ceiling for max bore → GO.
4. For each leaf, cite which assumption it discharges and the fallback (reduce max bore, shift positions, HOLD, or NO-GO).
5. Add the show-day logging rule: record actual readings against the envelope; a GO is valid only while readings stay inside the assumed bounds.

## Output

`outputs/weather-gate-YYYY-MM-DD.md`: the go/no-go decision tree with concrete thresholds, the wind envelope the proof depends on, the per-leaf fallback actions, and the reading-log template for the weather call.

## Notes

- The gate is only as good as the separation proof behind it — re-run `/separation-proof` for the worst-case envelope before trusting the wind cap.
- A toward-crowd wind shift is the classic killer; make direction a first-class branch, not a footnote.
- NO-GO and HOLD are valid outputs. The tree exists to make stopping the easy, pre-authorized choice.
