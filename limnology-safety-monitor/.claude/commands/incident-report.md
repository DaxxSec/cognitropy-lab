# /incident-report — Field Safety Incident Documentation

Document a field safety incident or near-miss with full detail for institutional reporting.

## Procedure

1. Gather incident details from the user:
   - **Date, time, location** (GPS if available)
   - **Personnel involved** (names, roles)
   - **Incident type:** Person in water, chemical exposure, equipment failure, medical event, weather event, wildlife encounter, vehicle/boat incident, other
   - **Description:** What happened, in chronological order
   - **Immediate response:** What actions were taken at the scene
   - **Injuries or exposures:** Type, severity, treatment provided
   - **Equipment damage or loss**
   - **Environmental conditions** at time of incident (weather, water temp, visibility)

2. Classify severity:
   - **Near-miss:** No injury or damage, but potential was present
   - **Minor:** First-aid level injury, no lost work time
   - **Moderate:** Medical treatment required, temporary work restriction
   - **Serious:** Hospitalization, significant injury, or significant equipment loss
   - **Critical:** Life-threatening, permanent disability, or fatality

3. Conduct preliminary root cause analysis:
   - Was the hazard identified in the pre-deployment risk assessment?
   - Were safety protocols followed? If not, which were bypassed and why?
   - Was equipment functioning properly?
   - Were weather/environmental conditions a factor?
   - Were personnel adequately trained for the situation?

4. Generate corrective action recommendations:
   - Immediate actions (equipment repair, protocol updates, personnel restrictions)
   - Short-term (training, equipment procurement, procedure revision)
   - Long-term (systemic changes, policy updates)

5. Output the incident report to `outputs/incident-[DATE]-[TYPE].md` and log a summary in `work-log/`.

6. Remind the user of required notifications:
   - Institutional safety office (within 24 hours for moderate+)
   - Regulatory agencies (if environmental release or public health impact)
   - Insurance carrier (if property damage or injury claim)
