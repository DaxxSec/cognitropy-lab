# Laban Movement Analysis — Effort Graphs Reference

> Quick reference for `/laban-tag`. Full treatment: Laban, *The Mastery of Movement* (4th ed., Ullmann, 1980); Newlove, *Laban for Actors and Dancers* (1993).

## The Four Effort Factors

| Factor | Polarity 1 | Polarity 2 | Mnemonic |
|---|---|---|---|
| **Weight** | Light | Strong | "How much pressure?" |
| **Time** | Sustained | Sudden | "How long?" |
| **Space** | Indirect | Direct | "How focused?" |
| **Flow** | Free | Bound | "How interruptible?" |

Each factor is a continuum, not a binary. Annotators may write `Light-leaning`, `mid`, `Strong-leaning` for finer granularity.

## The Eight Effort Actions

The 2×2×2 cube of (Weight × Time × Space), holding Flow aside:

| Action | Weight | Time | Space | Felt-As |
|---|---|---|---|---|
| **Float** | Light | Sustained | Indirect | A leaf drifting; an unmoored marionette swaying |
| **Punch** | Strong | Sudden | Direct | A quick decisive strike |
| **Glide** | Light | Sustained | Direct | A skater's traverse |
| **Slash** | Strong | Sudden | Indirect | A whip, a wild gesture |
| **Dab** | Light | Sudden | Direct | A typist's keystroke |
| **Wring** | Strong | Sustained | Indirect | Twisting a cloth |
| **Flick** | Light | Sudden | Indirect | Brushing off lint |
| **Press** | Strong | Sustained | Direct | Pushing through a heavy door |

Flow is annotated separately — every Action can be performed Free or Bound.

## Effort Drives (combinations of three factors)

Used when only three factors are foregrounded:

- **Action drive** — Weight + Time + Space (Flow is latent). Most common for puppetry rule annotations.
- **Passion drive** — Weight + Time + Flow (Space is latent). Useful for emotional sequences where direction is undefined.
- **Vision drive** — Time + Space + Flow (Weight is latent). Useful for dream sequences, ghosts, shadow-puppet flights.
- **Spell drive** — Weight + Space + Flow (Time is latent). Useful for hypnotic, ritual, or trance sequences.

## Detection Rule Modifiers

Rules in `outputs/rules/active/` use this vocabulary via the `|effort_quality:` modifier:

```yaml
detection:
  selection:
    category: video_annotation
    effort_observed|effort_quality: Light-Bound
    effort_called|effort_quality: Strong-Free
    effort_drift_magnitude|gt: 2-quadrants
```

A "quadrant" of drift is one polarity flip on one factor. Two-quadrant drift = polarity flips on two factors and is usually noticeable; three-quadrant drift is dramatic.

## Common Drift Patterns Worth Detecting

- **Light-Bound drift on intended Strong-Free.** Often signals string-system fatigue (puppet feels under-driven; performer compensates by holding tighter).
- **Sudden drift on intended Sustained.** Often signals mechanism slippage (a joint slipping under load gives a Sudden quality the performer didn't intend).
- **Direct drift on intended Indirect.** Often signals over-rigging (the puppet has been retuned to lose its expressive sway).
- **Bound drift on intended Free.** Often signals new-performer-on-the-rig (training pattern).

## Notation Shorthand for Logs

In `work-log/<date>.md`, Effort can be written compactly as 4-character codes:

```
LSIF   Light Sustained Indirect Free   (Float, Free)
SSDB   Strong Sustained Direct Bound   (Press, Bound)
LSdB   Light Sustained direct Bound    (Glide-leaning-direct, Bound)
```

Lowercase = leaning toward, uppercase = clear polarity. The agent expands these to full text in formal annotations.

## Limitations

- LMA captures *quality* of movement; it does not capture *quantity* (joules expended) or *kinematics* (joint angles). Pair with kinematic events for full coverage.
- LMA is annotator-dependent; inter-annotator agreement on Effort tagging is typically κ≈0.6 even among trained Certified Movement Analysts. Detection rules should not fire on a single annotator's tag without corroboration from joint-event or string-tension data.
- LMA training is non-trivial. Companies new to LMA should plan a workshop (most CMA-led intros run 2–3 days) before relying on `/laban-tag` for detection.
