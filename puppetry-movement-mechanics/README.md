# Puppetry Movement Mechanics Workspace

> An agent workspace that applies SOC / detection-engineering methodology — structured event logs, Sigma-style detection rules, peer-reviewed rule sets — to the physical motion of puppets, marionettes, bunraku figures, shadow puppets, and animatronics. Every rehearsal is a log; every recurring failure is a rule; no rule ships without peer review.

## What This Workspace Does

Puppet companies accumulate enormous amounts of tacit motion knowledge — "the left hand on the bunraku always lags by a sixteenth," "the marionette's right shoulder string stretches noticeably after about six performances," "the animatronic's lower-jaw servo drifts by about two degrees on warm nights." That knowledge usually lives in one or two senior puppeteers' heads and dies when they leave the company.

This workspace turns that tacit knowledge into a maintained corpus:

1. **Logs every rehearsal as a structured event stream** — joint angles, string tensions, manipulator inputs, dramaturg notes, audience-side observations — using the same shape an SOC analyst would use for endpoint telemetry.
2. **Encodes recurring failure patterns as Sigma-style detection rules** stored as YAML in `outputs/rules/`. The rule set is versioned, diffable, peer-reviewable.
3. **Gates every rule and every post-show report through formal peer review** with explicit red-team (try to break the rule), blue-team (validate the detection covers the failure), and purple-team (collaborative tuning) roles, drawn directly from cybersecurity detection-engineering practice.
4. **Replays past logs against the current rule set** so when you change a rule you immediately see which past anomalies it would now catch or miss — the regression-test pattern that detection engineers call rule backtesting.
5. **Maps every detected anomaly to a published failure-mode taxonomy** (the puppetry analogue of MITRE ATT&CK) so company-wide trend analysis is possible.

## Why This Workspace Exists

Two long-standing problems in puppetry production motivated this workspace:

**Problem 1 — institutional forgetting.** Touring shows accumulate hundreds of small mechanism drifts (a puppet bouncing back from a hard travel case, foam latex gradually losing memory in tropical climates, a costume hooking on a string for the third week in a row). Each drift gets diagnosed once, in the rehearsal room, by whichever puppeteer notices it. Six months later the same drift recurs and is rediscovered from scratch.

**Problem 2 — the dramaturg / rigger / puppeteer review loop is informal.** When something goes wrong in a performance, the post-show conversation usually surfaces multiple candidate causes (mechanism fatigue, manipulator timing, lighting cue, costume snag) and lands on whichever one the most senior person finds most plausible — the well-known "highest paid person's opinion" anti-pattern. SOC teams confronted the same problem in security operations a decade ago and solved it with formal detection-engineering peer review (red / blue / purple roles, written dispositions). This workspace transplants that practice.

The technique is **using peer review workflows** because that is what turns a private intuition ("I think the left arm slipped on cue 12") into shared, testable, replayable institutional knowledge ("rule `bunraku-hidari-lag-on-rapid-cross.yml` fired three times across the last four shows; review disposition: tune threshold from 80ms to 100ms").

## Getting Started

### Prerequisites

- A company or project working with puppets, marionettes, bunraku, shadow puppets, foam-latex characters, animatronics, or stop-motion figures.
- Some way of capturing motion data — at minimum, video from two angles. Optional: motion-capture suit data, IMU sensors on rigging, servo telemetry from animatronics, force-sensitive resistors on string anchors.
- A rehearsal cadence that supports a 10–20 minute post-rehearsal log + review pass.
- A peer-review roster — at minimum two reviewers with distinct perspectives (e.g. puppeteer + rigger; or omozukai + dramaturg; or builder + director).
- `python3` and `git` for the rule format and version control. No other external dependencies are required.

### Quick Start

