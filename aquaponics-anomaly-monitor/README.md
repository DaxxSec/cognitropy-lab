# Aquaponics Anomaly Monitor

### Automated Anomaly Detection for Closed-Loop Food Production Systems

**The Cognitropy Lab — Day 3 Workspace**

> *"In aquaponics, everything is connected. A failing biofilter kills fish. Dead fish crash the plant bed. A crashed plant bed is just expensive compost with a pump. The anomaly you ignored at 9 AM is a system failure by midnight."*

---

## What This Is

A full AI agent workspace for monitoring and diagnosing aquaponics systems with a focus on **automated anomaly detection** — catching deviations in water chemistry, biofilter performance, and fish/plant health before they cascade into system failures.

Aquaponics is a closed-loop system where fish waste feeds beneficial bacteria that convert ammonia into nitrates that feed plants — all in a recirculating water column. This interdependence is its strength and its vulnerability. A single parameter drifting out of range can trigger a cascade: elevated ammonia → bacterial die-off → nitrite spike → fish stress → oxygen depletion → system crash.

This workspace gives you the analytical framework to detect those drifts early, correlate multi-parameter events, perform root cause analysis, and maintain detailed operational logs.

---

## Who This Is For

- Backyard aquaponics hobbyists managing small systems (100–1000L)
- Commercial aquaponics operators with production-scale rigs
- Research institutions running controlled aquatic experiments
- Food security projects and community farms
- Anyone who has ever lost a batch of fish to a silent ammonia spike at 3 AM

---

## The Anomaly Detection Framework

The agent uses a three-tier detection model inspired by network security monitoring principles:

```
    TIER 1: Threshold Alerts         TIER 2: Rate-of-Change           TIER 3: Compound Events
    ─────────────────────────────    ──────────────────────────────   ──────────────────────────────
    Static min/max bounds per        Δ/hour triggers — sudden         Multi-parameter correlation
    parameter. First line of         changes matter even when         detects systemic failures
    defense.                         absolute values look fine        vs. simple noise
    
    pH < 6.5 → WARNING               pH drop >0.5/hr → ALERT          pH↓ + NH3↑ + NO2↑ → 
    NH3 > 0.5 ppm → CRITICAL         Temp drop >2°C/hr → ALERT        BIOFILTER CRASH
    DO < 4 mg/L → CRITICAL           DO drop >1 mg/L/hr → ALERT       NH3↑ + DO↓ → FISH KILL RISK
```

---

## Getting Started

### Prerequisites
- A Claude Code installation (or compatible AI CLI)
- Your system's sensor data (manual readings or exported CSV from controller)
- Basic aquaponics setup knowledge

### Setup

```bash
# Clone the Cognitropy Lab
git clone https://github.com/DaxxSec/cognitropy-lab.git
cd cognitropy-lab/aquaponics-anomaly-monitor

# Launch the agent
claude

# Initialize the workspace for your specific system
/onboard
```

The `/onboard` command will walk you through documenting your system — fish species, plant beds, tank volumes, biofilter type, sensor setup, and historical context. This establishes the baselines everything else is measured against.

---

## Slash Commands Reference

### `/onboard`
**Purpose:** Initialize the workspace for your aquaponics system.

Collects: fish species + stocking density, tank volume, plant bed type and area, biofilter type and age, sensor inventory, recent history (disease events, chemical treatments, system changes).

Output: Populated `context/project.md`, initial baseline estimates, system diagram in text format.

---

### `/scan`
**Purpose:** Run a full anomaly detection pass on your latest sensor readings.

Usage: Paste in your current readings or provide a CSV path.
```
/scan
pH: 6.9, Temp: 28.1°C, NH3: 0.08 ppm, NO2: 0.04 ppm, NO3: 22 ppm, DO: 7.1 mg/L
```

Output: Parameter-by-parameter status (OK/WARN/CRITICAL), rate-of-change flags if history is provided, compound event detection, prioritized action list.

---

### `/triage`
**Purpose:** Assess and prioritize multiple active alerts.

When multiple parameters are out of range simultaneously, this command determines what to address first and in what order — preventing you from fixing the symptom while the cause continues.

Output: Root event identification, intervention priority queue, time-to-critical estimates for each active issue.

---

### `/diagnose [parameter]`
**Purpose:** Deep-dive root cause analysis on a specific parameter anomaly.

```
/diagnose ammonia
/diagnose pH crash
/diagnose dissolved oxygen
```

Output: Differential diagnosis tree for that parameter, most likely causes ranked by probability, supporting questions, recommended confirmatory tests.

---

### `/baseline`
**Purpose:** Establish or update normal operating baselines for your system.

Requires: At least 7 days of stable readings (CSV or pasted).

Output: Statistical baselines (mean, ±1σ, ±2σ) for each parameter, anomaly thresholds calibrated to your specific system rather than generic textbook values.

---

### `/chemistry`
**Purpose:** Full water chemistry analysis including parameter interactions.

Output: Complete chemistry snapshot, nitrogen cycle efficiency assessment, mineral balance review, plant nutrient availability (Fe, Ca, Mg, K), recommended adjustments with dosage calculations.

---

### `/biofilter`
**Purpose:** Biofilter health assessment and nitrogen cycle audit.

