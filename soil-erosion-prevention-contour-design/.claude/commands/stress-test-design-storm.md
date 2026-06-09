# /stress-test-design-storm

Scenario-stress the whole erosion-control system: scale design storms for higher return periods and climate intensification, re-rank utilization across structures, and identify the first structure to fail (the bottleneck).

## Inputs

- The set of designed structures with their capacities and baseline utilizations (from `/forecast-runoff-capacity`, sizing commands).
- Baseline design return period.
- A scenario ladder: return-period steps (e.g. 10→25→100-yr) and/or rainfall depth-scaling factors (e.g. +10%, +20% per regional climate guidance).
- Soil-loss side: any worse cover scenario to test (e.g. residue removal, drought-thinned canopy).

## Steps

1. Read `context/workflows.md` "Workflow C: Capacity stress test".
2. For each scenario, recompute demand: scaled Qₚ (and runoff volume) and, where relevant, scaled RUSLE A.
3. Recompute **utilization** for every structure and for the soil budget (A/T) under each scenario; tabulate scenario × structure.
4. For each structure, find the scenario at which utilization crosses 1.0 — its failure point.
5. **Bottleneck:** the structure that fails earliest (lowest scenario step) governs the system's real service level. Rank all structures by failure scenario.
6. Recommend the cheapest capacity addition that buys the bottleneck one scenario step of headroom; note whether failures cluster (balanced-but-brittle) or are isolated (targeted fix).

## Output

`outputs/stress-tests/storm-stress-<system>-YYYY-MM-DD.md` — the scenario × structure utilization matrix, each structure's failure scenario, the ranked bottleneck list, the cluster-vs-isolated diagnosis, and the recommended headroom-buying fix.

## Notes

- A system where everything fails at the same scenario is well-balanced but has no spare — recommend a system-wide safety factor, not one structure's reinforcement.
- If the bottleneck fails *below* the design storm, the design is inadequate — return to sizing, don't paper over it.
- Climate scaling is a stated assumption, not a fact — cite the regional intensification guidance used and label it clearly.
