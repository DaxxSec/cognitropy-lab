---
description: Explore grid topology questions — contingencies, islanding, electrical vs. geographic distance, connectivity.
---

# /topology — Grid Topology Exploration

Invoke when the user wants to reason about connectivity, contingencies, islanding, or the relationship between electrical and geographic distance. The agent works from a topology the user supplies — it does not invent a grid.

## Required inputs (agent should prompt if missing)

1. **Topology representation.** Node-edge list, CIM export, PSS/E .raw, CYME or Synergi export, or a diagram the user describes. At minimum: nodes (buses / substations) and edges (lines / transformers) with impedances if an electrical question.
2. **The question.** Examples:
   - "If we lose line X, which customers lose power?"
   - "What is the shortest electrical path from substation A to B?"
   - "Which substations become islanded if the Y–Z corridor is out?"
   - "How far apart are substations P and Q — electrically vs. geographically?"
3. **Any relevant operating conditions** — switch states, normally-open ties, seasonal ratings.

## Canonical topology questions

**1. N-1 and N-2 contingencies.** Given a single (or double) element outage, what is the resulting connectivity? Use graph-connectivity reasoning first; defer true thermal/voltage limit checks to a load-flow tool.

**2. Islanding.** If the grid partitions, which pieces still have generation, and do those pieces have enough to carry their load? Islanding analysis needs both topology and generation/load data.

**3. Electrical vs. geographic distance.** Two substations may be 5 miles apart geographically but 80 miles electrically because the only path loops through a neighboring substation. This is central to wildfire PSPS planning, restoration routing, and congestion analysis.

**4. Radial vs. networked distribution.** Most distribution is radial with normally-open ties that can be closed under restoration. The agent should recognize the difference and reason about which ties would be closed to restore service.

**5. Loop and mesh analysis on transmission.** Bulk transmission is meshed — multiple parallel paths exist. The agent should reason in terms of paths, not a single route.

## Output shape

1. **Restatement** of the question with any topology assumptions flagged.
2. **Graph reasoning** — treat the grid as a graph, describe connectivity / paths / cuts in graph terms.
3. **Electrical nuance** — where graph-only reasoning is insufficient (capacity limits, voltage support, protection coordination), name it and recommend the next tool.
4. **Geographic context** — how the electrical answer relates to where things are on the ground.
5. **Caveats** — switch state assumptions, seasonal ratings, contingency combinations not modeled.

## Tooling advice the agent should offer when useful

- **`networkx`** for Python-based graph analysis on a node-edge export
- **PSS/E, PowerWorld, PSLF** for bulk-system AC load-flow and contingency screening
- **CYME, Synergi, OpenDSS** for distribution analysis
- **CIM+ GraphDB (Neo4j)** for integrated queries across transmission and distribution topology + geography

## What the agent should NOT do

- Do not report specific load-flow numbers (line loading in MW, voltage in pu) without a load-flow tool having produced them. Graph-connectivity results are valid; electrical limit results are not.
- Do not claim a contingency is "safe" — operational approval requires the utility's own contingency screening and operator judgment.
