# Constraints & Boundaries

> Populated by `/onboard` — edit as needed.

## Statutory / Code Boundaries (NON-NEGOTIABLE)
- **Pedestrian timing:** MUTCD 2009 §4E.06 — walk interval ≥ 7 s (preferred) or ≥ 4 s (minimum); pedestrian clearance interval at 3.5 ft/s walk speed (3.0 ft/s where slower-moving pedestrians are anticipated). Total walk + clearance must accommodate the longest pedestrian crossing distance. Do NOT propose timing that violates these.
- **Yellow change interval:** Per ITE Recommended Practice "Determining Vehicle Change Intervals" — `Y = t + (1.47 * V) / (2 * a + 64.4 * G)` with `t = 1.0 s`, `a = 10 ft/s2`, `G` = approach grade. Minimum 3.0 s, maximum 6.0 s.
- **Red clearance:** Long enough to clear the intersection at the approach speed.
- **ADA / PROWAG:** APS pushbutton, audible/vibrotactile signals where required.

## Agency / Policy Boundaries
- Posted speed limit and 85th-percentile speed (do not design coordination above the lower of the two).
- Maximum allowable cycle length per agency policy (commonly 120–150 s; some downtown grids cap at 90 s).
- Transit signal priority deployment policy (extension limit, priority frequency).
- Bicycle minimum green and clearance per NACTO Urban Bikeway Design Guide.

## Air-Quality / Environmental Boundaries
- Conformity SIP commitments — emissions cannot increase if corridor sits in non-attainment basin.
- Local Climate Action Plan CO2-eq reduction targets (cite year and baseline).
- Noise ordinance Leq limits if residential adjacency triggers them.

## Funding Boundaries
- CMAQ eligibility test (must show air-quality benefit; non-attainment area).
- HSIP eligibility test (safety benefit, separate FBA).
- TSMO funds vs. capital — most retiming uses operating funds, not capital.

## Technical / Data Boundaries
- Detector inventory: which approaches have presence vs. count detection, where dilemma-zone detection is missing.
- Communication backhaul: which intersections are on fiber/cellular vs. isolated.
- Controller firmware: NTCIP 1202 v03A object support varies; verify before assuming centralized timing push.

## Out of Scope
- Geometric changes (lane additions, channelization).
- Detector hardware procurement.
- Anything requiring a Conditional Use Permit.
