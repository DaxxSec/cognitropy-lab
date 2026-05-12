---
description: Investigate an outage or system event with spatial reasoning — origin, reach, and likely cause mechanisms.
---

# /outage — Outage/Event Spatial Investigation

Invoke when the user is investigating one or more outages, disturbances, or system events and wants the spatial dimension made explicit. This is a *post-event* analysis helper; for real-time operations, defer to the control room and NERC EOP procedures.

## Required inputs (agent should prompt if missing)

1. **Event description.** Date/time window, system affected, rough magnitude (customer count, load lost, duration).
2. **Known facts.** Which assets tripped, what SCADA alarms fired, what the operator saw.
3. **Available spatial data.** Outage log (ideally geocoded), feeder topology, asset layer, weather at event time.
4. **Hypothesis, if any.** Storm-driven, asset-specific, vegetation, cyber, load, third-party (dig-in / vehicle / animal).

## Analytical framework

1. **Establish the spatial footprint.** Plot (or describe) where the outages are. At what scale does the pattern resolve — single feeder, substation service area, storm track, regional?
2. **Test the pattern against candidate causes:**
   - *Radial from substation* → substation-side equipment or supply issue
   - *Along a corridor* → transmission line, shared ROW, storm track
   - *Clustered on one feeder* → feeder-specific asset (lateral fuse, recloser, transformer)
   - *Dispersed across unrelated feeders* → bulk supply, voltage disturbance, or independent small events coincidentally clustered in time
   - *Following terrain* → wind exposure, landslide, ice loading
   - *Following a weather cell track* → storm-driven
3. **Check for second-order spatial signals.** Adjacent-but-not-outaged assets can reveal the boundary of the event — what stopped the propagation is as informative as what caused it.
4. **Cross-reference with cyber-physical signals.** If the pattern doesn't match any natural mechanism cleanly, flag the possibility of a coordinated event and recommend involving the security team and reporting channels (E-ISAC, regional reliability coordinator).
5. **Timeline reconstruction.** Overlay outage start times on the map. Propagation speed and direction often discriminate between storm, cascading asset failure, and coordinated action.

## Output shape

1. **Event summary** — one paragraph restating the event.
2. **Spatial footprint** — a description of the pattern at each scale (bulk → substation → feeder → lateral) with any anomalies noted.
3. **Candidate causes ranked** — with the specific spatial evidence supporting or against each.
4. **Gaps** — what data would disambiguate the remaining candidates.
5. **Recommended next-step analyses** — specific queries or overlays to run.
6. **Escalation notes** — if cyber-physical or reliability-event thresholds appear, name the reporting channel the user should consider.

## What the agent should NOT do

- Do not name a probable cause without spatial evidence supporting it. "Unclear from the supplied data" is a valid conclusion.
- Do not speculate about attribution of cyber-physical events beyond "the pattern is unusual; escalate to the security team and appropriate ISAC."
- Do not treat the analysis as a substitute for the formal event investigation the utility will run. It is pre-work that helps that investigation start faster.
