# Getting Started with Emergency Triage Protocols Workspace

Welcome! This guide helps you begin using the Emergency Triage Protocols workspace for training, planning, and decision-support.

## 5-Minute Quick Start

### 1. Understand Your Role
- **Clinician?** You'll use `/protocol-check` and training simulations
- **Planner?** You'll use `/surge-forecast` and `/drill-plan`
- **Biomedical Engineer?** You'll use `/equipment-maint` for maintenance scheduling
- **Trainer?** You'll use `/triage-sim` and drill planning tools

→ Read `context/role.md` for your specific responsibilities

### 2. Review Triage Protocols
- Start with `resources/triage-quick-reference.md` (1-page decision trees)
- Protocols supported: START, JumpSTART, SALT, ESI
- Print and laminate for your triage area!

### 3. Run Your First Command
Choose based on your role:
- **Training:** `/triage-sim` — Run a 30-minute practice scenario
- **Planning:** `/surge-forecast` — Forecast next 24 hours of ED demand
- **Maintenance:** `/equipment-maint` — Check equipment risk status
- **Setup:** `/onboard` — Initialize your facility profile

## Core Concepts

### Triage Category System
All protocols use four core categories:
- **RED (Immediate):** Life-threatening, salvageable with immediate intervention
- **YELLOW (Delayed):** Serious but stable injuries
- **GREEN (Minor):** Walking wounded, minor injuries
- **BLACK (Expectant):** Non-salvageable in resource-constrained setting

### START Protocol (Most Common)
For adults in mass casualty scenes, assess three things in order:
1. **Respiration:** RR <10 or >30? → RED
2. **Perfusion:** Radial pulse? CRT <2 sec? → RED
3. **Mental Status:** Follows commands? → RED if unable

→ See `context/for-agent/domain-knowledge.md` for full protocol

### Risk Scoring (Equipment)
Equipment failure risk calculated as:
**Risk Score = (Operating Hours / MTBF Baseline) × 100**
- 0–50% = Green (normal)
- 50–75% = Yellow (schedule maintenance)
- 75–90% = Orange (urgent)
- 90%+ = Red (replace now)

## Available Commands

| Command | Purpose | Time |
|---------|---------|------|
| `/onboard` | Set up your facility profile | 30–45 min |
| `/triage-sim` | Run a training simulation | 30–120 min |
| `/protocol-check` | Validate a triage decision | 2–5 min |
| `/surge-forecast` | Predict ED demand | 15–30 min |
| `/equipment-maint` | Schedule equipment maintenance | 10–30 min |
| `/incident-report` | Generate after-action report | 30–90 min |
| `/resource-calc` | Calculate staffing/supply needs | 15–30 min |
| `/drill-plan` | Design a training exercise | 1–2 hours |

**Start with:** `/onboard` to initialize your facility context

## Key Files to Review

**Essential (Read First):**
1. `CLAUDE.md` — Agent role and commands
2. `README.md` — Full workspace overview
3. `resources/triage-quick-reference.md` — Decision trees (print!)

**For Your Role:**
- **Clinicians:** `context/for-agent/domain-knowledge.md`, `.claude/commands/protocol-check.md`
- **Planners:** `.claude/commands/surge-forecast.md`, `.claude/commands/drill-plan.md`
- **Engineers:** `.claude/commands/equipment-maint.md`, `resources/equipment-mtbf-reference.md`
- **Trainers:** `.claude/commands/triage-sim.md`, `prompts/triage-training-quiz.md`

**Reference:**
- `context/constraints.md` — Safety disclaimers, boundaries
- `planning/maintenance-schedule-template.md` — Edit with your equipment

## Workflow Examples

### Example 1: Train Your Team on START Protocol
1. Print `resources/triage-quick-reference.md`
2. Use `/triage-sim` to run a 30-minute scenario with your team
3. Debrief using the feedback provided
4. Log results in `work-log/session-log.md`

### Example 2: Prepare for Flu Season Surge
1. Run `/surge-forecast` with January historical data
2. Output will show: Peak demand day/time, staffing needs, supply forecast
3. Use `/resource-calc` to validate staffing surge plan
4. Share forecast with ED leadership for approval
5. Use `/drill-plan` to schedule a pre-season tabletop exercise

### Example 3: Schedule Equipment Maintenance
1. Gather equipment MTBF baseline from `resources/equipment-mtbf-reference.md`
2. Run `/equipment-maint` with your equipment operating hours
3. Output will show: Risk score, maintenance timing, contingency plan
4. Schedule with biomedical engineering
5. Update `planning/maintenance-schedule-template.md` with new schedule

### Example 4: Conduct Competency Assessment
1. Use `prompts/triage-training-quiz.md` to generate a 10-question quiz
2. Staff answer questions (START protocol focus)
3. Score results (90%+ competent, 70–89% needs review, <70% requires remedial training)
4. Document in `work-log/session-log.md` for annual competency records

## Important Disclaimers

**This Is a Decision-Support Tool, Not a Clinical System:**
- Real triage decisions must be made by qualified medical professionals
- Always defer to your facility's protocols and medical director
- Use this workspace for training, planning, and exercising
- Include medical oversight for all real-world decisions

**Safety First:**
- When uncertain, over-triage (recommend higher acuity)
- Patient safety is paramount
- Document all decisions and reasoning
- Continuous improvement through after-action review

## Getting Help

### For Triage Protocol Questions
- Read: `resources/triage-quick-reference.md` (fast reference)
- Read: `context/for-agent/domain-knowledge.md` (detailed explanation)
- Use: `/protocol-check` (validate a specific decision)
- Ask: Your facility's experienced triage officer or medical director

### For Command Usage
- Read: `.claude/commands/[command-name].md` (detailed instruction for each command)
- Example: To learn `/triage-sim`, read `.claude/commands/triage-sim.md`

### For Workspace Setup
- Run: `/onboard` (interactive facility profile setup)
- Read: `context/role.md` (your specific responsibilities)
- Read: `context/environment.md` (setup requirements, data sources)

### For Technical Issues
- Contact: Workspace administrator
- Or: Your facility IT support

## Next Steps

1. **Right Now (5 min):** Read this file + `CLAUDE.md`
2. **This Week (30 min):** Run `/onboard` to set up your facility
3. **This Week (1 hour):** Review `resources/triage-quick-reference.md` + print/laminate
4. **Next 2 Weeks:** Run your first command matching your role
5. **Ongoing:** Use `work-log/session-log.md` to log all exercises for continuous improvement

## Frequently Asked Questions

**Q: Can I use this for real-time clinical triage?**
A: No. This is a training and decision-support tool. Real triage decisions require qualified medical professionals and direct patient assessment.

**Q: What if I don't have all the data (census, MTBF, etc.)?**
A: That's okay! Share what you have, and I'll work with estimates and defaults. We can refine as you gather more data.

**Q: How often should we exercise?**
A: Recommend quarterly tabletop, annually full-scale. More frequent if identified gaps.

**Q: Can I modify the protocols?**
A: Facility-specific adaptations should be approved by your medical director. Document any deviations in `context/constraints.md`.

**Q: How do I track competency?**
A: Use `/triage-sim` or `prompts/triage-training-quiz.md` to assess. Document results in `work-log/session-log.md`. Compare results over time for trend analysis.

---

**You're Ready! Start with `/onboard` or read `README.md` for full overview.**

Last Updated: 2026-04-01
