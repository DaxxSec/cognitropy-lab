# protectee-threat-intake

## Purpose

Use at the start of a new trip when receiving the protectee + trip notification. Establishes the structured threat picture and tier baseline that all subsequent advance planning will reference.

## Prompt Template

```
Acting as the advance planner during initial trip notification intake.

Protectee + trip context:

- **Protectee tier:** [cabinet / agency head / contracted senior executive / family of principal]
- **Visit purpose:** [bilateral meeting / public address / media event / social function / transit]
- **Jurisdictions touched:** [list with dates per jurisdiction]
- **Trip dates:** [arrival, departure, in-country windows]
- **Known itinerary:** [venues, meeting partners, public events]
- **Public profile of visit:** [overt media-facing / low-profile no-press / mixed]
- **Recent prior trips (last 12 months):** [list with brief threat-tier summary per trip]
- **Current intel feed status:** [DS Watch active / OSAC subscription / host-nation MOI liaison]
- **Embassy DCM:** [name + contact]

Please:
1. Establish the protectee's baseline threat tier from prior-trip patterns + current intel.
2. Per jurisdiction, propose initial threat-tier assessment based on environment + protectee + visit profile.
3. Identify gaps in the threat picture — what we need to know but don't, who can fill the gap.
4. Recommend the advance-planning phase timeline (T-30 / T-21 / T-14 / T-7 / T-3 / T-1 milestones).
5. Recommend embassy DCM engagement cadence and host-nation MOI liaison touchpoints.
6. Identify any standing agreements (SOFA / BIA / MOU) likely to be invoked or constrain operations per jurisdiction.
7. Flag immediate-action items (host-nation diplomatic clearance, embassy notification cables, intel-feed activation).
```

## Expected Output

- Per-jurisdiction threat-tier baseline with rationale
- Information gap list with named POCs to fill
- Advance timeline with phase milestones
- Embassy / host-nation engagement plan
- Standing-agreement implications
- Immediate-action checklist

## Notes

- This is the seed for `/trip-advance-plan` — outputs of this prompt feed directly into the master advance packet.
- Threat tier baseline is iterated as advance progresses — initial baseline is starting point, not final.
- "Acceptable risk" is not a planner's call to make alone — escalate to RSO + protectee chain when the threat profile crosses a clear threshold.
