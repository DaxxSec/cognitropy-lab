# /jurisdiction-coord-matrix

Map host-nation police / military / EMS / fire / hospital coordination requirements with named POCs, escalation paths, and applicable agreements (SOFA / BIA / MOU).

## Inputs

- **Jurisdictions touched** by the trip (each host nation, each transit country).
- **Operational footprint per jurisdiction** — venues, routes, time-on-ground.
- **Standing agreements** — SOFA (Status of Forces Agreement), BIA (Bilateral Investment Agreement), MOU (Memorandum of Understanding), VWP (Visa Waiver Program) terms.
- **Embassy / consulate locations** + DCM / RSO POC.
- **Host-nation MOI / equivalent** — formal liaison contact.
- **Prior trip coordination notes** if any.

## Steps

1. Read `context/references.md` "DS regional standards" + `context/concepts.md` "Host-nation coordination doctrine".
2. Per jurisdiction, build coordination matrix entries:
   - **Host-nation police** — POC name, rank, agency, contact, escalation (precinct → district → MOI HQ), responsibilities (escort, perimeter, traffic plan)
   - **Host-nation military / gendarmerie** — if applicable, POC, escalation, responsibilities
   - **EMS** — POC, station serving each route, pre-position request, hospital pre-notification, response-time commitment
   - **Fire** — POC, station serving each route, standby request for high-density venues
   - **Hospital** — primary + alternate trauma centre, on-call POC, capability profile, pre-notification protocol
   - **Embassy / consulate** — DCM, RSO/PSC, MSG detachment commander, after-hours duty officer
3. Document the applicable standing agreements per jurisdiction — what authority you operate under, what's prohibited, what requires permission.
4. Document recent jurisdictional changes — government transitions, political crises, recent diplomatic friction.
5. Establish primary + alternate comms channels per POC.
6. Build the escalation tree — at what point does an issue escalate from local police precinct to MOI to DCM to State Department.
7. Generate one-page detail-leader carry summary + full matrix at `outputs/jurisdiction-matrices/<trip-id>/coord-matrix.md`.

## Output

A markdown coordination matrix at `outputs/jurisdiction-matrices/<trip-id>/coord-matrix.md` containing: per-jurisdiction entries (each POC named, contacted, responsibility documented), standing-agreement summary, escalation tree, comms channels, recent jurisdictional change notes. Detail-leader carry summary as separate one-page artifact.

## Decision points

- **If host-nation will not provide a requested POC contact** → escalate via DCM channel; document refusal; consider trip restructure.
- **If standing agreements don't cover an operational requirement** → request specific waiver via DCM; do not absorb the gap silently.
- **If a jurisdictional change happens mid-planning** (e.g. host-nation government changes) → re-validate all POCs and re-run matrix; transitions invalidate prior contacts.

## Notes

- Coordination matrix is not a static document — refresh weekly during pre-trip and daily during visit.
- POC names + contact details are sensitive; OPSEC handling required.
- Standing agreements are often classified or restricted; cite by reference not full text.
- After-hours duty officers matter most for the trip — verify their contact details, not just business-hours POCs.
