# Report Generation & Documentation Guide

## Overview

This workspace generates several types of reports to support quality improvement, compliance, and training documentation.

## Report Types

### 1. After-Action Reports (AARs)

**Purpose:** Document and analyze MCIs, surge events, or training exercises

**When Generated:**
- Within 48 hours of real MCI or major surge event
- Immediately following a significant training exercise
- Quarterly for trend analysis

**Contents:**
- Incident overview (type, timeline, patients, resources)
- Response performance (triage accuracy, communication, decisions)
- Strengths identified (what went well)
- Areas for improvement (gaps, challenges, root causes)
- Action items (specific improvements with owners and deadlines)
- Lessons learned (key takeaways)

**Output Locations:**
- `outputs/` directory: Primary storage
- Filename format: `AAR_[Date]_[IncidentType].pdf` or `.docx`
- Example: `AAR_2026-03-15_VehicleCollision.pdf`

**How to Generate:**
```
/incident-report

Input: Incident details (date, type, patients, resource utilization, challenges, improvements)
Output: Comprehensive after-action report with analysis and recommendations
```

---

### 2. Simulation Performance Reports

**Purpose:** Document training exercise outcomes and individual competency assessment

**Contents:**
- Scenario description
- Participant list
- Triage accuracy (number correct, percentage)
- Performance metrics (timing, communication, decisions)
- Individual competency scores (if assessment-based)
- Feedback and learning points
- Recommended follow-up actions

**Output Location:** `outputs/` directory
**Filename:** `SimReport_[Date]_[Scenario].pdf`

**How to Generate:**
After running `/triage-sim`:
- I provide summary report with accuracy, timing, resource utilization
- Manually document in `work-log/session-log.md` for permanent record
- Optional: Compile into formal report for compliance documentation

---

### 3. Surge Capacity Forecast Reports

**Purpose:** Predict ED demand and resource needs for planning

**Contents:**
- Historical baseline (normal ED volume, acuity, patterns)
- Anticipated event/surge trigger
- Hour-by-hour forecast (next 24–48 hours)
- Surge activation thresholds and recommendations
- Staffing surge calculations (by role)
- Supply demand projections
- Resource bottleneck identification
- Recommended activation timing and escalation points

**Output Location:** `outputs/` directory
**Filename:** `Forecast_[Date]_[EventType].pdf`

**How to Generate:**
```
/surge-forecast

Input: Current ED census, historical baseline, anticipated event
Output: Detailed capacity forecast with staffing and supply recommendations
```

---

### 4. Equipment Maintenance Reports

**Purpose:** Track equipment status and predict maintenance needs

