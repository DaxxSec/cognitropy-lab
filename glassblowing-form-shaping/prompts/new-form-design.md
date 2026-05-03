# Prompt — New Form Design (Sim-First)

Use when the artist is approaching a form they haven't made before, or a meaningful variation on a familiar form. Walks the agent through the canonical sim-first sequence.

## Inputs to Provide
- One-paragraph description of the target form (or a photo/sketch reference)
- Glass family in use today
- Whether this is a one-off exploration or a piece intended for a commercial line
- Any known constraints (time budget for the session, lehr capacity)

## Suggested Conversation Opening

> I'm starting a new form today. I'd like to walk through it sim-first before I light the glory hole. Here's the form: <description>. The glass family is <family>. <One-off / commercial line>. I have <X hours> at the bench and the lehr can hold <Y> pieces.
>
> Please run me through `/form-sim`, then `/scenario-test`. If both pass green, open the batch record. If anything is yellow or red, talk me through what to change before we proceed.

## What the Agent Will Do

1. Walk geometry capture — height, max width, wall thickness profile, foot/stem/neck if present, distinct features
2. Run `/form-sim` and produce the form spec
3. Run `/scenario-test` against the spec
4. Surface any yellow/red verdicts with specific recommended adjustments
5. Once verdicts are acceptable, open the day's batch record via `/batch-log` with the form pre-populated
6. Recommend whether to dry-run with a smaller-scale test piece first (default: yes for any genuinely new form, no for variations)

## Why This Prompt Exists

Most new-form failures are knowable from geometry and material data alone. The artist who works through `/form-sim` even once on a form they "know works" usually finds a working-time budget that's tighter than their intuition suggests. The discipline transfers — once it's habit, the artist starts pre-simulating in their head before the agent has to.

## Variations
- **For a known-good form variation:** ask the agent to diff the new variation against the existing form spec rather than starting from scratch
- **For a piece intended for a commercial line:** ask the agent to also generate a "production checklist" — a per-session record of which sim parameters mattered, so a future apprentice can reproduce
- **For a piece intended for a competition / juried show:** ask the agent to be conservative on yellow verdicts; production tolerance for failure is higher than competition tolerance
