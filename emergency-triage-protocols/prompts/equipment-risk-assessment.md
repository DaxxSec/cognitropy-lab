# Equipment Risk Assessment & Failure Prediction Prompt

## Purpose
Guide predictive failure analysis for critical medical equipment using MTBF data, usage patterns, historical failures, and statistical models.

## Use in Claude Prompt

When you need equipment risk assessment, use this approach:

```
Assess failure risk for [equipment type] with the following data:

EQUIPMENT DETAILS:
- Type: [e.g., ventilator, cardiac monitor, infusion pump]
- Model: [manufacturer and model number]
- Serial number: [if tracking individual unit]
- Current operating hours: [hours in service]
- MTBF baseline: [expected hours between failures]
- Last maintenance: [date and hours since maintenance]
- Installation date: [when equipment purchased/installed]

USAGE PATTERNS:
- Daily usage: [hours per day or patient count per day]
- Environment: [clean, dusty, high-humidity, temperature variations?]
- Usage intensity: [normal, heavy, emergency-only]
- Seasonal variations: [high-use periods, low-use periods]

FAILURE HISTORY:
- Number of failures to date: [count of failures]
- Failure modes: [e.g., battery failure, calibration drift, mechanical wear]
- Time between failures: [calculate MTBF from actual failures]
- Known issues: [e.g., "battery life declining," "occasional error messages"]
- Repair costs: [estimated or actual costs of repairs]

FACILITY CONSTRAINTS:
- Backup equipment available: [yes/no; if yes, when can it be deployed?]
- Spare parts availability: [available in stock? lead time if ordering?]
- Service contract status: [warranty active? extended service agreement?]
- Criticality to patient care: [essential / important / replaceable]

REQUESTED OUTPUT:
1. Risk score and category (Green/Yellow/Orange/Red)
2. Time-to-failure estimate
3. Failure probability analysis
4. Maintenance recommendation and timing
5. Risk mitigation strategy
6. Supply chain considerations
7. Contingency planning
8. Long-term replacement recommendation

Provide assessment in clinical decision-support format suitable for biomedical engineering and operations planning.
```

## Analysis Framework

### 1. Risk Score Calculation
```
Risk Score = (Current Operating Hours / MTBF Baseline) × 100

Interpretation:
- 0–50%: Green (Low Risk)
- 50–75%: Yellow (Medium Risk)
- 75–90%: Orange (High Risk)
- 90–100%: Red (Critical Risk)
```

### 2. Failure Probability Estimation
Based on exponential failure distribution (common for medical equipment):
```
Failure Probability = 1 − e^(−λt)

Where:
λ = failure rate = 1 / MTBF
t = time remaining until MTBF reached

Example:
MTBF = 5,000 hours
Current hours = 3,500
Remaining hours = 1,500
λ = 1/5,000 = 0.0002 failures per hour

Probability of failure in next 500 hours:
P = 1 − e^(−0.0002 × 500) = 1 − e^(−0.1) = 0.095 = 9.5%

Interpretation: ~10% chance of failure in next 500 hours (~6 weeks at 20 hrs/week)
```

### 3. Usage-Based Adjustment
If facility usage differs from manufacturer assumptions:
```
Adjusted MTBF = Manufacturer MTBF × (Standard Usage / Facility Usage)

Example:
Manufacturer assumes 8 hours/day average usage
Your facility uses 16 hours/day (double usage)
Adjusted MTBF = 5,000 × (8/16) = 2,500 hours

This means equipment fails twice as fast as manufacturer predicts due to higher usage.
```

### 4. Environmental Degradation Factors
- **Humid environment:** Reduce MTBF by 20–30% (corrosion, electronics degradation)
- **Dusty environment:** Reduce MTBF by 15–25% (filter clogging, motor wear)
- **Temperature extremes:** Reduce MTBF by 10–20% (battery, electronics sensitivity)
- **Frequent transport:** Reduce MTBF by 25–40% (vibration, connector wear)
- **Chemical exposure:** Reduce MTBF by 30–50% (corrosion, sealing degradation)

## Example Assessment

