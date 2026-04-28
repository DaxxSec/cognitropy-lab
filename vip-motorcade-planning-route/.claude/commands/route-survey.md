# /route-survey — Segmented, Geocoded Route Survey

Convert a candidate route into a numbered list of segments with the per-segment data required for `/risk-score`.

## Required Inputs
- Route as GPX / KML / address pair / paper drive
- Codename for the route (`PRIMARY-A`, `ALT-1`, `ABORT-X`)
- Origin and destination
- Time-of-day for the planned movement (traffic, daylight, crowd density vary)
- Source of survey: physical drive (preferred), advance team report, imagery only

## Procedure

### 1. Confirm Survey Source
- Tier 1 / high-threat post: physical drive is mandatory; refuse to score from imagery alone.
- Tier 2: physical drive within 7 d preferred; recent advance-team drive acceptable.
- Tier 3: imagery + recent street-level review acceptable.

If the survey source is below the tier minimum, emit a warning and stop until the user confirms either (a) it's been driven, or (b) we are doing an unscored *preliminary* survey only.

### 2. Segment the Route
Walk the route from origin to destination. A new segment starts whenever any of these change:
- Roadway geometry (lane count, divided/undivided, on/off ramp)
- Speed regime (highway / urban / parking deck)
- Building density / line-of-sight (urban canyon → boulevard → suburban)
- Choke condition (single lane, bottleneck, controlled intersection)
- Jurisdictional boundary (county line, district)
- Ingress/egress availability (alternate exits per minute)

Aim for 15–35 segments on a 20-minute urban leg. Number segments S01, S02, ...

### 3. Per-Segment Data Capture
For each segment, capture:

| Field | Notes |
|-------|-------|
| `id` | S01, S02, … |
| `start_lat`, `start_lon` | Decimal degrees, 5 places |
| `end_lat`, `end_lon` | Same |
| `length_m` | Approx ground distance |
| `speed_regime` | highway / urban / dense-urban / parking |
| `lane_count` | Total in motorcade direction |
| `los_standoff_m` | Minimum line-of-sight standoff to plausible firing position |
| `chokepoint` | true / false (and why) |
| `ingress_egress_count` | Number of alternate exits within the segment |
| `jurisdictional_zone` | Police district / municipality |
| `liaison_reachable` | Y / N — host-nation police comms work here |
| `crowd_density_peak` | Persons / 100 m² at planned T-0 |
| `dominant_hazards` | List from the typology in `domain-knowledge.md §2` |
| `notes` | Free text — construction, prior incidents, blind corners, parked vehicles |

### 4. Photo / Imagery Log
For physical-drive surveys, photograph every chokepoint and every segment's "worst feature." File path goes in the survey under `photos[]`. Photos themselves go to `outputs/<route-codename>/photos/` flagged `confidential-do-not-sync` (real geometry of real routes is sensitive).

### 5. Output
Write the survey to `outputs/<route-codename>/survey.md` with:
- Header: route codename, origin, destination, time of day, source-of-survey, surveyor name placeholder
- Segment table (the fields above)
- A summary "exposure profile" — count of chokepoints, count of dense-urban segments, total length, est. travel time, est. travel-time variance

Log to `work-log/<YYYY-MM-DD>-survey-<route-codename>.md`.

## Decision Rules

- If a segment is uniformly low-exposure for >2 km: split anyway every 1.5 km — long unsegmented stretches hide variance.
- If a segment changes characteristics mid-stretch (a chokepoint partway through): split there.
- If you cannot reach the segment to drive it (closed road, restricted area): mark `los_standoff_m = unknown` and `notes = surveyed by imagery only`. Such segments cap at residual ≤ Moderate during scoring; a real attack vector cannot be mitigated by guessing.
