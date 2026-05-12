# Eco-Driving / GLOSA Feasibility Prompt

## Purpose
Decide whether deploying GLOSA (Green Light Optimal Speed Advisory) or eco-approach signaling is worth pursuing on this corridor given current connected-vehicle (CV) market penetration.

## Prompt Template

I'm considering an eco-approach signaling overlay on the following corridor:

- **Corridor:** [name, length]
- **Number of signalized intersections:** [N]
- **Posted speed:** [mph]
- **85th-percentile speed:** [mph]
- **SPaT (Signal Phase and Timing) broadcast available:** [yes / no / planned]
- **MAP message available:** [yes / no / planned]
- **Backhaul to controllers:** [fiber / cellular / none]
- **Estimated CV market penetration:** [% — 2026 is roughly 1–3% of light-duty fleet for SPaT-aware vehicles]
- **Cooperative apps (e.g., Audi Traffic Light Information):** [available in jurisdiction yes/no]

Please evaluate:

1. **Theoretical fuel-saving ceiling.** At full CV penetration on this corridor, what's the upper-bound fuel saving from eco-approach? Cite the FHWA / Barth & Boriboonsomsin / SAE 2945 evidence base.
2. **Penetration-discounted realistic saving.** At declared CV penetration, what fraction of theoretical maximum is realistically capturable?
3. **Infrastructure requirement.** What needs to be deployed (RSU, SPaT broadcaster, MAP authoring, backhaul, NTCIP 1202 v03A object support)?
4. **Integration risk.** Does the SPaT broadcast match the actual phase actuation precisely (often a 1–2 s skew at adaptive intersections), and does that skew kill the eco-driving benefit?
5. **Cost-benefit framing.** Is the saving worth the deployment cost at current CV penetration, or should this wait for ~10% penetration (estimated 2030–2032)?

## Expected Output
- Quantitative theoretical and realistic fuel-saving estimates (% of corridor baseline)
- Infrastructure gap list
- 2–3 risk flags
- Single-sentence go/no-go/wait recommendation with the ETA threshold for revisiting
