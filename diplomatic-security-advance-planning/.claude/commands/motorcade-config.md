# /motorcade-config

Recommend motorcade configuration (lead, follow, CAT, control, decoy) sized to threat tier, available jurisdictional support, and venue topology.

## Inputs

- **Threat tier** for the increment (from `/trip-advance-plan`).
- **Available assets** — own vehicles + drivers, host-nation police escorts, CAT availability, medical assets.
- **Route topology** — chokepoints, civilian density, urban vs. open road, tunnels/bridges, controlled intersections, parade-route requirements.
- **Protectee characteristics** — single principal vs. delegation, family members, working staff requirements (binders, secure comms), medical considerations.
- **Visit visibility** — overt (motorcycle escorts, flashing lights) vs. low-profile (single vehicle, plainclothes).
- **Jurisdictional rules** — host-nation regulations on weapons in vehicles, vehicle type restrictions, escort speed limits.

## Steps

1. Read `context/concepts.md` "Motorcade doctrine" + `context/references.md` "Motorcade configurations" lookup.
2. Select base configuration template for the threat tier (T1 = 3-vehicle low-profile; T2 = standard 5-vehicle; T3 = enhanced 7-vehicle with CAT; T4 = full motorcade with decoy + CAT + control).
3. Adjust for route topology:
   - **High civilian density urban** — add control vehicle, reduce overall length, prefer host-nation motorcycle pace
   - **Open road / autobahn** — extended formation, increase follow distance, lead vehicle scouts ahead
   - **Tunnels** — minimize formation length, pre-position EMS at egress, alternate route plan ready
4. Adjust for protectee characteristics:
   - **Delegation** — add follow vehicles for working staff, dedicated comms vehicle
   - **Family** — separate family vehicle in formation, additional CAT coverage
   - **Medical considerations** — co-locate medical asset in formation, hospital pre-positioning
5. Document vehicle-by-vehicle:
   - Vehicle role (lead / control / VIP / follow / CAT / decoy / medical)
   - Crew (driver, agent / officer count, weapons load if authorised)
   - Equipment (armoured / soft-skin, ballistic windows level, comms suite, medical pack)
   - Position in formation (with spacing)
6. Document movement protocols — speed band, intersection handling (motorcycle leapfrog vs. host-nation hold), lane discipline, communication frequencies.
7. Document deviation handling — what triggers a configuration upgrade mid-trip.
8. Write configuration to `outputs/motorcade-configs/<trip-id>/<increment-id>-config.md`.

## Output

A markdown configuration at `outputs/motorcade-configs/<trip-id>/<increment-id>-config.md` containing: increment identification, threat-tier rationale, vehicle list (role, crew, equipment, position), movement protocols, communication plan, deviation triggers, signature block (RSO + Detail Leader + host-nation liaison).

## Decision points

- **If host-nation will not provide requested escort level** → either request waiver via DCM, accept the gap and document, or restructure the trip to avoid the increment.
- **If CAT is unavailable** → either restructure threat tier evaluation (CAT is a key mitigator for T3+), or reduce time-on-route at exposed segments.
- **If route topology forces a single-lane chokepoint** → pre-position counter-assault assets at the chokepoint OR change routes.

## Notes

- Motorcade doctrine varies by service (DS DSS, USSS, DSS protective details, private EP). Cite the applicable doctrine reference in the configuration so reviewers can audit.
- Vehicle armouring level (B4, B6, B7) drives ballistic protection but increases weight + reduces speed; choose based on threat profile and route demands.
- Decoy vehicles only function if visibility profile matches the real motorcade; a decoy in a low-profile run is itself a vulnerability indicator.
- Rehearsal is non-negotiable for new formations or new routes. Schedule rehearsal slot in the advance plan; don't skip even under time pressure.
