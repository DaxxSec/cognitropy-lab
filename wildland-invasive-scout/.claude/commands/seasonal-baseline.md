# /seasonal-baseline — Establish or Update Seasonal Ecological Baseline

## Purpose
Create or update a seasonal baseline record for a field area. This is the reference point against which all future anomaly detection runs. Baselines should be updated at the start of each new season (spring green-up, summer peak, fall dormancy, winter).

## Input Collection
Ask the operator:
```
1. Is this a NEW baseline or an UPDATE to an existing one?
2. What SEASON and approximate date? (e.g., "Early spring, March 26 — first greens just emerging")
3. FIELD AREA: Same as project.md or a new sub-zone?
4. SURVEY METHOD: Full plot survey (formal), walkabout observation (informal), or photos only?
5. How does this compare to LAST YEAR at this time, if you have that data?
```

## Baseline Data Collection Protocol

### Phenology Markers (note current status for each)
```
CANOPY TREES:
□ Bud break stage: dormant / swelling / burst / early leaf / full leaf
□ Leaf color: [primary color and any anomalies]
□ Any early senescence or stress visible?

UNDERSTORY:
□ Shrub/sapling leafing stage vs. expected
□ Any notable early bloomers present?
□ Invasive shrubs leafing earlier than native counterparts? (THIS IS A KEY ANOMALY FLAG)
   Note: Many invasive shrubs leaf out 2-4 weeks earlier than natives in spring — a key identifier

GROUND LAYER:
□ Ephemeral spring species present? (trout lily, trillium, bloodroot, spring beauty)
□ Native grasses vs. invasive grass emergence timing?
□ Any perennial invasives already dominant?

WATER FEATURES (if present):
□ Stream flow: normal / high (snowmelt/rain) / low (drought)
□ Riparian vegetation phenology
□ Any aquatic invasives showing early growth?

WILDLIFE:
□ Bird species currently present (particularly neotropical migrants if spring)
□ Amphibian activity: breeding chorus audible? Egg masses present?
□ Insect activity: bee/butterfly flight, tick activity starting?
□ Notable absences vs. expected?
```

### Baseline Metrics to Record
```yaml
baseline_record:
  date: [YYYY-MM-DD]
  season: [spring/summer/fall/winter]
  field_area: [name/coords]
  surveyor: [operator]

  canopy_status:
    dominant_species: []
    leaf_stage: [0-6 scale: 0=dormant, 6=full canopy]
    health_notes: ""

  understory_status:
    dominant_species: []
    bloom_species: []
    invasive_observations: []
    early_leaf_invasives: []  # KEY ANOMALY INDICATOR

  ground_layer:
    dominant_cover: []
    ephemerals_present: []
    bare_soil_percentage: ""

  invasive_pressure:
    detected_species: []
    highest_density_location: ""
    notable_changes_since_last: ""

  wildlife_indicators:
    birds_observed: []
    amphibians: ""
    insects: ""
    mammal_sign: []

  water_features:
    flow_status: ""
    riparian_health: ""
    aquatic_observations: ""

  overall_health_score: [1-10]
  anomalies_flagged: []
  notes: ""
```

## Drift Detection
If updating an existing baseline, auto-compare with previous record:

```
For each metric where comparison data exists:
→ Change > 10%: FLAG as drift item
→ New invasive detected: FLAG as new incursion
→ Previously documented species now absent: FLAG as loss event
→ Invasive leafing ≥2 weeks earlier than last year: FLAG as phenological shift
→ Overall health score change ≥ 2 points: ESCALATE
```

## Output
```markdown
## Seasonal Baseline Record
**Area:** [name]  **Date:** [date]  **Season:** [season]
**Previous Baseline Date:** [date or "NEW"]

### Summary
Overall Health Score: [N]/10 ([change from previous])
Dominant Canopy: [species]
Dominant Understory: [species]
Current Phenology Stage: [description]

### Invasive Pressure Assessment
[Table of detected invasives with density and change from previous]

### Anomalies vs. Previous Baseline
[List of drift items flagged]

### Recommended Actions Before Next Visit
[List]
```

Save to `context/project.md` (update baseline section) and `work-log/baseline-[date]-[season].md`.
