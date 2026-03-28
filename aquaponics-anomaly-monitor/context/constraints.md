# Operating Constraints

## System Constraints
- **Budget for interventions:** [e.g., limited — prefer natural corrections over chemicals]
- **Chemical use policy:** [e.g., Organic certification, no synthetic chemicals]
- **Water change limitations:** [e.g., municipal water with chloramine — must dechlorinate]
- **Power infrastructure:** [e.g., Solar-backed pump, 4-hour battery backup]
- **Climate control:** [e.g., Greenhouse can maintain 15°C minimum in winter]

## Operating Hours
- **Active monitoring:** [e.g., Check twice daily — morning and evening]
- **Automated monitoring:** [e.g., IoT sensors reporting every 15 min to Home Assistant]
- **Response time:** [e.g., Can respond within 2 hours during daylight]

## Agent Preferences

### Reporting Style
- Default to **actionable alerts** with severity levels
- Reference `resources/parameter-reference.md` for threshold values
- Cross-check any chemistry recommendations against `resources/species-profiles.md`
- Prioritize fish safety over crop optimization when in conflict

### Do Not Recommend
- [e.g., Antibiotics without veterinary consultation]
- [e.g., Alum flocculants in closed systems]
- [e.g., Rapid pH corrections > 0.5 units/hour]

### Escalation Triggers
_When to tell the operator to take immediate manual action:_
- NH3 > 1.0 ppm AND DO < 5 mg/L simultaneously
- pH < 5.5 or > 9.0
- Temperature deviation > 4°C from normal baseline
- NO2 > 1.0 ppm sustained > 2 hours
- Visible fish mortality > 5%
