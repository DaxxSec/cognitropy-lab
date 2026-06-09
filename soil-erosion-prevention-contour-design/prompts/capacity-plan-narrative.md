# Capacity-Plan Narrative

## Purpose

Use this to turn a set of structure sizing outputs into a stakeholder-readable capacity-planning narrative: demand, capacity, utilization, headroom, bottleneck, and residual risk, in plain language tied to the numbers.

## Prompt Template

```
You are an erosion-control agent. Read context/concepts.md "The capacity-planning analogy".
Synthesize the sizing outputs in outputs/ into a capacity-plan narrative.

- **Structures designed:** [list — terraces, waterway, basin, check dams, etc.]
- **Design return period (service-level target):** [e.g. 10-yr, 24-hr]
- **Sizing artifacts to draw from:** [paths in outputs/]
- **Audience:** [landowner / agronomist / reviewing engineer / cost-share agency]

Please:
1. For each structure, state demand, capacity, utilization (demand/capacity), and headroom in one line.
2. Identify the system bottleneck (highest utilization) and explain why it governs.
3. State the residual (above-design) risk and whether a safe overflow path exists.
4. Frame the maintenance cadence as capacity refresh, with the cost of deferral.
5. Close with a one-paragraph adequacy verdict for the stated audience.
```

## Expected Output

- A per-structure demand/capacity/utilization/headroom summary table.
- A named bottleneck with the reasoning.
- An explicit residual-risk statement at storms above the design return period.
- The maintenance-as-capacity-refresh framing and a plain-language adequacy verdict.
