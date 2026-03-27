# ECU Tune & Engine Build Workspace

> A Claude Agent Workspace for performance tuners, engine builders, and automotive enthusiasts who want an intelligent co-pilot for ECU calibration, build documentation, datalog analysis, and modification planning.

---

## What Is This?

This workspace transforms Claude into a knowledgeable tuning assistant that remembers your vehicle, your build, your safety limits, and your goals. It's designed for anyone who works with forced-induction or naturally-aspirated builds, standalone or OEM ECUs, and wants structured support through the entire tuning and build cycle.

Whether you're dialing in a street tune, chasing track numbers, or documenting a full engine build for posterity — this workspace keeps everything organized and gives Claude the context it needs to be genuinely useful rather than generic.

---

## Getting Started

### Step 1 — Clone or copy this workspace
Place the workspace in your preferred directory and open it in Claude Code.

### Step 2 — Run `/onboard`
This is the first command you must run. It will interview you about your vehicle, goals, ECU platform, and tuning environment, then populate the `context/` files so Claude can serve as your personalized tuning assistant.

```
/onboard
```

### Step 3 — Start working
Once onboarded, use the slash commands below to analyze tunes, review datalogs, log builds, plan dyno sessions, and more.

---

## Command Reference

| Command | Trigger | What It Does |
|---|---|---|
| `/onboard` | First run | Interviews you to populate all context files |
| `/analyze-tune` | After providing ECU map data | Analyzes maps for safety margins, timing, fuel, boost limits |
| `/review-datalog` | Paste or describe a datalog | Parses key channels, flags knock/lean/overboost events |
| `/build-log` | Adding or reviewing mods | Logs parts, installs, dyno numbers, notes |
| `/dyno-plan` | Before a dyno session | Creates a structured pull plan with safety protocol |
| `/parts-research` | Researching upgrades | Evaluates compatibility, specs, and fitment for your application |
| `/diagnose` | Chasing a problem | Interprets symptoms, codes, and observed behavior into likely causes |
| `/tune-diff` | Comparing tune revisions | Highlights what changed between two calibration states |

---

## Directory Structure

```
ecu-tune-engine-build-workspace/
├── CLAUDE.md                    # Lightweight agent config (loaded every prompt)
├── README.md                    # This file
├── context/
│   ├── project.md               # Vehicle, engine, ECU, and build configuration
│   ├── role.md                  # Your tuning experience level and goals
│   ├── constraints.md           # Safety limits, budget constraints, preferences
│   └── for-agent/
│       ├── environment.md       # Tools, software, dyno, and workshop details
│       └── workflows.md         # Detailed agent workflows and decision trees
├── work-log/                    # Session-by-session notes and activity
├── planning/                    # Dyno session plans, build roadmaps
├── user-docs/                   # Generated reference docs (your tune notes, etc.)
├── .claude/
│   └── commands/
│       ├── onboard.md
│       ├── analyze-tune.md
│       ├── review-datalog.md
│       ├── build-log.md
│       ├── dyno-plan.md
│       ├── parts-research.md
│       ├── diagnose.md
│       └── tune-diff.md
├── prompts/                     # Reusable prompt templates
├── resources/                   # Reference tables, checklists, specs
├── outputs/                     # Generated documents and reports
└── .mcp.json                    # Optional MCP server configurations
```

---

## Example Use Cases

### 1. Street/Track Tune Management
Keep a living document of your tune history. Every time you make changes — whether adjusting ignition timing tables, modifying boost targets, or tweaking fuel trims — log the session with `/build-log` and use `/analyze-tune` to sanity-check safety margins before hitting the road.

### 2. Datalog Review After a Pull
After a hard pull, paste your datalog CSV into Claude and run `/review-datalog`. The agent will parse key channels like AFR, knock counts, throttle position, boost pressure, and coolant temp to flag anything worth investigating before the next pull.

### 3. Engine Build Planning
Starting a fresh build? Use `/build-log` to create the initial parts manifest, track receipts and install notes, and document the baseline configuration. Use `/parts-research` to evaluate upgrade options based on your goals (e.g., "I want to push 600whp on pump gas on a built EJ257").

### 4. Dyno Day Preparation
Before trailering to the dyno, run `/dyno-plan` to generate a structured session plan: target power levels, pull strategy (2 pulls, 4th gear, brake at 7200rpm), cooldown protocol, safety pull sequence, and go/no-go criteria.

### 5. OBD Code Diagnosis
Hit a CEL? Run `/diagnose` with the code and any observed symptoms. Claude will walk through likely causes ranked by probability, suggest diagnostic tests, and cross-reference known issues for your specific platform.

### 6. Tune Version Comparison
Received a revised map file from your tuner? Use `/tune-diff` to document what changed between sessions, track the evolution of your calibration, and maintain a history of what worked vs. what didn't.

---

## Recommended Tools & Integrations

### Tuning Software (Describe your setup during /onboard)
- **Subaru/EJ/FA:** COBB Accessport / EcuFlash / RomRaider / EvoScan
- **Nissan/GM/Ford:** HP Tuners, EFI Live, Tuner Studio
- **Standalone:** MegaSquirt / Haltech / AEM / Link / Motec
- **Universal Logging:** RaceCapture, AiM Solo, GoPro Telemetry

### MCP Servers (Optional, configure in .mcp.json)
- **filesystem:** Direct access to your tune files, datalogs, and build notes
- **fetch:** Pull spec sheets, forum threads, and technical documentation
- **sqlite:** Store and query build history and dyno results in a local database

---

## Supported ECU Platforms

This workspace is platform-agnostic but has reference materials for:
- **OEM-based:** Subaru (EJ/FA/FB), Mitsubishi (4G63/4B11), Honda (K/B/H series), GM (LS/LT), Ford (Coyote/EcoBoost), Nissan (RB/SR/VQ/VR)
- **Standalone:** MegaSquirt series, Haltech Elite/Nexus, AEM Infinity, Link G4X, Motec M1/M150
- **Diesel Performance:** Cummins, Duramax, PowerStroke tuning workflows

---

## Safety Disclaimer

This workspace is a **documentation and analysis assistant**, not a replacement for hands-on tuning expertise or a calibrated dyno. All tuning decisions carry real risk of engine damage, fire, or injury. Always:

- Start conservative (lean timing, conservative fueling) and work toward targets
- Use a wideband O2 sensor — never trust narrow-band for tuning
- Have a fire extinguisher accessible during all dyno and road-tuning sessions
- Know your platform's knock sensitivity and safe timing windows
- Never tune on detonating fuel — verify octane before every session
- Consult a qualified tuner for safety-critical calibration decisions

---

## About This Workspace Template

Built following the [Claude Agent Workspace Model](https://github.com/danielrosehill/Claude-Agent-Workspace-Model). Inspired by the structured approach of purpose-built AI workspaces for technical domains.
