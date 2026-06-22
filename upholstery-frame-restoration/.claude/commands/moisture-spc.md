# /moisture-spc — Wood Moisture SPC vs. the Glue-Up Window

Track and chart wood moisture content (MC) against the safe equilibrium-moisture window and flag drift *before* joinery is committed — moisture is the process input most likely to open a joint months after it ships.

## Inputs

- MC readings (%) over time for the wood in question — incoming, during conditioning, at glue-up — each with meter type (pin/pinless), species correction applied?, and ambient RH/temp.
- The shop's **service EMC target** (typically 6–9%) and the **glue-up window** (mating surfaces within ~2% of service EMC; hard ceiling ~12%).
- The piece's destination environment, if known (humid vs. arid interior changes the EMC target).

## Steps

1. Confirm readings are **species-corrected** and taken at consistent depth — uncorrected meter values are not comparable across woods.
2. Plot MC over the conditioning period on an I-MR chart (`/control-chart`) with the **glue-up window** overlaid as spec lines.
3. Flag any reading **outside the window**, and any **downward/upward trend** that hasn't yet stabilized (wood still moving = not ready).
4. Estimate readiness: MC stable within the window across ≥ 2–3 consecutive readings ⇒ cleared for glue-up; otherwise defer and keep conditioning.
5. If a joint-gap chart shows signals, **cross-check this MC history** — off-window glue-up is the prime suspect in an OCAP.

## Output

A moisture-readiness report: the MC series vs. window, trend/stability assessment, glue-up clearance (cleared / defer), and the species-correction note. Save to `outputs/<frame-id>-moisture-spc.md`.

## Notes

- EMC depends on the *destination* climate, not the shop's — a frame glued at shop EMC then moved to a dry/humid home will still move. Target the service environment.
- A single in-window reading isn't readiness; wood that's still trending is wood that will keep moving after glue-up.
- Pinless meters read a volume average and are species/density sensitive; record the instrument so readings stay comparable on the chart.
