# Constraints & Boundaries

> Populated by `/onboard` — edit as needed.

## Hard Flight Rules (Non-Negotiable)

These are the **hard-fail** thresholds. A traverse that violates any of these is rejected before scoring — no override, no average-it-out. Copy in the rover-platform-specific numbers from `resources/flight-rules-quickref.md`:

- **Maximum drivable slope** (e.g., Curiosity ~30° static / 25° dynamic, Perseverance similar)
- **Maximum vehicle tilt** (rocker-bogie suspension limits)
- **Maximum rock height for blind drive** (typically ~1/2 the wheel diameter)
- **Maximum rock height for AutoNav** (rover-and-FSW-version dependent)
- **Maximum drive distance per sol** (energy + stop-and-think budget)
- **Mandatory comms-pass coverage** within sol N (no plans that strand the rover beyond next pass)
- **Forbidden terrain classes** (active sand sheets unless explicitly allowed; project-defined Special Regions)

## Mission / Project Constraints

- **Planetary protection.** No traverses into Special Regions (RSL, gully alcoves with possible transient water) without project planetary-protection-officer approval.
- **Sample tube depots / cache integrity.** Where applicable, no traverses that would disturb a sample-tube depot or the cache witness panels.
- **Embargoed datasets.** If using project-internal HiRISE products that are not yet PDS-released, the workspace contents must not be shared externally.
- **Data-volume budget.** Every science block has a downlink-volume cost; the agent must track total volume against the daily budget.

## Operational Constraints

- **Energy budget.** Solar (MER, Sojourner) vs RTG (MSL, M2020) — completely different planning regimes. Solar requires sun-on-array at planned times of sol; RTG mostly cares about thermal management.
- **Thermal cycles.** Diurnal temperature swings drive sol structure (warm-up periods, blanket heater usage, no contact science during temperature extremes).
- **Comms windows.** Direct-to-Earth (DTE) and orbital relays (MRO, Mars Odyssey, MAVEN, TGO) — passes are scheduled in advance and missed passes are expensive.
- **Onboard memory.** Every science observation is data; every data product must fit through the next available downlink window.

## Ethical & Disclosure Boundaries

- **The agent is an aid, not a decision authority.** All uplinked plans must be reviewed and signed off by a human reviewer panel; the decision log captures who.
- **No over-promising autonomy.** If a segment requires AutoNav and AutoNav has known issues with the terrain class (e.g., ripple fields), the agent must flag it explicitly, not bury it in an aggregate score.
- **Open peer dissent.** A reviewer's dissent must be recorded verbatim in the decision log, even if the quorum decision is to proceed.
- **Calibrate confidence.** When the underlying terrain data is older / lower-resolution / off-nadir, the agent must derate its hazard-map confidence and surface that derating to reviewers.

## Out of Scope

- Real-time autonomy decisions during a drive (this is the sol-planning workspace, not the FSW)
- Navigation away from the planned traverse during execution (handled by the rover's onboard hazard avoidance)
- Sample selection criteria (handled by the science team's separate sample-selection workflow; this workspace plans the *traverse to* sample sites)
- Strategic mission-level decisions (campaign selection, landing-site selection — those happen at a different cadence and forum)
