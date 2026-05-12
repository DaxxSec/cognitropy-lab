# Traverse Rationale Prompt

## Purpose
Use this prompt when you need to explain a traverse to someone who is not on the planning team — a strategic team member, an external reviewer, an outreach audience, or a journal/conference reader. The audience needs the *reasons*, not the rover-driver vocabulary. Translate the harmonic framework into plain language.

## Prompt Template

I have an approved traverse for sol <N> on <site name> with rover <platform>. I need to explain it to <audience>.

The traverse details:
- **Total distance:** <m>
- **Estimated drive time:** <min>
- **Strategic target:** <name>
- **Decision log:** <path>

The chord progression (for context, not necessarily for the explanation):
```
WP-0 (start) → WP-1 → WP-2 → WP-3 → ... → WP-N (parking)
I             ii    V7   vi (deceptive)   ...   I
```

Notable choices made during planning:
- **Substitutions:** <list — e.g., "tritone substitution at segment 3 to avoid a rocky climb">
- **Deceptive cadence:** <if any — e.g., "WP-5 is an opportunistic SuperCam target en route to the strategic target">
- **Dissents from peer review:** <list any captured dissents>

Please produce:

1. A 2-paragraph **executive summary** in plain language for <audience>. Avoid harmonic vocabulary unless the audience knows it. Lead with the destination and the science return; explain the chosen route in terms of "we chose to go around X to avoid Y."

2. A **trade-off table** showing the alternatives that were considered and why the chosen one was selected. Three rows: chosen / runner-up / rejected baseline. Columns: distance, drive time, hazard score, science return, why-chosen-or-not.

3. A **risk acknowledgment** paragraph that names the residual risks honestly and the contingencies that are in place for each.

4. A **what could go wrong** Q&A — anticipate three sharp questions and answer them in 2 sentences each. Pick questions that an external reviewer would actually ask, not softballs.

## Expected Output

A document suitable for: a strategic team email, an external review meeting, a journal supplement, or a public-facing outreach piece. Honest about trade-offs; specific about contingencies; uses harmonic vocabulary only if the audience does.
