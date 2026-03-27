# /site-risk — Field Site Hazard Assessment

Perform a pre-deployment site risk assessment for a limnological field site.

## Procedure

1. Ask the user to provide site details:
   - Water body name and type (lake, river, reservoir, wetland)
   - GPS coordinates or general location
   - Planned activities (boat-based sampling, shore-based, through-ice, wading)
   - Date/time window for field work
   - Number of personnel

2. Evaluate each hazard category using the matrix from `context/for-agent/workflows.md` (Workflow 1, Step 2):
   - Drowning risk
   - Exposure risk (heat, cold, UV)
   - Biological hazards (HABs, pathogens, wildlife)
   - Chemical hazards
   - Mechanical hazards
   - Access/remoteness
   - Weather

3. Score each category 1-5 and calculate total risk score.

4. Apply the risk interpretation scale:
   - 7-14: LOW — Proceed with standard precautions
   - 15-21: MODERATE — Enhanced PPE, strict buddy system, regular check-ins
   - 22-28: HIGH — Safety officer approval required, enhanced emergency plan
   - 29-35: EXTREME — No-go without institutional review

5. Check for hard no-go triggers (any single factor is sufficient to abort).

6. Generate a **Site Risk Assessment** document including:
   - Hazard matrix with scores and justifications
   - Overall risk level
   - Specific mitigation measures for each elevated hazard
   - Required safety equipment list
   - Emergency action plan (nearest hospital, emergency contacts, GPS coordinates)
   - Go/No-Go recommendation with clear rationale

7. Save the assessment to `outputs/` with filename: `site-risk-[SITE]-[DATE].md`
