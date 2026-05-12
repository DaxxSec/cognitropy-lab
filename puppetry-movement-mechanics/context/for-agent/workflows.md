# Workflows

Four core workflows; the technique constraint *using peer review workflows* is woven through all of them.

## Workflow 1 — Capture (after a rehearsal)

**Trigger:** rehearsal or performance just ended.
**Time budget:** 5–15 minutes.
**Owner:** primary puppeteer or stage manager.

### Steps

1. **`/movement-log` opens a session shell.**
2. The agent asks for the date, production, scene IDs, puppets in the session, and any cue-list reference.
3. The agent walks scene-by-scene asking for:
   - **Joint events** — point-in-time joint angle changes that the puppeteer remembers as significant.
   - **String-tension samples** — for marionettes, any moment a string felt tight, slack, or different from baseline.
   - **Manipulator inputs** — the puppeteer's own input actions (cue numbers, beats, breath cues).
   - **Audience-side observations** — anything a watcher (dramaturg, director, AD) noted from the front of house.
4. Each event is timestamped (HH:MM:SS or scene:beat) with a free-text observation field.
5. Output: `work-log/<YYYY-MM-DD>.md` with a structured event table per scene and a free-form notes section.

### Decision tree

```
Did anything fire from the active rule set?
├── No → log saved, no further action.
└── Yes → run /detect-anomaly to inspect the firing(s).
```

## Workflow 2 — Detect (replay a log against active rules)

**Trigger:** a new log is captured, or an active rule was tuned.
**Time budget:** 5–10 minutes.
**Owner:** detection engineer (or puppeteer wearing that hat).

### Steps

1. **`/detect-anomaly --log <path>`** loads the log and replays each rule in `outputs/rules/active/` against the log's event stream.
2. For each firing, the agent emits:
   - Rule ID and version
   - Matching events
   - Tactic / technique tags
   - Suggested next step (no action, draft a tuning, escalate to peer review)
3. **`/detect-anomaly --backtest <rule>`** replays one rule across all historical logs in `work-log/` and reports:
   - True positives (already known anomalies)
   - New firings (potentially false positives or newly-found real anomalies)
   - Missed firings (logs the rule should have caught but does not)

### Decision tree

```
Is the firing a known recurring pattern?
├── First seen in this log → note in work-log; do NOT draft a rule yet.
├── Seen in 2+ logs already   → run /rule-author to draft.
└── Seen for many runs but rule already active → run /peer-review --tune for threshold tuning.
```

## Workflow 3 — Author (draft a Sigma-style rule)

**Trigger:** a recurring pattern observed in 2+ logs.
**Time budget:** 15–30 minutes.
**Owner:** the person who noticed the pattern (puppeteer, rigger, dramaturg, animator).

### Steps

1. **`/rule-author`** asks for:
   - A short title ("right-shoulder support stretches past tuning band")
   - The two-or-more example logs that motivated the rule
   - The puppet types this rule applies to
   - The expected event categories the rule reads (joint_event, string_tension, ...)
   - The selection criteria (field-by-field thresholds)
   - Any benign filters (cases where the pattern is intentional)
   - Tactic / technique tags from `resources/puppet-mechanism-failure-modes.md`
   - Stated false-positive sources
2. The agent writes a draft rule to `outputs/rules/draft/<slug>.yml` using the schema in `resources/sigma-rule-template-puppetry.md`.
3. The agent runs `/detect-anomaly --backtest` on the draft to compute approximate firing rate against historical logs.
4. **Mandatory:** `/peer-review` is called with the draft as input.

### Authoring checklist

- [ ] Two or more example logs cited
- [ ] Tactic and technique tags present and from the published taxonomy
- [ ] At least one stated false-positive source
- [ ] Backtest run; firing rate reasonable
- [ ] Author named; date stamped

## Workflow 4 — Review (the peer-review gate)

**Trigger:** any rule draft, any post-show report, any tuning of an active rule.
**Time budget:** 15–45 minutes per pass.
**Owner:** at least two reviewers, **distinct roles** (puppeteer + rigger; omozukai + dramaturg; builder + director; ...).

### Steps

1. **`/peer-review --target <rule-or-report>`** opens a review pass.
2. The agent prompts each reviewer for their role (red / blue / purple) and walks them through:
   - **Red role.** "Construct or recall a log where the rule should fire but does not, or fires but should not."
   - **Blue role.** "Walk the rule against its stated example logs. Does it fire correctly? Are the tags correct?"
   - **Purple role.** "Suggest one specific change — threshold, window, field, scope — that improves the rule without narrowing it past usefulness."
3. Each reviewer writes a disposition: `accepted`, `tune <field>`, `reject`, `escalate`.
4. The agent assembles the pass record at `outputs/reviews/<YYYY-MM-DD>-<rule-slug>.md` with all reviewer comments and dispositions.
5. **Merge gate:**
   - If both reviewers wrote `accepted` → rule moves from `outputs/rules/draft/` to `outputs/rules/active/`.
   - If any reviewer wrote `tune` → rule stays in draft; author addresses the tune item; new review pass.
   - If any reviewer wrote `reject` → rule is closed; rationale logged.
   - If any reviewer wrote `escalate` → review escalates to a third reviewer (typically senior tradition-bearer or company lead) before disposition.

### Distinct-roles enforcement

The `/peer-review` command refuses to finalize if both reviewers are in the same role bucket. This is the single most important guard in the workflow; do not bypass it.

## Cross-Cutting Workflow — Calibration Audit

Run before opening night, after travel, after a major repair.

1. **`/calibration-audit --puppet <slug>`** loads the puppet's baseline from `outputs/baselines/<slug>.yml`.
2. The agent walks the rigger through measuring each tracked dimension (string lengths, hinge friction, servo offsets, foam-mech mouth travel).
3. Differences from baseline beyond the per-dimension tolerance are logged as audit findings.
4. Findings ride into the next `/post-show-report` or trigger immediate maintenance, depending on severity.

## Cross-Cutting Workflow — Post-Show Report

After every public performance, even if nothing fired.

1. **`/post-show-report`** assembles:
   - The performance's `work-log/<date>.md`
   - All rule firings from `/detect-anomaly`
   - Calibration findings since the last show
   - Free-form post-show notes from the rehearsal-room conversation
2. The agent emits an incident-shape report at `outputs/reports/<YYYY-MM-DD>-<production>.md`.
3. The report is queued for `/peer-review` with a 48-hour SLA.

## A Note on Live Performance

Detection rules **never** fire visibly during a live performance. The `/detect-anomaly` step always runs *after* the show. This is a hard rule — surfacing flags during a show would be more disruptive than helpful, and the detection engineering literature supports this (post-incident review beats live-flag noise for low-frequency, high-context detections).
