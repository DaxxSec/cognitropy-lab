# Wildland Invasive Scout

### Bushcraft Intelligence + Invasive Species Management Methodology

**A Claude Agent workspace that fuses wilderness skills with structured ecological surveillance — applying the systematic methodologies of invasive species managers to the work of field practitioners, guides, foragers, and land stewards.**

> *Cognitropy Assignment — Day 1: BUSHCRAFT × INVASIVE SPECIES MANAGEMENT, with automated anomaly detection*

---

## The Core Idea

Every invasive species manager knows something that most bushcraft practitioners don't: **wild landscapes have a detectable baseline, and anything that doesn't fit that baseline is a signal worth investigating.**

Invasive species managers use systematic transect surveys, anomaly scoring matrices, species classification protocols, and citizen science reporting pipelines as their standard toolkit. These are the same methodological building blocks that power anomaly detection in any domain — establishing a normal state, then flagging deviations with a severity score.

This workspace applies all of that to your work in the field — whether you're a wilderness guide, a homesteader managing 200 acres, a forager who wants to eat safely, or just a bushcraft practitioner who wants to understand what they're walking through.

---

## What It Does

The Wildland Invasive Scout gives you a structured intelligence system for wild environments:

- **Systematic field surveys** following invasive species management transect protocols
- **Anomaly detection** that scores deviations from ecological baseline with priority levels
- **Species identification** using the professional 4-Feature Rule with confidence scoring
- **Foraging safety cross-checks** against toxic lookalikes and site contamination risks
- **Camp site ecological evaluation** — water safety, vegetation hazards, invasive spread risk
- **Seasonal baseline tracking** — drift detection across multiple visits over time
- **Citizen science reporting** — EDDMapS and iNaturalist compatible output formats

---

## Who This Is For

- **Bushcraft practitioners** who want to understand ecosystems beyond "edible / not edible"
- **Wilderness guides** responsible for client safety and ecological literacy
- **Land stewards and homesteaders** monitoring their own property for invasive threats
- **Foragers** who want a structured safety protocol before harvesting
- **Hunters and anglers** who spend significant field time and want to contribute ecological data
- **Citizen scientists** wanting a systematic framework for contributing biodiversity observations
- **Anyone who feels unsettled when something in the woods "doesn't look right"**

---

## Quick Start

```bash
# Clone the workspace
git clone https://github.com/DaxxSec/cognitropy-lab.git
cd cognitropy-lab/wildland-invasive-scout

# Open with Claude Code
claude

# Initialize your workspace
/onboard
```

`/onboard` will walk you through setting up your field area, biome context, operator profile, and generate a personalized priority watch species list for your region.

---

## Command Reference

| Command | Purpose |
|---------|---------|
| `/onboard` | Initialize workspace — field area setup, priority watch list, baseline prep |
| `/field-survey` | Run structured transect or plot survey with full documentation output |
| `/species-id` | Apply 4-Feature Rule to identify an unknown plant, animal, or fungi |
| `/anomaly-report` | Score and document an ecological anomaly with priority level and actions |
| `/threat-matrix` | Generate prioritized threat matrix for all detected invasives in your area |
| `/forage-safety` | Full safety cross-check before harvesting — ID verification, lookalikes, site contamination |
| `/camp-eval` | Ecological site evaluation for a potential camp location |
| `/seasonal-baseline` | Record or update seasonal baseline; detect ecological drift over time |

---

## The Anomaly Detection Framework

The core innovation of this workspace is treating ecological observation like a structured anomaly detection system:

```
BASELINE ESTABLISHMENT
        │
        ▼
    What belongs here?    ←── State invasive watch list
    What's in season?     ←── Phenology calendar
    What's the health     ←── Plot survey data
    reference point?
        │
        ▼
    FIELD OBSERVATION
        │
        ▼
    ANOMALY SCORING MATRIX

    Score = Deviation × Spatial Extent × Historical Contrast × Threat Class

    ≤ 4    → Log and monitor
    5-9    → Investigate, submit to iNaturalist
    10-24  → Notify land manager / extension within 48h
    ≥ 25   → IMMEDIATE escalation — potential new incursion
        │
        ▼
    RESPONSE → DOCUMENT → UPDATE BASELINE → REPEAT
```

This isn't just for invasives. The same scoring matrix catches disease outbreaks, drought stress, overharvesting pressure, contamination events — anything that represents a real deviation from a known-healthy ecosystem.

---

## File Structure

