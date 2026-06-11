# LCA Inventory Buildout

## Purpose

Construct a defensible cradle-to-gate life-cycle inventory for an SMA part, with explicit boundaries, assumptions, and data-quality flags — the honest version, not a single fabricated number.

## Prompt Template

```
You are an LCA practitioner building a cradle-to-gate inventory for a shape-memory-alloy component,
following ISO 14040/14044. Favour transparency and ranges over false precision.

The part and process are:

- **Alloy / composition:** [e.g. binary Ni-50.8 at% Ti, or with X at% Hf]
- **Finished part mass / buy-to-fly ratio:** [e.g. 4 g finished, 3:1 scrap ratio]
- **Process route:** [VIM and/or VAR, hot/cold work passes, anneals, shape-set, finishing]
- **Functional unit:** [e.g. "one actuator delivering 3 mm stroke for 10^5 cycles"]
- **LCA database to reconcile against:** [ecoinvent / GaBi-Sphera / GREET / none yet]

Please:
1. State goal, scope, system boundary, and functional unit; list every cut-off.
2. Build the per-functional-unit inventory: Ni and Ti mass (scaled by scrap ratio), melting energy, working/annealing energy, shape-set energy, ternary additions.
3. Report GWP (kg CO₂e) and cumulative energy demand (MJ) as ranges, with a data-quality flag per line.
4. Attribute the hotspots and name the single biggest reduction lever.
5. List assumptions explicitly and mark anything you could not source.
```

## Expected Output

- A goal/scope/functional-unit/boundary statement.
- A per-functional-unit inventory table with energy and material lines.
- GWP + CED results as ranges with data-quality flags (not single point values).
- A hotspot attribution and the top reduction lever (often the scrap ratio).
- An explicit assumptions-and-gaps list so a reviewer can challenge the inventory.
