# Prompt: Seasonal Monitoring Program Design

Design a year-round lake monitoring program adapted to seasonal limnological dynamics.

## Input Variables
- `{LAKE_NAME}` — Name of the water body
- `{LATITUDE}` — Approximate latitude (determines ice cover, stratification timing)
- `{MAX_DEPTH}` — Maximum depth in meters
- `{PRIMARY_USE}` — Drinking water, recreation, fishery, ecosystem protection
- `{KNOWN_ISSUES}` — Nutrient loading, HABs, invasive species, contamination, etc.
- `{BUDGET_LEVEL}` — Low (volunteer/minimal), moderate (municipal), high (research/agency)

## Prompt

Design a seasonal monitoring program for {LAKE_NAME} (latitude ~{LATITUDE}, max depth {MAX_DEPTH}m). Primary use: {PRIMARY_USE}. Known issues: {KNOWN_ISSUES}. Budget level: {BUDGET_LEVEL}.

For each season, specify:

1. **Sampling frequency** and rationale (why more or less frequent in this season)
2. **Parameters** — which to collect and why they matter in this season
3. **Depth strategy** — integrated, discrete depths, profile, and why
4. **Stations** — any seasonal stations to add/remove (e.g., beach monitoring only in summer)
5. **Safety considerations** unique to the season (ice, heat, storms, blooms)
6. **Key ecological events** to capture (turnover, stratification onset, ice-on/ice-off, bloom season)

Also include:
- Annual QA/QC calendar (when to do performance audits, inter-lab comparisons)
- Data reporting milestones (when to compile seasonal summaries)
- Equipment maintenance schedule aligned to seasonal demands
- Budget allocation by season

Adapt the entire program to the specified budget level — a volunteer program looks very different from an agency program.
