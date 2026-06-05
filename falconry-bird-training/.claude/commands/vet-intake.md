# /vet-intake

Produce a structured avian-vet intake/referral packet for a raptor health concern — fast, complete, and ready to act on.

## Inputs

- The concerning sign(s): going light, fluffed/reluctant, mouth/crop lesions, labored breathing, vomiting, lameness, abnormal mutes.
- Recent weight trend (last 7–14 days from the log).
- Recent diet (note any pigeon/dove — frounce risk), housing/ventilation, onset and progression.

## Steps

1. Stop flying the bird; this command is for a health event, not training.
2. Pull the weight trend from `/weight-log` and attach it.
3. Record diet history (species, source, dates) — flag pigeon/dove for frounce.
4. Describe mutes and castings (appearance, timing) and any recent facility changes.
5. Match signs to leading differentials using the ailment table in `context/references.md` (frounce, aspergillosis, bumblefoot, parasites, sour crop, going light).
6. Format the intake with `prompts/raptor-health-vet-consult.md` and instruct the user to **call the avian vet now**.

## Output

`outputs/vet-intake-YYYY-MM-DD.md`: signalment (species/age/source/band), presenting signs with onset, weight trend, diet/housing history, mute/casting notes, and the candidate differentials — formatted for the vet.

## Notes

- Raptors mask illness until late; treat "going light" as disease until the vet rules it out.
- This organizes the history for the vet; it is **not** a diagnosis or treatment plan.
- If the bird dies, run `/incident-report` — mortality is typically reportable.
