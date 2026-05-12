# Advance Arrival Survey Prompt

## Purpose
Use this prompt when you need a structured advance survey of an arrival venue (hotel, conference centre, airport FBO, residence). It steps through chokepoint identification, vehicle-borne approach analysis, IED predictability, and exfil planning, with risk-matrix scoring on every component.

## Prompt Template

I'm conducting an advance for the principal codenamed `[CODENAME]` at the following arrival venue:

- **Venue type:** [hotel / conference centre / FBO / residence / restaurant / other]
- **Address (general — neighbourhood ok, building ok):** [...]
- **Arrival window:** [date/time, expected duration of dwell]
- **Mode of arrival:** [motorcade / walk-up / aviation transfer]
- **Public exposure level:** [closed / semi-public / public / press-attended]
- **Active matrix posture for vehicle-borne and IED rows:** [Y / O / R, per the engagement matrix]

Please walk me through the advance using the workspace's `/route-survey --venue` workflow:

1. **Chokepoints at the venue** — gate, entry, lobby, elevator, room/floor transitions. For each:
   - Forced or mitigable (alternates exist)?
   - Concealment availability
   - Standoff distances

2. **Vehicle-borne approach analysis** — for each ingress lane:
   - Maximum attainable speed by attacker class given lane length
   - Hand off to `/crash-kinematics` for the worst-credible scenario
   - Bollard / barrier rating audit (ASTM F2656 / PAS 68 / IWA 14-1) at each entry

3. **IED predictability** — fixed roadside features, parking spots within 30 m of principal's path, inspection regime status

4. **Exfil paths** — primary, alternate, contingency from each chokepoint, with drivability for our principal-vehicle class (state class explicitly)

5. **Surveillance-detection windows** — likely hostile observation positions and our pre-deploy options

6. **Recommendation** — proceed / proceed-with-mitigation / change venue / reschedule, with specific mitigation actions if proceed-with-mitigation

## Expected Output

- Annotated chokepoint table
- Kinematics-derived AIS band for the credible vehicle-borne scenario at this venue
- Bollard / HVM verdict (covers credible class? gap?)
- Exfil plan (P/A/C)
- Pre-deploy SD recommendations
- Posture for this venue, with cell trace
- Specific actions with owners (you / venue management / LE liaison / detail) and timing

Save outputs to `planning/route-survey-<engagement-id>-arrival.md` and update the active threat assessment if posture changes.
