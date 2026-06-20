# /comms-redundancy-audit

Audit primary + alternate + emergency communications (P25, GSM, satellite, runner protocols) against the trip's routes and venues — identify dead zones, single-points-of-failure, and protocol gaps.

## Inputs

- **Primary comms** — P25 / Tetra / VHF / UHF radios + frequency assignments + repeater locations.
- **Alternate comms** — GSM / 4G phones + carriers + roaming agreements.
- **Emergency comms** — satellite phones (Iridium, Inmarsat), SATCOM-on-the-Move (SOTM), HF backup.
- **Runner protocol** — vehicle-to-vehicle hand signals, pre-positioned runners at venues.
- **Routes** + **venues** from prior commands.
- **Known dead zones** — tunnels, basement levels, high-density urban canyons, underground parking.

## Steps

1. Read `context/references.md` "Communications channels" + `context/concepts.md` "Comms doctrine".
2. Per route, identify dead-zone segments — tunnels, urban-canyon corridors, basement parking transitions.
3. Per venue, identify indoor dead zones — basements, freight elevators, mechanical floors, kitchens.
4. Per dead zone, identify mitigation — DAS (Distributed Antenna System) at venue, repeater positioning, satellite backup, runner protocol.
5. Validate each comms method actually works at the dead zone — test in person during pre-trip, don't rely on coverage maps.
6. Document single-points-of-failure — if primary repeater fails, what's the recovery path? If host-nation comms infrastructure goes down, what's independent?
7. Map encryption / OPSEC posture — which channels carry which classification, who has keys, key-rotation schedule for visit window.
8. Document runner protocol — pre-positioned at venues, hand-signal vocabulary, runner-to-detail-leader chain.
9. Write audit report to `outputs/comms-audits/<trip-id>/comms-audit.md`.
10. Brief detail leader + agents on dead-zone mitigations before visit.

## Output

A markdown audit report at `outputs/comms-audits/<trip-id>/comms-audit.md` containing: comms inventory, per-route dead-zone analysis, per-venue dead-zone analysis, mitigation plan per dead zone, single-points-of-failure list with recovery paths, encryption / OPSEC posture, runner protocol.

## Decision points

- **If a critical segment (motorcade route) has no working comms** → mitigate via runner / SATCOM / route change before trip; do not accept uncovered.
- **If host-nation comms infrastructure can be unilaterally controlled (cellular shutdown)** → ensure independent SATCOM is operational and tested.
- **If venue dead zone covers a high-time-on-site area** → DAS request to venue, or in-venue runners, or move the area outside the dead zone.

## Notes

- Dead zone coverage from public databases or carrier maps is approximate; physical test is required.
- P25 / Tetra encryption + key management is separate from the device's ability to transmit — both must be validated.
- Runner protocols are old-school but proven; never skip even with rich digital comms.
- Comms posture changes between calm pre-trip and active visit — test under conditions that match active visit (vehicle in motion, multiple-channel traffic, jamming scenarios).
