# Harmony → Traverse Cheatsheet

The compact mapping table. Print this and put it on the planning meeting wall.

---

## Chord Tones → Waypoint Properties

| Tone | Waypoint Property | Values |
|------|-------------------|--------|
| **Root** | Terrain class | bedrock / regolith-rocky / regolith-fines / aeolian / conglomerate / mixed |
| **Third** | Slope class | flat (< 10°) / inclined (10–20°) / steep (20–25°) / extreme (> 25°, FORBIDDEN) |
| **Fifth** | Science value | none / opportunistic / strategic / priority-1 |

---

## Chord Quality → Waypoint Disposition

| Chord Quality | Definition | Operational Meaning | Color (for diagrams) |
|---------------|-----------|---------------------|---------------------|
| **Major triad (I)** | Stable — bedrock + flat + ≥ strategic | Ideal — drive there, do science, sleep there | Green |
| **Minor triad (vi, ii, iii)** | Stable — bedrock + flat + opportunistic, or bedrock + flat + none | Safe stop, modest science | Light green |
| **Dominant 7 (V7)** | Tense — bedrock + inclined + ≥ strategic, or any inclined-with-science | Wants to resolve — pause here, plan a resolution to a major chord | Yellow |
| **Half-diminished (vii⌀)** | Risky — regolith-rocky + steep + opportunistic | Risky stop, low science return — usually not a destination | Orange |
| **Fully diminished (vii°)** | Extreme — aeolian + extreme + none | FORBIDDEN — never plan a chord here | Red |
| **Suspended (sus)** | Ambiguous — mixed + inclined + strategic | Needs more data before committing | Grey |

---

## Voice-Leading Rules → Segment Smoothness

| Property | Good (≤) | Acceptable (≤) | Reject (>) |
|----------|----------|----------------|-----------|
| Slope change per metre | 5° | 8° | 10° (flag for review) |
| Heading change per 5 m | 30° | 45° | 60° (likely an autonomy mismatch) |
| Terrain class change | stepwise (e.g., bedrock ↔ regolith-rocky) | one-leap (e.g., bedrock ↔ regolith-fines) | leap (e.g., bedrock ↔ aeolian) |

---

## Cadence Patterns → Traverse Endings

| Cadence | Pattern | Operational Meaning | Frequency |
|---------|---------|---------------------|-----------|
| **Authentic (V → I)** | dominant → major triad | Standard drive-to-park | Most sols |
| **Plagal (IV → I)** | strategic-flat → major triad | Quiet drive, no risky lead-in | When new ground is gentle |
| **Deceptive (V → vi)** | dominant → unexpected minor | En-route opportunistic science stop, parking deferred | When downlink reveals a science target en route |
| **Half cadence (I → V)** | major triad → dominant | End sol on a tension that sol-N+1 resolves | Multi-sol traverse setup |
| **No cadence** | ends on dim / half-dim / sus | HARD FAIL | Never accept |

---

## Substitution Moves → Operational Meaning

| Substitution | What it does | When to use |
|--------------|--------------|-------------|
| **Tritone substitution** | Swap the segment's terrain class while keeping start and end waypoints | When a flagged segment has a same-destination alternate that crosses a different terrain class (typically: bedrock detour around regolith-rocky) |
| **Modal interchange** | Borrow the corresponding segment from a parallel "conservative" plan variant | When the optimistic plan's segment is risky and the conservative plan has already been generated |
| **Pivot-recovery** | Insert an intermediate pivot waypoint to break the segment into two safer halves | When the original segment is too long to safely verify in one drive |

---

## Pivot Chords → Strategic Flexibility

A pivot chord is a waypoint that:

1. Is a major or minor triad (safe parking)
2. Is reachable from at least two distinct candidate progressions toward the strategic target
3. Is a viable starting point for at least two distinct sol-N+1 candidates

Pivot chords are gold. They let you commit to sol-N without locking in sol-N+1.

---

## Tension/Resolution Pattern → Phrase Health

A **phrase** is a sub-progression that starts on a stable chord and ends on a stable chord.

| Phrase Pattern | Health | Action |
|----------------|--------|--------|
| `I → ii → V7 → I` | Healthy (ii–V–I) | Standard — accept |
| `I → V7 → I` | Healthy (authentic) | Accept |
| `I → IV → I` | Healthy (plagal) | Accept |
| `I → V7 → vi → ii → V7 → I` | Healthy (extended) | Accept; confirm deceptive cadence is intentional |
| `I → V7 → V7 → V7 → I` | Unhealthy (sustained tension) | Substitute or split into shorter phrases |
| `I → vii⌀ → vii⌀ → vii⌀` | HARD FAIL (sustained dissonance) | Reject — re-compose |
| `... → vii⌀` (final) | HARD FAIL (no resolution) | Reject — extend to a major/minor cadence |

---

## When the Metaphor Hurts

Drop the harmonic vocabulary and revert to plain rover-driver language when:

- Reviewers spend more time arguing about whether something is a "true ii–V–I" than about whether it's safe.
- Onboarding a new planner takes more time on the metaphor than on the actual planning logic.
- A plain-language description ("we go around the rocky patch and end at the bedrock outcrop") is clearly more useful than the harmonic one.
- The audience is non-expert (in which case use `prompts/traverse-rationale.md`).

The framework is a thinking tool. The thinking is the goal, not the metaphor.
