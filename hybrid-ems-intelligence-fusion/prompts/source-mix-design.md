# Source Mix Design

## Purpose

Use at the start of a new fusion-EMS project (or when a candidate new source becomes available) to decide which sources to integrate first. Forces an explicit cost / value trade-off rather than the default "integrate everything we can reach."

## Prompt Template

```
You are a hybrid-vehicle EMS engineer evaluating which intelligence sources to fuse into a route-aware power-demand prior. Apply this workspace's `concepts.md` source taxonomy and `references.md` default variance priors.

Project context:
- **Vehicle platform:** [HEV / PHEV / MHEV / REEV — architecture, mass class, battery size]
- **Target market region:** [EU / China / North America / Japan / other — coverage of cloud feeds, V2X deployment]
- **Production timeline:** [research / pre-development / B-sample / SOP-1y / SOP-6m]
- **Sources currently integrated:** [list]
- **Sources available but not integrated:** [list with notes on integration cost / latency]
- **Calibration KPI priorities:** [fuel / CO2 / battery wear / drivability — order by importance]

Please:
1. Score each candidate source on (a) expected information value for the priority KPIs given the architecture, (b) integration cost in person-weeks, (c) regulatory / security exposure introduced.
2. Recommend an integration order with explicit go / no-go criteria after each integration.
3. Identify the source(s) that would be highest-leverage at the project's current timeline stage (some sources only justify integration close to SOP; others are research-only).
4. Call out the riskiest source — the one most likely to introduce more noise than signal — and the audit-driven evidence that would justify retiring it.
```

## Expected Output

- Per-source value / cost / risk scorecard with rationale.
- A staged integration roadmap with go/no-go gates.
- A single "highest-leverage next move" recommendation tied to project stage.
- A "watch list" of sources that should be evaluated via `/cycle-replay` against a benchmark drive library before further integration.
