# /firing-energy-audit

Audit a kiln firing's energy — kWh or therms, soak and cooling losses, electric vs. gas — and convert to CO₂e so the firing footprint (the dominant share) is measured, not guessed.

## Inputs

- Kiln type (electric/gas), interior cubic footage, rated kW (electric) or BTU/h (gas).
- The firing schedule: ramp segments, peak cone, soak/hold duration, and total firing + cool hours.
- A measured kWh (from a meter) if available; the electric tariff or gas price; the grid CO₂e factor.
- Pieces loaded this firing (from `/kiln-load-density`).

## Steps

1. Estimate or read total energy: measured kWh if metered; else rated kW × effective firing hours (elements cycle, so apply a duty-factor < 1 — a controller log gives the real figure).
2. Break out where energy goes: ramp (most), soak/hold (steady draw at temperature), and standing/cooling losses (recoverable only by insulation/scheduling).
3. Convert to CO₂e: electric → kWh × grid factor (state it); gas → therms × ~5.3 kg CO₂e/therm. Compare electric vs. gas on both cost and CO₂e — they can disagree.
4. Compute **energy per piece** = firing energy ÷ pieces loaded. Re-run at the `/kiln-load-density`-optimized load to quantify the per-piece reduction.
5. Recommend the highest-leverage reduction: load density first, then off-peak tariff, tighter cone schedule, element/insulation maintenance, or fuel switch — ranked by kg CO₂e saved.

## Output

`outputs/firing-audit-YYYY-MM-DD.md`: total energy, the ramp/soak/loss breakdown, cost and CO₂e (electric and gas compared), energy-per-piece at current and optimized load, and a ranked reduction plan.

## Notes

- Firing is ~60–90% of a piece's cradle-to-gate footprint, so this audit usually finds the biggest available reduction in the whole studio.
- Always state the grid CO₂e factor and its source/date; an electric kiln on a coal-heavy peaker grid can have a larger footprint than gas.
