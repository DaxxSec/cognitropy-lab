# Wildland Invasive Scout — Field Workflows

## Overview

This workspace applies invasive species management methodology to bushcraft field operations using automated anomaly detection principles. The core insight: **every healthy ecosystem has a detectable baseline, and anything that doesn't fit that baseline is a signal worth investigating.**

This isn't just ecological tourism — it's systematic intelligence gathering applied to wild environments, using the same structured workflows that invasive species managers use on a landscape scale, adapted for the individual field operator.

---

## WORKFLOW 1: Baseline Establishment

### Purpose
You cannot detect anomalies without knowing what "normal" looks like. Baseline establishment is the first thing an invasive species manager does in a new area — and it should be the first thing a bushcraft practitioner does too.

### Protocol

**Phase 1: Desktop Baseline (pre-field)**
1. Query the USDA PLANTS database or a regional flora guide for your biome's expected native species
2. Pull the state invasive species "watch list" and "established" list from your state's invasive species council
3. Review recent EDDMapS reports for your county/watershed
4. Note any documented range expansions from neighboring states
5. Record expected seasonal phenology (what's blooming/leafing/seeding when you'll be there)

**Phase 2: Field Baseline (first visit)**
Conduct a structured 100m x 100m plot survey:
```
Step 1: Define plot corners (GPS waypoints A, B, C, D)
Step 2: Canopy survey — identify dominant trees ≥10cm DBH, count stems
Step 3: Understory survey — identify shrubs/saplings 1-3m height in 10m x 10m subplot
Step 4: Ground survey — identify ground cover by 1m² quadrats (5 random per plot)
Step 5: Edge survey — walk perimeter, note species within 5m of edge
Step 6: Disturbance assessment — note trails, logging, water crossings, deer pressure
Step 7: Photo documentation — cardinal direction shots from plot center + notable species
```

**Baseline Record Fields:**
```
Date:
Plot ID:
GPS Center:
Biome Type:
Dominant Canopy: [species list with % cover estimate]
Dominant Understory: [species list with % cover]
Ground Layer: [species list with % cover]
Disturbance Level: [1-5 scale]
Water Proximity: [distance to nearest water feature]
Notable Observations:
Baseline Score: [calculated — see Anomaly Scoring below]
```

---

## WORKFLOW 2: Field Survey Protocol

### Purpose
Systematic transect-based survey to detect invasive species presence and spread. Borrowed directly from invasive species management methodology.

### Transect Method
```
Standard: 100m transect, 5m corridor either side (1000m² total)
Extended: 500m transect for linear features (roads, streams, ridgelines)
Plot-based: 20m × 20m fixed plots at GPS waypoints for repeat monitoring
```

### Survey Steps

**Before You Start**
- [ ] Record: date, time, weather, surveyor name
- [ ] Record: GPS start waypoint
- [ ] Clean boots and gear to prevent spreading propagules from previous site
- [ ] Load reference: regional invasive watch list
- [ ] Note: last management activity in this area (if known)

**During Transect**
1. Walk slowly (1 km/hr) — you need time to look both up and down
2. At each flagging stop (every 20m), scan: canopy → midstory → ground in 360°
3. Record each non-native or suspicious species: GPS coords, count/density, phenology stage, habitat
4. Rate distribution: Isolated (1-5 individuals) / Patch (6-50) / Dense (50+) / Dominant (>30% cover)
5. Note association: Is it spreading along a water course? Road edge? Trail? Animal runway?
6. Photograph: whole plant, leaf detail, stem detail, any fruit/seed, root if possible

**Species Confirmation Decision Tree**
```
STEP 1: Do you recognize it as a native species you've seen before here?
  YES → Log as native confirmation, continue
  NO → Continue to STEP 2

STEP 2: Does it appear on your state invasive watch list?
  YES → High alert, photograph all diagnostic features, record density + spread vector
  UNSURE → Continue to STEP 3

STEP 3: Does it match any feature-set in the anomaly indicators list? (see resources/)
  YES → Flag as "Probable Invasive - Needs ID Confirmation"
  NO → Flag as "Unknown - Needs ID"
```

**At Each GPS Waypoint (every 100m)**
- Record: waypoint ID, species count, dominant native/invasive cover estimate
- Rate: site disturbance (1=undisturbed, 5=heavily impacted)
- Note: any spread vectors present (water, roads, trail, deer, wind corridor)

