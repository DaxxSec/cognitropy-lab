# Emergency Triage Protocols Workspace

A comprehensive decision-support system for emergency medical teams applying structured triage protocols to mass casualty incidents (MCIs), surge events, and high-volume emergency department (ED) scenarios. Integrates evidence-based triage algorithms (START, JumpSTART, SALT, ESI) with predictive analytics for resource demand forecasting and equipment maintenance scheduling.

## Overview

This workspace supports emergency medicine teams in:

- **Triage Protocol Application:** Structured decision-making using START, JumpSTART, SALT, and ESI algorithms
- **Mass Casualty Incident (MCI) Simulation:** Run realistic triage exercises with configurable patient counts and acuity distributions
- **Resource Forecasting:** Predict staffing, supply, and transport requirements based on patient volume and acuity
- **Equipment Maintenance Planning:** Use predictive failure analysis and MTBF data to schedule critical equipment maintenance
- **Training & Drills:** Design tabletop exercises and full-scale drills with realistic scenarios
- **Incident Reporting:** Generate structured after-action reports for quality assurance and continuous improvement

## Key Features

### 1. Triage Protocol Support
- **START (Simple Triage and Rapid Treatment):** For adults in high-casualty mass casualty scenes
- **JumpSTART:** Pediatric adaptation of START for children ages 1–8
- **SALT (Sort, Assess, Lifesaving interventions, Treatment/Transport):** Alternative comprehensive protocol with initial sort phase
- **ESI (Emergency Severity Index):** Five-level triage for emergency department resource allocation
- Decision trees and step-by-step validation for each protocol

### 2. Predictive Maintenance
- Mean Time Between Failures (MTBF) data integration for ventilators, monitors, defibrillators, infusion pumps
- Usage-based degradation modeling (cumulative hours, power cycles)
- Risk scoring and failure probability forecasting
- Scheduled vs. reactive maintenance recommendations

### 3. Surge Capacity Forecasting
- Historical pattern analysis for ED volume and acuity
- Time-series forecasting (daily, weekly, seasonal peaks)
- Staffing surge requirements by role (physicians, nurses, technicians)
- Supply demand (IV fluids, bandages, medications) based on case mix

### 4. Simulation Engine
- Configurable patient volumes (10–10,000+ patients)
- Acuity distribution by protocol (Immediate, Delayed, Minor for START; includes Expectant)
- Realistic scenario generators (vehicle crashes, building collapses, natural disasters)
- Exercise debriefing with metrics (triage accuracy, resource utilization, decision time)

### 5. Training & Compliance
- Interactive triage training quizzes with feedback
- Drill planning templates for tabletop and full-scale exercises
- After-action report generation
- Protocol compliance tracking

## Workspace Structure

```
emergency-triage-protocols/
├── CLAUDE.md                       # Agent role & available commands
├── README.md                       # This file
├── CREATION_REPORT.md              # Workspace initialization report
├── context/
│   ├── project.md                  # Project scope, goals, constraints
│   ├── role.md                     # User's role and responsibilities
│   ├── constraints.md              # Boundaries and limitations
│   └── for-agent/
│       ├── domain-knowledge.md     # Triage protocols, MTBF models, forecasting math
│       ├── workflows.md            # 4 core workflows with step-by-step details
│       ├── environment.md          # Setup requirements, dependencies, data sources
│       └── tools.md                # Available integrations and APIs
├── .claude/commands/               # Command implementations
│   ├── onboard.md                  # Facility profile & protocol setup
│   ├── triage-sim.md               # Simulation execution
│   ├── protocol-check.md           # Decision validation
│   ├── surge-forecast.md           # Capacity forecasting
│   ├── equipment-maint.md          # Maintenance scheduling
│   └── [more commands...]
├── prompts/
│   ├── mci-scenario-generator.md   # Prompt for generating realistic MCI scenarios
│   ├── equipment-risk-assessment.md # Failure risk analysis prompt
│   └── triage-training-quiz.md     # Training quiz generator
├── resources/
│   ├── triage-quick-reference.md   # Protocol decision trees at a glance
│   ├── equipment-mtbf-reference.md # MTBF data and failure rates
│   └── mci-scale-definitions.md    # Casualty scale definitions
├── user-docs/
│   ├── getting-started.md          # Quick start guide
│   └── report.md                   # Report generation guide
├── work-log/
│   └── session-log.md              # Exercise log and session notes
├── planning/
│   └── maintenance-schedule-template.md  # Equipment maintenance plan template
└── outputs/
    └── .gitkeep                    # Directory for generated reports and logs
```

## Quick Start

### 1. Initialize Your Workspace
```
/onboard
```
Answer questions about your facility:
- Type of facility (hospital ED, field triage site, critical care center)
- Protocols in use (START, SALT, ESI, or combination)
- Staffing model (roles and typical availability)
- Equipment inventory with MTBF data

### 2. Run a Triage Simulation
```
/triage-sim
```
Configure:
- Total patient count (10–10,000+)
- Acuity distribution (% Immediate, Delayed, Minor, Expectant)
- Scenario type (vehicle crash, building collapse, weather event, etc.)
- Protocol to use (START, JumpSTART, SALT, ESI)

