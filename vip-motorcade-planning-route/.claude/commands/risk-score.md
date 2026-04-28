# /risk-score — Apply 5×5 Risk Matrix to a Surveyed Route

Score every segment of a surveyed route on the 5×5 likelihood × impact matrix, then roll up to a route-level number.

## Required Inputs
- A completed survey at `outputs/<route-codename>/survey.md`
- A current threat baseline at `outputs/threat-baseline-<YYYY-MM-DD>.md` (≤ 14 d old)
- Motorcade composition for this leg (from `context/project.md`)
- Mitigation menu — what is *actually* available on this leg (advance team Y/N, CAT Y/N, route closure Y/N, etc.)

## Procedure

### 1. Validate Inputs
- Refuse to score if the threat baseline is older than 14 d. Run `/threat-baseline --refresh` first.
- Refuse to score if the survey has any unresolved `los_standoff_m = unknown` and the user's threat tier is 1.

### 2. Per-Segment Scoring
For each segment in the survey:

#### 2a. Inherent Likelihood
Take the highest base-likelihood from the threat baseline among the segment's `dominant_hazards`. Adjust:
- +1 if the segment is a chokepoint and the dominant hazard is ambush/IED/ramming.
- +1 if `crowd_density_peak ≥ 4 persons/m²` and dominant hazard is crowd-surge or lone-actor.
- +1 if `ingress_egress_count = 0` and dominant hazard is kidnap.
- Cap at 5.

#### 2b. Inherent Impact
From the typology in `domain-knowledge.md §2`:
- Catastrophic-class hazard with poor standoff (`los_standoff_m < 200`) and unhardened motorcade: I = 5.
- Critical-class hazard with hardened motorcade: I = 4.
- Significant-class hazard at slow chokepoint: I = 3 minimum.
- Otherwise use the typology's typical I.

#### 2c. Inherent Risk
`R_inherent = L_inherent × I_inherent`. Note the band (Low / Moderate / High / Very High / Extreme).

#### 2d. Mitigations Applied
List specific, attributable mitigations *actually* present on this segment:
- Advance team has cleared the segment within the last X minutes
- CAT vehicle in motorcade
- Hardened (B6/B7) principal vehicle
- Route closure / police escort active
- Crowd-line in place
- Counter-surveillance team running

Each mitigation moves L, I, or both. The agent must say *which* axis and *by how much*, with rationale.

Examples:
- Hardened vehicle reduces I for ambush from 4 → 3 (mass casualty unlikely; principal capture still possible if extracted).
- Route closure reduces L for crowd-surge from 4 → 2 (no crowd in segment).
- Advance sweep within 30 min reduces L for IED from 3 → 2 (sweep horizon).

#### 2e. Residual Risk
`R_residual = L_residual × I_residual`. Note the band.

If residual is Extreme: flag the segment as a route-killer.
If residual is Very High: flag for written contracting-office sign-off.

### 3. Route Roll-Up
- `route_max_residual = max(segment_residuals)`
- `route_high_plus_count = count(segments where residual band ≥ High)`
- `route_segment_count = N`
- `route_extreme_count = count(segments where residual band = Extreme)`

### 4. Sanity Pass
- Are any segments coasting at L=3, I=3 with no anchor? Flag for re-scoring.
- Are any mitigations counted on >5 segments without independent presence? Flag for re-scoring (a single advance team can plausibly cover a corridor; it cannot cover 30 segments simultaneously).
- Are inherent and residual identical for >50% of segments? You're not really mitigating; flag for review.

### 5. Output
Write `outputs/<route-codename>/scoring-sheet.md`:

```
# Scoring Sheet — <route-codename>
- Survey: outputs/<route-codename>/survey.md
- Baseline: outputs/threat-baseline-<YYYY-MM-DD>.md
- Date scored: YYYY-MM-DD
- Scorer: [placeholder]
- Composition / mitigation menu: [summary]

## Segment scores

| ID | Hazard | L_i | I_i | R_i | Band_i | Mitigations | L_r | I_r | R_r | Band_r | Notes |
|----|--------|-----|-----|-----|--------|-------------|-----|-----|-----|--------|-------|
...

## Roll-up
- max residual: 12 (S07, complex-ambush)
- High+ count: 3
- Very High count: 0
- Extreme count: 0

## Recommendation
[approved / approved with sign-off / re-engineer / reject]
```

Log to `work-log/<YYYY-MM-DD>-score-<route-codename>.md`.

## Decision Rules

- Any Extreme residual on any segment ⇒ recommendation: reject. Re-engineer or drop.
- Any Very High residual ⇒ requires written contracting-office sign-off; brief must list the specific tolerated risk.
- All segments ≤ Moderate ⇒ recommend approve.
- Mixed Moderate / High ⇒ recommend approve-with-sign-off and explicitly list the High segments in the brief.