**Post-Transect**
- [ ] Record GPS end waypoint
- [ ] Calculate survey area, time, and linear meters covered
- [ ] Tally: native species confirmed, invasive species detected, unknowns flagged
- [ ] Upload photos if connected, or queue for upload
- [ ] Submit to EDDMapS / iNaturalist if new incursion detected

---

## WORKFLOW 3: Species Identification Protocol

### The 4-Feature Rule
Never confirm an invasive species ID on fewer than 4 distinguishing features. Misidentification leads to both missed detections and unnecessary alarm.

**Feature Categories (collect from as many as possible)**
1. **Leaf morphology:** shape, margin (smooth/toothed/lobed), arrangement (opposite/alternate/whorled), texture, color, venation pattern
2. **Stem/bark:** color, texture, cross-section shape (round/square/ridged), presence of prickles/hairs, odor when broken
3. **Flower/fruit:** color, number of petals, arrangement, fruit type and color, seed dispersal mechanism
4. **Root/rhizome:** (if accessible without destructive sampling) color, smell, rhizome vs. taproot vs. bulb
5. **Habit:** climbing/trailing/upright/rosette, height, density, monoculture tendency
6. **Phenology:** when leafing, when blooming, when fruiting relative to surrounding natives
7. **Habitat preference:** sun/shade tolerance, soil preference, moisture requirement, where in the landscape it's concentrated

**Confidence Scoring**
```
4-5 features match → 85%+ confidence → Record as confirmed ID, proceed with management advisory
3 features match → 65-84% confidence → Record as probable ID, verify with expert before management action
2 features match → 40-64% confidence → Record as possible ID, photograph for expert review
<2 features match → <40% confidence → Record as unknown, submit photos to iNaturalist for community ID
```

**High-Priority Species Requiring Immediate Escalation**
If you observe ANY of these, treat as HIGH PRIORITY regardless of confidence level:
- Spotted lanternfly (*Lycorma delicatula*) — egg masses on bark look like dried mud patches
- Emerald ash borer evidence — D-shaped exit holes in ash bark
- Sudden oak death (*Phytophthora ramorum*) — bleeding cankers on oaks/tanoaks
- Giant hogweed (*Heracleum mantegazzianum*) — severe burn risk, do NOT touch
- Kudzu (*Pueraria montana*) — new incursion outside established range
- Japanese knotweed (*Reynoutria japonica*) — near waterways, rapid spread risk
- Water hyacinth (*Eichhornia crassipes*) — in any waterway outside known range

---

## WORKFLOW 4: Anomaly Detection System

### What Counts as an Ecological Anomaly?

An anomaly is any observation that doesn't fit the established baseline for that location, season, and habitat type. Anomalies are NOT always invasives — but every invasive incursion starts as an anomaly.

**Anomaly Categories**

| Category | Examples | Response Priority |
|---|---|---|
| **Phenological anomaly** | Plant blooming 4+ weeks early/late; leaf-out before frost risk has passed | Medium — may indicate climate signal or stress |
| **Structural anomaly** | Monoculture patch in otherwise diverse area; unnaturally dense understory | High — invasives often form monocultures |
| **Color anomaly** | Unusual foliage color for the season; unusual fruit/berry color in that habitat | Medium — verify species |
| **Spatial anomaly** | Same plant appearing suddenly along a trail corridor or stream edge | High — dispersal event likely |
| **Disturbance anomaly** | Unexpected soil disturbance; track patterns inconsistent with known wildlife | Medium — investigate spread vector |
| **Behavioral anomaly** | Wildlife avoiding an area they normally use; unusual herbivory patterns | Medium — may indicate toxin or habitat degradation |
| **Absence anomaly** | A species you always see here is suddenly absent from its normal habitat | High — may indicate disease, toxin, or competitive displacement |

### Anomaly Scoring Matrix
```
Score = (Deviation Magnitude) × (Spatial Extent) × (Historical Contrast) × (Threat Classification)

Deviation Magnitude:  1=slight, 2=moderate, 3=significant, 4=extreme
Spatial Extent:       1=single plant, 2=small patch (<10m²), 3=large patch (<100m²), 4=stand (>100m²)
Historical Contrast:  1=expected variation, 2=unusual, 3=never seen here before, 4=contradicts all records
Threat Classification: 1=benign, 2=native species anomaly, 3=non-native/unknown, 4=confirmed invasive

Score ≤ 4:   Log and monitor next visit
Score 5-9:   Log, investigate, submit to iNaturalist for ID
Score 10-24: Escalate to county extension or land manager within 48 hours
Score ≥ 25:  Escalate immediately — potential new invasive incursion
```

