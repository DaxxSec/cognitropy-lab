# /venue-survey-checklist

Produce a venue-specific survey checklist tied to venue type (residence, hotel, official building, public event) and the trip's documented threat tier.

## Inputs

- **Venue identifier** — name, address, jurisdiction.
- **Venue type** — private residence, hotel, official government building, embassy, public event venue, religious institution, restaurant, transit point (airport, station).
- **Protectee tier** + **trip threat tier** as established by `/trip-advance-plan`.
- **Visit purpose** — bilateral meeting, public address, media event, social function, transit.
- **Anticipated time on site** (minutes / hours) and **media exposure** (none / pool / open press).
- **Local security partner** — host-nation police, embassy MSG, contracted in-country team.

## Steps

1. Read `context/concepts.md` "Venue-survey methodology" + the protocol matrix for the venue type at the documented threat tier.
2. Select the venue-type-specific checklist (residence vs. hotel vs. official building vs. public event vs. transit have materially different sections).
3. Populate the checklist with venue specifics — entry/egress points, holding-room candidates, motorcade staging, evacuation routes, hospital pre-positioning distance/time.
4. Add the threat-tier overlay — at elevated tiers, additional sections activate (counter-surveillance sweep, technical surveillance countermeasures (TSCM) request, additional standoff distance requirements).
5. Identify the venue's vulnerability profile — sightlines, standoff distances, HVAC reentry, mailroom processing, vendor/staff access, guest screening, parking-area access.
6. Map jurisdiction support requirements — host-nation police presence type/count, EMS pre-position, fire support standby, hospital pre-notification.
7. Document the venue's contingency posture — primary evac route, alternates, shelter-in-place location, hard room/safe area.
8. Write the checklist to `outputs/venue-surveys/<trip-id>/<venue-id>-checklist.md` with sign-off slots for advance agent + RSO + venue POC.
9. Conduct the survey in person; populate fields with actual observations + photos.

## Output

A markdown checklist + supporting photos at `outputs/venue-surveys/<trip-id>/<venue-id>-checklist.md`. Each item has: protocol reference, expected value, observed value, deviation note (if any), sign-off. Photos in subdirectory with explicit captions tied to checklist items.

## Decision points

- **If the venue cannot be surveyed in person before the visit** → flag as elevated risk; either cancel that increment, conduct virtual survey + remote-eyes verification, OR reduce time-on-site to absolute minimum with elevated motorcade presence.
- **If the venue's vulnerability profile triggers threat-tier escalation** → re-engage `/motorcade-config` and `/contingency-tree` for that increment specifically.
- **If host-nation police presence at the venue is below protocol minimum** → request increase via embassy DCM channel; if denied, document risk + brief detail leader + protectee.

## Notes

- Venue types differ substantively. A hotel checklist has 50+ sections (housekeeping access, room-service vector, parking-garage egress, freight-elevator routing). An official-building checklist has different emphasis (host-nation building security, accreditation, inner-cordon control). Use the correct base template.
- Photos are protocol-required for vulnerability-relevant items (sightlines, screened standoff distances, evac routes); store with explicit OPSEC handling.
- Re-survey on every visit even if you've been to the venue before — venue staff turnover, construction, new neighbours, and policy changes are common between visits.
