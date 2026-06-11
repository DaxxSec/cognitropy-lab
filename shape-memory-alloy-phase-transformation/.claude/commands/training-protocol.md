# /training-protocol

Design a thermomechanical training schedule to imprint a two-way shape memory effect (TWSME) or to stabilize a one-way actuator before service.

## Inputs

- Target behavior: two-way (spontaneous shape change on cooling with no applied load) or stabilized one-way actuation.
- The two memorized shapes / strains and the actuation stroke required.
- Alloy and its transformation temperatures; available equipment (furnace, fixture, load frame, electrical heating).

## Steps

1. Read `context/concepts.md` on training mechanisms: oriented dislocation/defect fields and retained martensite create internal stresses that bias variant selection on cooling.
2. Choose a training route: (a) overdeformation of martensite, (b) repeated thermal cycling under constant load, (c) repeated SME cycling, or (d) combined pseudoelastic + SME cycling — match the route to equipment and the TWSME strain target.
3. Specify the schedule: deformation strain, load, temperature limits (cycle between below Mf and above Af), and **cycle count** (typically tens to a few hundred, until the spontaneous strain stabilizes).
4. Track the developing TWSME strain each block; stop when it plateaus — over-training adds residual strain and embodied energy without payoff.
5. Define the **stability envelope**: TWSME degrades if the part is later heated above the training temperature or cycled past the training strain — state these service limits explicitly.
6. Record the full schedule so it is reproducible, and flag the energy cost (furnace hours × cycles) for the LCA use-phase / cradle-to-gate accounting.

## Output

`outputs/training-protocol-<part>-YYYY-MM-DD.md`: the chosen route, the step-by-step schedule (strain, load, temperatures, cycles), the achieved TWSME strain curve vs. cycle, the service stability limits, and the training energy estimate.

## Notes

- TWSME strain is always smaller than one-way SME (typically ~2–5% vs. 6–8%) and fades with use — never promise one-way magnitudes from a trained two-way part.
- Training is itself functional fatigue applied deliberately — there is no free lunch; the part is partly "spent" before service. Coordinate with `/functional-fatigue-budget`.
- Heating above the training/shape-set temperature erases the training; pin the maximum service temperature.
