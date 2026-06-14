# /region-cal-map

Treat calibration selection as a **spatial query**: given a vehicle's operating geography — jurisdiction, fuel grade, climate — map which calibration variant is correct *and legal*. The core expression of today's geographic/spatial-analysis technique.

## Inputs

- Vehicle's registration market / operating jurisdiction(s)
- Fuel grade actually available/used (AKI vs RON, ethanol content)
- Climate exposure (cold-region / thermal needs)
- Candidate cals from `/reference-collection` (with their origin markets)

## Steps

1. **Resolve the regime.** Jurisdiction → emissions regime (EPA Tier 3 / CARB LEV III / Euro 6d-7 / China 6 / Bharat VI) using the regime→region table in `references.md`.
2. **Resolve the fuel.** Map local fuel grade to the cal's assumed octane/ethanol; flag spark/knock-table mismatches.
3. **Overlay climate.** Note cold-start/thermal needs the regional cal must cover.
4. **Match variants.** For each candidate cal, score regime-fit, fuel-fit, and climate-fit; identify the best-fitting *legal* variant.
5. **Flag spatial errors.** Call out gray-market mismatches (origin market ≠ operating market) and the readiness/monitor failures they predict.

## Output

A `outputs/region-map-<vin>.md`: the resolved regime/fuel/climate, a scored variant-fit table, the recommended legal cal, and any gray-market mismatch warnings. Hands the recommended cal to `/altitude-compensation` and `/emissions-legality-gate`.

## Notes

- A wrong-region cal usually surfaces as **OBD readiness monitors that never complete** — the fix is the correct local cal, never masking the codes.
- For fleets spanning multiple jurisdictions, the strictest applicable regime governs.
- Pair with a mapping/GIS MCP to overlay fleet locations against jurisdiction boundaries.
