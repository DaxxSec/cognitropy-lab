# /advance-survey

Run a venue / residence / route advance security survey, derive protective decisions (not just an inventory), and grade it as the EPA-1 workplace-based assessment.

## Inputs

- Site type and address/details; planned principal activity and timing
- Floor plans / maps / prior surveys if available
- Threat tier from the principal's risk profile
- Apprentice author + current EPA-1 entrustment level

## Steps

1. Walk the **CPTED** survey: natural surveillance, access control, territorial reinforcement, maintenance.
2. **CARVER** the site from the adversary's perspective — find single points whose loss equals mission failure.
3. Run the advance decision tree (`context/workflows.md` §3): safe haven within 30s, nearest Level I/II trauma center + time-distance, observable APOD, command post, access/magnetometer plan.
4. Produce **primary / alternate / emergency routes** for arrival and egress.
5. Compile a **vulnerability register** with owners and a site-specific **EAP** hook (hand to `/eap-builder`).
6. Record the **EPA-1** entrustment observation — was the output decisions-derived or just a list?

## Output

`outputs/advance-<site>-<date>.md` — CPTED + CARVER findings, decision tree results, routes, safe haven, medical plan, command post, vulnerability register, and EPA-1 evidence footer.

## Notes

- "Time spent in advance is never wasted." The grade hinges on whether the survey produced **decisions**, not whether it filled in every field.
