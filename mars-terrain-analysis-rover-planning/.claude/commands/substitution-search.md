# /substitution-search — Find Tritone & Modal-Interchange Substitutions

Replace a flagged segment with an alternate that resolves to the same destination chord at lower risk or higher science return.

## Required Inputs

- Candidate file (`planning/candidates/<sol>-<id>.md`)
- Index of the flagged segment (e.g., "segment 3, between WP-2 and WP-3")
- Substitution type: `tritone` (default), `modal-interchange`, `pivot-recovery`, or `auto` (try all)
- Maximum acceptable drive-time penalty as a fraction of the segment's original cost (default 0.20 — 20% slower is acceptable)

## Procedure

### 1. Load the Segment Context

- Identify start chord (WP-N), end chord (WP-N+1), and the segment's original cost components.
- Pull the hazard sub-raster bounded by a generous box around the segment (default: extend 30 m on every side).

### 2. Tritone Substitution

**Operational meaning:** find a different-terrain-class path that ends at the same WP-N+1.

- Re-run a constrained `networkx.shortest_path` between WP-N and WP-N+1, *requiring* that the path crosses no pixels of the original segment's dominant terrain class.
- For example: if the original segment crosses `regolith_rocky`, find the lowest-cost path that uses only `bedrock` or `conglomerate` pixels.
- Validate that the substitute resolves to the exact same WP-N+1 chord (terrain, slope, science).
- Record the substitute as a candidate substitution with:
  - Original cost vs substitute cost
  - Hazard delta (lower / higher / equivalent)
  - Drive-time delta
  - Voice-leading delta (smoother or rougher transitions)

### 3. Modal Interchange

**Operational meaning:** borrow the corresponding segment from the *conservative* plan variant.

- Generate (or read, if cached) the "conservative" candidate for the same start/end WPs. Conservative = `/traverse-compose --mode conservative` runs with weight `w_s = 0.55, w_r = 0.20, w_o = 0.25, w_c = 0.0` (slope-and-roughness dominant) and forbids `regolith_fines` and `aeolian` entirely.
- If the conservative variant has a different segment between WP-N and WP-N+1, propose it as a modal-interchange substitute.
- Same metrics as tritone substitution.

### 4. Pivot-Recovery (Optional)

**Operational meaning:** insert a pivot waypoint (a safer intermediate waypoint that can support a different sub-progression).

- Identify pivot-eligible waypoints near the segment: waypoints that are safe parking spots AND lie within the broader candidate corridor.
- Propose: WP-N → pivot → WP-N+1, splitting the original segment into two safer halves.
- Cost-evaluate as a 2-segment substitute.

### 5. Score and Rank

For each substitution, compute the substitution score:

```
sub_score = w1 * (-hazard_delta)
          + w2 * (-voice_leading_delta)
          + w3 * (science_value_delta)
          - w4 * max(0, drive_time_delta - allowed_drive_time_penalty)
```

Default weights: `w1 = 0.45, w2 = 0.25, w3 = 0.20, w4 = 0.10`.

Rank substitutions descending; only present substitutes with positive `sub_score` *unless* the user explicitly asks for "all candidates."

### 6. Generate the Substitution Report

Write `planning/candidates/<sol>-<id>-sub-<segment-idx>.md`:

```markdown
# Substitution Report — Candidate <sol>-<id>, Segment <idx>

## Original Segment
WP-2 (regolith-rocky, inclined, opportunistic) → WP-3 (bedrock, flat, strategic)
Cost: 0.42 (hazard 0.38, voice-leading 0.18, drive-time 6.2 m)

## Substitution Candidates

### Sub-A: Tritone (terrain swap to bedrock corridor)
- New path: WP-2 → WP-2a → WP-3
- Cost delta: +12% drive time
- Hazard delta: -0.31 (much safer)
- Voice-leading delta: +0.05 (slightly smoother)
- **Recommendation: STRONG** — accept this substitution

### Sub-B: Modal interchange (borrow from conservative plan)
- ...

### Sub-C: Pivot recovery (insert WP-2.5)
- ...
```

### 7. Update the Candidate

If the user accepts a substitution, update the candidate file:
- Increment its revision number
- Replace the flagged segment with the substitute
- Recompute total distance, drive time, and chord progression
- Save the prior revision under `planning/candidates/history/<sol>-<id>-rev<N>.md`

### 8. Recommend Re-Running `/risk-cadence`

Substitutions can shift the overall tension/resolution pattern. After accepting any substitution, re-run `/risk-cadence` on the revised candidate before going to `/peer-review`.

## Output

The substitution report and an updated candidate file (if a substitution is accepted). The user is asked to accept/reject explicitly — substitutions are not auto-applied.
