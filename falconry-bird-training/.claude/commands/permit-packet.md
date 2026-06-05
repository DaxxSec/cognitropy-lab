# /permit-packet

Assemble or audit a falconry permit application/renewal packet and the facility-inspection readiness checklist for the state wildlife agency.

## Inputs

- Permit class being applied for or renewed, and the **state**.
- Falconer identity, existing permit numbers, sponsor attestation (apprentices).
- Species requested and current bird roster (for possession-limit checks).
- Facility details: mews dimensions, perch types, weathering area, entry/safety design.

## Steps

1. Pull class/state requirements from `context/references.md` and flag anything that must be confirmed with the state coordinator directly.
2. Verify the species request is allowed at this class/state and that possession limits aren't exceeded.
3. Run the **facility checklist**: mews size, padded bow/block perches, bath pan, weathering area, predator-proofing, ventilation (aspergillosis prevention), safety/double-door entry.
4. List facility photos the inspector will want and note which are missing.
5. Draft the cover letter from `prompts/permit-renewal-cover-letter.md`, summarizing the program and any changes since last renewal.
6. Check the deadline: renewals must be filed **before** expiry — never lapse with a bird in possession.

## Output

`outputs/permit-packet-YYYY-MM-DD.md`: a completion checklist (done / missing), the facility-inspection readiness list, the drafted cover letter, and the filing deadline. Photo placeholders reference files under `outputs/facility/`.

## Notes

- A failed inspection costs weeks — fix every facility gap before requesting it.
- This packet structures your submission; the state's form/portal is authoritative for required fields.
