# /onboard — Facility Profile & Protocol Initialization

## Purpose
Gather your facility's profile, current protocols, staffing model, equipment inventory, and baseline data. This initializes the workspace for your specific context.

## When to Use
- First time using this workspace (initial setup)
- After significant facility changes (new protocols, major staffing changes, equipment upgrades)
- Annually (refresh baseline data)

## Duration
30–45 minutes for initial setup

## What You'll Provide

I'll ask structured questions covering:

### 1. Facility Profile
- Facility name and type (hospital ED, field triage, urgent care, critical care center)
- Location and regional context
- Typical ED volume (patients/day)
- Bed capacity and specialty units

### 2. Current Triage Protocols
- Which protocols does your facility use? (START, JumpSTART, SALT, ESI, or combination)
- For pediatric patients, do you use JumpSTART?
- Any facility-specific protocol modifications or deviations?
- Do you have a current protocol quick reference that I should review?

### 3. Staffing Model
- Typical ED staffing (physicians, nurses, technicians, support)
- Available surge staffing (call-in protocols, mutual aid agreements)
- Staffing availability by shift (day, evening, night)
- Training frequency and compliance data

### 4. Equipment Inventory
- Critical equipment currently in use (ventilators, monitors, infusion pumps, defibrillators, suction units, etc.)
- Equipment quantities for each item type
- Known MTBF baseline data (from manufacturer or historical service records)
- Recent equipment failures or reliability concerns?

### 5. Historical Data
- Do you have 12 months of ED census data? (volume, acuity trends, seasonal patterns)
- Equipment service records available?
- Previous MCI or surge event documentation?
- Forecast accuracy from any prior forecasting tools?

### 6. Facility Goals
- What's your primary goal with this workspace? (training, planning, maintenance, compliance)
- Key challenges you want to address (triage competency, surge preparedness, equipment reliability)
- Success metrics (e.g., 90% triage accuracy, 40% reduction in equipment downtime)

## Output

After answering these questions, I will:

1. **Customize workspace for your facility:**
   - Update `context/role.md` with your facility context
   - Populate `planning/maintenance-schedule-template.md` with your equipment inventory
   - Note any facility-specific protocol variations

2. **Establish baseline data:**
   - Document typical ED volume and acuity mix
   - Set surge activation thresholds (Green/Yellow/Orange/Red)
   - Establish equipment risk scoring baseline

3. **Create initialization summary:**
   - Document facility profile
   - List assumptions made
   - Identify any data gaps or follow-up needed
   - Recommend next steps (e.g., first simulation, equipment baseline establishment)

4. **Prepare for your first exercise:**
   - Recommend appropriate scenario type (tabletop vs. full-scale)
   - Suggest target competency areas based on your goals
   - Schedule next steps (training, drill planning, etc.)

## How to Run

**In chat, type:** `/onboard`

Then answer the interview questions I present. You can:
- Provide detailed answers or rough estimates (I'll work with what you have)
- Skip questions if data isn't available (we'll note the gap)
- Ask clarifying questions if anything is unclear
- Modify answers if you reconsider (just let me know)

## After Onboarding

You'll be ready to:
- Run simulations with realistic patient volumes and acuity distributions
- Schedule equipment maintenance based on your facility's MTBF baseline
- Plan surge capacity for your facility's typical demand patterns
- Design training exercises tailored to your protocols and staffing
- Track competency and continuous improvement over time

---

**Last Updated:** 2026-04-01
