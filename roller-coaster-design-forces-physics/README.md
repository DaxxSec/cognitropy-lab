# Roller Coaster Design Forces Physics Workspace

> A ride-dynamics workspace for triaging roller coaster forces — g-loads, jerks, restraint demands — against ASTM F2291 / EN 13814 envelopes using explicit decision trees.

## What This Workspace Does

Roller coaster forces sit at the intersection of multibody dynamics, biomechanics, and safety regulation. A single 0.4-second airtime spike, a poorly-banked transition, or a 0.3g lateral kick on the wrong vertebra can turn an enthusiastic ride into a head-banging review or a Serious Bodily Injury report. This workspace gives an engineer (or a safety auditor walking the manufacturer's data) a deterministic, **decision-tree-driven** way to triage each track segment from the simulator output:

- **Force-envelope decision tree** — vertical, lateral, longitudinal, sustained vs. transient, peak vs. duration-weighted — keyed off ASTM F2291 §6.4 limit curves and EN 13814 Annex G.
- **Restraint-class decision tree** — derives the minimum restraint family from inversion presence, peak negative-g, and lateral-g signature, anchored to the IAAPA Ride Restraint Standard categories.
- **Jerk-budget decision tree** — third-derivative audit for the transitions where helmets get cracked: pullout-to-airtime, airtime-to-curve, brake-to-turntable.
- **Incident triage tree** — walk a rider complaint or sensor event through a nuisance / monitor / hold / pull-from-service bin.

The "with decision tree triage workflows" technique is what shapes this workspace: instead of one big "review the ride" command, every analytical command is a *named tree* with named nodes, so the verdict is always **explainable and auditable**.

## Why This Workspace Exists

Force review tends to live in spreadsheets, simulator screenshots, and engineering judgment. That works fine until an incident, at which point reviewers want to know: which node of which tree said this was acceptable? This workspace formalises those trees so each verdict carries provenance — `node L-3-b: lateral 1.18g @ 1.4s @ 1.1m heartline → REWORK` rather than `"reviewed and approved"`. It also fits the entropy of the daily-build series: roller coaster physics is a low-volume, high-stakes domain whose vocabulary (heartline, OTSR, jerk-limit, airtime-pop) doesn't carry over to any other workspace, which is exactly the point.

## Getting Started

### Prerequisites

- Force-vs-time export from a ride simulator (NoLimits 2, Newton 2, RideTracker, MATLAB multibody, in-house Python — anything with `t, ax, ay, az` columns).
- Optional: track centerline + banking + speed profile (CSV or `.nl2elem` export) for `/heartline-analysis`.
- Familiarity with ASTM F2291 §6 and EN 13814 Annex G. PDFs are paywalled; cite the section, not the body text.
- A simulator or telemetry source that reports forces in a known frame (track or heartline) — undocumented frame is a `REJECT` at the door.

### Quick Start

1. Drop your force-vs-time export into `outputs/inbox/<segment-id>.csv` (or pass it inline).
2. Run `/force-envelope-check segment=<id> frame=<track|heartline> standard=ASTM-F2291` to walk the envelope tree.
3. Run `/restraint-class-decide` with the inversion list and the negative-g floor from step 2 to lock the restraint class for the element.
4. Run `/jerk-budget-audit` over the transition window flagged by step 2 to catch head-banging risk the envelope check misses (the envelope cares about peaks; the jerk audit cares about *slopes*).
5. If a complaint or sensor event appears, run `/incident-triage` instead of starting at envelope — incident triage routes back into envelope-check only when warranted.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/force-envelope-check` | Walks the ASTM/EN envelope decision tree across the force trace. | First pass on any new segment, new train, or modified element. |
| `/restraint-class-decide` | Derives minimum restraint class from inversion + negative-g + lateral-g. | Before specifying a train, after any inversion-adding modification. |
| `/heartline-analysis` | Translates track-frame forces to heartline-frame for a 1.1 m sternal-notch reference. | Whenever a sim reports track-frame only, or a curve is banked aggressively. |
| `/jerk-budget-audit` | Audits third-derivative profile across transitions. | After envelope check flags a "borderline pass" — jerk is where borderline passes fail. |
| `/incident-triage` | Bins a rider complaint or sensor event into nuisance / monitor / hold / pull-from-service. | Front-line response to a force-related complaint or anomaly. |
| `/banking-curvature-tune` | Suggests bank-angle and curvature changes to fit lateral-g inside envelope. | After a `REWORK` verdict on a lateral exceedance; before re-simulating. |

## Directory Structure

```
roller-coaster-design-forces-physics/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # Six bespoke commands for force triage
├── context/
│   ├── concepts.md           # Heartline, force envelopes, restraint classes
│   ├── workflows.md          # The decision trees themselves
│   └── references.md         # Limit tables, standards index, sim output columns
├── prompts/                  # Element design review, post-mod re-sim, audit writeup
└── outputs/                  # Force traces, decision-tree walks, audit findings
```

## Example Use Cases

### Pre-shipment validation of a new manufacturer simulator pack
The manufacturer delivers an `.nl2elem` + force CSV per element. Run `/force-envelope-check` across all 47 segments, batch the verdicts, and produce a single rework list for elements with `REWORK` or `REJECT` nodes.

### Restraint downgrade investigation
The operator wants to move a family coaster from OTSR to lap-bar to improve throughput. Feed the negative-g and inversion data to `/restraint-class-decide`; the decision tree either greenlights the downgrade or names the specific element that locks OTSR in.

### Whiplash complaint cluster
Five guests report neck pain on a specific element. `/incident-triage` bins the complaint; if it routes to `monitor`, `/jerk-budget-audit` then re-examines the transition window to spot the jerk spike envelope-check missed.

### Modification re-validation after retracking
Track section is repoured with a slightly different curve. `/heartline-analysis` recomputes forces at the rider's chest; `/banking-curvature-tune` proposes bank tweaks if lateral-g now exceeds envelope.

## Recommended MCP Servers

- **filesystem MCP** — pull force CSVs out of `outputs/inbox/` and shove decision-tree walks back into `outputs/walks/`.
- **python-exec MCP** (or any sandboxed numeric runner) — `/jerk-budget-audit` needs a numeric derivative pass; pure-LLM differentiation of noisy traces is unreliable.

## Legal & Ethical Considerations

- **Advisory, not approval.** Outputs do not replace a licensed Professional Engineer's stamped review nor AHJ acceptance under ASTM F770 / F893 / F1193 lifecycle. Treat verdicts as a structured first pass.
- **In-house limits override published limits when stricter.** Never relax a limit to fit an element; redesign the element.
- **Incident data is sensitive.** Rider medical detail in `/incident-triage` should be de-identified before being saved to `outputs/`; keep PHI / PII out of the workspace.
- **Do not extrapolate beyond the envelope.** ASTM F2291 limit curves are calibrated for typical guest demographics; pediatric, geriatric, and pregnancy carve-outs are operator policy, not engineering judgment.

## Technical References

- [ASTM F2291 — Standard Practice for Design of Amusement Rides and Devices](https://www.astm.org/f2291-23.html) — primary force envelope source (paywalled).
- [EN 13814:2019 — Safety of amusement rides and amusement devices](https://standards.iteh.ai/catalog/standards/cen/65a6c39d-7f64-470a-86fb-c00d4b1da9d3/en-13814-1-2019) — European limit framework.
- [IAAPA Ride Restraint Containment Guidelines](https://www.iaapa.org/safety-and-standards/safety-resources) — restraint family taxonomy.
- [Pfeiffer / Brake / Jerk in Coaster Design — Erlebnis Karten Verlag whitepapers](https://www.coasterforce.com/forums/threads/jerk-and-acceleration.40927/) — community-curated jerk literature.
- [No Limits 2 element export format reference](https://www.nolimitscoaster.com/) — `.nl2elem` schema for centerline + banking.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