```
wildland-invasive-scout/
├── CLAUDE.md                    # Agent instructions (lightweight)
├── README.md                    # This file
├── context/
│   ├── project.md               # Your field area and baseline data
│   ├── role.md                  # Your background and objectives
│   ├── constraints.md           # Safety limits and scope
│   └── for-agent/
│       ├── environment.md       # Tool integrations and behavior notes
│       └── workflows.md         # 8 detailed domain workflows (600+ lines)
├── .claude/commands/
│   ├── onboard.md
│   ├── field-survey.md
│   ├── species-id.md
│   ├── anomaly-report.md
│   ├── threat-matrix.md
│   ├── forage-safety.md
│   ├── camp-eval.md
│   └── seasonal-baseline.md
├── prompts/
│   ├── field-briefing.md        # Pre-field situational awareness template
│   ├── species-description-intake.md  # Systematic unknown species intake form
│   └── land-manager-report.md  # Formal notification report generator
├── resources/
│   ├── high-priority-invasives-reference.md  # Tier 1/2/3 species reference
│   ├── lookalike-pairs-reference.md          # Dangerous species lookalike guide
│   └── reporting-platforms-guide.md          # EDDMapS, iNaturalist, state programs
├── work-log/                    # Survey records, anomaly reports, species IDs
├── planning/                    # Threat matrices, monitoring schedules
├── user-docs/                   # Your custom reference materials
└── outputs/                     # Generated reports and citizen science submissions
```

---

## Resources Included

### High-Priority Invasives Reference
Covers Tier 1 (federal watch list — spotted lanternfly, giant hogweed, emerald ash borer), Tier 2 (high-impact established — Japanese knotweed, kudzu, purple loosestrife, garlic mustard, autumn olive, barberry, tree of heaven), and Tier 3 (monitor and document). Each entry includes diagnostic features, ecological impact, and what to do.

### Dangerous Lookalike Pairs Reference
The pairings that kill people: wild carrot vs. poison hemlock and water hemlock; ramps vs. lily of the valley and false hellebore; chanterelle vs. jack-o-lantern; elderberries vs. pokeweed. Each pairing includes a feature comparison table and definitive ruling criteria.

### Reporting Platforms Guide
How to submit observations to iNaturalist, EDDMapS, iMapInvasives, USDA APHIS ReportAPest, and eBird. Includes photo standards, offline workflow for no-service areas, and state-level program contacts.

---

## Example Workflows

### Before a Foraging Trip
1. Run `/onboard` to set up your field area (first time) or review your baseline (return trip)
2. Use the `prompts/field-briefing.md` template to get a pre-field briefing
3. In the field, run `/forage-safety` for each harvest target
4. Log any anomalies with `/anomaly-report`

### Monitoring Your Land
1. Run `/seasonal-baseline` at the start of each season to establish reference points
2. Run `/field-survey` quarterly along the same transects
3. Log all detected invasives and run `/threat-matrix` to prioritize management actions
4. Generate reports for county extension office using `prompts/land-manager-report.md`

### Teaching Ecological Literacy
1. Brief students using field-briefing template
2. Walk through the `/species-id` protocol as a teaching exercise with unknown specimens
3. Score anomalies together using `/anomaly-report` — the scoring matrix is educational
4. Submit observations to iNaturalist as citizen science contribution

---

## Integration with External Tools

The workspace is designed to work with:
- **iNaturalist** — observation upload and community ID
- **EDDMapS** — invasive species reporting
- **Gaia GPS / onX Hunt** — waypoint and track file input
- **USDA PLANTS Database** — native/non-native status verification
- **eBird** — bird observation data

No API connections required — all integrations are workflow-based (the agent generates properly formatted data for manual upload, or guides you through app-based submission).

---

## Safety Notice

This workspace provides advisory assistance and educational content. It does not replace:
- Expert botanical or mycological identification for consumption decisions
- Professional ecological surveys required for regulatory purposes
- Medical treatment (if you've had contact with a toxic plant, call Poison Control: 1-800-222-1222)

**When in doubt about any wild food: DO NOT CONSUME.**

---

## About This Workspace

Built by the [Cognitropy Lab](https://github.com/DaxxSec/cognitropy-lab) — an entropy-driven agent workspace factory where Claude gets assigned a random domain each day and has to build something useful.

Day 1 Assignment: **BUSHCRAFT × INVASIVE SPECIES MANAGEMENT, with automated anomaly detection.**

The crossover turned out to be genuinely compelling: invasive species managers already do exactly what good bushcraft practitioners should be doing — systematic observation, anomaly detection, evidence-based decision making, and structured documentation. They just usually do it on managed landscapes with government backing. This workspace brings that methodology to the individual practitioner operating in the field.
