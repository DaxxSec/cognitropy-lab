# /field-survey — Run Structured Invasive Species Field Survey

## Purpose
Guide the operator through a systematic transect or plot survey following invasive species management methodology. Produces a structured survey record suitable for EDDMapS, iNaturalist, and internal documentation.

## Pre-Survey Setup
Ask the operator:
1. Survey type: **Transect** (linear feature, trail, road edge) or **Plot** (fixed area, baseline monitoring)?
2. Survey location: GPS start coordinates or description
3. Duration available: (affects transect length — standard 100m vs. extended 500m)
4. Are you starting a new area or returning to an existing waypoint from `context/project.md`?

## Survey Execution Guide

### If Transect Survey:
Walk the operator through each 20m interval. At each stop, prompt:
```
📍 STOP [N] — [distance]m from start
Record:
□ Any non-native or suspicious species visible? (describe or list)
□ Dominant native species at this point?
□ Site condition: [1=pristine / 2=minimal impact / 3=moderate / 4=disturbed / 5=degraded]
□ Any spread vectors present? (water feature / road edge / trail / animal trail)
□ GPS waypoint marked? (Y/N)
```

### If Plot Survey:
Walk through the 4-step plot protocol:
```
STEP 1: Canopy — identify dominant trees ≥10cm DBH
STEP 2: Understory — 10m×10m subplot, shrubs and saplings 1-3m
STEP 3: Ground — 1m² quadrats (5 random), identify ground cover species
STEP 4: Edge — perimeter walk, species within 5m of edge
```

## During Survey — Species Flags
For each species flagged as non-native or suspicious:
- Apply the 4-Feature Rule (see workflows.md)
- Assign Anomaly Score (see workflows.md Anomaly Scoring Matrix)
- Determine distribution class: Isolated / Patch / Dense / Dominant

## Post-Survey Output
Generate a structured survey record:

```markdown
## Field Survey Record
**Date:** [date]
**Surveyor:** [operator name/role]
**Location:** [GPS or description]
**Survey Type:** [Transect/Plot]
**Duration:** [time]
**Weather:** [conditions]
**Transect Length / Plot Size:** [meters / m²]

### Species Detected
| # | Species | Status | Count/Density | GPS | Anomaly Score | Photos |
|---|---------|--------|---------------|-----|---------------|--------|
| 1 | | | | | | |

### Anomalies Flagged
| ID | Observation | Category | Score | Action Required |
|----|------------|---------|-------|-----------------|
| | | | | |

### Summary
- Native species confirmed: [count]
- Invasive species confirmed: [count]
- Unknown / needs ID: [count]
- High-priority anomalies: [count]
- Recommended follow-up: [list]

### Submission Checklist
□ EDDMapS report filed for confirmed invasives
□ iNaturalist observations uploaded
□ Photos uploaded/backed up
□ context/project.md updated with new detections
```

Save survey record to `work-log/survey-[date]-[location].md`
