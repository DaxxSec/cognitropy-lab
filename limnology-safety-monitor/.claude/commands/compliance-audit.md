# /compliance-audit — Sampling Procedure Compliance Review

Audit sampling procedures against regulatory standards and institutional requirements.

## Procedure

1. Ask the user which framework(s) to audit against:
   - EPA Clean Water Act monitoring requirements
   - State-specific DEQ/DEP standards (ask which state)
   - QAPP (Quality Assurance Project Plan) — does the user have one?
   - Institutional field safety policy
   - OSHA occupational safety requirements

2. Walk through each audit category from `context/for-agent/workflows.md` (Workflow 7):

### Personnel Qualifications
   - First aid / CPR certifications — current?
   - Boat operator certification — state-specific requirements met?
   - Institutional safety training — completed and documented?
   - Swim proficiency documentation

### Equipment Maintenance
   - Calibration records — current, complete, within tolerance?
   - Safety equipment inspection dates — within compliance window?
   - Watercraft registration and required safety equipment?
   - Communication equipment — tested and functional?

### Sampling Procedures
   - Methods match approved QAPP?
   - Holding times met for all analytes?
   - Chain of custody — complete and accurate?
   - Field blanks and duplicates — collected at required frequency (typically 10%)?
   - Sample preservation — correct preservatives, temperature maintained?

### Data Management
   - Data entry within specified timeframe?
   - QA/QC flags applied appropriately?
   - Correct units and significant figures?
   - Exceedances reported within required timeframe?

### Documentation
   - Field notebooks complete and legible?
   - Safety plans current and site-specific?
   - Incident reports filed for all events?
   - Training records up to date?

3. For each item, classify as:
   - **COMPLIANT** — meets requirements
   - **MINOR FINDING** — administrative gap, easily corrected
   - **MAJOR FINDING** — procedural gap that could affect data quality or safety
   - **CRITICAL FINDING** — regulatory violation or immediate safety concern

4. Generate audit report with findings, corrective actions, and recommended timeline.

5. Save to `outputs/compliance-audit-[DATE].md`
