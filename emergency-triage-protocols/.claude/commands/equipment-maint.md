# /equipment-maint — Equipment Maintenance Scheduling & Predictive Analytics

## Purpose
Schedule preventive maintenance for critical ED equipment using MTBF (Mean Time Between Failures) data and predictive failure analysis. Reduces unplanned downtime and optimizes maintenance costs.

## When to Use
- Establish baseline MTBF for new or existing equipment
- Calculate failure risk and schedule maintenance
- Identify high-risk equipment requiring urgent attention
- Plan equipment replacement cycles
- Optimize supply chain and parts procurement
- Conduct post-maintenance acceptance testing

## Duration
10–30 minutes per equipment item or batch

## Input Required

I'll ask you to provide:

### 1. Equipment Identification
- **Equipment type:** (e.g., ventilator, cardiac monitor, infusion pump, defibrillator, portable suction)
- **Model & manufacturer:** (e.g., Philips Intellivue Monitor, Baxter PCA pump)
- **Serial number:** (if tracking individual units)
- **Quantity in service:** (if tracking equipment class, e.g., "3 ventilators")

### 2. Operating Hours & Usage Data
- **Current operating hours:** (total hours in service to date)
- **Typical daily usage:** (hours per day or patients per day)
- **Usage pattern:** (consistent, variable, surge-dependent)
- **Date last serviced:** (maintenance history)
- **Hours since last service:** (cumulative operating hours since last maintenance)