### Anomaly Detection Passes
When conducting any field operation (not just formal surveys), run mental "anomaly passes":
1. **Skyline pass** — scan the canopy from a clearing. Does anything look structurally different from surrounding trees? (Crown damage, die-back, unusual vine coverage)
2. **Mid-story pass** — look at 1-3m height. Any monoculture shrubs? Any plants with unusually aggressive growth?
3. **Ground pass** — look at your feet. Any unbroken mats of the same species? Any rosettes in unusual density?
4. **Water-edge pass** — stream banks and pond edges are the highest-risk zones for new incursions. Spend extra time here.
5. **Disturbance-edge pass** — trail edges, old log landings, road corridors. These are invasive superhighways.

---

## WORKFLOW 5: Foraging Safety Cross-Check

### Purpose
Before harvesting any wild food, check it against known invasive and toxic species that could be confused with your target, and assess site contamination risks.

### Pre-Harvest Protocol
```
Step 1: POSITIVE ID — confirm at least 4 features of your intended target species
Step 2: LOOKALIKE SCREEN — identify the top 2-3 dangerous lookalikes for your target
Step 3: CONFUSION CHECK — verify you have all features that distinguish target FROM lookalikes
Step 4: SITE HISTORY CHECK — any known herbicide application, industrial contamination, or
         heavy invasive management in this watershed?
Step 5: INDICATOR SPECIES CHECK — are native indicator species present that suggest a healthy,
         intact ecosystem? (Absence can indicate ecosystem disruption)
Step 6: INVASIVE CONTAMINATION CHECK — are any of the known accumulator invasives present?
         (Some invasives concentrate heavy metals, alter soil chemistry, or produce allelopathic compounds)
Step 7: GO/NO-GO DECISION
```

### High-Risk Lookalike Pairs (Core Knowledge)
```
Target: Wild garlic / Ramps (Allium tricoccum)
Risk:   Lily of the valley (Convallaria majalis — toxic) and False hellebore (Veratrum viride — toxic)
Check:  Garlic odor is definitive — crush a leaf; if no garlic smell, do NOT harvest

Target: Wild carrot (Daucus carota)
Risk:   Poison hemlock (Conium maculatum) and Water hemlock (Cicuta maculata) — DEADLY
Check:  Hairy stems on wild carrot; purple-blotched hollow stems on hemlock; distinct carroty smell

Target: Elderberries (Sambucus canadensis)
Risk:   Pokeweed berries (Phytolacca americana) and water hemlock
Check:  Elder grows as shrub, berries in flat-topped clusters, leaves pinnately compound

Target: Hen of the woods / Maitake (Grifola frondosa)
Risk:   Berkeley's polypore (edible but bitter), various toxic shelf fungi
Check:  Gray-brown frond coloration, white interior, mild pleasant odor, attached at single base

Target: Chanterelle (Cantharellus cibarius)
Risk:   Jack-o-lantern mushroom (Omphalotus olearius — toxic)
Check:  True chanterelle has forked false gills (ridges); jack-o-lantern has true gills, grows in clusters

Target: Chicken of the woods (Laetiporus sulphureus)
Risk:   Confusion low, but note: toxic on certain host trees (locust, eucalyptus, conifers in some regions)
Check:  Confirm host tree species before harvesting
```

### Site Contamination Indicators
These conditions = DO NOT FORAGE:
- Evidence of herbicide application (wilted/discolored vegetation in linear patterns)
- Industrial upstream (mining, smelting, tanning operations — heavy metal accumulation)
- Heavy runoff contamination (foam on waterways, unusual odors, discolored water)
- Dense populations of known accumulator invasives (e.g., garlic mustard allelopathically alters soil microbiome)
- Within 50m of roads or rail corridors (heavy metal contamination)
- Former agricultural land with unknown history (pesticide residue)

---

## WORKFLOW 6: Camp Site Ecological Evaluation

### Purpose
Select and manage camp sites that minimize ecological impact, with attention to invasive species spread risk and ecosystem health indicators.

