# /species-id — Identify and Classify a Field Species

## Purpose
Apply the 4-Feature Rule to systematically identify an unknown plant, animal, fungi, or other organism and classify it as native, non-native, invasive, or unknown — with a confidence score.

## Input Collection
Ask the operator to describe as many of the following as they can observe:

```
IDENTITY CLUES — describe what you see:

1. GROWTH FORM: Tree / Shrub / Vine / Herbaceous plant / Grass / Fern / Mushroom / Animal / Insect / Other?
2. SIZE: Approximate height/length/width
3. LEAF/FROND/CAP: Shape, edge (smooth/toothed/lobed), texture, color top/bottom, arrangement on stem
4. STEM/BARK/STALK: Color, texture, cross-section (round/square/ridged), any hairs/thorns/spines
5. FLOWER/FRUIT/SPORES: Color, structure, any fruits or seeds visible
6. ROOT: Visible? Type (taproot/fibrous/rhizome/bulb), color, odor when broken
7. SMELL: Crush a leaf or break a stem — any distinctive odor?
8. LOCATION: What kind of habitat? (forest edge / stream bank / disturbed soil / open meadow)
9. WHAT SURROUNDS IT: What native plants is it growing near?
10. PHENOLOGY: What state is it in right now? (new growth / full leaf / flowering / fruiting / dormant)
11. PHOTOS: Available? What angles?
12. GEOGRAPHIC CONTEXT: What state or region are you in?
```

## Identification Process

1. **Build the feature profile** from operator inputs
2. **Apply biome filter** — narrow candidates to species plausible in their region
3. **Screen against invasive watch list** — check all region-appropriate invasive species that match ANY of the features
4. **Screen against toxic lookalikes** — flag any dangerous lookalikes to the probable ID
5. **Apply the 4-Feature Rule** — calculate confidence score
6. **Classify:**

```
CLASSIFICATION CATEGORIES:
├── NATIVE CONFIRMED (high confidence, ≥4 features, known native range)
├── NATIVE PROBABLE (3 features, consistent with native range)
├── NON-NATIVE, NON-INVASIVE (not on watch list, introduced but not spreading aggressively)
├── INVASIVE — WATCH LIST SPECIES (confirmed or probable match to regional invasive)
├── INVASIVE — NEW INCURSION SUSPECTED (watch list species outside known established range)
├── UNKNOWN — NEEDS EXPERT ID (insufficient features or no match)
└── TOXIC RISK — HANDLE WITH CARE (regardless of native/invasive status)
```

## Output Format

```markdown
## Species Identification Result

**Date:** [date]  **Location:** [coordinates or description]

### Probable ID
**Common Name:** [name]
**Scientific Name:** [Genus species]
**Confidence:** [%] — based on [N] features matched

### Feature Match Summary
| Feature | Observed | Match? |
|---------|---------|--------|
| Leaf shape | [described] | ✅ / ⚠️ / ❌ |
| Stem | [described] | ✅ / ⚠️ / ❌ |
| Habitat | [described] | ✅ / ⚠️ / ❌ |
| Other | [described] | ✅ / ⚠️ / ❌ |

### Classification
**Status:** [NATIVE CONFIRMED / INVASIVE — WATCH LIST / etc.]
**Regional Invasive Status:** [state-level status if applicable]

### Lookalike Warning
⚠️ This species could be confused with:
- [species] — [how to distinguish]
- [species] — [how to distinguish]

### Recommended Actions
- [ ] [action based on classification]
- [ ] [report to EDDMapS/iNaturalist if invasive]

### Verification Note
[Any caveats, especially if confidence < 80%]
```

Save to `work-log/species-id-[date].md` if invasive or unknown.
