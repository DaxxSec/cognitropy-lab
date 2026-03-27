# /camp-eval — Evaluate a Camp Site

## Purpose
Systematic ecological and safety evaluation of a potential camp site, borrowing the site assessment methodology from invasive species managers. Covers water safety, vegetation health, wildlife indicators, invasive spread risk, and Leave No Trace impact assessment.

## Input Collection
Ask the operator:
```
1. LOCATION: GPS coordinates or description
2. SIZE of intended camp area (solo bivy vs. group site)
3. WATER SOURCE: Nearest water feature and approximate distance
4. VEGETATION: Dominant plants you can see in the immediate area
5. WILDLIFE SIGNS: Tracks, scat, browse marks, burrows observed?
6. SOIL TYPE: Rocky / sandy / clay / duff / swampy?
7. INTENDED DURATION: One night / multi-day / base camp for extended operations
8. ANY KNOWN HISTORY of the site: previously used camp, old logging area, agricultural land?
```

## Evaluation Protocol

### Water Assessment
```
□ Source type: stream / lake / spring / collected rain
□ Distance: ≥ 60m from water source? (LNT standard)
□ Upstream land use: any industrial, agricultural, heavy residential?
□ Visual indicators: clear, free of foam, no unusual odor or color
□ Aquatic invasives present? (water hyacinth, purple loosestrife, Phragmites at banks)
□ Blue-green algae signs? (green/blue surface scum, musty odor) → DO NOT CONTACT
□ Waterfowl density: excessive waterfowl = elevated pathogen load
```

### Vegetation Assessment
```
□ Dominant species: native or invasive? (flag if >30% invasive cover)
□ Ground cover type: intact duff (ideal) / compacted soil / bare soil / monoculture (concern)
□ Any toxic plants requiring clearing? (identify before ANY clearing activity)
   - Poison ivy/oak/sumac — urushiol contact dermatitis
   - Stinging nettle — manageable, gloves required
   - Wild parsnip — phototoxic sap, severe burns
   - Giant hogweed — EXTREME HAZARD, do not disturb
□ Fire risk vegetation: dead standing timber, drought-stressed grass, accumulated duff depth
□ Widow-maker hazard: dead branches overhead that could fall
□ Allelopathic plants: black walnut (juglone toxicity — affects cooking near roots), garlic mustard
```

### Wildlife Indicator Assessment
```
□ Expected species present? (tracks match biome and season expectations)
□ Predator sign: bear scat/scrapes, mountain lion sign, coyote dens, in area?
□ Disease vector habitat: tick habitat assessment
   - Ecotone (forest-meadow edge): HIGH tick risk
   - Deep closed canopy: LOW tick risk
   - Tall grass / leaf litter: MODERATE tick risk
□ Rodent activity near camp: burrows, runways, caching activity → food storage implications
□ Unusual absence: should deer tracks be here? Bird calls absent?
```

### Invasive Spread Risk
```
□ Any seed-producing invasives at dispersal stage in immediate area?
   (You become a dispersal vector — seeds hitchhike on gear and clothing)
□ Sticky-seed species present? (burdock, cleavers, beggar's ticks)
□ Boot-cleaning protocol between this site and your next destination?
□ Any management activities here that could have opened invasion windows? (recent logging, fire)
```

### Leave No Trace Assessment
```
□ Previously used site (compacted, fire ring present)? → Prefer this over pristine ground
□ Durable surface for camping (rock, gravel, sand, established duff) → Better
□ Sensitive ground (cryptobiotic soil crust, wetland edge, new vegetation) → Avoid
□ 60m+ from water, trails, and other campers?
□ Trees of appropriate size for hammock/hang? (≥20cm DBH recommended, no dead trees)
```

## Output Format

```markdown
## Camp Site Evaluation Report

**Date:** [date]  **Location:** [GPS/description]
**Evaluated For:** [solo/group, duration]

### Score Summary
| Category | Status | Notes |
|----------|--------|-------|
| Water | 🟢🟡🔴 | |
| Vegetation safety | 🟢🟡🔴 | |
| Wildlife/disease vectors | 🟢🟡🔴 | |
| Invasive spread risk | 🟢🟡🔴 | |
| LNT impact | 🟢🟡🔴 | |

### VERDICT: GO / CONDITIONAL GO / NO-GO

**If GO or Conditional:** Specific precautions required:
- [Precaution 1]
- [Precaution 2]

**If NO-GO:** Reason and nearest alternative recommendation.

### Ecological Notes
[Anything worth documenting about this site's health, unusual observations]
```
