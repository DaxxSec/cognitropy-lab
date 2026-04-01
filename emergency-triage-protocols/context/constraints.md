# Boundaries & Constraints

## Critical Disclaimer

**This workspace is a DECISION-SUPPORT AND TRAINING TOOL, not a clinical system.**

All triage decisions in real-world scenarios must be made by qualified, licensed medical professionals (physicians, trauma surgeons, emergency nurses, paramedics) following your institution's established protocols and current clinical guidelines. This tool:
- Supports clinician decision-making through protocol validation
- Trains staff through realistic simulations
- Aids planning through resource forecasting
- Facilitates continuous improvement through exercise logging

**Real-world clinical decision-making authority rests solely with qualified medical professionals.**

## Safety Constraints

### Patient Safety Priority
1. **Over-triage when uncertain.** When a patient's acuity level is ambiguous, recommend a higher (more urgent) category rather than under-triaging
2. **Evidence-based decisions.** All protocol recommendations must cite specific algorithm steps and criteria
3. **Qualified oversight required.** Real clinical decisions must involve licensed medical professionals
4. **No definitive diagnoses.** This tool does not diagnose; it applies triage protocols based on vital signs and mechanism of injury
5. **Defer to clinical judgment.** When this tool's output conflicts with experienced clinician assessment, defer to the clinician

### Scope Limitations

**In Scope:**
- Triage protocol validation and training
- Mass casualty incident simulation and drill planning
- ED surge capacity and resource forecasting
- Equipment maintenance scheduling and predictive analytics
- Exercise debriefing and after-action reporting

**Out of Scope:**
- Real-time clinical decision-making without medical oversight
- Definitive patient treatment or medication recommendations
- Production EHR system integration
- Direct equipment control or monitoring
- Dispatch, communication, or logistics systems
- Financial analysis or billing processes
- Infection control or safety protocols (beyond triage context)

## Regulatory & Compliance Constraints

### Required Compliance
- **Hospital Policies:** This tool must align with your facility's established emergency management plan and triage protocols
- **Medical Director Approval:** Deployment and use must be approved by your hospital medical director
- **Accreditation Standards:** Use must support compliance with TJC, ACS, and CMS requirements
- **Privacy/Security:** No real patient data without proper de-identification; maintain HIPAA compliance
- **Quality Improvement:** Use must support your facility's QA and patient safety programs

### Training & Competency
- Staff must receive formal training before using this tool in any real-world context
- Annual competency assessments required for all clinical users
- Training records must be maintained for accreditation purposes
- Exercise results should be documented and reviewed by medical director

### Documentation & Reporting
- All simulations and exercises must be logged in `work-log/session-log.md`
- After-action reports must be generated within 48 hours of real MCI or major surge events
- Performance data must be analyzed and used to drive continuous improvement
- Incident reports must follow facility reporting requirements

## Data & System Constraints

### Data Requirements
- Historical ED census and acuity data (minimum 3 months, ideally 12 months)
- Equipment service records and failure logs
- Staffing schedule and resource availability
- Facility layout and resource constraints
- Known surge patterns and seasonal variations

### Data Quality Assumptions
- Input data is accurate and current
- MTBF baselines reflect your facility's actual equipment performance
- Historical patterns are representative of future conditions
- Staff availability data is realistic and maintainable

### Data Limitations
- Forecasts are probabilistic, not deterministic; accuracy depends on data quality and historical patterns
- Equipment failure predictions are based on statistical models, not guaranteed outcomes
- Simulations use representative scenarios, not real-world certainty
- Small sample sizes may reduce forecast accuracy

## Protocol Application Constraints

### Applicable Protocols
- **START (Simple Triage and Rapid Treatment):** For adults in mass casualty scenes
- **JumpSTART:** For children ages 1–8
- **SALT (Sort, Assess, Lifesaving interventions, Treatment/Transport):** Comprehensive alternative
- **ESI (Emergency Severity Index):** For ED resource allocation in surge scenarios
- **Facility-Specific Protocols:** This tool supports your facility's established protocols

### Protocol Limitations
- Protocol selection must be made by medical director or incident commander
- Protocols may require modification for your facility's specific context
- Special populations (pregnant, disabled, behavioral health) may require protocol adaptation
- Triage categories are guidelines; clinical judgment may override algorithm output
- Decision criteria may conflict in edge cases; clinician judgment prevails