```
EQUIPMENT RISK ASSESSMENT

Equipment: Infusion Pump (Baxter PCA Pump)
Serial #: P-001
Assessment Date: March 2026

BASELINE DATA:
- Installation date: March 2017 (9 years old)
- Current operating hours: 12,400 hours
- Manufacturer MTBF: 5,000 hours
- Last maintenance: November 2024 (4 months ago)
- Maintenance type: Routine calibration + battery replacement
- Hours since last maintenance: 2,200 hours
- Daily usage: ~3–4 hours/day (variable)
- Environment: Controlled ED, occasional transport

FAILURE HISTORY:
- Total failures recorded: 2 in 9-year history
  - Failure #1 (Year 3): Battery failure, corrected by replacement
  - Failure #2 (Year 7): Calibration drift, corrected by service
- Time between failures: 4 years / 1 failure = 4-year intervals
- Historical MTBF: ~4,000 hours actual (vs. 5,000 rated)
- Repair costs: $200–400 per service call
- Known issues: Battery depletes faster in high-temp summer months

FACILITY ADJUSTMENTS:
- Usage pattern: Variable (heavy in summer, lighter in winter)
- Seasonal peak (summer): 5–6 hours/day × 90 days = ~450 hours
- Baseline (other months): 3–4 hours/day × 275 days = ~1,050 hours
- Annual usage: ~1,500 hours/year average
- Environmental factor: Controlled, no significant degradation factors
- Adjusted MTBF = 4,000 hours × (1 / 1) = 4,000 hours (facility matches manufacturer)

RISK CALCULATION:
Risk Score = (12,400 / 4,000) × 100 = 310%

ASSESSMENT:
🚨 CRITICAL RISK — IMMEDIATE ACTION REQUIRED

This pump has exceeded its expected lifespan by 310% (3.1 times over). This indicates:
1. Equipment is operating well beyond design life
2. Failure is imminent; risk of sudden breakdown is very high
3. Continued use without immediate replacement is not recommended

TIME-TO-FAILURE ESTIMATE:
- Equipment already exceeded MTBF by 8,400 hours
- Expected failure within: Days to weeks (imminent)
- Failure probability in next 500 hours: 99%+ (essentially certain)

FAILURE MODE PREDICTION:
Based on age and history:
- Most likely: Battery/electrical system failure (age-related degradation)
- Secondary risk: Mechanical wear (pump mechanisms)
- Tertiary risk: Calibration drift (repeated cycling stress)

MAINTENANCE RECOMMENDATION:
❌ MAINTENANCE NOT RECOMMENDED
- Equipment has exceeded economical service life
- Maintenance cost ($200–400) is not justified given imminent failure risk
- Replacement is the only appropriate action

RISK MITIGATION STRATEGY (Immediate):
1. ✓ RESTRICT USE: Limit pump to stable, non-critical patients only
2. ✓ ACTIVATE BACKUP: Identify and bring backup pump into service immediately
3. ✓ EMERGENCY ALERT: Flag this pump in equipment management system; alert all staff
4. ✓ CONTINGENCY PLANNING: Identify alternative infusion method if backup not available (manual infusion, alternate pump)
5. ✓ PROCUREMENT: Initiate emergency replacement order (delivery typically 4–6 weeks; interim use of backup unit)

SUPPLY CHAIN CONSIDERATIONS:
- Spare parts: Limited availability for 9-year-old model; recommend replacement
- Service availability: May be reduced for older equipment model
- Compatibility: New model may require staff training; plan transition window
- Warranty: New equipment typically includes 2–3 year manufacturer warranty

CONTINGENCY PLAN (If Failure Occurs While Awaiting Replacement):
1. Activate backup pump immediately
2. If no backup available:
   - Manual infusion (nurse-controlled bolus administration)
   - Refer to IV drip monitoring protocols
   - Increase nursing assessment frequency
   - Document incident and contingency response
3. Contact biomedical engineering for emergency service (may not be available for this model)
4. Request loaner unit from another department or hospital

LONG-TERM REPLACEMENT RECOMMENDATION:
✓ APPROVE REPLACEMENT — REQUEST IN CAPITAL BUDGET
- Current equipment: 9 years old, exceeded useful life
- Replacement cost: ~$15,000 for new pump with 5-year warranty
- Benefit: Improved reliability, staff training opportunity, updated safety features
- Timeline: Order immediately; replace within 4–6 weeks after delivery

BUDGET JUSTIFICATION:
- Current repair costs: $200–400 per service (2 failures in 9 years = $400–800 total)
- Projected future repairs: Likely 2–4 per year given age → $400–1,600/year
- New equipment cost: $15,000 with 5-year warranty = $3,000/year amortized
- ROI: 5-year warranty + improved reliability justifies replacement cost

STAFF COMMUNICATION:
- Alert nursing staff: Pump P-001 has limited availability; use backup pump if available
- Notify pharmacy: May need to adjust infusion protocols for backup equipment
- Inform biomedical engineering: Equipment marked for emergency replacement
- Document in equipment management system: Critical risk flag

POST-REPLACEMENT PLAN:
1. Train staff on new pump model (2–4 hour session)
2. Run parallel operation with old pump during transition (if possible with temporary backup)
3. Decommission old pump (hazardous waste disposal, equipment recycling)
4. Update equipment inventory and MTBF baselines in management system
5. Establish new maintenance schedule for replacement equipment (per manufacturer guidelines)

ASSESSMENT CONCLUSION:
Equipment P-001 has exceeded its expected service life and poses unacceptable failure risk. Immediate replacement is recommended. Interim: Restrict use, activate backup, monitor closely.

Next Assessment: After replacement equipment installed and baseline established.
```

---

## Key Metrics for Assessment

| Metric | Green | Yellow | Orange | Red |
|--------|-------|--------|--------|-----|
| **Risk Score** | 0–50% | 50–75% | 75–90% | 90–100%+ |
| **Time to Failure** | 6–12+ months | 2–6 months | 2–4 weeks | Days–weeks |
| **Failure Probability (next 500 hrs)** | <5% | 5–20% | 20–50% | 50–99%+ |
| **Action** | Monitor | Schedule maintenance | Prioritize maintenance | Replace immediately |
| **Backup Needed** | No | Consider | Yes | Required |
| **Urgency** | Routine | Soon | High | Critical |

---

**Last Updated:** 2026-04-01
