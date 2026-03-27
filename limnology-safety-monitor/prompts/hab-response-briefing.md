# Prompt: HAB Response Briefing

Generate a Harmful Algal Bloom response briefing for stakeholders.

## Input Variables
- `{WATER_BODY}` — Name of the affected lake/reservoir
- `{DATE_DETECTED}` — Date of initial bloom detection
- `{MICROCYSTIN_LEVEL}` — Measured microcystin concentration (μg/L)
- `{SPATIAL_EXTENT}` — Localized or lake-wide
- `{AFFECTED_USES}` — Recreation, drinking water, irrigation, etc.

## Prompt

You are a limnological safety specialist responding to a harmful algal bloom on {WATER_BODY}, first detected on {DATE_DETECTED}. Microcystin concentration measured at {MICROCYSTIN_LEVEL} μg/L. Bloom extent: {SPATIAL_EXTENT}. Affected uses: {AFFECTED_USES}.

Generate a response briefing that includes:

1. **Current Status** — Advisory level (Caution/Advisory/Warning/Danger based on concentration), bloom description, extent

2. **Health Risk Assessment** — Routes of exposure (skin contact, ingestion, inhalation of spray), vulnerable populations (children, pets, immunocompromised), specific risks based on affected uses

3. **Immediate Actions Required** — Public notifications, area closures, signage, water utility notifications (if drinking water source), pet owner warnings

4. **Field Team Safety** — Required PPE for ongoing monitoring, exposure time limits, decontamination procedures

5. **Monitoring Plan** — Sampling frequency increase, additional sampling locations, parameters to add (phycocyanin, species ID, additional toxins)

6. **Communication Template** — Draft public advisory notice suitable for posting at access points and distributing to media

7. **Escalation Criteria** — What conditions would trigger the next advisory level

Keep all recommendations specific and actionable. Include exact thresholds and reference EPA recreational water quality criteria.
