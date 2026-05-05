# Post-Drive Debrief Prompt

## Purpose
Use this prompt after a sol's drive completes (or aborts). The debrief feeds back into the next sol's plan and into the lessons-learned record. The audience is the next sol's planner, who needs to know what actually happened vs. what was planned.

## Prompt Template

The sol-<N> drive is complete (or aborted). I want to debrief.

**Plan reference:**
- **Sol plan:** <path to outputs/sol-plans/...>
- **Decision log:** <path to outputs/decision-log/...>
- **Approved candidate:** <id>

**As-executed:**
- **Drive distance achieved:** <m> (planned: <m>)
- **Drive time used:** <min> (planned: <min>)
- **End-of-drive position:** <coords> (planned: WP-N at <coords>)
- **Heading at end:** <deg> (planned: <deg>)
- **Mechanism state:** <nominal / anomalous, describe>
- **Energy state:** <%> (predicted: <%>)
- **Memory state:** <% used> (predicted: <%>)
- **Comms passes hit:** <list> (planned: <list>)
- **Anomalies during drive:** <list — hazcam rejects, slope warnings, mechanism faults, comms misses>

Please produce:

1. A **plan-vs-actual delta report** in table form. Columns: metric, planned, actual, delta, was-it-an-issue. Cover every numbered metric above.

2. A **chord-progression as-executed** comparison. The plan was a sequence like `I → ii → V7 → I`. What did the rover *actually* execute? Did any segment turn out to be a different chord quality than predicted (e.g., a planned ii turned out to be a half-dim because the terrain class was misclassified)?

3. A **lessons-learned section** with three buckets:
   - **Hazard-map calibration:** did any pixel turn out to be more / less hazardous than its score predicted? Should the scoring formula be retuned?
   - **Voice-leading calibration:** did any segment have a worse voice-leading penalty than predicted? (Often a heading-change estimate problem.)
   - **Reviewer rubric calibration:** did any reviewer's flagged concern materialize? Any concern that *didn't* materialize but was worried about?

4. A **substitution-retrospective**: were any substitutions (from `/substitution-search`) a clear win, a clear loss, or a wash? Specifically: if a tritone substitution was applied, was the substitute's actual cost what the substitution report predicted?

5. A **handoff to sol-<N+1>** section:
   - Updated rover state (pose, mechanism, energy, memory)
   - Recommended starting strategic priority
   - Any new hazards or features observed during the drive that should change the sol-<N+1> hazard map
   - Any flight-rule update suggestions

6. An **archive entry** for `work-log/<YYYY-MM-DD>.md` summarizing the debrief in 8–12 lines.

## Expected Output

A debrief document saved as `outputs/debriefs/sol-<N>.md`, an updated `planning/state.md`, and an entry in `work-log/`. Be specific and unsentimental — debriefs that hide misses are debriefs nobody trusts.
