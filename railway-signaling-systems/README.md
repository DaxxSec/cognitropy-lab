# Railway Signaling Systems Workspace

> **Cognitropy Lab** · Engineering & Technical · Day 19 · Technique: Apprenticeship Progression Tracking

A structured learning environment for railway signaling engineers at all stages — from first-year apprentices handling basic track circuits to senior technicians preparing for Incorporated or Chartered Engineer status with the Institution of Railway Signal Engineers (IRSE).

Signal Mentor guides you through the full signaling discipline: electrical track circuits, mechanical and electronic interlockings, ATP/ATC systems, ETCS/ERTMS, safety integrity levels, and the competency assessments required to advance through your apprenticeship.

---

## What This Workspace Does

- **Tracks your apprenticeship progression** through structured competency levels (Foundation → Developing → Competent → Proficient → Expert)
- **Explains signaling concepts** with the safety-critical depth they deserve — no handwavy oversimplification
- **Generates practice assessments** mapped to IRSE competency frameworks and NVQ/SVQ standards
- **Analyzes historical incidents** (Ladbroke Grove, Grayrigg, Potters Bar) as learning tools
- **Guides exam preparation** for IRSE Licences, NVQ Level 3/4, and Engineering Council registration

---

## Who This Is For

- Apprentice signal technicians (Year 1–4 of a railway signaling apprenticeship)
- Qualified signal technicians upskilling to engineering grades
- Graduate engineers rotating through signaling disciplines
- Experienced engineers refreshing knowledge after a domain gap
- Academics and students studying railway systems engineering

---

## Quick Start

1. Clone or open this workspace in your Claude environment
2. Run `/onboard` — the agent will assess your current level and set up your learning profile
3. Review `context/role.md` to confirm your details are accurate
4. Use `/progress` to see your competency map and what to tackle next
5. Dive into any concept with `/explain [topic]`

---

## Directory Structure

```
railway-signaling-systems/
├── CLAUDE.md                        # Agent identity and command list
├── README.md                        # This file
├── CREATION_REPORT.md               # Why this workspace was built
├── context/
│   ├── project.md                   # Active learning goals
│   ├── role.md                      # Your apprenticeship level and background
│   ├── constraints.md               # Regulatory boundaries and preferences
│   └── for-agent/
│       ├── domain-knowledge.md      # Railway signaling technical reference
│       ├── workflows.md             # Apprenticeship progression workflows
│       ├── tools.md                 # Software tools and testing methods
│       └── environment.md          # Your work/study environment
├── .claude/commands/
│   ├── onboard.md                   # Workspace initialization
│   ├── progress.md                  # Competency tracking
│   ├── explain.md                   # Deep-dive explanation
│   ├── quiz.md                      # Knowledge assessment
│   └── incident.md                  # Incident analysis
├── prompts/                         # Reusable prompt templates
├── resources/                       # Reference materials and standards guides
├── planning/                        # Study plans and milestone tracking
├── work-log/                        # Session history
└── outputs/                         # Generated documents, assessments
```

---

## Domain Overview: Railway Signaling

Railway signaling is the system of rules, equipment, and processes that control the movement of trains to prevent collisions and derailments. It is one of the most safety-critical engineering disciplines — failures have historically caused mass casualties.

### Core Signaling Principles

**The Fundamental Problem:** Multiple trains must share the same track network safely, often without line-of-sight communication between trains or between drivers and controllers.

**Block Working:** The network is divided into *block sections* — segments of track that can only be occupied by one train at a time. The signaling system enforces this separation.

**Fail-Safe Design:** All railway signaling equipment must be designed so that any failure defaults to the *most restrictive* (safest) state. A broken signal defaults to red, not green. A track circuit failure shows the section as *occupied*, not clear.

### Signal Types

| Type | Description | Era |
|------|-------------|-----|
| Semaphore | Mechanical arm position indicates proceed/stop | 1840s–present (heritage) |
| Colour Light | LED/lamp aspect signals (red/yellow/green/double yellow) | 1920s–present |
| LED Position Light | Matrix of white dots indicating route/aspect | UK suburban lines |
| ETCS Cab Signal | No lineside signal — all information in driver's cab | Modern ERTMS lines |

### Train Detection Methods

**Track Circuits:** An electrical circuit through the rails detects a train's presence by the short circuit created through its steel wheels and axles. Immune to counting errors but sensitive to rail breaks and ballast contamination.

**Axle Counters:** Count axles entering and leaving a section. More immune to rail conditions than track circuits but require careful reset procedures — a key competency area.

