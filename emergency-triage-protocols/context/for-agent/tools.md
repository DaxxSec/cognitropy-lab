# Tools & Integrations

## Internal Tools (Within This Workspace)

### Triage Protocol References
- **Quick Reference:** `resources/triage-quick-reference.md` — Decision trees for START, JumpSTART, SALT, ESI
- **Domain Knowledge:** `context/for-agent/domain-knowledge.md` — Full protocol details, MTBF models, forecasting mathematics
- **Commands:** `.claude/commands/` — Detailed implementation of each available command

### Simulation & Training Tools
- **Scenario Generator:** `prompts/mci-scenario-generator.md` — Template for realistic MCI scenario creation
- **Risk Assessment:** `prompts/equipment-risk-assessment.md` — Failure risk analysis prompt
- **Training Quiz:** `prompts/triage-training-quiz.md` — Interactive quiz generator for competency assessment

### Planning & Documentation Templates
- **Maintenance Schedule:** `planning/maintenance-schedule-template.md` — Equipment baseline and tracking
- **Session Log:** `work-log/session-log.md` — Exercise and event documentation
- **Outputs Directory:** `outputs/` — Repository for generated reports and analysis

## External Integrations

### Hospital Information Systems

**Electronic Health Record (EHR)**
- Purpose: Access current ED census, patient acuity, demographic data
- Use: Inform surge forecasting models, validate simulation scenarios
- Constraint: No real patient data imported; reference only, de-identified for analysis
- Integration: Manual export of de-identified historical data into forecasting models

**Hospital Analytics / Business Intelligence**
- Purpose: Historical ED volume, acuity trends, surge patterns
- Use: Baseline data for forecasting model, trend analysis
- Constraint: Monthly/quarterly data exports sufficient; real-time integration not required
- Integration: CSV or Excel import into forecasting tools

**Biomedical Equipment Management System**
- Purpose: Equipment inventory, service records, MTBF baselines
- Use: Populate maintenance-schedule-template.md, track operating hours
- Constraint: May require manual data entry if system doesn't export
- Integration: Quarterly sync to update equipment baseline

### Hospital Operations

**Bed Management System**
- Purpose: Real-time bed availability, ED surge capacity
- Use: Monitor surge thresholds, validate resource calculations
- Constraint: Reference only; not for patient assignment
- Integration: Manual check during surge planning

**Staffing & Scheduling System**
- Purpose: Staff availability, call-in procedures, surge staffing protocols
- Use: Validate staffing surge calculations, coordinate training schedules
- Constraint: Historical scheduling data only; respects privacy
- Integration: Aggregate/summary data only

**Supply Chain / Inventory Management**
- Purpose: Supply consumption rates, lead times, replacement ordering
- Use: Equipment procurement planning, supply chain risk assessment
- Constraint: Current inventory and lead time data
- Integration: Quarterly review with supply chain team

### External Resources

**CDC Emergency Preparedness & Response**
- Resource: SALT triage algorithm, MCI guidance, equipment standards
- Access: Public documents, website: https://www.cdc.gov/
- Use: Validate protocols, research best practices

**American College of Surgeons**
- Resource: ATLS trauma assessment, triage standards
- Access: Training programs, publications
- Use: Protocol validation, evidence-based guidelines

**Emergency Nurses Association (ENA)**
- Resource: ESI triage algorithm, emergency nursing standards
- Access: Training, publications, website: https://www.ena.org/
- Use: ESI protocol reference, competency standards

**Equipment Manufacturers**
- Resource: MTBF specifications, maintenance guidelines, service bulletins
- Access: Facility service contracts, product documentation
- Use: Baseline MTBF data, maintenance protocols, spare parts information
- Examples: Ventilator (Philips, Maquet), Monitors (GE, Philips), Pumps (Baxter, Alaris)

**State/Federal Emergency Management**
- Resource: Mutual aid agreements, disaster response protocols, resource sharing
- Access: State health department, FEMA, state emergency management agency
- Use: Surge resource planning, MCI response coordination

## Command-Line & Data Tools

### Data Analysis (Optional, for advanced use)

**Spreadsheet Software (Excel, Google Sheets, LibreOffice)**
- Purpose: Trend analysis, performance metrics, forecasting
- Use: Analyze session logs, calculate triage accuracy, project equipment failure
- Tools: Pivot tables, charts, MTBF calculations
- Data: Import from `work-log/session-log.md`, maintenance records

