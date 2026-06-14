# /altitude-compensation

Verify that fueling, spark, boost, and thermal behaviour are correct across the vehicle's operating **elevation band** — a spatial analysis of the barometric (BARO) compensation maps. The vertical axis of today's geographic technique.

## Inputs

- The vehicle's operating elevation band (min/max metres), single-site or fleet-wide
- The candidate cal's BARO/altitude compensation tables (fuel enrichment, spark, boost limit, fan/thermal)
- (Optional) a high-altitude variant from `/reference-collection`

## Steps

1. **Define the band.** Establish min/max elevation from operating geography (use the altitude-band table in `references.md`).
2. **Pull the compensation tables.** Locate BARO-indexed fuel, spark, boost-limit, and thermal/fan tables in the candidate cal.
3. **Check coverage.** Do the table breakpoints span the actual band, or does the vehicle operate *off the edge* of the map (extrapolation risk)?
4. **Compare variants.** Where a dedicated high-altitude cal exists, compare its compensation against the candidate across the band.
5. **Recommend.** Variant or documented legal correction whose compensation actually covers the band; flag any lean-at-altitude or over-boost risks.

## Output

A `outputs/altitude-<vin>.md`: the elevation band, BARO-table coverage assessment, variant comparison, and a recommendation with explicit risk flags for the uncovered range.

## Notes

- **Operating off the edge of a BARO map** is a real danger — fixed sea-level cals can run lean or over-boost at altitude.
- For a single fixed high-altitude site, a dedicated high-altitude cal usually beats a sea-level cal leaning on compensation.
- Altitude interacts with fuel grade (high-altitude US "regular" can be 85–86 AKI) — cross-check with `/region-cal-map`.
