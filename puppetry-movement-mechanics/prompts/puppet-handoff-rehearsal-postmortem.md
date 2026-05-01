# Prompt — Puppet-Handoff Rehearsal Postmortem

A reusable prompt for postmortem-shaped review after a puppet-handoff fumble (a moment in rehearsal where one performer hands off a puppet, or part of a puppet, to another and the transition slipped). Use after the rehearsal-room conversation, before tomorrow's rehearsal.

## When to Use

- A handoff in today's rehearsal slipped (visible drop, unintended motion, late catch)
- A handoff that has been rehearsed for weeks suddenly degraded
- A new performer is being trained on a handoff and rehearsing the same fumble repeatedly

## Prompt Body

> You are running a postmortem on a puppet-handoff fumble. This postmortem follows blameless-postmortem conventions from cybersecurity and SRE practice — focus on systemic causes, not individual blame.
>
> ### 1. The Timeline
> Build a 30-second-window timeline of the fumble. From the rehearsal log:
> - T-15s: what was happening before the handoff?
> - T-5s: what cues were called?
> - T-0: what was supposed to happen?
> - T+0..T+5: what actually happened?
> - T+10: how was the fumble recovered (or not)?
>
> ### 2. The Five Whys
> For each apparent cause, ask "why" recursively until you reach a systemic factor. Examples:
> - Fumble → late catch (why?) → handoff cue arrived early (why?) → omozukai's breath cue accelerated (why?) → omozukai was compensating for a slow string-system (why?) → puppet's right-shoulder support has stretched 4mm past tuning band (rule `string-system-drift--right-shoulder-stretch` would have caught this had it existed; queue draft).
>
> ### 3. Systemic vs. Individual Factors
> Sort the discovered causes into:
> - **Systemic** (mechanism, calibration, cue list, training pattern, environment)
> - **Individual** (a performer's fatigue, attention, skill gap)
>
> Detection rules can address systemic factors. Individual factors belong in the company's training conversation, not the rule set.
>
> ### 4. Ruleable Findings
> For each systemic factor, decide:
> - Is there an existing rule in `outputs/rules/active/` that would have flagged this? If yes, why didn't it fire? (Threshold? Missing event category? Log gap?)
> - If no, is the pattern recurring enough to draft a rule? Cross-reference with `outputs/reports/` for prior occurrences.
> - Draft `outputs/rules/draft/<slug>.yml` if 2+ prior occurrences are documented.
>
> ### 5. Trainable Findings
> For each individual factor, queue an item in `planning/training-followups.md` for the company training lead. Do not gate the rehearsal on individual training items.
>
> ### 6. Output
> Write the postmortem to `outputs/reports/<date>-handoff-postmortem-<scene-id>.md`. Open `/peer-review` against the postmortem with at least one reviewer who was *not* in the rehearsal room (outside-eyes role).
>
> ### 7. The Blameless Frame
> A useful postmortem names systemic causes without naming individual fault. The performer in the fumble is not the cause; the systemic conditions that made the fumble likely are. Frame every finding in those terms.

## Why This Prompt Exists

Most handoff fumbles are rehearsed once, blamed on whichever performer was nearest the slip, and forgotten. Two months later the same handoff slips again with a different performer in the same role, because the underlying systemic cause was never named. This prompt's structure transplants the blameless-postmortem culture from SRE practice and forces the conversation to name the systemic factor.

## Reference

- Beyer, Betsy et al. — *Site Reliability Engineering* (O'Reilly, 2016), Chapter 15: Postmortem Culture
- Allspaw, John — "Blameless PostMortems and a Just Culture" (Etsy engineering blog, 2012)
- "The Five Whys" technique (Toyota Production System; popularized in Western lean / SRE practice)
