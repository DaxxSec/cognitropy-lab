# Agent Environment Notes

## Primary Interface
This workspace is designed for use in the field or at a basecamp setup. The operator may be:
- At a computer before/after a field session (full typing capability)
- On a phone via Claude mobile (shorter input; prioritize concise outputs)
- Dictating notes (output should be structured for quick editing)

## Tool Integrations (Optional)
If the operator has these tools available, leverage them:

- **iNaturalist API** — for cross-referencing species observations
- **EDDMapS** — Early Detection & Distribution Mapping System for invasives
- **GBIF** — Global Biodiversity Information Facility
- **USDA PLANTS Database** — authoritative for US native/non-native status
- **Gaia GPS / onX** — if exporting waypoints or track files
- **iMapInvasives** — state-level invasive reporting network

## Data Formats
- Field observations: prefer markdown tables with GPS coords, date/time, habitat
- Species records: follow iNaturalist observation format for compatibility
- Reports: use EDDMapS-compatible structured format when possible
- Maps: accept KML, GPX, or coordinate pairs (lat/long decimal degrees)

## Agent Behavior Notes
- When species confidence is < 80%, ALWAYS request more distinguishing features
- When an anomaly could indicate a new invasive incursion, flag with HIGH PRIORITY
- Always include a "verification recommended" note for consequential decisions
- Adjust output verbosity to context: field notes = terse; reports = comprehensive
- Use metric/imperial based on operator's stated preference (default: both)

## Offline Context
The agent should be able to function with pre-loaded reference data when the operator
has no internet access (common in deep wilderness). Key offline resources are in
`resources/` — reference them directly when needed.
