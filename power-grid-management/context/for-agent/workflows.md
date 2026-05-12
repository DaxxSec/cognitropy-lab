# Canonical Spatial-Analysis Workflows

This document gives Grid Spatial Analyst a catalog of the most common workflows it will be asked to run. Each is a template — not a rigid sequence — that the agent adapts to the user's question and available data.

---

## 1. Vegetation + Fire-Weather Exposure Scoring

**When to use:** Prioritizing rights-of-way for clearing, setting PSPS triggers, supporting FAC-003 vegetation management compliance in wildfire-prone regions.

**Inputs:** Transmission / distribution line geometry, canopy height model (LiDAR-derived, typically a raster), fire-weather layer (Red Flag days, fuel moisture, NIFC), ROW width by voltage class.

**Method outline:**
1. Project all layers to a common projected CRS (state plane or UTM).
2. Buffer the line geometry by ROW half-width to get the corridor polygon.
3. Run zonal statistics of the canopy height raster within each buffer — extract max and mean height, and count of cells above a threshold (e.g., 15 ft within striking distance).
4. Sample the fire-weather raster within the same buffer — mean of the top-10th-percentile day values over the season.
5. Normalize each factor (z-score or min-max across the set of buffers).
6. Combine with explicit weights (e.g., 0.6 vegetation, 0.4 fire-weather) into a composite score.
7. Rank. Visualize as a sequential-ramp corridor map (see `/map`).

**Caveats:** Tree species matters — a 30 ft eucalyptus is not the same risk as a 30 ft maple. Composite scores hide trade-offs; always show the component factors in the output, not just the composite.

---

## 2. Outage Pattern Spatial Investigation

**When to use:** Post-event review, storm debrief, recurring reliability complaint from a customer or regulator.

**Inputs:** Outage log (start time, duration, customers affected, ideally geocoded; otherwise feeder / transformer reference), feeder topology, asset layer, weather at event time (NWS storm reports, lightning density).

**Method outline:** See `.claude/commands/outage.md` for the full framework. Key steps:
1. Geocode the outage log if it isn't already (join on transformer / pole ID, fall back to feeder centroid for ungeocoded entries with a clear caveat).
2. Plot outages at 3 scales: territory-wide, per-substation, per-feeder.
3. Test the pattern against candidate causes (radial from substation, along a corridor, clustered on one feeder, dispersed).
4. Overlay outage start times to build a propagation animation (conceptually — the agent doesn't animate, but describes what the animation would show).
5. Compare to weather overlay if applicable.

**Caveats:** Ungeocoded outages cluster at feeder centroids and create false patterns. Always separate geocoded from ungeocoded in any density map.

---

## 3. Contingency Reach Mapping

**When to use:** Storm preparation, planned outage coordination, resilience study.

**Inputs:** Transmission or distribution topology with switch states, customer counts per delivery point.

**Method outline:**
1. Build the network graph (nodes = substations/buses, edges = lines/transformers/switches).
2. Remove the contingency element(s). Compute connected components.
3. For each component, sum customer counts / load.
4. Identify components without generation → these are outaged customers.
5. Identify alternate supply paths (normally-open ties that could be closed for restoration).
6. Map the result as a choropleth of customer impact by feeder/substation.

**Caveats:** Connectivity-only analysis does not check thermal or voltage limits — pass the short list to a load-flow tool for the top contingencies before drawing operational conclusions.

---

## 4. Substation Siting

**When to use:** Load growth area needs a new distribution substation; evaluating candidate sites.

**Inputs:** Load density (forecast) as a raster or polygon layer, existing substation locations and capacities, candidate site polygons (from land-use constraints), transmission supply points, environmental constraint layers (wetlands, endangered species habitat, floodplain, tribal lands).

**Method outline:**
1. Compute service area of each candidate under a simple nearest-substation (Voronoi) assumption.
2. Sum forecast load inside each candidate's service area → forecast loading.
3. Compute line length from the candidate to the nearest suitable transmission supply point (weighted by terrain if known).
4. Overlay environmental constraints as hard exclusions.
5. Score candidates on: (load served) ÷ (distance to supply) × (1 − constraint penalty).
6. Present top 3 with trade-off notes.

**Caveats:** Voronoi service-area assumption ignores feeder capacity and network ties. For a real siting study, the distribution planning group would use its planning tool. This workflow is a screening step.

---

## 5. PMU / Phasor Disturbance Propagation

**When to use:** Reconstructing the spatial spread of a system disturbance (e.g., frequency or voltage event).

**Inputs:** PMU time-series exports (phase angle, frequency, voltage magnitude) with coordinates, event time, topology.

**Method outline:**
1. Align all PMU time series to a common timebase.
2. Identify the first PMU to register the disturbance signature.
3. Measure the arrival time at each subsequent PMU relative to the first.
4. Map arrival time vs. distance (both electrical and geographic) to see whether the propagation is consistent with an electromechanical wave, a local oscillation, or a coincidental multi-location event.
5. Overlay on topology to identify the likely origin region.

**Caveats:** PMUs are sparsely deployed on some systems — the origin region may be *between* PMUs and not directly observed. Do not overclaim precision.

---

## 6. Cyber-Physical Incident Geolocation

**When to use:** Correlating a cyber event, alarm anomaly, or physical intrusion report with asset geography.

**Inputs:** Event report (time, type, source asset or IP, source / indicator), asset layer with network/cyber attributes (IP, SCADA RTU ID, substation), service territory.

**Method outline:**
1. Locate the reporting asset (or its RTU / controller) on the map.
2. Identify the blast radius — which substations / feeders / customers depend on it for operational visibility or control.
3. Overlay CIP-covered asset layer (handle with sensitivity).
4. Correlate the event timeline with any operational anomalies (SCADA alarms, protective relay operations, OMS events) in the same footprint.
5. Escalate per utility procedure — E-ISAC, regional reliability coordinator, or internal SOC.

**Caveats:** This is *pre-work* for the formal investigation, not a substitute. Always route through the utility's incident response process.

---

## Session Workflow: A Typical Analysis

1. **Open.** Agent reads `context/role.md` and `context/project.md`, checks `work-log/session-log.md` for the last session's status.
2. **Clarify.** Agent restates the active question and asks what's new since last time.
3. **Plan.** Agent proposes a method tailored from one of the workflows above.
4. **Execute or advise.** For things the agent can do in chat (reason about topology, propose a map design, draft a method document), it does them. For things requiring the analyst's tooling, it writes an executable runbook.
5. **Capture.** Session ends with the agent offering to log the session in `work-log/session-log.md` and update `context/project.md`.
