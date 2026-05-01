# Getting Started

> A quick-start for puppeteers, riggers, and dramaturgs new to this workspace. If you've never used a SIEM or a Sigma rule before, that's fine — the workspace is designed to teach you the methodology by using it.

## What You're About to Do

You're going to turn your rehearsal practice into a structured corpus that can answer the question "has this failure happened before?" with evidence rather than memory. The methodology is borrowed from cybersecurity SOC operations:

1. Each rehearsal becomes a structured log.
2. Recurring failure patterns become YAML rules.
3. Rules are peer-reviewed (red / blue / purple roles) before they go live.
4. Rule changes are backtested against past logs.
5. Every public performance gets an incident-shape post-show report.

## Day 0 — Onboard

```
/onboard
```

This walks you through:
- Naming the company, productions, and puppet inventory
- Building the peer-review roster (at least two people in distinct role buckets)
- Setting communication preferences for the agent
- Sanity-checking the failure-mode catalog against your puppets

Plan ~30–45 minutes for a first onboard. The session output is saved across `context/project.md`, `context/role.md`, `context/constraints.md`.

## Day 1 — First Calibration Audit

```
/calibration-audit --puppet <slug> --reason scheduled
```

For each puppet in inventory. Establishes the baseline against which all future drift detection runs. Plan ~20 minutes per puppet (faster after the first).

## Day 2+ — Daily Practice

After every rehearsal:

```
/movement-log
```

The agent walks you scene-by-scene; you dictate events. Output: `work-log/<date>.md`.

After each log:

```
/detect-anomaly
```

Replays the active rule set against the log. Initially the rule set is empty — that's expected.

## Week 2 — Your First Rule

Once you've noticed a pattern across two or more logs:

```
/rule-author
```

The agent walks you through drafting a Sigma-style YAML rule. The draft must cite at least two `work-log/` entries; this is enforced.

## Week 2 — Your First Peer Review

```
/peer-review --target outputs/rules/draft/<slug>.yml --reviewers <r1>:<role1>,<r2>:<role2>
```

Two reviewers, distinct roles. The agent walks each reviewer through their assigned color (red / blue / purple) and writes the pass record to `outputs/reviews/`.

## Week 3+ — Performance Reports

After every public performance:

```
/post-show-report
```

Produces an incident-shape report. Goes through `/peer-review` within 48 hours.

## Common Questions

### "Do I need to be a detection engineer to use this?"

No. The methodology is the value, not the SOC vocabulary. The agent translates between detection-engineering language ("Sigma rule", "false positive", "tactic / technique tag") and puppetry vocabulary ("recurring slip", "expected benign cause", "what kind of failure is this") based on your stated experience in `context/role.md`.

### "Do I need video for this?"

No, but more instrumentation = more rule expressiveness. Tier 0 (notebook only) supports manipulator-input and audience-observation rules. Tier 1 (video) adds video-annotation rules. Tier 3 (sensors) adds quantitative rules.

### "Won't this slow rehearsals down?"

`/movement-log` is post-rehearsal, ~5–15 minutes. `/detect-anomaly` is automated. `/peer-review` is the time-investment, ~15–45 minutes per pass — but each pass produces an artifact that pays back across the rest of the run.

### "What about the art? I don't want detection rules telling me how to direct."

Detection rules describe failure modes — mechanism drift, sync loss, calibration off-baseline. They don't describe aesthetic choices. The constraint is explicit in `context/constraints.md`: a director's deliberate hesitation is not an anomaly. When unsure, the agent asks before flagging.

### "How does this differ from just keeping a rehearsal journal?"

A journal is unstructured personal memory. The workspace produces structured, replayable, peer-reviewed institutional memory. The shapes you'll come to value:

- Backtesting: when you change a rule, you immediately know which past anomalies it now catches or misses.
- Peer review: a second perspective is required *before* a rule lands — not after a problem.
- Tagging: every rule maps to a published failure-mode taxonomy, so company-wide trends are visible in aggregate.

## Next Steps

- Run `/onboard` if you haven't.
- Read `context/for-agent/domain-knowledge.md` for the depth — it's the agent's reference, but it's also a useful standalone read.
- Read `resources/peer-review-disposition-language.md` before your first peer review.
