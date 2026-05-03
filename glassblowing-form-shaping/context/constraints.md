# Constraints and Guardrails

## Hard Rules (the agent will not violate these)

1. **Single COE family per session.** No batch record may co-mix two COE families. Sessions involving multiple families are split into separate batch records.
2. **No proceed-to-bench on red sim verdict** unless the user explicitly overrides in writing in the batch record.
3. **Lehr program changes are user-confirmed.** The agent recommends; the user enters and verifies on the controller.
4. **Compatibility deltas > 0.5 (× 10⁻⁷ K⁻¹) are blocking.** A documented fused-strip test override is the only path through.
5. **Never delete batch records.** Append-only. Corrections are amendments, not overwrites.
6. **Successional follow-ups must be closed before next session opens** for the same date or the next day's session — missed follow-ups are a finding, not background noise.

## Soft Constraints (the agent surfaces but doesn't block)

1. **Prefer fewer reheats** — every reheat costs working time on subsequent operations and increases total session length
2. **Prefer thicker walls for thermal robustness vs. material economy** — when in doubt and not a design constraint, suggest the thicker wall
3. **Prefer first-fire of a new color rod lot in a low-stakes test piece** — flag this as a "good idea, not required" recommendation when a new rod lot is being introduced
4. **Prefer batch records authored during the session** to ones reconstructed at the end — but reconstructed records are still valuable; the choice is "now vs. never"

## Studio-Specific Constraints

These get filled in during `/onboard`:
- **Lehr capacity** — physical max piece dimensions, number of pieces per program
- **Daily session length** — natural bounds on plan size
- **Glory hole fuel cost** — affects how aggressively to budget reheats
- **Inventory of color rod lots** — bounds what's available for any given session
- **Appointment-driven studio access** (rented hot shops) — affects whether a multi-day form is viable

## Ethical and Safety Considerations

1. **Beginner supervision** — outputs of `/form-sim` and `/scenario-test` are not a substitute for in-person supervision. The agent does not evaluate physical readiness.
2. **PPE assumed** — didymium glasses, leather/Kevlar arm coverage, ventilation, fire suppression. The workspace assumes these are in place.
3. **Material data sheets supersede** — every reference table in this workspace is studio-grade approximate. When manufacturer SDS or technical sheets give different numbers, trust the manufacturer.
4. **Apprentice contributions** — when a non-owner logs a session, the workspace treats the record as the apprentice's own data; the owner can comment but should not overwrite.
5. **No transmission of personally identifying information** about studio members beyond first name + role to outside services or shared documents without consent.

## Output Format Constraints

- **All persistent state in this workspace's directory** — no external databases, no API calls. The studio computer may be offline.
- **All writes are markdown** — no proprietary formats, no binary state (photos under `outputs/photos/<piece-id>/` are the one binary exception)
- **Date format is `YYYY-MM-DD`** (ISO 8601) without exception — `/lineage-trace` relies on date sort
- **Slugs are kebab-case** — lowercase, hyphen-separated
