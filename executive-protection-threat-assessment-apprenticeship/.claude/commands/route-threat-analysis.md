# /route-threat-analysis

Analyse movement routes between sites for choke points, ambush exposure, and attack-on-principal drill points; generate EPA-4 evidence.

## Inputs

- Origin and destination, departure window, vehicle/motorcade configuration
- Map data and known construction/event/closure constraints
- Threat tier and any actor with route knowledge (from prior assessments)
- Apprentice author + current EPA-4 entrustment level

## Steps

1. Lay out **primary, alternate, and emergency** routes — never present a single route.
2. For each, mark **choke points** (forced-slow geometry: tunnels, bridges, single-lane, gates) and **ambush geometry** (elevation, cover, escape-favourable layouts).
3. Identify **AOP / AOV drill points** — where the detail rehearses "get off the X," and where the nearest off-route safe haven and trauma center sit.
4. Assess **timing predictability**: would a hostile observer be able to time the movement? Recommend variation.
5. Cross-reference against suspected hostile surveillance (hand to `/surveillance-detection-plan`).
6. Record the **EPA-4** entrustment observation.

## Output

`outputs/route-<origin>-<dest>-<date>.md` — annotated route options, choke-point and ambush register, AOP drill points, timing/variation recommendation, and EPA-4 evidence footer.

## Notes

- Embus/debus is the highest-risk moment of any movement — treat route endpoints as advance sub-surveys.
