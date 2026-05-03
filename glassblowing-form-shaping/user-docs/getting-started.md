# Getting Started

Welcome. This workspace is for hot-glass artists who want to plan with simulation and document with the discipline a soil-microbiome research plot gets. The workflow is unfamiliar at first; this document walks you through the first three sessions.

## Before Your First Session

1. **Run `/onboard`.** Allow ~20 minutes. The agent will ask about your studio, equipment, glass families, and the forms you make most. The answers populate the `context/` files; they're how every subsequent command reasons about your work.
2. **Read `README.md`.** Specifically the "Microbiome-Inspired Batch Record" section — that's the mental model the workspace runs on.
3. **Skim `resources/glass-viscosity-reference.md` and `resources/failure-mode-taxonomy.md`.** You don't need to memorize them; you just need to know they exist so when the agent references them you know where to look.
4. **Decide your documentation posture.** The agent can either enforce a batch record per session strictly, or treat batch records as opt-in. Strict is recommended once you've worked with the workspace for a few sessions; opt-in is fine while you're learning the rhythm.

## Session 1 — The Calibration Session

Your first session under this workspace should be a session you've done many times before. Don't try to learn the workspace AND a new form on the same day.

### Pre-session
1. Run `/batch-log` to open today's record. Confirm the header: glass family, ambient, glory hole soak, lehr program.
2. For each piece you plan to make today, run `/form-sim`. Even though you've made these pieces a thousand times, run the sim. The point is to calibrate the simulator's defaults against your actual experience.
3. After each `/form-sim`, run `/scenario-test`. Most should come back all-green for familiar forms.

### During session
- Log gathers, operations, reheats, and any anomalies. Use 24-hour times.
- If something feels off — gather felt heavier than usual, color rod gave you trouble, lehr was warmer than expected — log it. The "trivial" anomalies are exactly what `/lineage-trace` will look for in three months.

### After session
1. Run the closeout pass of `/batch-log`. Populate the outcomes table, confirm lehr program ran as planned, schedule the four successional follow-ups (24h / 7d / 30d / 90d).
2. For each finished piece, the agent will create or update `outputs/pieces/<piece-id>.md`. Take a phone photo and drop it under `outputs/photos/<piece-id>/`.
3. **Reflect on the simulator's calibration.** The form-sim verdicts and your lived experience should match. If they don't (sim said yellow, you breezed through; sim said green, you struggled), tell the agent — adjustments to your studio's specific defaults go into `context/for-agent/environment.md`.

## Session 2 — Introducing a New Variable

Pick one variable to change: a new color rod lot, a slightly modified form, a different ambient (work in the morning instead of afternoon). Keep everything else the same as Session 1.

The point is to see the workspace's value in action. The variable will produce one of:
- A different sim verdict (the simulator caught something)
- An anomaly during the session (the batch record will hold the evidence)
- A successional follow-up that surfaces something later (the lineage will hold the cause)

Whichever way it goes, the workspace earned its keep.

## Session 3 — Trying a New Form

Now run the `prompts/new-form-design.md` flow on a form you've genuinely never made. Be conservative on yellow verdicts; ideally do a smaller-scale test first.

After the session, even if everything went well, do a self-`/post-mortem` on the most marginal piece — what nearly went wrong, what would you do differently. The taxonomy and the diagnostic discipline reward investment up front.

## When Things Don't Make Sense

- **The simulator's working time budget feels wrong.** The defaults are studio-grade approximations. If your studio's actual budget is consistently different (you have a hotter glory hole, a colder ambient, a different gather technique), tell the agent and the defaults shift to match your studio.
- **The COE compatibility matrix flags a combination you've used for years without problems.** You may have been lucky, or the published COE may not match the actual lot you've been using. Run the pretest protocol to confirm; document the result either way.
- **A post-mortem comes back low confidence.** That's the diagnostic system being honest. Add the case to `outputs/post-mortems/research-cases/` and revisit when you have more data.

## A Note on Discipline

The workspace's value compounds. The first session feels like overhead. The tenth session feels normal. By the thirtieth session, when a piece cracks unexpectedly, you'll be able to answer "what changed in the last month that this piece shared with the other failures?" in ten minutes instead of staring at the wall. That payoff is the entire point.