**Transponders/Balises:** Fixed beacons in the track (ETCS Eurobalise, legacy AWS magnets) that communicate route and speed information to passing trains.

### Interlocking Systems

The interlocking is the heart of the signaling system. It enforces that signals and points (switches) cannot be set in conflicting configurations — preventing head-on collisions or derailments through wrongly-set routes.

**Mechanical Interlockings:** Physical levers in a signal box connected by mechanical linkages. Still in use on heritage and some rural lines.

**Relay Interlockings (RI):** Electromechanical relay logic. The dominant UK technology from ~1950–1990. Extremely reliable but large, expensive to maintain.

**Solid-State Interlockings (SSI):** Microprocessor-based, introduced in UK from 1985. Smaller, cheaper to maintain. Still widely deployed.

**Computer-Based Interlockings (CBI):** Modern software-defined interlockings (e.g., Westinghouse IXL, Alstom Smartlock). COTS hardware with proprietary safety-certified software.

**European Vital Computer (EVC):** The onboard computer in ETCS-equipped trains.

### Automatic Train Protection & Control

- **AWS (Automatic Warning System):** UK legacy system — magnet in track triggers a horn/bell in the cab; driver must acknowledge
- **TPWS (Train Protection & Warning System):** UK overlay to AWS; triggers emergency brake if train overruns a signal at danger
- **ATP (Automatic Train Protection):** Generic term for systems that enforce speed and stop commands without driver action
- **ETCS (European Train Control System):** Standardized European ATP with three application levels (Level 1, 2, 3)
- **ERTMS:** European Rail Traffic Management System — the broader program including ETCS and GSM-R radio

### Safety Integrity Levels

Railway signaling systems are assessed against IEC 62279 (formerly EN 50128) and IEC 62280 using Safety Integrity Level (SIL) classification:

| SIL | Tolerable Hazard Rate | Typical Application |
|-----|----------------------|---------------------|
| SIL 4 | < 10⁻⁸/hour | Vital interlocking, ATP enforcement |
| SIL 3 | < 10⁻⁷/hour | Cab signaling, train detection |
| SIL 2 | < 10⁻⁶/hour | Level crossing protection |
| SIL 1 | < 10⁻⁵/hour | Non-vital control systems |

Understanding SIL is essential from Developing level onward — you will be tested on this in IRSE assessments.

---

## Apprenticeship Competency Levels

| Level | Title | Typical Stage | Key Competencies |
|-------|-------|---------------|-----------------|
| L1 | Foundation | Year 1 apprentice | Health & safety, basic electrical, signal identification |
| L2 | Developing | Year 2–3 apprentice | Track circuits, signal maintenance, fault-finding basics |
| L3 | Competent | Year 4 / NVQ Level 3 | Interlocking maintenance, axle counter resets, full fault diagnosis |
| L4 | Proficient | Signal engineer / NVQ Level 4 | Design review, modification approval, IRSE Licence |
| L5 | Expert | Senior / CEng candidate | System architecture, safety cases, mentoring |

---

## Key Standards and References

- **IRSE Licensing Scheme** — UK professional competency framework for signal engineers
- **Network Rail Standards (NR/SP/SIG)** — UK infrastructure manager's signaling standards
- **IEC 62279 / EN 50128** — Software for railway control and protection systems
- **IEC 62280 / EN 50159** — Safety-related communication in railway systems
- **RIS-0737-CCS** — Network Rail requirements for computer-based interlockings
- **GM/RT2447** — Requirements for TPWS
- **ERA ETCS Subset documents** — European ETCS specifications

---

## Slash Command Reference

| Command | Usage |
|---------|-------|
| `/onboard` | First-run setup: assess level, capture background, set goals |
| `/progress` | Show competency map, flag what to tackle next |
| `/explain [topic]` | Detailed technical explanation with safety context |
| `/quiz [level or topic]` | Generate assessment questions |
| `/incident [name or description]` | Analyze a real or hypothetical incident |

---

## Tips for Using This Workspace

- Be specific about your level when asking questions — "explain track circuits for a Year 1 apprentice" gets better results than just "explain track circuits"
- Use `/incident` with real events (Ladbroke Grove 1999, Potters Bar 2002, Grayrigg 2007) to understand how signaling failures cascade
- Log each study session in `work-log/session-log.md` so the agent has context across sessions
- When you pass an assessment or milestone, update `context/role.md` — Signal Mentor calibrates its depth to your documented level

---

*Built by Cognitropy Lab · 2026-04-13 · Engineering & Technical domain*