**Statistical Software (Optional: Python, R, SPSS)**
- Purpose: Advanced forecasting, trend analysis, predictive modeling
- Use: Time-series forecasting (ARIMA), failure prediction models
- Tools: Scikit-learn, TensorFlow, statsmodels
- Data: Historical ED census, equipment failure logs

### Simulation Software (Optional)

**Patient Simulation Platforms**
- Examples: METI iStan, Laerdal SimPad, CAE LMS
- Purpose: Full-scale exercise with realistic vital signs, patient responses
- Use: High-fidelity training, competency assessment
- Cost: Subscription or rental models

**Scenario Management Tools**
- Examples: Microsoft Excel/SharePoint, Atlassian Confluence, custom databases
- Purpose: Organize scenario libraries, track exercise history
- Use: Archive MCI scenarios, manage training curriculum
- Integration: Export scenarios to PDF for use in exercises

## Reporting & Documentation Tools

### Document Generation
- **Format:** PDF, Word, Markdown (depending on facility preference)
- **Tools:** Word processor, PDF generator, Markdown converters
- **Use:** Generate after-action reports, competency assessments, training materials
- **Location:** `outputs/` directory for storage and sharing

### Data Visualization
- **Tools:** Excel charts, PowerPoint, visualization software (Tableau, Power BI)
- **Use:** Create surge capacity dashboards, equipment failure trends, performance metrics
- **Examples:** 
  - ED census trend graph (line chart)
  - Triage category distribution (pie/bar chart)
  - Equipment risk scoring matrix (heat map)

### Records Management
- **Location:** Facility document repository (SharePoint, OneDrive, Box, etc.)
- **Purpose:** Central archive for all workspace outputs, session logs, reports
- **Retention:** Per facility records management policy
- **Access:** Restricted to authorized personnel

## Communication & Coordination Tools

### Emergency Communication
- **Incident Command System (ICS):** Facility uses standard ICS radio, overhead announcements, secure messaging
- **Integration:** Workspace supports HICS decision-making; actual incident uses facility communication systems
- **Activation:** During real MCI, use facility emergency notification system

### Training & Scheduling Coordination
- **Email / Messaging:** Schedule training, disseminate materials, coordinate facilitators
- **Calendar:** Manage exercise dates, track competency assessment cycles
- **Notifications:** Alert staff to surge events, training requirements, improvement actions

### After-Action Review Coordination
- **Meeting Software:** Virtual/in-person debrief sessions (Zoom, Teams, in-person)
- **Document Collaboration:** Shared documents for AAR notes, lesson learning
- **Record Keeping:** Compile findings and store in outputs directory

## Facility-Specific Customizations

### Local Protocol Adaptations
- Many exercises use generic START/SALT/ESI
- If your facility has specific protocol variations, note them in:
  - `context/constraints.md` — Document any deviations from standard protocols
  - `CLAUDE.md` — Add facility-specific commands or considerations
- Update prompts and reference materials to reflect local protocols

### Integration with Facility Systems
- **EHR vendor-specific tools:** If your facility uses Epic, Cerner, etc., may be able to export de-identified data for forecasting
- **Biomedical equipment systems:** Equipment tracking systems vary by vendor; coordinate with biomedical engineering
- **Hospital analytics platforms:** Facility may have custom dashboards; integrate with forecasting models

## Training & Support for Tool Use

### For Triage Protocol Questions
- Review `resources/triage-quick-reference.md` for decision tree
- Consult `context/for-agent/domain-knowledge.md` for detailed protocol explanation
- Use `/protocol-check` command to validate specific decisions
- Contact experienced triage officer or medical director for edge cases

### For Equipment Maintenance Questions
- Review `resources/equipment-mtbf-reference.md` for baseline data
- Consult equipment manufacturer service manuals
- Contact biomedical engineering for maintenance scheduling
- Use `/equipment-maint` command to calculate risk and schedule

### For Simulation & Training
- Use prompts in `prompts/` directory for scenario generation
- Reference command implementations in `.claude/commands/` for detailed guidance
- Consult experienced facilitators for exercise design and debriefing
- Log all exercises in `work-log/session-log.md`

### For Technology & Access Issues
- Contact workspace administrator or IT support
- Check facility documentation for system access, permissions
- Request data exports from appropriate departments (analytics, biomedical, operations)

---

**Last Updated:** 2026-04-01
