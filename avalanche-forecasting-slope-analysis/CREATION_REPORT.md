# Creation Report: avalanche-forecasting-slope-analysis

## Metadata

| Field | Value |
|---|---|
| Project Day | 26 |
| Build Date | 2026-04-20 |
| Category | Outdoor & Adventure |
| Primary Domain | avalanche forecasting slope analysis |
| Technique | with predictive maintenance scheduling |
| Crossover | no |
| Rotation Reason | Engine assigned `security clearance vetting investigation` (Security & Intelligence) — a direct duplicate of an existing workspace. Rotated to Outdoor & Adventure to fill one of six uncovered categories. |

## Why This Workspace

Avalanche forecasting lives at the intersection of snow physics, terrain analysis, weather prediction, and human factors. It's a domain where:

- **The data volume is small** (a handful of study plots, weather stations, and observer reports per region), but
- **The consequence of a wrong call is extreme** — dead guides, buried skiers, blocked highways, evacuated towns.

A forecasting agent built well has to do more than pattern-match on column tests. It has to **maintain institutional memory** about persistent weak layers that may have gone quiet for weeks, track instrument calibration, keep mitigation hardware ready, and enforce language discipline in the public-facing bulletin.

That last element — the predictive-maintenance cadence — is exactly what the Cognitropy engine selected today's technique for. PM scheduling is often thought of in industrial / mechanical contexts, but it maps beautifully onto forecasting discipline:

- Scheduled snowpack tests catch PWL behavior drift.
- Scheduled instrument calibration prevents undetected weather-data corruption.
- Scheduled asset readiness checks mean when a storm cycle hits, the avalauncher does not have a cold-start problem.

## Domain Diversity Check

Categories **already** represented in the lab (19 prior workspaces):

- Cyber & DFIR, RF/SDR/Signals, Automotive & Engine, Hardware & Embedded, Engineering & Technical, Transportation & Logistics, Environmental & Earth, Security & Intelligence (x2), Space & Aviation, Computing & Software, Finance & Economics, Education & Training, Medical & Health, Food & Agriculture (x2), Earth Sciences / Life Sciences

Categories **still uncovered** entering Day 26:

- Physical Sciences
- Trades & Crafts
- **Outdoor & Adventure** <- this workspace fills this
- Arts & Creative
- History & Culture
- Unusual & Niche

## Workspace Highlights

- Six domain slash commands mapped to the real forecaster workflow: daily bulletin, snowpack analysis, slope-scale decision, mitigation planning, incident review.
- Structured **problem-type matrix** (9 official types adopted by CAIC/AAC/Avalanche Canada) as a resource file.
- Predictive-maintenance schedule template covering snow observations, instruments, explosive assets, and bulletin language audits.
- **Safety posture baked into CLAUDE.md**: never publish without a certified forecaster, never use the word "safe."
- Human-factors grounding via the **FACETS framework** (Familiarity, Acceptance, Commitment, Expert halo, Tracks/scarcity, Social facilitation) in `/incident-review`.

## Intended Users

Primary: avalanche center forecasters, ski-patrol leads, DOT highway avalanche programs, and professional guides.
Secondary: AIARE / CAA instructors building curriculum, researchers studying forecaster cognition, backcountry-ops program managers.
Not intended for: untrained recreational users seeking a "go / no go" app. This workspace assumes Level 2+ training and professional use.

## Ethical Posture

The bulletin that a forecast center publishes is a **public safety product**. The agent drafts; a human forecaster signs. InfoEx-protected observations remain protected. Explosive asset tracking in this workspace is meant to be paired with the agency's own accountability system, not to replace it.

## Ideas for Future Iteration

- Add a `/weather-brief` command that pulls NAM / HRRR model data and auto-converts to mountain-weather summary.
- Integrate ATES (Avalanche Terrain Exposure Scale) polygon reasoning for `/slope-check`.
- Extend `/incident-review` with an SHA-256 evidence manifest analogous to COSINT's approach.
- Add a companion `/curriculum-day` command for AIARE instructors reusing the problem matrix.