### 3. MTBF Baseline
- **Manufacturer MTBF specification:** (if known, e.g., "5,000 hours for Philips monitors")
- **Facility historical MTBF:** (your facility's actual baseline from service records)
- **Failure history:** (number of failures, failure modes, time between failures)
- **Environmental factors:** (high-dust environment? frequent transport? extreme temperatures?)

### 4. Maintenance History
- **Last scheduled maintenance:** Date and hours
- **Maintenance type:** (preventive, corrective, emergency)
- **Issues found/fixed:** (battery replacement? recalibration? part failure?)
- **Downtime:** (how long was equipment out of service?)

### 5. Current Status & Concerns
- **Is equipment performing normally?** (any abnormalities or warning signs?)
- **Known issues:** (e.g., "battery dies faster than expected," "alarm intermittent")
- **Replacement possibility:** (can be sent out for service, or must be replaced in-house?)

## How Equipment Maintenance Works

**Step 1: Calculate Risk Score**

Risk Score = (Current Operating Hours / MTBF Baseline) × 100

Example:
- Ventilator: Operating hours = 3,500, MTBF = 5,000 hours
- Risk Score = (3,500 / 5,000) × 100 = 70%

**Step 2: Categorize Risk Level**

| Risk Score | Category | Action |
|-----------|----------|--------|
| 0–50% | Green (Low Risk) | Continue normal operation; routine monitoring |
| 50–75% | Yellow (Medium Risk) | Schedule maintenance within 2–4 weeks |
| 75–90% | Orange (High Risk) | Prioritize maintenance within 1 week; consider backup |
| 90–100% | Red (Critical Risk) | Immediate maintenance or replacement within 24–48 hours |

**Step 3: Estimate Time to Failure**

Based on risk score and usage rate:
- Green (50% of MTBF remaining): ~6–8 months before expected failure
- Yellow (25% remaining): ~2–3 months before expected failure
- Orange (10% remaining): ~2–4 weeks before expected failure
- Red (0–10% remaining): Imminent failure risk, days to weeks

**Step 4: Schedule Maintenance**

- **Green:** Annual maintenance per manufacturer schedule or every 12 months
- **Yellow:** Schedule within 2–4 weeks; plan for minimal ED disruption
- **Orange:** Urgent scheduling within 1 week; consider backup equipment
- **Red:** Emergency maintenance or replacement; activate backup immediately

**Step 5: Coordinate & Execute**

- Contact biomedical engineering with recommended maintenance window
- Plan for equipment downtime (backup unit identified?)
- Brief ED staff on status and any precautions
- Post-maintenance testing and acceptance

## Example Equipment Maintenance Scenarios

### Scenario 1: Routine Preventive Maintenance
```
EQUIPMENT: Cardiac Monitor (Philips Intellivue)
Serial #: 12345, Qty: 1

OPERATING DATA:
- Current hours: 2,800 hours
- Daily usage: 12 hours/day (continuous in-use)
- Last service: 6 months ago
- Hours since last service: 2,200 hours

MTBF BASELINE:
- Manufacturer MTBF: 5,000 hours
- Facility historical: 4,800 hours (slightly worse than manufacturer spec)

RISK CALCULATION:
Risk Score = (2,800 / 4,800) × 100 = 58.3% (Yellow zone)

ASSESSMENT:
- Equipment is 58% of expected life
- ~2,000 hours remaining before expected failure
- At 12 hours/day usage: ~167 days (~5.5 months) remaining

RECOMMENDATION:
✓ Schedule maintenance in 2–4 weeks (at ~3,500 operating hours)
✓ Preventive maintenance: battery check, electrode connector cleaning, 
  calibration check, display assessment
✓ Schedule during low-volume shift (e.g., overnight or weekend)
✓ Backup monitor available during service? Confirm.
✓ Estimated maintenance time: 2 hours
✓ Expected downtime: 2–3 hours

ACTION PLAN:
- Contact biomedical engineering this week
- Propose service window for 2–3 weeks out
- Notify ED of planned service (if single unit)
- Ensure backup monitor is available and functional
- After service: Confirm equipment pass acceptance testing
- Update maintenance log with: service date, hours serviced, issues found, next maintenance window
```

### Scenario 2: High-Risk Equipment Requiring Urgent Maintenance
```
EQUIPMENT: Ventilator (Philips Respironics)
Serial #: V-001, Qty: 1 (primary ICU vent)

OPERATING DATA:
- Current hours: 7,200 hours
- Daily usage: 20 hours/day (high-acuity use)
- Last service: 14 months ago
- Hours since last service: 5,200 hours (way overdue!)

MTBF BASELINE:
- Manufacturer MTBF: 5,000 hours
- Facility historical: 4,500 hours

RISK CALCULATION:
Risk Score = (7,200 / 4,500) × 100 = 160% (RED—way overdue!)

ASSESSMENT:
- Equipment is 160% of expected MTBF
- Already exceeded expected failure point by 2,700 hours
- Failure risk: EXTREMELY HIGH (likely imminent)
- Historical concern: "Compressor sounds different lately"

ALERT:
🚨 CRITICAL RISK—IMMEDIATE ACTION REQUIRED

RECOMMENDATION:
✓ EMERGENCY: Restrict clinical use of this ventilator immediately
✓ Activate backup ventilator (if available) or request from another unit
✓ Contact biomedical engineering TODAY for emergency service
✓ Options: (1) Emergency repair/calibration within 24 hours, or (2) Replace immediately
✓ If emergency repair not possible: Order replacement ventilator with expedited delivery
✓ Notify ICU director and respiratory therapy of equipment status
✓ Document decision and contingency plan in equipment log

CONTINGENCY PLAN:
- Backup ventilator: Unit-XX (status: good, in storage)
- If service delayed > 4 hours: Activate backup immediately
- If repair not feasible: Procure replacement; lead time ~4–6 weeks

POST-ACTION:
- If repair: Full testing before return to clinical service
- If replacement: Staff training on new equipment
- Review: Why was maintenance deferred 14 months? Prevent recurrence
- Update: Maintenance schedule to never exceed 80% of MTBF
```

### Scenario 3: Equipment Replacement Planning
```
EQUIPMENT: Infusion Pumps (Baxter PCA Pump)
Serial #: P-001, P-002, P-003, Qty: 3

OPERATING DATA (ALL THREE UNITS):
- Average age: 8 years old
- Average operating hours: 12,000+ hours each
- Last service: Varied (ranging 6–18 months ago)
- Known issues: "Battery life declining," "occasional calibration drift"

MTBF BASELINE:
- Manufacturer MTBF: 5,000 hours
- Facility historical: 4,800 hours
- Expected useful life: 7–8 years

RISK ASSESSMENT:
- All three pumps: >200% of expected MTBF
- All are past "end of useful life" per manufacturer
- Failure rate increasing (2 pump failures in last 12 months)
- Spare parts becoming harder to source
- Newer models available with improved safety features

RECOMMENDATION:
✓ PLAN REPLACEMENT: Phase out all three pumps over next 12–24 months
✓ Timeline: Replace P-001 (worst condition) in Q2, P-002 in Q3, P-003 in Q4
✓ Procurement: Request capital approval for 3 new pumps (~$45K total)
✓ Lead time: 4–6 weeks per pump; order phased replacements
✓ Transition: Staff training on new pump model before each replacement
✓ Contingency: Interim support from other departments if needed

INTERIM MANAGEMENT (Until Replacement):
- Intensive monitoring of all three pumps (biweekly checks)
- Restrict use of worst pump (P-001) to known-stable patients
- Have backup pump from another department on standby
- Order critical spare parts (batteries, seals) for emergency repairs

COST-BENEFIT:
- Repair costs for old pumps: ~$2K/year (increasing)
- New pumps: ~$15K each with 5-year warranty
- Benefit: Improved reliability, staff time savings, patient safety
- Recommendation: Approve replacement in capital planning process
```

## Advanced Maintenance Features

### Failure Mode Analysis
If equipment has history of failures:
- What are the common failure modes? (e.g., "battery fails" vs. "display flickers")
- Are failures preventable or inevitable?
- Should maintenance schedule target these failure modes specifically?

Example:
```
Ventilator failure history:
- Failure #1 (3 years ago): Compressor seal failure
  - Root cause: Inadequate lubrication
  - Action: Increase lubrication checks to every 500 hours

- Failure #2 (1.5 years ago): Display malfunction
  - Root cause: Humidity exposure
  - Action: Use desiccant cartridges in storage; improve environmental controls

Updated maintenance protocol: Add lubrication checks + humidity monitoring
```

### Surge-Related Maintenance Planning
During high-volume surge periods, equipment gets intensive use:
- Accelerated MTBF consumption (20+ hours/day instead of 12)
- Increased failure risk during surge
- Post-surge intensive maintenance needed to restore baseline

Example:
```
Surge event: 48-hour heat wave with double normal ED volume
Monitor #1: Ran 20 hours/day for 2 days = additional 40 hours of use
Accelerated MTBF consumption: 40 hours × 1.5x intensity = 60 hours effective wear

Schedule post-surge maintenance: Check for abnormalities, replace consumables
(batteries, fans, seals) that degrade faster under intensive use
```

### Supply Chain Coordination
- Lead time for parts? (2 weeks for battery, 6 weeks for circuit board?)
- Stock critical components to avoid delays
- Plan major maintenance during periods with backup equipment available

## Output & Documentation

After equipment maintenance analysis, I provide:

1. **Risk Assessment:**
   - Current risk score and category (Green/Yellow/Orange/Red)
   - Time to expected failure
   - Urgency level for action

2. **Maintenance Recommendation:**
   - Maintenance schedule (when and what type)
   - Estimated downtime and impact
   - Backup/contingency plan

3. **Action Items:**
   - Who to contact (biomedical engineering, procurement)
   - When to schedule
   - What to prepare (backup equipment, supplies, staff notification)

4. **Documentation:**
   - Update `planning/maintenance-schedule-template.md` with new maintenance dates
   - Log in equipment records for future reference
   - Communicate status to relevant stakeholders

## Integration with Facility Operations

### Quarterly Review Cycle
- Review all critical equipment risk scores
- Identify upcoming maintenances
- Coordinate with operations for scheduling
- Update MTBF baselines based on actual failure history

### Capital Planning Integration
- Equipment approaching or exceeding end-of-life
- Propose replacements with business case
- Plan multi-year replacement schedules
- Optimize procurement and budgeting

### Compliance & Accreditation
- Equipment maintenance records support TJC compliance
- Document preventive maintenance procedures
- Track maintenance compliance rates
- Support patient safety and quality initiatives

---

**Last Updated:** 2026-04-01