### Site Evaluation Checklist
```
WATER HAZARD SCREEN
□ Water source within 200m (for drinking/cooking)
□ Waterway bank condition: stable or eroding?
□ Upstream land use: any industrial, agricultural, or heavy urban runoff risk?
□ Aquatic invasives visible? (water hyacinth, purple loosestrife, Phragmites)
□ Blue-green algae indicators? (avoid all contact)

VEGETATION ASSESSMENT
□ Dominant species ID: primarily natives or invasives?
□ Ground cover type: intact duff layer (good) or bare soil/monoculture (bad)
□ Fire risk: drought-stressed vegetation? Ladder fuels? Invasive grasses?
□ Thorny/toxic plants requiring clearance? (identify before clearing)
□ Evidence of allelopathic plants? (black walnut, garlic mustard — affects plant growth in area)

WILDLIFE INDICATOR SCREEN
□ Wildlife signs: track species expected for this biome?
□ Evidence of disease vectors: tick habitat assessment (leaf litter, low brush in ecotone)
□ Rodent activity near proposed food storage area?
□ Bird diversity: high diversity = healthy habitat; absence = potential concern

SOIL/GEOLOGY SCREEN
□ Soil type: compaction risk vs. resilience to foot traffic?
□ Evidence of soil erosion in vicinity?
□ Evidence of previous camping impact: compaction, fire scarring, waste?

INVASIVE SPREAD RISK ASSESSMENT
□ Will this camp site place humans as a seed dispersal vector? (sticky seeds, berry consumption)
□ Any invasive seed-producing plants at peak dispersal stage adjacent to site?
□ Boot-cleaning protocol required between this site and your next destination?

VERDICT: GO / MONITOR / NO-GO (with reason)
```

---

## WORKFLOW 7: Reporting for Citizen Science

### EDDMapS Report Format
EDDMapS (Early Detection & Distribution Mapping System) is the primary invasive species mapping platform in North America.

Required fields:
```yaml
species_name: [scientific name preferred, common name accepted]
observation_date: [YYYY-MM-DD]
location:
  latitude: [decimal degrees]
  longitude: [decimal degrees]
  accuracy_meters: [GPS accuracy estimate]
  state: [2-letter code]
  county: [name]
  locality_description: [text description of location]
abundance: [isolated / few / many / abundant]
phenology: [vegetative / flowering / fruiting / dormant]
habitat: [forest edge / wetland / disturbed / roadside / etc.]
photos: [Y/N — attach if available]
notes: [any additional context]
observer_name: [your name or iNaturalist handle]
```

### iNaturalist Upload Checklist
- [ ] Photo(s) included — minimum 1, ideally: habit, leaf, stem, any reproductive parts
- [ ] GPS coordinates attached to photo metadata OR manually entered
- [ ] Date correct (check timestamp if auto-imported)
- [ ] Species ID attempt made (even "Plant — Eudicots" is better than nothing)
- [ ] Observation notes include: habitat, associated species, behavior if applicable
- [ ] Marked captive/cultivated: NO (for wild observations)
- [ ] Added to relevant iNaturalist project (state invasive species projects exist for most states)

---

## WORKFLOW 8: Seasonal Drift Detection

### Purpose
Return visits to the same area should detect ecological drift — changes over time that may indicate successful invasive establishment, treatment effectiveness, or natural succession.

### Drift Detection Protocol (Repeat Visits)
```
Step 1: Return to same GPS waypoints used in baseline
Step 2: Repeat the same survey protocol (same transect, same plot)
Step 3: Complete the Drift Comparison Form:

DRIFT COMPARISON FORM
Site: _______________  Baseline Date: ___________  Current Date: ___________

Native Species Change:
  Species gained (new natives observed): ___________
  Species lost (natives no longer found): ___________
  Cover change estimate for dominants: ___________

Invasive Species Change:
  New invasives detected since baseline: ___________
  Known invasives — spread assessment: expanded / stable / reduced
  Treatment response (if applicable): ___________

Anomaly Count:
  Baseline anomaly count: ___
  Current anomaly count: ___
  New anomalies requiring investigation: ___________

Overall Ecological Health Score (1-10):
  Baseline: ___  Current: ___  Trend: Improving / Stable / Declining

Recommended Actions:
  [ ] Continue monitoring
  [ ] Escalate to land manager
  [ ] Submit new incursion report
  [ ] Adjust management strategy
  [ ] Document as resolved
```

### Trend Indicators

| Signal | Positive Interpretation | Negative Interpretation |
|---|---|---|
| Native diversity increasing | Succession proceeding, ecosystem recovering | — |
| Invasive cover decreasing | Treatment working, competition recovering | — |
| Anomaly count stable or falling | Good baseline stability | — |
| New invasive every survey | — | Active propagule pressure — check spread vectors |
| Natives disappearing | — | Competitive displacement or disease |
| Uniform species composition | — | Monoculture invasion underway |
| Wildlife absence/shift | — | Habitat quality decline |
