# /forage-safety — Cross-Check Foraging Target for Safety

## Purpose
Before harvesting any wild food, run a structured safety check: positive ID verification, dangerous lookalike screening, and site contamination assessment. Output is a GO / CONDITIONAL GO / NO-GO advisory.

## ⚠️ SAFETY NOTICE
This command provides an advisory check. It does NOT replace expert field identification.
When in doubt: DO NOT CONSUME. No meal is worth a medical emergency.

## Input Collection
Ask the operator:
```
1. WHAT are you trying to harvest? (common name, scientific name if known)
2. DESCRIBE what you have: as many features as possible (see /species-id for feature list)
3. HOW MANY specimens of this are present in the area?
4. WHERE exactly? (habitat type, GPS or description)
5. SITE HISTORY: Any known herbicide use, agriculture, industry, or roads nearby?
6. Do you have a field guide confirmation? (Y/N — which guide?)
7. Have you harvested this species from this location before?
```

## Positive ID Verification
Run the 4-Feature Rule check for the stated target species.
If confidence < 80%: → OUTPUT: NO-GO (Insufficient ID confidence)
If toxic lookalike cannot be ruled out: → OUTPUT: NO-GO (Lookalike risk unresolved)

## Lookalike Screen
For the identified target, pull the known dangerous lookalikes from resources/lookalike-pairs-reference.md
Walk through each distinguishing feature that separates target from lookalikes:
```
For each lookalike:
□ Can you rule it out? YES = document the ruling feature / NO = NO-GO
```

## Site Contamination Check
```
□ Within 50m of a paved road or rail corridor? → Flag: heavy metal contamination risk
□ Evidence of herbicide application nearby? (wilted/discolored vegetation in patterns) → NO-GO
□ Agricultural land use in watershed? → Ask: what crops, what practices?
□ Any industrial, mining, or tanning activity upstream? → NO-GO
□ Dense invasive species nearby that are known soil chemistry modifiers? → Conditional flag
   (Garlic mustard alters soil microbiome; spotted knapweed produces allelopathic catechin)
□ Contaminated water indicators? (foam, odor, discoloration, algae bloom) → NO-GO
```

## Harvest Safety Check
```
□ Harvesting the correct part? (some plants: edible root, toxic leaves — or vice versa)
□ Harvesting at the correct growth stage? (some species safe at one stage, toxic at another)
□ Correct preparation method confirmed? (some species require cooking; others toxic when cooked)
□ Quantity appropriate? (some edible species can cause issues in very large quantities)
□ Any known allergies or sensitivities to this plant family?
```

## Output Format

```markdown
## Foraging Safety Check

**Date:** [date]  **Location:** [GPS/description]
**Target Species:** [common name] (*scientific name*)
**Operator ID Confidence:** [%]

### Positive ID Check
| Feature | Observed | Matches Target? |
|---------|---------|----------------|
| | | ✅ / ❌ / ⚠️ |

**ID Score:** [N features matched] / 4 minimum required

### Lookalike Ruling
| Lookalike | Rule-Out Feature | Confirmed Clear? |
|-----------|-----------------|-----------------|
| | | ✅ / ❌ / ⚠️ |

### Site Contamination
| Risk Factor | Present? | Severity |
|-------------|---------|---------|
| Road proximity | | |
| Herbicide signs | | |
| Industrial upstream | | |
| Invasive modifiers | | |
| Water contamination | | |

### VERDICT

🟢 **GO** — Proceed with harvest. [Any notes]

🟡 **CONDITIONAL GO** — Acceptable to harvest IF: [specific conditions met]

🔴 **NO-GO** — DO NOT HARVEST. Reason: [specific reason]

### Harvest Notes
[Correct part, preparation method, quantity guidance]
```
