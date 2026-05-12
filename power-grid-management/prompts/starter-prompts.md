# Starter Prompts — Power Grid Management

Copy, adapt, and use these to kick off focused sessions with Grid Spatial Analyst.

---

## Onboarding

```
/onboard

I'm a distribution reliability engineer at a mid-sized IOU in the PJM footprint.
Main voltages we operate are 69 kV sub-transmission and 12 kV distribution.
My job for the next quarter is to produce a ranked list of feeders that should
get investment in undergrounding or reclosers based on outage history and
customer density. I have access to our OMS, our GIS (ArcGIS Pro), and SCADA
historian. No direct access to CYME but our planning group runs it.
```

```
/onboard

I'm a grid cyber analyst transitioning from IT security. I need to understand
the geography of our bulk system well enough to correlate cyber events with
operational impact. No GIS background — strong Python, know networkx. Utility
is a federal PMA with extensive 230/500 kV transmission.
```

---

## Vegetation and Fire

```
/analyze

Goal: rank our 115 kV ROW segments by combined vegetation + fire-weather
exposure for the upcoming wildfire season.
Scope: one of our divisions (~800 miles of 115 kV).
Data available: ROW centerline in an ESRI feature class (ROW_115kV_v2024),
LiDAR canopy height raster (2 m, from last year's flight), NIFC fire-weather
index raster (seasonal mean).
Decision: informs our Q3 clearance crew scheduling and capital plan for
resilience retrofits.
```

```
/map

I need a single-page leave-behind for our executive team showing which of
our 10 substation service areas saw the worst storm performance in the Feb
2026 ice event. Audience: CFO + COO. Medium: letter-size PDF.
```

---

## Outage Investigation

```
/outage

Event: Thursday evening (2026-03-05) between 19:40 and 20:25 we saw 47
distribution events clustered in the south-east district, ~9,800
customer-outage-minutes total.
Known facts: no storm activity; feeder breakers on two 12 kV feeders fed
from different substations operated within a ~6-minute window.
Data: OMS export (geocoded), feeder topology, SCADA alarm export, weather
(nothing notable).
Any hypothesis: no obvious one — asking you to help think through what
pattern this is.
```

---

## Contingency and Topology

```
/topology

If we lose the 230 kV double-circuit between substations DELTA and EPSILON,
which parts of our service territory are electrically isolated from the
bulk system? We have a small hydro plant at ECHO (12 MW) — does it anchor
any island with sufficient load to be viable?

Data: CIM export of the transmission and sub-transmission, 2026 peak-load
case. Happy to paste a node-edge list if easier.
```

---

## Interconnection / Siting

```
/analyze

Goal: screen 5 candidate sites for a new 200 MW battery storage facility
that needs 230 kV interconnection in our south zone.
Scope: 5 candidate polygons (attached), existing 230 kV supply substations,
environmental constraint layers from state DEQ.
Decision: short-list for the developer to take into detailed study.
```

---

## Cyber-Physical

```
/outage

Security team flagged anomalous Modbus traffic on the RTU at Substation
GAMMA between 02:14 and 02:33 UTC, no operational impact logged. I'd like
to understand: what does GAMMA control, how far does its footprint extend
electrically and geographically, and are there correlated operational
events in the same window I should look for?
```

---

## Quick Reference Questions

```
Question: what's the standard NERC CIP-014 sampling process for identifying
"critical" substations? (L3 depth is fine.)
```

```
Question: in ArcGIS Pro, what's the cleanest way to attach a feeder ID to
outage points that only carry a pole ID, when I have a poles-to-feeders
cross-reference table?
```
