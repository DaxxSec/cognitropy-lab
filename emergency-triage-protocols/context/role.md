# User's Role & Responsibilities

## Role Overview

You are an **Emergency Medicine Professional** with responsibility for triage decision-making, emergency planning, resource allocation, and staff training in mass casualty and surge scenarios. This workspace supports your work as a clinician, planner, trainer, or administrator.

## Role-Specific Responsibilities

### If You Are a Clinical Team Lead or Physician
- **Triage Direction:** Apply and validate triage protocol decisions during MCIs and surge events
- **Staff Supervision:** Ensure team members follow protocols and make appropriate categorization decisions
- **Training:** Lead competency assessments and ongoing protocol training
- **Oversight:** Review decisions for quality assurance and continuous improvement

**Your Key Tools:**
- `/protocol-check` — Validate individual triage decisions
- `/triage-sim` — Run practice scenarios to train your team
- Triage quick reference in `resources/triage-quick-reference.md`

### If You Are an Emergency Planner or Administrator
- **Surge Preparedness:** Forecast ED capacity needs and resource requirements
- **Resource Allocation:** Plan staffing, supplies, and equipment based on forecasts
- **Drill Design:** Organize training exercises and competency assessments
- **Policy Development:** Support evidence-based emergency management policies

**Your Key Tools:**
- `/surge-forecast` — Predict capacity and staffing needs
- `/drill-plan` — Design tabletop and full-scale exercises
- `/incident-report` — Generate after-action reports
- `/resource-calc` — Calculate supply and transport requirements

### If You Are a Biomedical/Clinical Engineer
- **Equipment Baseline:** Establish MTBF and failure rate data for critical equipment
- **Maintenance Planning:** Schedule preventive maintenance and track compliance
- **Risk Analysis:** Identify high-risk equipment needing replacement or intensive monitoring
- **Supply Chain:** Coordinate with vendors for parts and replacement schedules

**Your Key Tools:**
- `/equipment-maint` — Schedule maintenance with predictive analytics
- `resources/equipment-mtbf-reference.md` — MTBF baseline data
- `planning/maintenance-schedule-template.md` — Editable maintenance schedule

### If You Are a Training or Education Specialist
- **Competency Development:** Design and deliver protocol training programs
- **Simulation:** Conduct and debrief exercises with realistic scenarios
- **Performance Tracking:** Log exercise results and identify improvement areas
- **Curriculum Development:** Create training materials based on facility needs

**Your Key Tools:**
- `/triage-sim` — Run training simulations with feedback
- Quiz generators in `prompts/triage-training-quiz.md`
- `work-log/session-log.md` — Track training progress
- Scenario generators in `prompts/mci-scenario-generator.md`

## Key Responsibilities

### 1. Clinical Safety & Decision Quality
- Ensure triage decisions prioritize patient safety
- Use evidence-based protocols consistently
- Report and learn from decision errors
- Maintain competency through ongoing training
- Defer to qualified medical professionals in real-world scenarios

### 2. Resource & Planning Oversight
- Validate forecasts against actual utilization
- Adjust plans based on feedback and performance data
- Coordinate with operations for surge preparation
- Monitor equipment maintenance compliance
- Support continuous improvement initiatives

### 3. Staff Development & Training
- Ensure all clinical staff complete annual protocol training
- Conduct competency assessments and remedial training as needed
- Use simulations and drills to identify skill gaps
- Provide feedback and coaching based on exercise performance
- Log training and competency records

### 4. Data Management & Documentation
- Maintain accurate session logs in `work-log/`
- Document exercise outcomes and lessons learned
- Track equipment maintenance and failure data
- Preserve after-action reports for QA review
- Support data-driven decision-making

### 5. Compliance & Quality Assurance
- Ensure protocol compliance during exercises and actual events
- Participate in after-action reviews
- Support process improvement initiatives
- Maintain documentation for regulatory and accreditation requirements
- Report safety events and near-misses

## Authority & Decision-Making

### Your Authority
- **For Training & Exercises:** Full authority to design, conduct, and debrief simulations
- **For Planning:** Authority to recommend staffing, supply, and equipment needs
- **For Protocol Validation:** Authority to review and validate triage decisions in training context
- **For Documentation:** Authority to create and maintain session logs and reports

### Escalation & Oversight
- **Real Clinical Events:** All decisions must involve qualified medical professionals; this tool is decision-support only
- **Protocol Changes:** Defer to medical director and emergency management committee
- **Safety Issues:** Escalate immediately to quality and patient safety leadership
- **Equipment Failures:** Report to biomedical engineering and operations
- **Training Deficiencies:** Escalate to medical director and training leadership

### Restrictions
- **Do not** use this tool for real-time clinical decision-making without medical oversight
- **Do not** diagnose patients or prescribe treatments
- **Do not** override established facility protocols
- **Do not** make assumptions about patient acuity without documented vital signs and mechanism
- **Do not** use real patient data without proper de-identification

## Required Competencies

### For All Users
- Familiarity with one or more triage protocols (START, SALT, ESI, etc.)
- Basic understanding of mass casualty incident management
- Ability to interpret patient presentations and vital signs
- Knowledge of your facility's emergency response plans

### For Trainers
- Expertise in adult learning and facilitation
- Ability to provide constructive feedback
- Experience with simulation and exercise management
- Knowledge of competency assessment methods

### For Planners
- Understanding of resource allocation and surge management
- Familiarity with facility operations and capacity constraints
- Ability to analyze data and identify trends
- Project management skills

### For Biomedical Engineers
- Knowledge of equipment maintenance and failure modes
- Ability to interpret MTBF and reliability data
- Understanding of predictive maintenance concepts
- Supply chain and procurement familiarity

## Support & Escalation

### Questions About Triage Protocols
- Review `resources/triage-quick-reference.md`
- Check `context/for-agent/domain-knowledge.md` for detailed protocol information
- Use `/protocol-check` to validate specific decisions
- Consult facility medical director or experienced triage officer

### Questions About Forecasting & Resource Planning
- Review forecasting methodologies in `context/for-agent/domain-knowledge.md`
- Use `/surge-forecast` with your facility data
- Analyze assumptions and adjust parameters as needed
- Consult operations and planning colleagues

### Questions About Equipment & Maintenance
- Review MTBF data in `resources/equipment-mtbf-reference.md`
- Use `/equipment-maint` with your facility inventory
- Consult biomedical engineering colleagues
- Reference manufacturer guidelines and service records

### General Workspace Questions
- Review `README.md` and `CLAUDE.md`
- Check `user-docs/getting-started.md`
- Review command documentation in `.claude/commands/`
- Contact workspace administrator or training coordinator

---

**Last Updated:** 2026-04-01