1. Run `/onboard` to populate `context/project.md`, `context/role.md`, and `context/constraints.md` with your puppet inventory, performance context, instrumentation level, and review roster.
2. After your next rehearsal, run `/movement-log` and walk through the prompts — it will produce a timestamped event log in `work-log/<date>.md`.
3. Run `/detect-anomaly` against that log to see what the current (initially empty) rule set surfaces.
4. When you notice a recurring pattern across two or more logs, run `/rule-author` to draft a Sigma-style YAML rule.
5. Run `/peer-review` on the rule. Two reviewers minimum, distinct roles, written dispositions. Only after disposition `accepted` does the rule move from `outputs/rules/draft/` to `outputs/rules/active/`.
6. After every show, run `/post-show-report` to produce an incident-shaped writeup.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/onboard` | Initialize workspace context, puppet inventory, review roster | First time setup |
| `/movement-log` | Capture a rehearsal as a timestamped event log | After every rehearsal or performance |
| `/detect-anomaly` | Replay a log against the active rule set | Right after `/movement-log`, and after any rule change (regression-test) |
| `/rule-author` | Draft a Sigma-style movement-detection rule | When a pattern appears in two or more logs |
| `/peer-review` | Run a structured red / blue / purple review pass | Before any rule moves to the active set; after every post-show report |
| `/laban-tag` | Annotate a movement segment with Laban (Body / Effort / Shape / Space) | When a detection needs Effort-quality data, not just kinematic data |
| `/calibration-audit` | Audit puppet calibration state (string lengths, hinge friction, servo offsets) | Before opening night, after travel, before re-mounts |
| `/post-show-report` | Produce a structured incident-shape report for a performance | After every public performance |

## Directory Structure

```
puppetry-movement-mechanics/
├── CLAUDE.md                                # Agent role and foundational instructions
├── README.md                                # This file
├── CREATION_REPORT.md                       # Workspace creation rationale
├── context/
│   ├── project.md                           # Your puppets, productions, peer-review roster
│   ├── role.md                              # Your role (puppeteer / rigger / dramaturg / director)
│   ├── constraints.md                       # Artistic / safety / IP constraints
│   └── for-agent/
│       ├── domain-knowledge.md              # Puppetry traditions, motion physics, detection engineering, Laban Movement Analysis
│       ├── workflows.md                     # The four core workflows: log, detect, review, ship
│       ├── environment.md                   # Stage / studio instrumentation level
│       └── tools.md                         # Tool integrations (video, IMU, servo telemetry, git)
├── .claude/commands/
│   ├── onboard.md                           # Workspace initialization
│   ├── movement-log.md                      # Rehearsal-to-log capture
│   ├── detect-anomaly.md                    # Rule-set replay against a log
│   ├── rule-author.md                       # Sigma-style rule drafting
│   ├── peer-review.md                       # Red / blue / purple review pass
│   ├── laban-tag.md                         # Laban Movement Analysis annotation
│   ├── calibration-audit.md                 # Pre-show / post-travel calibration scan
│   └── post-show-report.md                  # Performance incident-shape report
├── prompts/
│   ├── bunraku-three-actor-sync-review.md   # Peer-review prompt for bunraku triple-actor coordination
│   ├── marionette-string-drift-investigation.md  # Tour-long control-bar drift investigation
│   └── puppet-handoff-rehearsal-postmortem.md    # Postmortem template after a handoff fumble
├── resources/
│   ├── lma-effort-graphs.md                 # Laban effort qualities reference (Weight / Time / Space / Flow)
│   ├── puppet-mechanism-failure-modes.md    # Puppetry-ATT&CK: tactic × technique taxonomy
│   ├── sigma-rule-template-puppetry.md      # Adapted Sigma rule YAML schema for movement detections
│   └── peer-review-disposition-language.md  # Recommended disposition vocabulary (accepted / tune / reject / escalate)
├── planning/                                # Active plans (rule-set roadmap, instrumentation upgrades)
├── outputs/
│   ├── rules/draft/                         # Drafted rules awaiting peer review
│   ├── rules/active/                        # Peer-reviewed, accepted rules — the live rule set
│   ├── reviews/                             # Peer-review pass records (one file per pass)
│   └── reports/                             # Post-show reports
├── user-docs/
│   ├── getting-started.md                   # Quick start guide
│   └── report.md                            # User-facing summary report template
└── work-log/
    └── session-log.md                       # Session logging template
