# /threat-matrix — Generate Priority Threat Matrix

## Purpose
Synthesize all detected invasive species in the project area into a prioritized threat matrix. Outputs a ranked action plan for land management or personal monitoring decisions.

## Input
Reference `context/project.md` Known Invasive Threats table and any work-log survey records.
Ask operator: Any new detections to add before generating the matrix?

## Scoring Dimensions
Each detected species is scored across 5 dimensions:

```
1. ESTABLISHMENT STAGE (how entrenched is it?)
   1 = Single sighting/unconfirmed
   2 = Isolated patch, recent detection
   3 = Multiple established patches
   4 = Widespread / dominant in area

2. SPREAD POTENTIAL (how fast could it get worse?)
   1 = Slow-spreading, limited dispersal
   2 = Moderate spread, one dispersal vector
   3 = Fast-spreading or multiple vectors (wind + water + wildlife)
   4 = Explosive spreader (bamboo, kudzu, knotweed, water hyacinth)

3. ECOLOGICAL IMPACT (what damage does it cause?)
   1 = Minor, coexists with natives
   2 = Competes with natives, some displacement
   3 = Forms monocultures, displaces native communities
   4 = Alters ecosystem function (fire regime, hydrology, soil chemistry, allelopathic)

4. HUMAN/WILDLIFE SAFETY RISK (direct harm potential)
   1 = No direct harm
   2 = Minor (contact irritation, unpalatable)
   3 = Moderate (toxic if consumed, thorns, aggressive)
   4 = Severe (giant hogweed burns, highly toxic, aggressive wildlife vectors)

5. MANAGEMENT FEASIBILITY (how tractable is elimination/control?)
   1 = Very difficult (deep roots, massive seed bank, biological control unavailable)
   2 = Difficult (requires repeated treatment, professional equipment)
   3 = Manageable (hand-pulling, targeted herbicide, mechanical removal)
   4 = Easy (isolated patch, controllable with basic tools)
```

## Priority Score Calculation
```
Priority Score = (Establishment × 2) + (Spread × 2) + (Ecological Impact × 1.5) + (Safety Risk × 1.5) + (Feasibility × 1, INVERTED: 5 - score)

Higher score = higher priority for action.
```

## Output Format

```markdown
## Invasive Species Threat Matrix
**Area:** [field area from project.md]
**Generated:** [date]

### Priority Rankings

| Rank | Species | Est. | Spread | Impact | Safety | Feasibility | SCORE | Recommended Action |
|------|---------|------|--------|--------|--------|-------------|-------|--------------------|
| 1 | | | | | | | | |
| 2 | | | | | | | | |
...

### Action Plan

#### IMMEDIATE (Score ≥ 20)
[Species name] — [recommended management action, timeline, resources needed]

#### SHORT-TERM / THIS SEASON (Score 12-19)
[Species name] — [action]

#### MONITOR (Score 6-11)
[Species name] — [monitoring frequency, trigger for escalation]

#### LOW PRIORITY (Score ≤ 5)
[Species name] — [log and document, no active management needed]

### Resources & Contacts
- State invasive species program: [link/contact]
- Recommended control methods: [by species, with any permit notes]
- Cost/labor estimate: [rough estimate if available]

### Reporting Due
□ EDDMapS submissions needed for: [species list]
□ Land manager notification recommended for: [species list]
```

Save to `planning/threat-matrix-[date].md`.
