# /stakeholder-brief

Turn any analysis (codex, transcription, diagnosis, root-cause, provenance) into an audience-tuned stakeholder communication, using the templates in `prompts/`. This is the build's core technique — stakeholder communication templates — made operational.

## Inputs

- The source analysis (one or more `outputs/` artifacts).
- The target audience: line baker / head chef-QA / cost controller / junior baker / front-of-house.
- The purpose: spec, defect report, cost memo, training, or menu copy.

## Steps

1. Select the matching template from `prompts/` (see the audience→template map in `context/workflows.md`).
2. Apply the **five-part frame**: Audience → Purpose → Key message (one line) → Evidence → Action.
3. Translate the analysis into the audience's vocabulary — fold math for the line, root cause + fix for the chef, waste % and butter cost for finance, the "why" for trainees, sensory + allergen language for guests.
4. Strip anything the audience can't act on; keep every claim traceable to a source artifact.
5. Run the **allergen/provenance check**: any product mention must declare gluten/milk/egg and stay within supportable provenance claims.

## Output

A finished communication at `outputs/brief-<audience>-<topic>-<date>.md`, ready to send, with a one-line provenance footer citing the source `outputs/` artifacts.

## Notes

- Never send evidence without an action, or an action without its evidence — that pairing is what makes the brief trustworthy.
- One analysis often spawns several briefs (line + chef + finance from one failed batch); generate them as separate audience-tuned files, not one mixed memo.
