# /sampling-plan — Water Sampling Campaign Design

Design a statistically valid, safety-compliant sampling plan for a water body.

## Procedure

1. Confirm project objectives with the user:
   - Regulatory compliance monitoring vs. research study vs. incident response
   - Target parameters (or recommend based on objectives)
   - Temporal scope (single event, seasonal, ongoing)
   - Budget/resource constraints

2. Design station layout following `context/for-agent/workflows.md` (Workflow 2):
   - Index station at deepest point
   - Tributary and outflow stations
   - Littoral/near-shore stations as needed
   - Special stations (discharge points, beaches, intakes)

3. Safety-check every station:
   - Accessible by planned watercraft?
   - Near navigation channels or restricted areas?
   - Maximum open-water transit distance?
   - Optimal sampling order to minimize exposure time?

4. Select parameters and methods:
   - Core limnological suite (temp, DO, pH, conductivity, Secchi, TP, TN, Chl-a)
   - Extended parameters based on objectives
   - Sampling depth strategy (account for thermal stratification)

5. Build QA/QC plan:
   - Field blanks, duplicates, equipment blanks
   - Calibration schedule
   - Chain of custody procedures

6. Create safety-integrated timeline:
   - Pre-dawn weather check
   - Calibration and safety gear inspection
   - Safety checkpoints at launch, hourly, and return
   - Target completion time (before afternoon thermal winds)

7. Output a complete sampling plan document to `outputs/sampling-plan-[SITE]-[DATE].md` including:
   - Station map description with GPS coordinates
   - Parameter list with methods and holding times
   - Equipment manifest
   - QA/QC requirements
   - Safety-integrated schedule
   - Required personnel and qualifications
