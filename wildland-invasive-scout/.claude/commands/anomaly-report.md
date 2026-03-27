# /anomaly-report — Document an Ecological Anomaly

## Purpose
Quickly capture and score an ecological anomaly observed in the field. Applies the Anomaly Scoring Matrix from workflows.md to assess priority and determine whether escalation is required.

## Input Collection
Ask the operator:

```
1. WHAT did you observe? (describe as specifically as possible)
2. WHERE? (GPS coords or description; habitat type)
3. WHEN? (date, time, season context — e.g., "late March, last frost was 2 weeks ago")
4. HOW BIG? (spatial extent — single plant, patch, stand, linear feature)
5. HOW DIFFERENT? (compared to surroundings and what you normally see here)
6. PHOTOS? (Y/N — what angles captured)
7. Any ASSOCIATED observations? (wildlife behavior, other plants affected, soil conditions)
8. Your GUT FEELING: Does this feel like something that belongs here?
```

## Anomaly Scoring
Apply the matrix from workflows.md:

```
Score = Deviation Magnitude × Spatial Extent × Historical Contrast × Threat Classification

Deviation Magnitude:   1=slight, 2=moderate, 3=significant, 4=extreme
Spatial Extent:        1=single, 2=small patch, 3=large patch, 4=stand/dominant
Historical Contrast:   1=expected variation, 2=unusual, 3=never seen, 4=contradicts records
Threat Classification: 1=benign, 2=native anomaly, 3=non-native/unknown, 4=confirmed invasive

RESPONSE THRESHOLDS:
≤ 4:    Log and monitor
5-9:    Investigate + submit to iNaturalist
10-24:  Notify land manager / extension within 48h
≥ 25:   Immediate escalation — potential new incursion
```

## Output Format

```markdown
## Anomaly Report

**Report ID:** ANO-[YYYYMMDD]-[N]
**Date/Time:** [datetime]
**Location:** [GPS] | [Habitat description]
**Reported By:** [operator]

### Observation
[Detailed description of what was observed]

### Anomaly Category
[Phenological / Structural / Color / Spatial / Disturbance / Behavioral / Absence]

### Scoring
| Factor | Score | Reasoning |
|--------|-------|-----------|
| Deviation Magnitude | /4 | |
| Spatial Extent | /4 | |
| Historical Contrast | /4 | |
| Threat Classification | /4 | |
| **TOTAL** | **/256 max** | |

### Priority Level
🟢 LOG & MONITOR / 🟡 INVESTIGATE / 🟠 NOTIFY 48H / 🔴 IMMEDIATE ESCALATION

### Probable Explanation
[Best hypothesis for what this anomaly is — list alternatives if uncertain]

### Associated Observations
[Wildlife, soil, water, surrounding vegetation notes]

### Photo Documentation
- [ ] Whole habitat context
- [ ] Close-up of anomaly
- [ ] Scale reference
- [ ] GPS tagged

### Recommended Actions
1. [Action 1]
2. [Action 2]
3. [Reporting: EDDMapS / iNaturalist / extension office / land manager]

### Follow-Up Required
□ Return visit by: [date]
□ Expert ID needed: Y/N
□ EDDMapS report filed: Y/N
□ iNaturalist observation submitted: Y/N
```

Save all anomaly reports to `work-log/anomaly-[date]-[N].md`.
Append summary line to `context/project.md` Active Monitoring Zones table.
