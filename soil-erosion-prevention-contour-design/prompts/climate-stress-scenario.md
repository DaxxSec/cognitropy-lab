# Climate Stress Scenario

## Purpose

Use this to stress-test an existing or proposed design against intensified storms — higher return periods and climate-scaled rainfall — to quantify the headroom remaining and find the structure that fails first.

## Prompt Template

```
You are an erosion-control agent. Read context/workflows.md "Workflow C" and the /stress-test-design-storm command.
Stress-test my system against an escalating storm ladder.

- **Structures & baseline utilizations:** [from outputs/capacity/ — list structure: utilization at design storm]
- **Baseline design return period:** [e.g. 10-yr, 24-hr]
- **Return-period ladder to test:** [e.g. 10 → 25 → 50 → 100-yr]
- **Climate depth-scaling factors:** [e.g. +10%, +20% intensity — cite the regional guidance]
- **Worse cover scenario (optional):** [e.g. residue removed, drought-thinned canopy]

Please:
1. Recompute demand and utilization for every structure across the scenario ladder.
2. Mark the scenario where each structure's utilization crosses 1.0.
3. Identify the bottleneck (earliest failure) and whether failures cluster or are isolated.
4. Recommend the cheapest capacity addition that buys the bottleneck one scenario step of headroom.
5. State the climate-scaling assumptions explicitly as assumptions, with their source.
```

## Expected Output

- A scenario × structure utilization matrix.
- Each structure's failure scenario and the ranked bottleneck list.
- A cluster-vs-isolated diagnosis and a targeted vs system-wide recommendation.
- Clearly labeled climate-scaling assumptions and their source.
