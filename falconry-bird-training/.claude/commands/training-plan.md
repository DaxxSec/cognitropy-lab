# /training-plan

Build a stage-gated training progression for a specific bird, with a stakeholder communication checkpoint attached to each gate.

## Inputs

- The bird: species, source (passage/eyass/imprint/captive-bred), age, current stage.
- Discovered or estimated flying-weight band (from `/weight-log`).
- Goals: quarry targeted, season timeline, whether abatement or game-hawking.

## Steps

1. Lay out the gates: manning → jump-to-fist → creance flights → free flight → entering on quarry → conditioning/fitness.
2. Define each gate's **exit criterion** in weight + response terms (e.g. "flies 50 ft to the fist on the creance, 3 sessions running, at flying weight").
3. Attach a **comms checkpoint** to each gate: first creance flight & first free flight → `/sponsor-report`; entering on quarry → milestone note; any setback → log + possibly `/vet-intake`.
4. Tie the plan to the daily `/weight-log` so readiness is read from response-at-safe-weight, not weight alone.
5. Set telemetry as a hard prerequisite before free flight.
6. Schedule realistic timeframes and note molt/seasonal constraints.

## Output

`outputs/training-plan-<bird>-YYYY-MM-DD.md`: the gate sequence with exit criteria, the comms checkpoint per gate, telemetry/equipment prerequisites, and a tentative timeline.

## Notes

- Never advance by dropping weight to force a gate — hold the gate and address the trust/manning or health issue.
- Poor response at a safe weight is a manning gap, not a weight problem.
- Reset the plan after the molt when the bird returns to flying condition.
