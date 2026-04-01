# Emergency Triage Protocols Workspace — Creation Report

**Date Created:** 2026-04-01  
**Template:** `emergency-triage-protocols` v1.0  
**Category:** Medical & Health  
**Technique:** Predictive Maintenance Scheduling  

## Purpose

This workspace provides emergency medical teams with a comprehensive decision-support system for applying structured triage protocols (START, JumpSTART, SALT, ESI) to mass casualty incidents (MCIs) and high-volume emergency department scenarios. It integrates triage algorithm validation with predictive analytics for resource demand forecasting and equipment maintenance scheduling.

## Workspace Contents

### Core Documentation (3 files)
1. **CLAUDE.md** — Agent role, available commands, foundational instructions
2. **README.md** — Comprehensive guide, feature overview, quick start, workflows
3. **CREATION_REPORT.md** — This file

### Context & Agent Knowledge (7 files)
4. **context/project.md** — Project scope, objectives, success criteria
5. **context/role.md** — User's role in emergency triage and planning
6. **context/constraints.md** — Boundaries, limitations, safety disclaimers
7. **context/for-agent/domain-knowledge.md** — Full triage protocols (START, JumpSTART, SALT, ESI), decision trees, MTBF models, forecasting mathematics
8. **context/for-agent/workflows.md** — 4 detailed core workflows with step-by-step procedures
9. **context/for-agent/environment.md** — Setup requirements, data sources, dependencies
10. **context/for-agent/tools.md** — Available integrations, APIs, external tools

### Command Implementations (8 files)
11. **.claude/commands/onboard.md** — Interactive facility profile and protocol setup
12. **.claude/commands/triage-sim.md** — Mass casualty simulation execution
13. **.claude/commands/protocol-check.md** — Triage decision validation against protocols
14. **.claude/commands/surge-forecast.md** — ED surge capacity and resource forecasting
15. **.claude/commands/equipment-maint.md** — Equipment maintenance scheduling with predictive analysis
16. **.claude/commands/incident-report.md** — After-action report generation
17. **.claude/commands/resource-calc.md** — Staffing, supply, and transport calculations
18. **.claude/commands/drill-plan.md** — Tabletop and full-scale exercise design

### Prompts & Generators (3 files)
19. **prompts/mci-scenario-generator.md** — Prompt template for realistic MCI scenario creation
20. **prompts/equipment-risk-assessment.md** — Failure risk analysis and prediction prompt
21. **prompts/triage-training-quiz.md** — Interactive training quiz generator

### Reference Materials (3 files)
22. **resources/triage-quick-reference.md** — Decision trees and protocol summaries
23. **resources/equipment-mtbf-reference.md** — MTBF data and failure rate tables
24. **resources/mci-scale-definitions.md** — Casualty scale definitions and incident categories

### User Documentation (2 files)
25. **user-docs/getting-started.md** — Quick start guide for new users
26. **user-docs/report.md** — Report generation and export guide

### Working Directories (2 files)
27. **work-log/session-log.md** — Exercise and session log template
28. **planning/maintenance-schedule-template.md** — Editable equipment maintenance schedule template
29. **outputs/.gitkeep** — Directory for generated reports and simulation outputs

## Key Features Implemented

### 1. Triage Protocol Coverage
- START algorithm (adults, mass casualty scenes)
- JumpSTART algorithm (pediatric, ages 1–8)
- SALT algorithm (comprehensive with interventions)
- ESI framework (ED resource allocation)
- Decision trees for each protocol
- Validation logic against established criteria

### 2. Predictive Maintenance Engine
- MTBF (Mean Time Between Failures) baseline data
- Usage-based degradation modeling
- Risk scoring (low/medium/high failure probability)
- Failure prediction algorithms
- Maintenance scheduling recommendations
- Supply chain and replacement planning

### 3. Resource Forecasting
- Historical pattern analysis
- Time-series forecasting (daily, weekly, seasonal)
- Staffing surge calculations by role
- Supply demand estimation (IV fluids, bandages, medications)
- Transport resource planning
- Capacity bottleneck identification