Input: Ammonia, nitrite, nitrate readings + biofilter type, age, and media volume.

Output: Nitrogen cycle efficiency score, bacterial colony health estimate, media loading assessment, recommended corrective actions.

---

### `/report`
**Purpose:** Generate a structured system health report.

Output: Executive summary, parameter table with trend indicators, active alerts, 7-day trend analysis (if log history available), recommended maintenance actions, report saved to `outputs/`.

---

## Water Chemistry Quick Reference

### The Nitrogen Cycle — The Heart of Every Aquaponics System

```
    Fish eat food
         │
         ▼
    Fish excrete ammonia (NH3/NH4+)
         │
         ▼
    Nitrosomonas bacteria oxidize NH3 → Nitrite (NO2-)    ← TOXIC to fish
         │
         ▼
    Nitrobacter/Nitrospira oxidize NO2- → Nitrate (NO3-)  ← Plant food
         │
         ▼
    Plants absorb NO3- → removes it from the system
```

**If the cycle breaks:**
- NH3 spikes → check biofilter, look for dead fish, check pH (acidic pH kills bacteria)
- NO2 spikes → NH3 was converted but cycle is incomplete — Nitrobacter under stress
- NO3 builds up without conversion → insufficient plant uptake or system overloaded

### Ideal Parameter Ranges by Fish Species

| Parameter | Tilapia | Trout | Perch | Catfish | Carp |
|---|---|---|---|---|---|
| Temperature | 26–30°C | 12–18°C | 18–24°C | 24–30°C | 20–28°C |
| pH | 6.5–8.5 | 6.5–8.0 | 6.5–8.5 | 6.5–8.5 | 6.5–8.0 |
| NH3 max | 0.5 ppm | 0.3 ppm | 0.5 ppm | 0.5 ppm | 0.4 ppm |
| DO min | 4 mg/L | 7 mg/L | 5 mg/L | 4 mg/L | 5 mg/L |

### Parameter Interactions — Compound Alert Matrix

| Combination | Likely Cause | Urgency |
|---|---|---|
| NH3↑ + NO2↑ + pH↓ | Biofilter crash | 🔴 Critical |
| NH3↑ + NO2↑ + pH stable | Biofilter overloaded | 🟠 High |
| DO↓ + Temp↑ | Warm water holds less O2, check aeration | 🟠 High |
| pH↓ + DO stable | CO2 buildup — check plant zone | 🟡 Medium |
| NO3↑ steady rise | Insufficient plant uptake or overfeeding | 🟡 Medium |
| EC↑ + pH stable | Mineral buildup — partial water change | 🟡 Medium |
| Temp↓ sudden + NH3↑ | Equipment failure (heater), stressed biofilter | 🔴 Critical |

---

## File Structure

```
aquaponics-anomaly-monitor/
├── CLAUDE.md                        # Agent brain (this powers the agent)
├── README.md                        # This file
├── context/
│   ├── project.md                   # Your system details (fill via /onboard)
│   ├── role.md                      # Operator expertise and context
│   ├── constraints.md               # System limits and preferences
│   └── for-agent/
│       ├── environment.md           # Sensor setup, data sources
│       └── workflows.md             # Deep domain workflows (200+ lines)
├── .claude/commands/
│   ├── onboard.md
│   ├── scan.md
│   ├── triage.md
│   ├── diagnose.md
│   ├── baseline.md
│   ├── chemistry.md
│   ├── biofilter.md
│   └── report.md
├── prompts/
│   ├── anomaly-scan-template.md
│   ├── root-cause-analysis-template.md
│   └── weekly-health-report-template.md
├── resources/
│   ├── parameter-reference.md
│   ├── species-profiles.md
│   └── troubleshooting-matrix.md
├── work-log/                        # Session notes and findings
├── planning/                        # Investigation plans and goals
└── outputs/                         # Generated reports
```

---

## Example Session

```
Operator: pH is reading 6.1 this morning, was 7.0 yesterday. Fish are at the surface.
 
Agent: CRITICAL — Rapid pH crash detected (Δ-0.9 over ~12 hours).
       Fish surfacing = low dissolved oxygen, likely secondary to pH crash.
       
       Differential diagnosis:
       1. [MOST LIKELY] CO2 buildup overnight — check if aeration was disrupted
       2. Acid dose mishap — did any pH-down product get added recently?
       3. Biofilter crash + acid metabolite buildup
       4. Rainwater intrusion (low pH source)
       
       Immediate actions (in order):
       1. Check and restore aeration immediately — fish need DO now
       2. Test DO — if <4 mg/L, add emergency aeration
       3. Test ammonia — if >0.5 ppm, we have a biofilter event not just a gas event
       4. Do NOT try to rapidly correct pH — a swing back is as dangerous as the crash
       5. Gradual sodium bicarbonate buffering if DO is restored and NH3 is clean
       
       What does your ammonia read right now?
```

---

## Built By

The Cognitropy Lab — Day 3 Workspace  
Assigned by: [cognitropy.py](../cognitropy.py)  
Domain: Aquaponics | Technique: Automated Anomaly Detection  
Built by: Claude (Anthropic) × [DaxxSec](https://github.com/DaxxSec)  
Date: 2026-03-28