Review output:
- Patient roster with triage decisions
- Resource utilization summary
- Decision timing and accuracy metrics
- Bottleneck analysis

### 3. Validate a Triage Decision
```
/protocol-check
```
Input:
- Patient presentation (vital signs, chief complaint, mechanism of injury)
- Protocol in use
- Your proposed triage level

Output:
- Decision validation (correct/incorrect with reasoning)
- Alternative considerations
- Protocol step citations

### 4. Forecast Surge Capacity
```
/surge-forecast
```
Specify:
- Time horizon (next 24 hrs, 1 week, 1 month)
- Current ED census
- Expected influx (MCI size, seasonal surge, etc.)

Receive:
- Staffing surge requirements by role
- Supply demand estimates
- Transport resource needs
- Bottleneck predictions

### 5. Schedule Equipment Maintenance
```
/equipment-maint
```
Input:
- Equipment type (ventilator, monitor, defibrillator, pump)
- Usage hours/cycles to date
- Last maintenance date
- Facility MTBF baseline

Output:
- Recommended maintenance schedule
- Risk scoring (low/medium/high failure probability)
- Predictive failure alerts
- Supply chain recommendations

### 6. Generate an Incident Report
```
/incident-report
```
Provide:
- Incident date and type (MCI or surge event)
- Patient count and acuity distribution
- Staffing and resource utilization
- Issues encountered and decisions made

Receive:
- Structured after-action report (AAR)
- Metric summary
- Recommendations for improvement
- Lessons learned logging

## Core Workflows

### Workflow 1: MCI Response & Triage Execution
1. Incident activation and field scene assessment
2. Apply initial sort phase (SALT) or rapid assessment (START)
3. Assign triage categories to patients
4. Route patients to treatment/transport stations
5. Monitor resource consumption and surge events
6. Document decisions and outcomes

### Workflow 2: ED Surge Management
1. Monitor census and arrival patterns
2. Activate surge protocols at predetermined thresholds
3. Apply ESI or START-based triage for incoming patients
4. Reallocate beds, staffing, and supplies
5. Forecast capacity and activate escalation procedures
6. De-escalate when surge subsides

### Workflow 3: Equipment Maintenance Planning
1. Inventory critical equipment and baseline MTBF
2. Log usage hours, power cycles, and service dates
3. Calculate failure risk scores
4. Schedule preventive maintenance before high-risk periods
5. Coordinate with biomedical/clinical engineering
6. Track maintenance compliance and effectiveness

### Workflow 4: Training & Drill Execution
1. Select protocol and scenario
2. Generate realistic patient list with presentations
3. Run training exercise with real-time feedback
4. Score performance (triage accuracy, speed, resource use)
5. Debrief and identify improvement areas
6. Log exercise results and track competency

## Triage Protocols Reference

### START (Simple Triage and Rapid Treatment)
**Use for:** Adults in mass casualty scenes
**Categories:**
- **Immediate (Red):** Respirations > 30 or < 10, BP < 90, altered mental status
- **Delayed (Yellow):** Severe but stable injuries
- **Minor (Green):** Walking wounded, minor injuries
- **Expectant (Black):** Unsurvivable injuries in resource-constrained settings

### JumpSTART
**Use for:** Children ages 1–8
**Modifications to START:**
- Respiratory rate thresholds: > 40 or < 15
- Special assessment for ability to follow commands
- Pediatric shock indicators

### SALT (Sort, Assess, Lifesaving interventions, Treatment/Transport)
**Use for:** Comprehensive triage with interventions component
**Steps:**
1. **Sort:** Initial wave assessment (walk, sit, lie down)
2. **Assess:** Respirations, perfusion, mental status
3. **Lifesaving interventions:** Hemorrhage control, airway positioning
4. **Treatment/Transport:** Route to appropriate facility

### ESI (Emergency Severity Index)
**Use for:** ED resource allocation
**Levels:**
- **Level 1 (Emergent):** Requires immediate intervention
- **Level 2 (Emergent):** High-risk situation, confusion, severe pain
- **Level 3 (Urgent):** Stable, limited resources needed
- **Level 4–5 (Less urgent):** Stable with minimal resource needs

## Data & Integration

### Data Sources
- Facility ED census and acuity logs
- Equipment service records and MTBF documentation
- Historical MCI and surge event records
- Staffing schedules and availability patterns

### Integration Points
- EHR systems (HL7 FHIR for patient data)
- Biomedical equipment management systems
- Hospital surge capacity tools
- Training and compliance platforms

## Disclaimer

**This is a decision-support and training tool, not a clinical system.** Triage decisions must always be made by qualified medical professionals following your facility's established protocols and current clinical guidelines. This workspace is designed to:
- Train staff on triage protocols
- Simulate scenarios for exercise and planning
- Aid in resource forecasting and equipment maintenance
- Support continuous improvement through exercise debriefing

Always defer to your institution's medical director, emergency management plan, and current evidence-based guidelines. Do not use this tool for real-time clinical decision-making without qualified medical oversight.

## Support & Feedback

For issues, questions, or feature requests, contact your emergency management or training coordinator. See `work-log/session-log.md` for session history and notes.

---

**Last Updated:** 2026-04-01 | **Version:** 1.0
