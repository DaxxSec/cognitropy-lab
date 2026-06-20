# /aar-debrief

Run the structured After Action Review against the trip's protocol matrix — what worked, what didn't, protocol revision proposals — within 72 hours of trip conclusion.

## Inputs

- **Trip identification** + dates + jurisdictions.
- **Pre-trip artifacts** — advance plan, venue surveys, route recons, motorcade configs, contingency tree, comms audit, threat-stream briefs.
- **In-trip log** — protocol checklist sign-offs, deviation logs, threat-stream updates, comms event log.
- **Detail team** — agents, drivers, CAT lead, medical, intel support.
- **Outcomes** — incidents (if any), close calls, near-misses, complaints.

## Steps

1. Read `context/workflows.md` "Post-trip debrief" + `context/concepts.md` "AAR doctrine".
2. Convene the AAR session — all detail members present in person or by secure conference; lockout external interruptions.
3. Walk through trip chronologically — each increment, each venue, each protocol checkpoint.
4. Per increment, ask the canonical AAR questions:
   - **What was planned to happen?**
   - **What actually happened?**
   - **What went well?**
   - **What didn't go well?**
   - **What protocol revision would address what didn't go well?**
5. Document every deviation from protocol — intentional and inadvertent.
6. Identify pattern findings — recurring issue across venues / increments / jurisdictions.
7. For each pattern, draft a protocol revision proposal — specific, actionable, accountable.
8. Identify training-need findings — specific to a team member or to the team collectively.
9. Identify equipment-need findings — what gear was missing or inadequate.
10. Generate the AAR memo at `outputs/aars/<trip-id>/aar-<YYYY-MM-DD>.md` with: trip summary, per-increment findings, pattern findings, protocol revision proposals, training-need findings, equipment-need findings, sign-off by detail leader + RSO.
11. Circulate to detail leadership + RSO for review + sign-off.
12. Submit protocol revision proposals to the practice's protocol-governance review.

## Output

A markdown AAR memo at `outputs/aars/<trip-id>/aar-<YYYY-MM-DD>.md` containing: trip summary, per-increment findings (what was planned / what happened / what went well / what didn't / revision proposal), pattern findings across increments, training + equipment needs, protocol revision proposals (specific + actionable), sign-off block.

## Decision points

- **If AAR surfaces a serious near-miss not previously reported** → escalate to RSO leadership immediately; do not let the AAR be the only documentation.
- **If pattern findings indicate systemic gap** → propose DMAIC-equivalent process improvement project; this is bigger than per-trip protocol revision.
- **If a team member's performance was substantially below standard** → handle through detail-leader chain separately from AAR; protect AAR's openness by separating performance-review channels.

## Notes

- AAR is candid by design — protect openness by keeping it from performance-review channels.
- Within 72 hours is non-negotiable; memory fades fast, and inter-trip transitions blur findings.
- Patterns matter more than per-incident findings — track patterns across multiple trips to surface systemic gaps.
- Protocol revisions must be actionable and accountable — name the owner, define the change, schedule the review.
