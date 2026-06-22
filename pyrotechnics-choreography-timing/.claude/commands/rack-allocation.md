# /rack-allocation

Assign effects to mortars/racks and firing-module channels, and prove the allocation is electrically feasible (no double-booked channel, no over-current burst).

## Inputs

- The canonical cue sheet (cues, `t_fire`, positions; channels possibly `TBD`).
- Firing-hardware inventory: modules, pins per module, per-module max simultaneous e-matches / current budget, settle window.
- Rack inventory: tubes per rack, bore, angles, positions.

## Steps

1. Read the CURR/CHAN obligations from the spec catalog and the hardware limits from `context/references.md`.
2. Assign each cue a `(module, pin)`; for a `TBD` cue, choose a free pin at a position consistent with its bore and the site layout.
3. **CHAN:** verify no pin is assigned to two cues (a pin fires once). Any clash ⇒ counterexample.
4. **CURR:** bucket cues by module into settle-window windows; check `K ≤ max_simultaneous` in every window. Finale bursts are the binding case. Any over-budget window ⇒ counterexample (module, window, K vs. limit).
5. If infeasible, propose a repair: split the burst across modules, stagger by one settle window, or re-rack — then re-check CHAN+CURR and hand SEP back to `/separation-proof` (re-racking moves positions).

## Output

`outputs/rack-allocation-YYYY-MM-DD.md`: the cue→(module, pin, rack) assignment table, CHAN/CURR verdicts with any counterexamples, and the per-module simultaneous-fire profile over time.

## Notes

- A resource feasibility result is a model statement — the on-site continuity test still governs whether every channel actually reads connected.
- Re-allocation that moves a position invalidates the prior separation proof — always re-run `/separation-proof` after.
- Treat the finale chain as the worst case: CURR, CHAN, and SEP all bind there simultaneously.
