# /trip-advance-plan

Generate the full advance-planning packet for a protectee visit — itinerary expansion, venue list, route candidates, contact matrix, contingency framework, protocol matrix.

## Inputs

- **Protectee tier** (e.g. cabinet-level / agency head / contracted senior executive on diplomatic-adjacent travel) — drives threat tier baseline and motorcade configuration.
- **Trip dates** (arrival, departure, in-country windows by jurisdiction).
- **Itinerary intake** — known venues, meeting partners, public-vs-private events, any media-facing components.
- **Jurisdictions touched** — host nations, transit countries, any third-country layovers.
- **Standing threat tier** for the protectee + each jurisdiction (DS Watch / OSAC / host-nation MOI baseline).
- **Available resources** — own team size, host-nation police support level, CAT availability, medical assets.
- **Constraints** — budget, time-on-ground hard caps, public-event nonnegotiables (e.g. press availability that can't be cancelled).

## Steps

1. Read `context/concepts.md` "Advance-planning fundamentals" + `context/workflows.md` "Pre-trip advance".
2. Expand itinerary into operational increments — each venue + transit between venues + lodging + media windows.
3. Per increment, assign threat tier (derived from protectee baseline + jurisdiction baseline + venue-type modifier + media-exposure modifier).
4. Identify venues requiring `/venue-survey-checklist`; queue them.
5. Identify routes requiring `/route-recon-report`; queue them.
6. Build coordination requirements via `/jurisdiction-coord-matrix` (host-nation police clearance, EMS pre-positioning, hospital pre-notification, fire support standby).
7. Propose motorcade configurations per increment via `/motorcade-config` placeholder; finalize after route recon.
8. Define contingency framework via `/contingency-tree`.
9. Run `/comms-redundancy-audit` against the planned route's known dead-zones.
10. Assemble master advance packet: itinerary increments, threat-tier-per-increment, coordination matrix, motorcade plan, contingency tree, comms plan, signal-handling escalation, OPSEC handling guidance.
11. Write packet to `outputs/advance-packets/<trip-id>/<YYYY-MM-DD>-master.md` with all attached artifacts referenced.

## Output

A markdown master packet at `outputs/advance-packets/<trip-id>/<YYYY-MM-DD>-master.md` containing: trip identification, protectee + jurisdictions + dates, per-increment threat tier, venues + routes + coordination requirements, motorcade plan, contingency tree summary, comms redundancy summary, OPSEC handling notes, sign-off block (RSO/Detail Leader).

## Decision points

- **If protectee threat tier escalates mid-planning** → revisit all increments; motorcade + contingency planning must adjust.
- **If host-nation will not grant requested coordination level** → escalate to Embassy / DS leadership; do not absorb the gap silently.
- **If a venue / route cannot be surveyed in person before the visit** → that's a documented risk; flag explicitly in packet; consider cancellation of that increment.

## Notes

- Master packet is the single source of truth for the trip; it references every other artifact and remains under change-control during pre-trip phase.
- Threat tier per increment is rarely uniform across the trip — public-facing venues + media windows + civilian-density chokepoints differ from official-building stops.
- Always include a "what we know we don't know" section — pre-trip planning has known information gaps that the AAR will close after the trip.
