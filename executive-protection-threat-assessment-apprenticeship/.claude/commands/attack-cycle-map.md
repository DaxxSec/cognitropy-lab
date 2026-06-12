# /attack-cycle-map

Map a known or hypothesised threat onto the hostile planning cycle, locate the cheapest interdiction window, and generate EPA-6 evidence.

## Inputs

- The actor/threat (from `/adversary-assessment`) or a red-team hypothesis
- Observed indicators tied to specific cycle phases
- Current protective posture and protective-intelligence collection
- Apprentice author + current EPA-6 entrustment level

## Steps

1. Place the actor on the **hostile planning cycle** (target selection → initial surveillance → final selection → pre-attack surveillance → rehearsal → execution → escape) using observed indicators.
2. Cross-reference the **path to intended violence** (grievance → ideation → research → preparation → breach → attack) for the behavioural trajectory.
3. For each remaining phase, list the **detection signature** and the **cheapest protective interdiction** (per `context/references.md`).
4. Recommend the **highest-leverage interdiction window** — usually pre-attack surveillance, not execution.
5. Note residual risk if the window is missed and the fallback (immediate-action drills).
6. Record the **EPA-6** entrustment observation.

## Output

`outputs/attack-cycle-<subject>-<date>.md` — phase placement, detection signatures, interdiction options ranked by leverage, recommended window, residual-risk note, and EPA-6 evidence footer.

## Notes

- The strategic message to teach: **prevention is upstream**. Out-shooting an attacker at execution is the most expensive and least reliable interdiction.
