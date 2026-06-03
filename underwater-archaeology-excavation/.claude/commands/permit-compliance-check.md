# /permit-compliance-check

Gate the project against UNESCO 2001 Annex Rules and national heritage law **before** any seabed disturbance. A hard precondition, not a formality.

## Inputs

- Jurisdiction and maritime zone (internal waters, territorial sea, contiguous zone, EEZ, continental shelf, the Area).
- Whether the relevant state has ratified UNESCO 2001, and any national heritage-protection statute/designation.
- Project design: methods, funding, conservation/curation provision, archiving plan, personnel competence.
- Site status flags: age (>100 years?), human remains, sovereign/state vessel, war grave.

## Steps

1. Read `context/references.md` ("UNESCO 2001 Annex Rules — the ones that bite a CBA").
2. Confirm the **in-situ default (Rule 1)** has been genuinely considered and that excavation is justified, not assumed.
3. Check **funding & conservation provision (Rules 9–13, 25)**: is conservation/curation funding secured *before* fieldwork? If not, the project fails the gate.
4. Check **non-commercial (Rule 2)**: no part of the assemblage may be sold or commercially exploited.
5. Check **archive integrity (Rule 33)**: the project archive will be kept together and accessible.
6. Identify required **permits/licences** for the jurisdiction and zone, and the consenting authority.
7. Flag **special-status** conditions: human remains, sovereign immunity, war graves — each adds obligations independent of the CBA.
8. Produce a pass/fail gate with the unmet conditions listed.

## Output

`outputs/compliance-<site>-YYYY-MM-DD.md`: a checklist against UNESCO 2001 and national law, the permits required and their authority, special-status flags, and a clear PASS / FAIL with remediation items for any failure.

## Notes

- Treat UNESCO 2001 as the ethical baseline even in non-ratifying states — funders and journals increasingly require it.
- "Conservation funding secured before fieldwork" is the rule most often failed in practice and the one that creates conservation backlogs.
- Sovereign wrecks and war graves can be legally off-limits regardless of significance or threat — a failed flag here overrides the CBA.
