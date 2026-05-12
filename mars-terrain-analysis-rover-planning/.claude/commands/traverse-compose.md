# /traverse-compose — Compose a Candidate Traverse (Harmonic Framework)

Build 1–N candidate traverses from current rover position to a strategic target, using the chord-progression framework from `context/for-agent/domain-knowledge.md` Part 2.

## Required Inputs

- Current rover position (x, y, heading) — from `planning/state.md`
- Strategic target waypoint (x, y) — from `planning/plan.md`
- Hazard raster + terrain-class raster — from `/terrain-assess`
- Drive distance budget (m per sol)
- Sol number (for output naming)
- Mode (default: `tactical`; alternatives: `strategic`, `recovery`)

## Procedure

### 1. Build the Waypoint Graph

- Sample candidate waypoints across the AOI: regular grid (e.g., 5 m spacing for tactical, 25 m for strategic) plus dense sampling around the strategic target and known scientifically-interesting features.
- Drop any waypoint whose hazard score is above the drivable threshold (filter with `drivable.tif`).
- For each surviving waypoint, build the **chord** (terrain class, slope class, science value):
  - Terrain class from the per-pixel `terrain_class.tif`.
  - Slope class binned: flat (< 10°), inclined (10–20°), steep (20–25°), extreme (> 25°). Extreme is forbidden — drop the waypoint entirely.
  - Science value from a project-supplied science-target overlay (priority-1 / strategic / opportunistic / none).

### 2. Build the Candidate Edge Set

- For each pair of waypoints within a "neighborhood" (default 25 m for tactical, 100 m for strategic), evaluate the segment between them:
  - Cost = drive-time-estimate + voice-leading penalty + hazard-line-integral.
  - Reject segments that cross a high-hazard pixel exceeding `drivable.tif` threshold.
  - Reject segments that cross a forbidden-terrain pixel (extreme slope, planetary-protection Special Region).

### 3. Compose the Top-K Progressions

- Use `networkx.shortest_simple_paths(graph, source=current, target=strategic_target, weight="cost")` to enumerate the top K (default 5) lowest-cost candidate progressions.
- For each, record the chord sequence in `planning/candidates/<sol>-<id>.md` with the canonical structure:

```yaml
candidate_id: <sol>-<id>
mode: tactical
total_distance_m: <>
estimated_drive_time_min: <>
chord_progression:
  - waypoint_id: WP-0  # current rover position
    chord: { root: bedrock, third: flat, fifth: priority-1 }
    quality: major-triad
  - waypoint_id: WP-1
    segment_to_prev: { distance_m: 6.2, voice_leading_penalty: 0.18, hazard_integral: 0.31 }
    chord: { root: bedrock, third: inclined, fifth: opportunistic }
    quality: dominant-7
  ...
  - waypoint_id: WP-N  # parking
    chord: { root: bedrock, third: flat, fifth: strategic }
    quality: major-triad
    role: cadence
```

### 4. Verify Cadence

- The final waypoint **must** be a major or minor triad (resolution chord). If the path's natural endpoint isn't, extend by one segment to a verified safe parking pixel.
- Reject any candidate whose final chord is dominant, half-diminished, fully diminished, or suspended.

### 5. Apply Mode-Specific Rules

- **Tactical mode:** standard rules.
- **Strategic mode:** prefer routes through pivot waypoints (waypoints that appear in ≥ 2 candidate progressions). Mark pivot waypoints in the chord progression.
- **Recovery mode:** stricter — no half-diminished chords anywhere in the progression; segment length ≤ 5 m; every segment ends on a verified parking-eligible chord.

### 6. Render Visual Summary

For each candidate, render a PNG showing the waypoint sequence over the hazard map, with chord-quality colour coding (green = major/minor, yellow = dominant, orange = half-dim, red = forbidden).

### 7. Update Planning Index

Append to `planning/plan.md`:

```markdown
## Sol <N> Candidates (composed <YYYY-MM-DD HH:MM>)

| ID | Distance | Drive Time | Cadence | Notes |
|----|----------|------------|---------|-------|
| <sol>-A | 14.2 m | 38 min | authentic (V→I) | through bedrock band |
| <sol>-B | 17.8 m | 45 min | plagal (IV→I) | longer, fewer dominants |
| <sol>-C | 12.1 m | 31 min | authentic (V→I) | crosses ripple field at WP-3 — flag for substitution |
```

### 8. Recommend Next Step

Output for the user:
- Which candidate(s) look strongest?
- Which segments should be passed to `/substitution-search`?
- Which candidate is ready for `/risk-cadence` directly?

## Output

The candidate files in `planning/candidates/`, the updated `planning/plan.md`, the per-candidate PNGs, and a recommendation. The next command is typically `/risk-cadence` (or `/substitution-search` for a flagged segment).
