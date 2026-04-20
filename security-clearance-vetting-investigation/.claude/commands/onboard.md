# /onboard

Initialize this workspace for the current user by capturing role, agency context, authorities, and constraints. Populates four context files.

## Inputs
Interactive Q&A. No file inputs required.

## Steps
1. Greet the user and confirm they understand this is a planning aid, not an authoritative adjudication system.
2. Ask:
   - Agency or organization name (pseudonymized OK).
   - Role (investigator, adjudicator, FSO, insider-threat analyst, other).
   - Authorities under which they operate (EO 12968, EO 13467, SEAD 4, NISPOM / 32 CFR 117, agency-specific).
   - Approximate caseload size and clearance-level mix.
   - Tool stack (DISS, NBIS, JPAS, Scattered Castles, internal ticketing).
   - Handling caveats applicable to outputs (FOUO, CUI basic, CUI specified).
   - Mission criticality flavor (industrial / IC / DoD civilian / interagency).
3. Write the collected information to:
   - `context/project.md` — mission scope and touchpoints
   - `context/role.md` — user role and authority
   - `context/constraints.md` — data-handling rules
   - `context/for-agent/environment.md` — tool stack, storage, paths
4. Seed `planning/plan.md` with the user's stated caseload goals.
5. Append to `work-log/YYYY-MM-DD.md`.

## Output
Four context files populated, `planning/plan.md` seeded, session logged. Confirm to the user what was saved.
