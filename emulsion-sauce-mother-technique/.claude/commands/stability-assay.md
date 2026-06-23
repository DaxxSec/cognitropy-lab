# /stability-assay

Run a structured stress test on an emulsion and grade its stability — the objective evidence the review round weighs alongside sensory scores.

## Inputs

- The emulsion specimen and its intended use (cold-held dip vs warm-held service sauce — sets which stresses matter).
- Available stress methods: time-at-rest, refrigerated/ambient cycling, warm-hold, mechanical shear, centrifuge (if available).
- The acceptance target (e.g. "no visible separation after 2-hour service hold").

## Steps

1. Define the stress that matches the use: warm-hold + time for hollandaise on a pass; fridge time + transport shear for mayonnaise.
2. Establish t0 condition (photograph, note gloss/body).
3. Apply the stress in defined increments; at each checkpoint record creaming, oiling-off, weeping, or break — and whether it re-blends (creaming) or not (coalescence).
4. If a centrifuge is available, spin a sample to accelerate creaming and quantify the separated fraction.
5. Map observations to the defect-severity scale (`/defect-grade`) and assign an overall stability grade.
6. Note the failure threshold (the time/temperature at which it first separated) — that number is the deliverable for service planning.

## Output

`outputs/stability-<formula-id>-YYYY-MM-DD.md`: stress protocol, checkpoint observations, separated fraction (if centrifuged), failure threshold, stability grade, and a use-fit verdict (holds for intended service or not).

## Notes

- Distinguish creaming (re-mixable, often fine) from coalescence (true break) — they have very different verdicts.
- Test under *realistic* conditions: a sauce that holds at the bench but breaks at pass temperature fails for service.
