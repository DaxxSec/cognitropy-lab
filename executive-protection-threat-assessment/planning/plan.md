# Active Plan

> One file. One plan. Pivots go in `pivots/` (create on first pivot).

## Engagement under plan

- **Engagement-id:** _(set by `/onboard`)_
- **Principal codename:** _(set by `/onboard`)_
- **Window:** _(set by `/onboard`)_
- **Geography:** _(set by `/onboard`)_

## Current posture

- **Aggregated posture:** _(updated by latest `/threat-assessment`)_
- **Driving cells:** _(matrix cells colour-coded Orange or Red)_
- **Last matrix refresh:** _(ISO date)_
- **Last pre-attack indicator scan:** _(ISO date — must be ≤ 14 days)_

## Workflow status

| Workflow | Run | Last run | Next due |
|----------|-----|----------|----------|
| `/onboard` | Y/N | | one-time per principal |
| `/risk-matrix` | Y/N | | quarterly OR on threat shift |
| `/threat-assessment` | Y/N | | per engagement |
| `/route-survey` | Y/N (per leg) | | per engagement leg |
| `/crash-kinematics` | Y/N (per scenario) | | per credible vehicle-borne row |
| `/protective-formation` | Y/N | | per engagement |
| `/report-findings` | Y/N | | once posture is finalised |

## Open mitigation actions

| # | Action | Owner | Due | Driving cell | Status |
|---|--------|-------|-----|--------------|--------|
| 1 | _(specific action)_ | _(role)_ | _(date)_ | _(matrix coord)_ | _(open/in-progress/complete)_ |

## Decisions log

| Date | Decision | Driver | Made by |
|------|----------|--------|---------|
| _(ISO)_ | _(decision)_ | _(matrix cell or external trigger)_ | _(detail role)_ |

## Pivots

If posture changes materially mid-cycle (new pre-attack indicator, geography shift, principal mission change), record the pivot in `pivots/<ISO-date>-<short-name>.md` and link from the decisions log here.

## Next review

- **Date:** _(ISO)_
- **Trigger:** _(scheduled / engagement T-7d / pre-attack indicator)_
- **Required artefacts to refresh:** _(list)_
