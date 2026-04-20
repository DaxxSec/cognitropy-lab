# Tools & Data Sources

## Public Data Sources (no login)

- NOAA NWS point forecasts (api.weather.gov)
- NOAA HRRR / NAM / NBM model output (nomads.ncep.noaa.gov)
- SNOTEL stations (wcc.sc.egov.usda.gov/nwcc/)
- MADIS aggregator (madis-data.cprk.ncep.noaa.gov)
- MesoWest (mesowest.utah.edu)
- CAIC public observations
- MIN (Mountain Information Network) via Avalanche Canada
- Avalanche Center public products (AAC, NWAC, SAC, etc.)

## Professional / Licensed

- InfoEx (credentialed access only)
- Agency internal telemetry feeds
- Snowpilot pro layer

## Observation Formats

- Snow profile JSON / CAAML XML
- Bulletin data in CAAML avalanche bulletin format
- CSV exports of station telemetry

## Integration Notes

If an MCP server is configured for any of the above, the agent should prefer the MCP over ad-hoc web fetch. See `.mcp.json` if present.
