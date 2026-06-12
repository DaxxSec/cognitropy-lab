# /protectee-risk-profile

Build the baseline threat-exposure profile for a principal and tag the EPA-2 evidence the artifact generates for its apprentice author.

## Inputs

- Principal identity and public role (title, visibility, sector)
- Known exposure factors: wealth/notoriety, controversy, prior incidents, family, residences, travel pattern, digital footprint
- Any existing threat communications or persons of concern
- Apprentice author + their current EPA-2 entrustment level (1–5)

## Steps

1. Inventory **exposure factors** and rate each (low/med/high) with a one-line justification.
2. Map the **threat landscape**: enumerate who would plausibly target this principal and why (grievance, ideology, extortion, IPV/insider, fixation, opportunistic).
3. For each candidate threat class, note current capability/intent/opportunity at a coarse level (detailed work-up is `/adversary-assessment`).
4. Synthesise a **risk tier** (T1–T4 from `context/references.md`) with explicit reasoning — resist defaulting to "high."
5. Derive **decisions**: which sites to advance, which routes to harden, which actors to assess, what protective-intelligence collection to stand up.
6. Record the **EPA-2 entrustment observation** for the apprentice author (Miller level reached, score, one-line justification).

## Output

`outputs/risk-profile-<principal>-<date>.md` — exposure register, threat landscape, justified risk tier, derived protective decisions, and an EPA-2 evidence footer (author, assessor, score, date). Drives every downstream command.

## Notes

- There is **no demographic profile** of an attacker; assess exposure and behaviour, not stereotype.
- Never commit real principal PII to a public repository — use role descriptors and redaction.