### Ambiguity & Edge Cases
- Patients with unclear vital signs or mechanism of injury should be over-triaged
- Multiple injuries may require classification to highest acuity component
- Pediatric age cutoffs (JumpSTART uses age 1–8) must be adhered to strictly
- Environmental factors (weather, scene safety) may affect triage staging

## Resource Forecasting Constraints

### Forecast Accuracy Limitations
- Forecasts are **probabilistic estimates**, not guarantees
- Accuracy typically within 15–20% for 24-hour window, decreases with longer horizons
- Historical patterns may not predict unprecedented events (novel pathogens, climate events, etc.)
- Staffing availability assumptions may not hold during system-wide crises

### Assumptions
- Historical surge patterns remain representative
- Staffing availability matches baseline assumptions
- Equipment functionality is maintained at baseline MTBF
- Supply chain processes function normally
- No major system disruptions (power loss, communications failure, etc.)

### Contingency Planning
- Forecasts should be used to support contingency planning, not substitute for it
- Facility surge protocols should account for forecast uncertainty
- Mutual aid agreements should be pre-established
- Alternative resource sources should be identified in advance

## Equipment Maintenance Constraints

### MTBF Limitations
- MTBF data is based on manufacturer specifications and historical facility data
- Actual equipment lifespan varies based on usage patterns, environment, and maintenance quality
- Predictive models assume continued availability of spare parts and service technicians
- New equipment may not follow historical failure patterns until baseline is established

### Maintenance Scheduling
- Recommended schedules should be reviewed by biomedical engineering
- Manufacturer guidelines take precedence over statistical models
- Equipment failures may still occur before predicted intervals
- Maintenance costs should be budgeted based on MTBF and facility utilization

### Supply Chain Dependencies
- Equipment replacement depends on vendor availability and lead times
- Parts shortages may require protocol adjustments
- Maintenance scheduling must account for equipment downtime
- Backup equipment should be identified for mission-critical items

## Training & Competency Constraints

### Training Scope
- Simulations are realistic but not exhaustive
- Real MCI scenarios will differ from training exercises
- Competency assessments measure protocol knowledge, not real-world performance
- Stress, fatigue, and team dynamics may affect real-world triage decisions

### Competency Limitations
- Training cannot guarantee real-world performance
- Annual refresher training is required to maintain competency
- Team exercises should supplement individual competency assessments
- Medical director should establish facility-specific competency standards

### Documentation
- Training records must be maintained per accreditation requirements
- Competency assessments must be documented and linked to personnel files
- Exercise attendance and performance should be recorded
- Remedial training should be documented if competency gaps are identified

## Ethical & Professional Constraints

### Professional Standards
- All users must adhere to their professional code of ethics
- This tool supports but does not replace professional judgment
- Clinicians retain full responsibility for real-world decision-making
- Bias or discrimination is never acceptable in triage decisions

### Equity Considerations
- Triage should be purely clinical; no consideration of age, race, ethnicity, socioeconomic status, etc.
- Resource allocation should follow evidence-based protocols, not bias
- Training should emphasize equitable treatment of all patients
- Performance data should be analyzed for potential disparities

### Informed Consent & Privacy
- Real patient data should never be used in simulations without proper de-identification
- Participants should understand the training context and simulation nature
- Session data should be protected and used only for quality improvement
- No video or audio recording without explicit consent

## Operational Constraints

### Deployment Requirements
- Hospital IT support for secure system access
- Biomedical engineering support for equipment data
- Operations support for facility resource data
- Quality and compliance support for governance

### System Assumptions
- Stable access to historical data and facility records
- Ability to conduct tabletop and full-scale exercises
- Support from leadership for training and competency assessments
- Collaborative culture supporting continuous improvement

### Sustainability
- Ongoing maintenance of session logs and documentation
- Annual review and updates of MTBF baselines
- Continuous monitoring of forecast accuracy
- Regular competency assessment cycles

## Disclaimer Summary

1. **This is not a clinical decision-making system.** Real decisions require qualified medical professionals.
2. **Evidence-based protocols are foundational.** All recommendations cite protocol criteria.
3. **Patient safety is paramount.** When in doubt, recommend higher acuity.
4. **Qualified oversight is required.** Medical director approval and oversight mandatory.
5. **Continuous improvement is essential.** Collect data, conduct after-action reviews, adapt protocols.

---

**Last Updated:** 2026-04-01  
**Review Cycle:** Annually with Medical Director
