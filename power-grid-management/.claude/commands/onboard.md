---
description: Initialize the Grid Spatial Analyst workspace — capture role, utility, jurisdiction, current analysis, and available data.
---

# /onboard — Workspace Initialization

Run this the first time the workspace is used, or when a new analyst takes it over.

## What the agent should do

1. **Confirm role.** Ask the user which of the following best fits:
   - Transmission / bulk-power operator or planner
   - Distribution utility engineer or operator
   - DER / interconnection engineer
   - Reliability coordinator or balancing authority staff
   - Vegetation management / wildfire mitigation analyst
   - Grid cyber-physical security analyst
   - Researcher or student
   - Other (capture free-text)

2. **Capture the utility / organization context** without pressing for sensitive specifics:
   - Utility type (IOU, muni, coop, federal, independent operator, research lab, consultancy)
   - Rough geography (ISO/RTO region or country if non-US; not a precise territory)
   - Voltage classes in scope (bulk transmission / sub-transmission / primary distribution / secondary)

3. **Establish experience level.** Map the user's self-description onto L1–L5 from `README.md`. If they're not sure, ask 2–3 calibration questions (e.g., "Can you read a geographical one-line?", "Have you run a load-flow case yourself?").

4. **Capture the active analysis goal.** Examples of what a good goal looks like:
   - "Identify top-10 riskiest distribution feeders by combined vegetation and fire-weather exposure before May 1."
   - "Investigate last Thursday's outage cluster on the 12kV feeder network in the south district."
   - "Propose a map design for our monthly reliability report."
   - "Evaluate whether a proposed 69 kV substation at (lat, lon) is better than the current candidate at (lat, lon)."

5. **Inventory available data.** Ask what the user can bring to the analysis:
   - GIS layers (Shapefile, GeoJSON, GeoPackage, ESRI feature classes)
   - Topology exports (CIM, PSS/E .raw, PSLF, CYME, Synergi)
   - Outage logs (OMS exports with or without geocoding)
   - SCADA / historian exports (time-series with tag metadata)
   - PMU / synchrophasor data
   - Weather / fire-weather feeds (NWS, GOES, NIFC)
   - LiDAR or satellite imagery (for vegetation / corridor analysis)

6. **Flag data-handling posture.** Remind the user about `context/constraints.md`: most utility spatial data is sensitive and should be redacted, aggregated, or sampled before pasting into chat.

7. **Populate context files.** Write the captured information into:
   - `context/role.md` — user profile
   - `context/project.md` — active analysis goal, data inventory, target completion
   - `context/for-agent/environment.md` — any environmental specifics (on-prem GIS, tooling restrictions, etc.)

8. **Offer three realistic first moves** appropriate to the stated goal — e.g. "I can propose a map design; I can walk through a feeder-by-feeder exposure scoring method; I can sketch a SQL query you'd run against your outage management system to geocode uncoded events."

## What the agent should NOT do

- Do not invent a utility or jurisdiction if the user declines to share.
- Do not ask for credentials, passwords, or direct access to any operational system.
- Do not pressure the user into sharing CIP-protected or customer-PII data. Aggregates and samples are fine.
