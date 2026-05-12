# /laban-tag — Annotate a Movement Segment with Laban Movement Analysis

Some failure modes are kinematically subtle but Effort-readable. This command guides the user through a Laban Movement Analysis (LMA) annotation pass on a video segment, producing `video_annotation` events that downstream rules can read.

## Background

LMA (Rudolf Laban, codified by Lisa Ullmann in *The Mastery of Movement*, 4th ed., 1980) describes movement on four axes:

- **Body** — what is moving
- **Effort** — *how* it moves, along Weight / Time / Space / Flow factors
- **Shape** — the form the moving body assumes
- **Space** — pathways through external space

Full reference in `resources/lma-effort-graphs.md`.

## Required Inputs

- `--video <uri>` — the video file or URI to annotate
- `--scene <id>` — scene identifier
- `--segments <ranges>` — optional list of timecode ranges to focus on

## Steps

### 1. Body — What Is Moving

For each segment, name the principal mover:
- whole puppet
- head
- left / right arm
- mouth
- legs (or kimono-suggested legs for female bunraku)

### 2. Effort — How It Moves

For each segment, place it on the four Effort factors. Use the eight named Effort Actions when one cleanly fits:

| Action | Weight | Time | Space |
|---|---|---|---|
| Float | Light | Sustained | Indirect |
| Punch | Strong | Sudden | Direct |
| Glide | Light | Sustained | Direct |
| Slash | Strong | Sudden | Indirect |
| Dab | Light | Sudden | Direct |
| Wring | Strong | Sustained | Indirect |
| Flick | Light | Sudden | Indirect |
| Press | Strong | Sustained | Direct |

Flow (Free / Bound) is the fourth dimension and is annotated independently — Free = uninterrupted, Bound = controlled, can be stopped at any moment.

### 3. Shape

Annotate Shape change:
- Spreading / Enclosing
- Rising / Sinking
- Advancing / Retreating

### 4. Space

Annotate the pathway through external space (kinesphere); reach scale (near / mid / far); planes (door / table / wheel).

### 5. Annotated Director Intent

Critical step for detection: ask the user "what was the director's called Effort quality for this segment?" Record both:
- `effort_called:` — the intended Effort
- `effort_observed:` — what the annotator reads

A drift between called and observed is the signal that downstream Effort-quality rules detect.

### 6. Output Events

Each annotation becomes a `video_annotation` event in the segment's parent log:

```yaml
- timestamp: 02:14
  category: video_annotation
  segment: scene-2.1.beat-3
  body: right-arm
  effort_observed: Light-Bound
  effort_called: Strong-Free
  shape: Rising
  space: near-kinesphere, door-plane
  notes: "Directorial intent was Strong-Free; observation reads as Light-Bound — likely string-system fatigue."
```

### 7. Cross-Reference to Detection Rules

After annotation, automatically flag whether any rule in `outputs/rules/active/` keys off the annotated Effort qualities (rules using `|effort_quality:` modifiers). If yes, run a quick `/detect-anomaly --log <log>` against the freshly-annotated log.

## Output

- `video_annotation` events appended to `work-log/<date>.md` (or to the named log)
- A summary block at the end of the annotation pass with the count of called-vs-observed Effort drifts

## Failure Modes

- **Annotator unfamiliar with LMA.** Walk through `resources/lma-effort-graphs.md` first; if still unfamiliar, fall back to a simpler "what was intended? / what did you see?" pair without the LMA vocabulary.
- **No video.** Tier 0 workspaces cannot use this command. Refuse and recommend tier 1 instrumentation.

## Reference

- Laban, Rudolf — *The Mastery of Movement* (4th ed., Lisa Ullmann, 1980)
- Bartenieff, Irmgard — *Body Movement: Coping With the Environment* (1980) for the Bartenieff Fundamentals extension
- Newlove, Jean — *Laban for Actors and Dancers* (1993) for a working-room introduction
