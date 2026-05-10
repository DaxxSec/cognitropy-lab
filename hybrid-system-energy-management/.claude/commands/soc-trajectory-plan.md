# /soc-trajectory-plan

Plan the SOC reference trajectory for a known route — PHEV utility-factor weighting + the CS-mode setpoint.

## Inputs

- Route definition (start/end, distance, elevation profile, anticipated traffic).
- PHEV battery usable energy (kWh) and electric-only range estimate.
- Trip-length posterior (mean + variance, or a categorical over short / medium / long).
- Driver-class posterior (calm / sport / urban-stop-go).

## Steps

1. Read `context/concepts.md` for the CD vs. CS distinction and SAE J2841 utility factor framing.
2. Compute the expected CD distance under the trip-length posterior — this sets where SOC nominally hits the CS setpoint.
3. Decide CD policy: pure depletion (favours efficiency on short trips) vs. blended (favours total trip if posterior tail is long).
4. Set CS-mode SOC band (typical 30-50% with 5% hysteresis).
5. Account for elevation: pre-charge before climbs, allow regen capacity before descents — explicit reservation logic.
6. Validate against trip-length posterior tails — the policy should not collapse on the 10th-percentile longest trip.

## Output

A markdown file `outputs/soc-trajectory-YYYY-MM-DD.md` containing: trip posterior summary, chosen CD policy, CS band setpoints, elevation-aware adjustments, and a small ASCII sketch of (distance, SOC) over the expected route.

## Notes

- Map data resolution matters — 1 km elevation samples lose hill detail; 100 m samples capture them.
- PHEV utility factor (SAE J2841) is region-specific (US vs. EU vs. China) — use the regional curve.
- Never hard-clip SOC at exactly 0% or 100% in the reference; the controller will fight the cell-protection thresholds.
