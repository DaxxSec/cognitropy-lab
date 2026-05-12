# The Jazz Harmony Framework — Plain-Language Explanation

If you've never played jazz, the harmonic vocabulary in this workspace is going to feel arbitrary at first. This document explains the *why* in plain language, so the metaphor earns its keep.

## Why borrow from jazz harmony at all?

Rover traverse planning is a multi-objective trade-off problem with a vocabulary problem. Words like "risky," "bold," "conservative," "elegant" are real planner words but they're imprecise. They don't help two reviewers agree on what specifically is being traded.

Jazz harmony is a centuries-old analytical framework for talking about *how chords move and resolve*. The framework is sharp, well-developed, and has terminology for exactly the kinds of moves traverse planners make: smooth voice leading, substitutions, cadences, deceptive cadences, modal interchange, pivot chords. Borrowing the vocabulary forces planners to be precise about the move they're making.

It's not poetry. It's a mature mental model from one field, applied to another.

## The three core ideas

### Idea 1: Each waypoint has three properties, and they form a chord

A musical chord is built from notes that combine into a quality (major, minor, dominant, etc). A waypoint in the workspace is built from three properties:

- **Terrain class** (bedrock, regolith-rocky, etc.) — the *root* of the chord
- **Slope class** (flat, inclined, steep) — the *third*
- **Science value** (none, opportunistic, strategic, priority-1) — the *fifth*

Combine the three and you get a chord *quality*: a flat bedrock waypoint with priority-1 science is a "major triad" — the safest, most valuable kind. A steep aeolian waypoint with no science is a "fully diminished" chord — forbidden to plan there.

You can ignore the names if you want. What matters is that each waypoint gets a quality label that captures all three properties at once. That's the precision win.

### Idea 2: Segments are voice-leading moves

In jazz, *voice leading* is how each note moves from one chord to the next. Smooth voice leading is when each note moves by a small step; bad voice leading is when notes leap or cross.

In rover planning, voice leading is how the rover's slope, heading, and terrain class change over a segment. Smooth voice leading is good: ≤ 5° slope change per metre, ≤ 30° heading change per 5 m, terrain class moving stepwise (bedrock → regolith-rocky is fine; bedrock → aeolian is a leap).

The thing the metaphor does for you: you stop thinking about slope, heading, and terrain transitions as three separate problems and start thinking about them as one *smoothness* problem. That's how an experienced rover driver actually thinks; the metaphor makes that thought reproducible.

### Idea 3: The traverse must end on a resolution

In jazz, a phrase ends on a *cadence* — a closing motion that resolves tension. Authentic cadence (V → I), plagal cadence (IV → I), deceptive cadence (V → vi when you expected V → I).

In rover planning, the traverse must end on a verified safe parking spot — a *resolution chord*. No traverse may end on a dominant, half-diminished, or fully diminished chord, because none of those are safe overnight positions. This is a hard rule, not a guideline.

The deceptive cadence is the interesting one. Sometimes you plan to end at a strategic target (V → I), but downlinked imagery reveals an opportunistic science target en route. The traverse becomes V → vi: dominant resolved unexpectedly to a different stable chord. The framework gives you a name for what you just did, which makes it easier to talk about with the science PI.

## Substitutions, in one paragraph each

### Tritone substitution
In jazz: replace one dominant chord with another whose root is a tritone away. Operationally: replace a risky segment with a different-terrain-class segment that ends at the same waypoint. If your candidate climbs over a rocky ridge, find a longer contoured detour through bedrock that ends at the same place. Same destination, different path.

### Modal interchange
In jazz: borrow a chord from a parallel scale (the parallel minor of a major key). Operationally: borrow a segment from a parallel "conservative" plan variant. The conservative variant trades drive distance for safety; modal interchange lets you take the conservative segment for a single risky position without rewriting the whole plan.

### Pivot chords
In jazz: chords that fit naturally in two different keys. Operationally: waypoints that work as stable parking spots for *multiple* candidate traverses. Pivot waypoints are gold — they let you commit to a near-term traverse without locking in the medium-term plan. When you have two candidates that score similarly, prefer the one passing through more pivot waypoints.

## When to drop the metaphor

The framework is a thinking tool. The thinking is the goal, not the metaphor.

Drop it and revert to plain rover-driver language when:

- Reviewers spend more time arguing about whether something is a "true ii–V–I" than about whether it's safe.
- Onboarding a new planner takes more time on the metaphor than on the actual planning logic.
- Plain language is clearly more useful ("we go around the rocky patch and end at the bedrock outcrop").
- The audience is non-expert (use `prompts/traverse-rationale.md` instead).

If the metaphor is helping the conversation, keep it. If it's getting in the way, drop it. Either way is fine.

## A quick listening recommendation, if you want it

If you want to hear what voice leading sounds like, listen to the first 30 seconds of any Bill Evans recording — "Peace Piece," "Waltz for Debby," "My Foolish Heart." Notice how each chord change feels inevitable rather than abrupt. That feeling is what good voice leading does. Aim for traverses that feel the same way: each segment leads naturally into the next, no leaps, no surprises, ends on a satisfying resolution. The traverse equivalent of "Waltz for Debby" is what `/peer-review` is checking for.

## Recommended further reading

- Mark Levine, *The Jazz Theory Book* (Sher Music, 1995) — canonical text. The chord/cadence/substitution chapters are what this framework borrows from.
- Mark Levine, *The Jazz Piano Book* — voice-leading worked examples; useful for intuition.
- Aldwell, Schachter, & Cadwallader, *Harmony and Voice Leading* — the classical-theory foundation.
- For the rover side, see the references in `README.md` — Maki et al. (2020), Rankin et al. (2020), and Verma et al. (2023).
