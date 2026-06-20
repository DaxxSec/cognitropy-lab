# venue-advance-survey

## Purpose

Use when arriving at a venue for the in-person advance survey. Structures the walk-through against the venue-type-specific checklist and the trip threat tier overlay, producing the signed-off survey artifact.

## Prompt Template

```
Acting as the advance agent conducting an in-person venue survey.

Venue context:

- **Venue identifier:** [name, address, jurisdiction]
- **Venue type:** [residence / hotel / official building / public event / religious institution / restaurant / transit point]
- **Visit purpose at this venue:** [bilateral / address / social / transit]
- **Anticipated time on site:** [VALUE]
- **Anticipated media exposure:** [none / pool / open press]
- **Trip threat tier:** [T1 / T2 / T3 / T4]
- **Venue POC:** [name + role + contact]
- **Host-nation police partner:** [agency + POC]
- **Prior trip notes (if any):** [VALUE]

Please:
1. Run the venue-type-specific checklist from /venue-survey-checklist; produce a structured walk-through plan.
2. Apply the threat-tier overlay — identify additional sections that activate (TSCM, counter-surveillance, additional standoff requirements).
3. Identify the vulnerability profile — sightlines, standoff distances, HVAC reentry, mailroom processing, vendor/staff access.
4. Identify the holding-room candidates + the hard-room/safe-area location.
5. Identify primary evac route + alternates + shelter-in-place location.
6. Recommend jurisdiction support requirements — host-nation police presence type/count, EMS pre-position, fire support standby.
7. Document the survey items requiring photo evidence (subject to venue OPSEC posture).
8. Identify any deviations from protocol expectation; propose mitigation.
```

## Expected Output

- Structured walk-through plan
- Threat-tier-overlay activations
- Vulnerability profile + holding-room + hard-room
- Evacuation plan summary
- Jurisdiction support requirements
- Photo evidence list
- Deviation log with proposed mitigations

## Notes

- Survey is conducted IN PERSON; this prompt structures the walk-through, doesn't replace it.
- Photo-document vulnerability-relevant items; do not photograph items that violate venue OPSEC or host-nation regulations.
- Sign-off requires advance agent + RSO + venue POC; all three signatures are non-negotiable.
- Re-survey on every visit even if recently surveyed — venue staff turnover, construction, neighbour changes are common.
