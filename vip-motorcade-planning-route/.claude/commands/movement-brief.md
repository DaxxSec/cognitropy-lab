# /movement-brief — Operational Brief, Driver Brief, Principal Brief

Generate the three artefacts the detail moves on: an operational brief for the protective detail, a 1-page driver brief, and a principal-facing brief that explains residual risk in plain language.

## Required Inputs
- Route decision (`planning/route-decision-<YYYY-MM-DD>.md`)
- Scoring sheets for primary, alternate, abort
- Contingencies set (`outputs/<route-codename>/contingencies/*.md`)
- Advance findings (`outputs/<window>/advance-checklist-<YYYY-MM-DD>.md`)
- Movement window — specifically the planned T-0 (relative time used in the artefact)

## Procedure

### 1. Operational Brief
Detail-leader-and-team-facing. ~5–8 pages.

Sections:
1. **Executive summary** — principal placeholder, leg, T-0, primary route codename, residual ceiling, top-3 hazards.
2. **Composition** — vehicle list, crew assignments, comms callsigns.
3. **Threat baseline summary** — top actors with intent/capability, current targeting indicators, baseline expiry.
4. **Primary route** — origin → destination, segment-by-segment table with residual band, dominant hazard, mitigation present, drill reference.
5. **Alternate route** — same structure.
6. **Abort route** — survivability-focused; nearest authorized safe location.
7. **Contingency drills** — full drill cards in segment order.
8. **Advance findings** — what the advance team turned up, and what changed in the plan.
9. **Liaison and comms** — host-nation contacts (placeholders), call sequences, hospital network.
10. **Sign-off block** — detail leader, contracting office (if High+ residual).

Output: `outputs/<window>/operational-brief-<YYYY-MM-DD>.md`.

### 2. Driver Brief — 1 Page
Driver-facing. Must fit on one printed side. Sections:
- Route codename, T-0, principal placeholder
- Primary route — first turn / second turn / dominant landmarks (sanitized)
- Top-3 contingency drills tied to specific segments (just the trigger and action — the full card is in the vehicle)
- Comms callsigns, frequencies, MEDEVAC route, abort signal
- "If lost / out of comms" default behavior

Output: `outputs/<window>/driver-brief-<YYYY-MM-DD>.md`.

### 3. Principal Brief
Principal-facing. ~1 page, plain language, no tradecraft jargon.

Sections:
- "The plan today" — origin, destination, expected duration
- "What you'll see" — number of vehicles, expected pace, dwell points
- "What we're protecting against today" — residual risk in plain words ("we believe today's primary risk is crowd disruption at the venue arrival; we have a crowd-line in place and the path through the lobby has been swept")
- "If something happens" — what the principal does on a "go-loud" command (head down, stay in vehicle, follow my hand on your shoulder)
- A short "what we don't know" — uncertainty disclosed in plain words ("the venue's loading dock has not been swept; we will not use it")

Output: `outputs/<window>/principal-brief-<YYYY-MM-DD>.md`.

### 4. Distribution Discipline
- All artefacts use placeholders (`[PRINCIPAL]`, `[VENUE_A]`) in their synced form. The fielded copy substitutes real names at print time.
- Print, sign, distribute, recover unused copies, destroy per unit policy.
- Never email a non-sanitized brief over open networks.

## Decision Rules

- If the operational brief exceeds 12 pages: the plan is too complex; the detail won't read it. Push complexity into the drill cards and trim the narrative.
- If the driver brief doesn't fit on one page: cut content, not font. A 6-pt-font driver brief fails the test.
- If the principal-facing brief contains tradecraft jargon ("CAT", "VBIED standoff", "deconfliction"): rewrite. The principal is not a tradecraft consumer.
- If the residual ceiling is exceeded: do not produce a brief that pretends the movement is approved. Stop, and surface the gap to the detail leader.