### 4. Simulation Framework
- Configurable patient volumes (10–10,000+)
- Acuity distribution controls
- Realistic scenario generators
- Real-time resource tracking
- Performance metrics and feedback
- Debrief and improvement recommendations

### 5. Training & Compliance Tools
- Interactive quizzes with answer keys
- Drill planning templates
- Competency tracking
- After-action report generation
- Lessons learned logging

## Workflows Supported

**Workflow 1: MCI Response & Triage Execution**
- Field scene assessment, initial sort, triage assignment, patient routing, resource monitoring, outcome documentation

**Workflow 2: ED Surge Management**
- Census monitoring, surge activation, ESI triage, bed/staff reallocation, capacity forecasting, de-escalation

**Workflow 3: Equipment Maintenance Planning**
- Inventory baseline, usage logging, failure risk calculation, preventive scheduling, service coordination, compliance tracking

**Workflow 4: Training & Drill Execution**
- Protocol selection, scenario generation, real-time training, performance scoring, debriefing, competency logging

## Technical Details

### Domain Expertise
- Evidence-based triage algorithms per CDC, ACEP, and emergency management guidelines
- Predictive failure analysis using statistical MTBF models
- Time-series forecasting for ED surge capacity
- Risk stratification for equipment replacement

### Decision Support Approach
- Step-by-step protocol validation with citations
- Patient safety-first recommendations (over-triage when uncertain)
- Resource optimization and surge planning
- Continuous improvement through exercise logging

### Data Integration
- Facility census and acuity logs
- Equipment service records
- Historical MCI/surge data
- Staffing availability patterns
- Supply chain baselines

## Safety & Compliance

**Critical Disclaimer:** This is a decision-support and training tool, not a clinical system. Actual triage decisions must be made by qualified medical professionals following your institution's established protocols and current clinical guidelines.

Key safety measures:
- All recommendations include evidence-based citations
- Over-triage recommended when decision is ambiguous
- Real-time clinical oversight required
- Compliance with hospital policies and emergency management plans
- Training modules include disclaimers
- After-action review for continuous improvement

## Usage Patterns

### For Emergency Planners & Coordinators
- `/surge-forecast` for capacity planning
- `/drill-plan` for exercise design
- `/equipment-maint` for maintenance scheduling
- `/incident-report` for post-event analysis

### For Triage Training & Competency
- `/triage-sim` for skill practice
- `/protocol-check` for decision validation
- `/onboard` for facility-specific setup
- Quiz generators in `prompts/`

### For Clinical Teams
- Protocol quick references in `resources/`
- Real-time decision support via `/protocol-check`
- Resource calculations via `/resource-calc`
- MCI scenario simulations via `/triage-sim`

### For Quality Assurance
- Session logging in `work-log/`
- Performance metrics from simulations
- After-action reports from `/incident-report`
- Equipment maintenance compliance tracking

## Next Steps

1. **Customize facility profile:** Run `/onboard` to establish your facility's baseline, protocols, and staffing
2. **Review domain knowledge:** Read `context/for-agent/domain-knowledge.md` for protocol details and MTBF models
3. **Run initial simulation:** Use `/triage-sim` with your facility's expected scenario
4. **Set equipment baseline:** Populate `planning/maintenance-schedule-template.md` with your equipment inventory
5. **Design a drill:** Use `/drill-plan` to schedule a training exercise
6. **Review logs:** Check `work-log/session-log.md` after each exercise

## Files Created

Total: **29 files** across **9 directories**

| Directory | Files | Purpose |
|-----------|-------|---------|
| Root | 3 | Core documentation |
| context/ | 4 | Project and agent context |
| context/for-agent/ | 3 | Detailed knowledge and workflows |
| .claude/commands/ | 8 | Command implementations |
| prompts/ | 3 | Scenario and training generators |
| resources/ | 3 | Reference materials |
| user-docs/ | 2 | User guides |
| work-log/ | 1 | Session logging |
| planning/ | 1 | Maintenance planning |
| outputs/ | 1 | Output directory |

---

**Workspace Status:** READY FOR USE  
**Last Updated:** 2026-04-01  
**Version:** 1.0
