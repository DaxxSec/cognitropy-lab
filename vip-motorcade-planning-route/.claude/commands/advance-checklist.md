# /advance-checklist — Pre-Movement Advance Team Checklist

Generate the advance team checklist for a specific movement leg, anchored to the chosen primary route.

## Required Inputs
- Route decision at `planning/route-decision-<YYYY-MM-DD>.md`
- Lead time available (T-72 h / T-24 h / T-12 h / T-4 h)
- Advance team composition (count, roles)

## Procedure

### 1. Lead-Time Tier
The depth of the checklist depends on lead time:

- **T-72 h:** Full deep advance — counter-surveillance setup, route drive, venue advance, hospital network confirmation, host-nation liaison brief.
- **T-24 h:** Standard advance — route drive, venue arrival/departure points, hospital confirmation, comms test.
- **T-12 h:** Compressed — route drive, top-3 chokepoints inspected, comms test, abort confirmed open.
- **T-4 h (rolling advance):** Drive-immediately-ahead, top-3 hazards visually cleared, no full physical sweep.

### 2. Items by Domain

#### Counter-Surveillance
- [ ] CS team in place ≥ 6 h before movement (full advance) / on-net at T-1 h (compressed)
- [ ] Static observation of motorcade origin / destination / dwell points
- [ ] Mobile CS run on the primary route within 12 h
- [ ] Indicator log started; flag if any of the priority indicators surface
- [ ] Vehicle plate / face check against host-nation persons-of-interest list (where lawfully shared)

#### Physical Sweep
- [ ] Motorcade vehicle sweep — under-vehicle inspection, interior IED check (per host-nation EOD trained operator)
- [ ] Garage / staging area access controlled and logged
- [ ] Route drive within window — flag construction, road closures, parked-vehicle changes vs survey
- [ ] Top-N chokepoints visually re-checked at T-2 h
- [ ] Venue arrival point and curtilage swept; egress route confirmed unblocked

#### Liaison
- [ ] Host-nation police lead — confirmed on-net and aware of window
- [ ] Traffic control — confirmed for any planned closures
- [ ] Hospital network — primary trauma facility on-call, ED contact confirmed; secondary as backup
- [ ] Embassy RSO (if applicable) — duty officer aware of movement
- [ ] Fire / rescue (for crowd or large venue) — aware of crowd plan

#### Comms
- [ ] Encrypted handheld test on motorcade net — every vehicle, every member
- [ ] Cellular fallback confirmed (signal in tunnels, dead zones documented)
- [ ] Satellite check (if used)
- [ ] Callsign / channel discipline brief delivered to all detail members

#### Documentation
- [ ] Operational brief printed and distributed (and prior copies destroyed per unit policy)
- [ ] 1-page driver briefs in each vehicle
- [ ] Drill cards (top-3) laminated for principal vehicle
- [ ] MEDEVAC routes printed and in every vehicle
- [ ] Principal-facing brief delivered to principal's chief of staff (sanitized)

### 3. Output
Write `outputs/<window>/advance-checklist-<YYYY-MM-DD>.md` with:
- Header: window codename, leg, lead-time tier, advance team lead placeholder
- Checklist items with `[ ]` boxes for sign-off
- Findings section — anything the advance team flagged that changes the plan (and what changed)
- Sign-off line

Log to `work-log/<YYYY-MM-DD>-advance-<leg>.md`.

## Decision Rules

- If counter-surveillance flags an indicator (vehicle, individual, pattern) — pause the movement until cleared. Default is *not* to push through.
- If a chokepoint is *blocked* by something not in the survey (truck unloading, accident, demonstration) — declare the segment temporarily unsurveyable, switch to alternate.
- If hospital-network primary has gone offline (no beds, lockdown) — re-rank to secondary and update brief before movement.
- If the advance team itself is targeted (surveillance against advance, attempted contact) — the entire movement is escalated; route decision is re-opened.