**Contents:**
- Equipment inventory (model, serial #, age)
- Operating hours and usage rate
- Risk score and failure probability
- Maintenance history and recommendations
- Replacement timeline and cost-benefit analysis
- Supply chain considerations

**Output Location:** `planning/maintenance-schedule-template.md` (editable)
**Filename:** `Equipment_Status_[Date].pdf` (export from spreadsheet)

**How to Generate:**
```
/equipment-maint

Input: Equipment type, operating hours, MTBF baseline
Output: Risk assessment with maintenance recommendations and timeline
```

---

### 5. Drill Planning & Evaluation Reports

**Purpose:** Document exercise design, execution, and outcomes

**Contents:**
- Drill objectives and scenario description
- Participant list and role assignments
- Timeline (schedule and actual progression)
- Facilities and resources used
- Performance observations (by task/competency)
- Competency assessment results (if applicable)
- Lessons learned and improvement recommendations
- Follow-up actions with owners and deadlines

**Output Location:** `outputs/` directory
**Filename:** `DrillReport_[Date]_[ExerciseType].pdf`

**How to Generate:**
```
/drill-plan

Output: Comprehensive drill plan with materials, scenario, facilitator guide, evaluation forms
```

Then after execution:
- Complete observer forms
- Compile performance data
- Facilitate debrief
- Document findings in `work-log/session-log.md`
- Generate formal report for compliance

---

## Session Logging (Work Log)

**Purpose:** Maintain permanent record of all exercises, incidents, and improvements

**Location:** `work-log/session-log.md` (editable markdown file)

**What to Log:**
- Date and time of exercise/incident
- Type (tabletop / full-scale / real incident)
- Objective or scenario
- Participants (attendees, facilitators, observers)
- Key outcomes (triage accuracy, timing, resource utilization)
- Issues identified and root causes
- Improvement actions with owners and target dates
- Status of previous action items

**Example Log Entry:**
```markdown
## 2026-03-15 — Multi-Vehicle Collision (Real Incident)

**Incident Type:** Vehicle collision, Highway 101
**Patients:** 18 (4 Immediate, 8 Delayed, 6 Minor)
**Triage Accuracy:** 89% (16/18 correct)
**Average Triage Time:** 2.2 minutes/patient
**Staffing Surge:** Phase 1 activated, adequate

**Strengths:**
- Rapid triage area setup (5 minutes)
- Good resource allocation
- Clear incident command

**Issues:**
1. Mental status assessment: 2 misclassifications
   - Root cause: Rushed assessment, inadequate protocol adherence
   - Action: Protocol training on START Step 3, target 4/15/2026
2. Supply chain communication delay: 15 minutes to secure IV fluids
   - Root cause: Supply chain not alerted to surge activation
   - Action: Update surge protocol to auto-alert supply chain, target 4/1/2026

**Owner:** ED Director
**Status:** In progress
**Next Review:** 6 months
```

---

## Document Management & Storage

### Primary Storage
- **Location:** `outputs/` directory (workspace)
- **Backup:** Facility document repository (SharePoint, Box, etc.)
- **Access:** Restricted to authorized personnel (ED leadership, quality, compliance)

### File Organization
```
outputs/
├── AAR_2026-03-15_VehicleCollision.pdf
├── Forecast_2026-01-15_FluSeason.pdf
├── Equipment_Status_2026-03-01.pdf
├── DrillReport_2026-02-20_Tabletop.pdf
└── [other reports]
```

### Retention Requirements
- **Real MCIs:** 5+ years (compliance, liability, continuous improvement)
- **Training exercises:** 3 years minimum (competency documentation)
- **Equipment maintenance:** 5–7 years (manufacturer requirements, warranty)
- **Surge forecasts:** 2+ years (trend analysis, continuous improvement)

---

## Report Distribution

### Who Receives What

| Report Type | ED Director | Staff | Leadership | Quality/Compliance |
|-------------|-------------|-------|-----------|-------------------|
| AAR | Yes | Summary | Yes | Yes |
| Simulation Report | Yes | Results | If competency-based | Yes |
| Forecast | Yes | Summary | Yes | If triggered surge |
| Equipment Status | If critical | Alert only | If replacement needed | Yes |
| Drill Report | Yes | Yes | Summary | Yes |

### Distribution Timeline
- **Real incident AAR:** Within 48 hours to leadership; summary to staff
- **Drill report:** Within 1 week to participants and leadership
- **Equipment alert:** Immediate if critical; routine status quarterly
- **Forecast:** Real-time updates during surge events

---

## Compliance & Accreditation

### Documentation Required for Accreditation
- **Joint Commission (TJC):**
  - MCI incident reports and AARs
  - Triage protocol compliance documentation
  - Equipment maintenance records
  - Staff training and competency assessments
  - Surge protocol activation records

- **CMS (Centers for Medicare & Medicaid):**
  - ED quality metrics (triage, throughput, outcomes)
  - Incident reports for adverse events
  - Equipment maintenance compliance

- **State Health Department:**
  - MCI reports (if triggered)
  - Mutual aid coordination records
  - Public health emergency reports

### Required Elements in Formal Report
1. **Identification:** Incident date, type, location, facility
2. **Narrative:** Objective description of events
3. **Analysis:** What worked, what didn't, why
4. **Actions:** Specific improvements with ownership
5. **Signatures:** Approval by medical director, ED director
6. **Distribution:** Who received report, when

---

## Quality Improvement Integration

### Monthly Review
- Session logs reviewed for trends
- Equipment alerts aggregated
- Staff feedback compiled

### Quarterly Review
- Comprehensive performance metrics
- Triage accuracy trends
- Equipment MTBF baseline updates
- Action item status

### Annual Review
- Full program evaluation
- Competency assessment results
- Equipment replacement planning
- Strategic improvements for coming year
- Medical director and leadership sign-off

---

## Exporting & Sharing Reports

### Formats Available
- **PDF:** Professional, read-only, printable
- **Word (.docx):** Editable, suitable for collaboration
- **Markdown (.md):** Text-based, version-control friendly
- **Spreadsheet (.xlsx):** For data analysis and trend graphing

### Security Considerations
- **No real patient identifiers:** All reports use de-identified or synthetic patient data
- **Access control:** Restrict to authorized personnel only
- **Email:** Use facility secure email; avoid unencrypted transmission
- **External sharing:** Request permission from medical director and compliance

---

## Troubleshooting & FAQs

**Q: How do I generate a formal compliance report?**
A: Use `/incident-report` for comprehensive AAR, or compile manual report using output template with medical director sign-off.

**Q: Can I modify a generated report?**
A: Yes. Export to Word format and edit as needed. Always maintain original for record, and document any changes made.

**Q: How do I track action items across multiple exercises?**
A: Log all actions in `work-log/session-log.md` with owner and target date. Review quarterly to track completion.

**Q: Should we share reports externally (insurance, legal)?**
A: Check with hospital legal and risk management. Some reports are discoverable in litigation; follow your institution's protocols.

**Q: What if we don't have perfect baseline data?**
A: Use best available estimates. Document assumptions in report. Refine data over time as you gather more information.

---

**Last Updated:** 2026-04-01
