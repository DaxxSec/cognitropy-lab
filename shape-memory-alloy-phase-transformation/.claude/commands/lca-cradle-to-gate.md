# /lca-cradle-to-gate

Build a cradle-to-gate life-cycle inventory for an SMA part — embodied energy and global warming potential from ore to finished component — per ISO 14040/14044.

## Inputs

- Bill of materials: alloy composition, part mass, and buy-to-fly / scrap ratio (NiTi machining loses a lot of material).
- Process route: melting method (VIM, VAR, or both), hot/cold working passes with interpass anneals, shape-setting, finishing (electropolish, etch).
- The LCA database you will reconcile against (ecoinvent, GaBi/Sphera, GREET) and the functional unit (e.g. "one actuator delivering X stroke for N cycles").

## Steps

1. Read `context/concepts.md` and `context/references.md` for the LCA framing (goal & scope, functional unit, system boundary) and the order-of-magnitude embodied-energy / GWP figures for primary nickel and titanium — **both are high, titanium especially (Kroll process)**.
2. Define the system boundary explicitly (cradle-to-gate = raw extraction → ingot → mill product → finished part) and the functional unit; state every cut-off.
3. Inventory the inputs per functional unit: kg of Ni and Ti (scaled up by the scrap/buy-to-fly ratio), melting energy, working/annealing energy, shape-set furnace energy, and any Pt/Pd/Hf ternary additions (very high embodied carbon).
4. Apply characterization factors (e.g. ReCiPe or TRACI) to get GWP (kg CO₂e), cumulative energy demand (MJ), and at least one resource-depletion/supply-risk indicator for the critical metals.
5. **Attribute the hotspots**: state which stage dominates (usually raw-material extraction + the high scrap ratio, then vacuum melting). The buy-to-fly ratio is frequently the biggest lever.
6. Report figures as ranges with data-quality flags — extraction GWP swings widely with ore type (sulfidic vs. lateritic Ni) and energy mix; never present a single point value as settled.

## Output

`outputs/lca-cradle-to-gate-<part>-YYYY-MM-DD.md`: goal/scope/functional-unit statement, the per-FU inventory table, GWP + CED + supply-risk results with ranges, the hotspot attribution, and an explicit list of assumptions and cut-offs.

## Notes

- Honesty over precision: SMA LCA numbers are database- and ore-dependent. Present ranges, cite the database, and flag low-quality data rather than fabricating a tidy single figure.
- The scrap ratio often dominates — reducing machining waste (near-net shape) can beat any material substitution.
- This is cradle-to-**gate** only; the use phase and end of life are handled by `/use-phase-energy-balance` and `/recyclability-eol-assessment`. Don't claim a full footprint from this command alone.