```

## The Detection-Engineering / Puppetry Mapping

| SOC concept | Puppetry analogue |
|---|---|
| Endpoint telemetry (process, file, network events) | Joint-angle events, string-tension samples, manipulator inputs, audience-side observations |
| MITRE ATT&CK matrix | `resources/puppet-mechanism-failure-modes.md` — tactic (e.g. *string-system drift*) × technique (e.g. *gradual-stretch on shoulder support*) |
| Sigma rule | YAML rule in `outputs/rules/active/` describing a logsource pattern that fires on a specific failure mode |
| Detection-as-code peer review (Splunk, Elastic, Panther workflows) | `/peer-review` with red / blue / purple roles, written dispositions |
| Backtest a tuned rule against historical events | `/detect-anomaly` against past `work-log/` files |
| Postmortem after an incident | `/post-show-report` after a performance |

The mapping is not metaphorical — the data shapes match. A puppet's joint-angle stream over time is the same shape as a stream of `process_started` events, and the same anomaly-detection primitives (threshold, sequence, frequency, absence) work on both.

## Example Use Cases

### A touring marionette company tracks string drift across a six-month tour
The company runs `/calibration-audit` at every venue, `/movement-log` after every rehearsal, and `/post-show-report` after every show. By month three, the active rule set catches "right-shoulder support drifted past tuning band" before the rigger has to feel for it on the airplane control. By month six, the rule set has been peer-reviewed dozens of times and is the company's default starter set for the next tour.

### A bunraku studio formalizes the triple-actor handoff training
The studio captures rehearsals where a junior `hidarizukai` (left-arm puppeteer) is training under a senior `omozukai` (head + right-arm puppeteer). `/laban-tag` annotates the Effort qualities of each cross-stage move; `/detect-anomaly` flags timing slips beyond a threshold the senior puppeteer set and peer-reviewed; the junior reviews their own logs as part of training.

### An animatronics shop maintains a fleet of theme-park figures
Each figure has a `calibration-audit` baseline. Servo telemetry feeds into `movement-log` automatically. Rules in `outputs/rules/active/` catch creep on specific axes. The shop's two senior builders do a weekly `/peer-review` pass on rules drafted by the rest of the team. The MITRE-shaped failure-mode catalog powers monthly trend reports to maintenance management.

### A shadow-puppet (wayang kulit) ensemble investigates screen-distance drift
The dalang (puppeteer/narrator) suspects a particular character's silhouette has been "going soft" — losing screen contrast. A `/movement-log` of three performances plus video review flags that the screen-puppet distance varies by 4–7 cm during certain scene transitions. A peer-reviewed rule now catches this against future logs.

### A stop-motion studio backtests a new arc-of-motion rule against a year of dailies
The animator drafts a rule for "elbow arc tightness on a follow-through" using Disney's twelve-principles vocabulary. `/peer-review` with a co-animator and the supervising animator. `/detect-anomaly` then runs the rule against the past year's daily-shot logs to backtest false-positive rate before it lands in `outputs/rules/active/`.

## Recommended MCP Servers

- **filesystem** — Read/write rehearsal logs, draft rules, review records.
- **shell** — Optional: run `git log`/`git diff` to audit rule history; invoke ffmpeg or similar for video timestamp extraction.
- **python** — Optional: run small DSP scripts (joint-angle smoothing, IMU integration, simple FFT for tremor detection).

## Legal & Ethical Considerations

- **Consent and likeness.** Rehearsal logs may capture performers' bodies and voices. Confirm consent before storing video or audio. Logs themselves (timestamps + numbers) typically do not raise consent issues; raw video does.
- **Tradition stewardship.** Bunraku, wayang kulit, traditional Czech / Sicilian / Indonesian / Indian puppetry forms each carry living lineages. Failure-mode taxonomies authored for these forms should be reviewed by tradition-bearers, not only by detection engineers. Treat the failure-mode catalog as collaborative cultural property.
- **Safety.** Detection rules are diagnostic, not authoritative. A rigger's body sense and on-the-ground judgment always overrides a rule's silence. Never gate a safety call on the absence of a rule firing.
- **Open-format rules.** The Sigma-style YAML rules are intentionally portable — sharable across companies under whatever license the company chooses. Detection-engineering culture in cybersecurity has been strengthened by open rule-sharing (the Sigma project, Elastic detection-rules repo); the same is likely true for puppetry.

## Technical References

- Bell, John — *American Puppet Modernism: Essays on the Material World in Performance* (Palgrave Macmillan, 2008).
- Blumenthal, Eileen — *Puppetry: A World History* (Harry N. Abrams, 2005).
- Laban, Rudolf — *The Mastery of Movement* (4th edition, Lisa Ullmann, 1980). The canonical reference for Laban Movement Analysis (Body / Effort / Shape / Space).
- Adachi, Barbara — *The Voices and Hands of Bunraku* (Kodansha, 1978). Reference for the omozukai / hidarizukai / ashizukai triple-actor system.
- Thomas, Frank and Ollie Johnston — *The Illusion of Life: Disney Animation* (Hyperion, 1981). The twelve principles of animation; directly applicable to stop-motion and animatronic timing.
- Henson, Jim — Workshop notebooks and the [Jim Henson's Creature Shop archives](https://www.henson.com/creatureshop) for foam-latex and rod-puppet mechanism design.
- [MITRE ATT&CK](https://attack.mitre.org/) — tactic × technique matrix shape, adapted into `resources/puppet-mechanism-failure-modes.md`.
- [Sigma project](https://github.com/SigmaHQ/sigma) — open generic detection rule format; the YAML schema in `resources/sigma-rule-template-puppetry.md` is adapted from Sigma.
- [Elastic detection-rules](https://github.com/elastic/detection-rules) — exemplar of detection-as-code peer-review workflow (PR-based review, written dispositions, regression backtests). The `/peer-review` command structure mirrors this.
- Chuvakin, Anton — *Detection Engineering Maturity Model* (multiple posts, 2022–2024). The maturity model informs the workspace's rule lifecycle (draft → reviewed → active → tuned → retired).
- Daw-Ming Lee — *Indonesian Wayang Kulit Performance Practice* (various ethnographic sources). Reference for shadow-puppet screen-distance dynamics.
