---
description: Run a structured spatial analysis on a supplied dataset, scenario, or question.
---

# /analyze — Structured Spatial Analysis

Invoke when the user wants a rigorous, reproducible walk-through of a grid question that has a spatial component. The agent's job is to produce *method* first and *answer* second — so the user can repeat the work in their own tooling.

## Required inputs (agent should prompt for any missing)

1. **The question.** One sentence stating what needs to be known. Good: "Which 5 miles of our 115 kV ROW have the highest combined vegetation and fire-weather exposure?" Poor: "Tell me about risk."
2. **The spatial scope.** Polygon, corridor, service territory, feeder set, or bounding box. "All assets in county X" is fine; "our system" is not.
3. **Available data.** Layer names, formats, CRS, attribute columns, time window.
4. **Decision context.** What decision will this inform, and what is the tolerance for approximation? A screening study needs less precision than a 10-year capital plan.

## Output shape

Return a response with these sections, in order:

1. **Restatement of the question** in specific, answerable form — with any assumptions flagged.
2. **Data requirements** — the layers, columns, and derived fields the analysis needs.
3. **Method** — a numbered sequence of steps with enough detail to reproduce. For each step, name the tool or operation (e.g., "buffer 30 m around ROW using `ST_Buffer`" or "overlay with fire-weather raster via `zonal statistics`"). Mention the coordinate reference system at the first geometric step.
4. **Interpretation guidance** — what the output means and what it does *not* mean. Flag edge cases that would invalidate the ranking.
5. **Uncertainty and caveats** — data-quality issues, temporal mismatches, projection artifacts, small-number effects.
6. **Next steps** — three tiered follow-ups (quick check, standard deepening, advanced).

## Methodological rules

- Always state the coordinate reference system explicitly. For US work, projected CRS (e.g., EPSG 3857 for web, state plane or UTM for measurements) — never assume WGS84 lat/lon for distance-sensitive operations.
- When mixing raster and vector layers, state the sampling strategy (cell-center, area-weighted, majority).
- When scoring assets on multiple factors, be explicit about normalization (min-max vs. z-score) and weighting. Do not hide arbitrary weights inside a composite score.
- For outage / event analysis, separate *spatial pattern* from *spatial correlation*: a pattern may be random, or may correlate with an asset class, storm track, or feeder boundary. State which test would distinguish the two.
- If the analysis would need live operational data the user likely can't share (real-time SCADA, customer-level OMS), offer a synthetic equivalent and clearly label it.

## When to say "I can't answer this"

- The user provides no data scope or only vague descriptions.
- The question requires operational approval (e.g., "should we switch feeder X?"). Steer to `context/constraints.md` and suggest the analysis input to that decision rather than the decision itself.
- The analysis requires domain-specific software the user doesn't have (e.g., certified load-flow tool for contingency screening). Describe the method and flag the tool dependency.
