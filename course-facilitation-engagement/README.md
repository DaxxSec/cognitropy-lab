# Course Facilitation Engagement Workspace

> An agent workspace for designing and running the multi-stakeholder communication system that keeps a live cohort course engaged — from pre-launch through certification — using parameterized message templates aligned to engagement-science frameworks.

## What This Workspace Does

This workspace turns "facilitator scrambling to write the next email" into a structured cadence. Rather than ad-hoc messaging, it codifies a stakeholder-by-phase template library and an engagement-trigger system that fires the right message to the right audience at the right moment.

The agent guides you through the full delivery loop:
1. Profile your cohort, modalities, and the stakeholders who need to stay informed
2. Build a Power–Interest map and RACI for the delivery
3. Design the pre/during/post communication cadence and assign templates
4. Watch engagement signals (attendance, submission, forum, pulse) and fire the right escalation
5. Generate stakeholder-specific recaps after every module
6. Close the loop with a Kirkpatrick-aligned sponsor readout

The technique that ties it together — **stakeholder communication templates** — is what makes this scalable across cohorts: the same parameterized template renders for any organization, any cohort name, any module title.

## Why This Workspace Exists

Course delivery is where most learning programs lose their ROI. Curriculum is solid, the facilitator knows the material, but mid-cohort the cadence falls off — managers stop reinforcing, sponsors drift, learners drop, and the post-course readout reads like a postmortem. The fix is not "more discipline"; it is a pre-built communication system with explicit triggers.

This workspace codifies that system. It pairs the engagement frameworks that actually predict completion (Community of Inquiry, Self-Determination Theory, the Five Moments of Need) with a usable template library that L&D teams can run from day one.

## Getting Started

### Prerequisites
- A live or upcoming cohort course (instructor-led, blended, or fully virtual)
- Access to your delivery channels (LMS, email, Slack/Teams, calendar)
- A stakeholder list — at minimum: facilitator, learners, learners' line managers, an executive sponsor, and L&D admin
- Optional: engagement analytics from the LMS (login, submission, forum, video-watch data)
- A baseline reading level and brand-voice expectation for the organization

### Quick Start
1. Clone or instantiate this workspace
2. Run `/onboard` to capture the course profile, cohort, modalities, and stakeholder roster
3. Run `/map-stakeholders` to produce the Power–Interest matrix and RACI
4. Run `/draft-cadence` to generate the full pre/during/post communication calendar in `planning/plan.md`
5. Render the kickoff pack from `prompts/cohort-kickoff-pack.md`
6. After each module, run `/recap-module`
7. At the midpoint, run `/pulse-check`
8. Whenever a learner signal trips a threshold, run `/at-risk-outreach`
9. At the cohort close, run `/sponsor-readout`

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/onboard` | Capture course profile, cohort, stakeholders, channels, calendar | First time setup |
| `/map-stakeholders` | Build Power–Interest map, salience model, and a RACI per phase | After onboarding, before drafting any messages |
| `/draft-cadence` | Generate the full pre/during/post communication calendar with template IDs | After the stakeholder map is approved |
| `/recap-module` | Build a four-audience recap pack (learner, manager, facilitator, sponsor) | Within 24 hours of every module's close |
| `/pulse-check` | Run a mid-course pulse and produce stakeholder-specific summaries | At the cohort midpoint, or when engagement signals dip |
| `/at-risk-outreach` | Convert an engagement signal into a graduated outreach chain | A learner trips a threshold (no login 7 days, missed assignment, low pulse score) |
| `/sponsor-readout` | Generate a Kirkpatrick-aligned executive readout | Cohort close, or quarterly for ongoing programs |

## Directory Structure

```
course-facilitation-engagement/
├── CLAUDE.md                                   # Agent role and instructions
├── README.md                                   # This file
├── CREATION_REPORT.md                          # Workspace creation details
├── context/
│   ├── project.md                              # Course profile (populated by /onboard)
│   ├── role.md                                 # Your facilitator/L&D role
│   ├── constraints.md                          # Brand voice, compliance, accessibility limits
│   └── for-agent/
│       ├── domain-knowledge.md                 # Engagement theory, stakeholder taxonomy, template grammar
│       ├── workflows.md                        # 4 core workflows with decision trees
│       ├── environment.md                      # LMS, email, messaging, calendar setup
│       └── tools.md                            # Channel and integration cheatsheets
├── .claude/commands/
│   ├── onboard.md                              # Initialization interview
│   ├── map-stakeholders.md                     # Power–Interest, salience, RACI
│   ├── draft-cadence.md                        # Pre/during/post calendar generator
│   ├── recap-module.md                         # Multi-audience module recap
│   ├── pulse-check.md                          # Pulse design + summary
│   ├── at-risk-outreach.md                     # Triggered escalation chain
│   └── sponsor-readout.md                      # Kirkpatrick-aligned exec readout
├── prompts/
│   ├── cohort-kickoff-pack.md                  # Pre-launch full-stakeholder pack
│   ├── silent-cohort-revival.md                # Whole-cohort disengagement intervention
│   └── exec-sponsor-quarterly-readout.md       # Ongoing-program sponsor cadence
├── resources/
│   ├── stakeholder-template-library.md         # Parameterized template inventory (≈40 templates)
│   ├── engagement-frameworks-reference.md      # CoI, SDT, Kirkpatrick, Five Moments, UDL, salience
│   └── engagement-metrics-reference.md         # Signals, thresholds, source mapping
├── planning/                                   # plan.md = the live cadence calendar
├── outputs/                                    # Rendered messages, recap packs, readouts
├── user-docs/                                  # Facilitator-facing reference docs
│   ├── getting-started.md                      # Quick start
│   └── report.md                               # Cohort-close report template
└── work-log/                                   # Daily logs of triggered communications
    └── session-log.md                          # Session logging template
```

## The Stakeholder Template Grammar

Every template in `resources/stakeholder-template-library.md` is identified by a four-part code:

```
<phase>-<stakeholder>-<intent>-<channel>

phase:        pre | during | post | trigger
stakeholder:  learner | manager | sponsor | facilitator | admin | smex | alumni
intent:       inform | invite | nudge | remind | recap | escalate | celebrate | reflect
channel:      email | slack | lms | sms | calendar | loom
```

Examples:
- `pre-learner-invite-email` — kickoff invitation (T-14)
- `during-manager-nudge-email` — module-3 manager reinforcement nudge
- `trigger-learner-remind-sms` — assignment-deadline-minus-24h SMS
- `post-sponsor-recap-email` — cohort-close executive summary

Templates carry the same variable set across stakeholders so a single onboarding fact (`{{cohort_name}}`) renders consistently in 40+ places. A new course launches by setting variables once, not by rewriting prose.

## Engagement Frameworks That Drive the System

Every template ties to at least one of these frameworks (full reference in `resources/engagement-frameworks-reference.md`):

### 1. Community of Inquiry (Garrison, Anderson & Archer)
Three presences must be sustained for cohort engagement: **cognitive presence** (sense-making), **social presence** (belonging), **teaching presence** (direction). Templates are tagged so the cadence balances all three.

### 2. Self-Determination Theory (Deci & Ryan)
Sustainable engagement comes from supporting **autonomy**, **competence**, and **relatedness**. Templates are designed to reinforce — never erode — those three drivers.

### 3. Kirkpatrick's Four Levels
Reaction, Learning, Behavior, Results. The cadence and the sponsor readout move sponsor attention up the levels rather than stalling at smile-sheet reactions.

### 4. Five Moments of Need (Mosher & Gottfredson)
New, More, Apply, Solve, Change. Triggered messaging targets the moment the learner is actually in.

### 5. Power–Interest Matrix and Stakeholder Salience
Mendelow's matrix and Mitchell-Agle-Wood's power/legitimacy/urgency model decide who gets which cadence at what depth.

### 6. Universal Design for Learning (UDL)
Multiple means of representation, action/expression, and engagement — built into channel selection and copy variants.

## Example Use Cases

### Six-week leadership cohort, 30 learners, three-tier corporate sponsor
Run `/onboard`, then `/map-stakeholders` to produce a 12-stakeholder register. `/draft-cadence` produces a 38-touch calendar across email, Slack, and LMS. After Module 3, a learner missed two submissions — `/at-risk-outreach` produces the three-message escalation. `/sponsor-readout` at week 7 produces a Level-3 (Behavior) commitment dashboard, not a satisfaction sheet.

### Quarterly compliance refresher, 1,200 learners, manager-driven reinforcement
The cohort is too large for individual outreach, so the cadence pivots to manager-led reinforcement. `/draft-cadence` produces manager-targeted nudges that learners never see directly; pulse-check is short and stratified by business unit.

### Bootcamp-style cohort, public-pay, alumni network
Sponsors are the learners themselves (self-paid). The sponsor lane folds into the alumni lane post-completion. `/sponsor-readout` becomes an alumni-focused outcomes piece, useful for marketing and for next-cohort recruitment.

### Highly regulated industry (financial services / pharma)
`context/constraints.md` carries compliance review SLAs and approved-language lists. Every template is tagged with a compliance owner and a review-window. The cadence calendar has explicit "freeze windows" before regulator filings.

### Asynchronous self-paced course with cohort sprints
The "live" engagement is the sprint, not the entire program. `/recap-module` produces a sprint-close recap rather than a module-close recap, and `/pulse-check` runs on sprint cadence rather than calendar cadence.

## Recommended MCP Servers

- **filesystem** — Read/write rendered templates and the planning calendar
- **gmail / outlook / smtp** — Send rendered email templates (the agent drafts, the user reviews and sends)
- **slack / teams** — Post channel announcements and DM nudges
- **lms (canvas / moodle / cornerstone / docebo)** — Pull engagement signals, post announcements
- **calendar (google / microsoft)** — Create rich-description session invites
- **sheet / table** — Maintain the cohort register and engagement scorecard

## Legal & Ethical Considerations

- **Privacy.** Engagement signals are personal data. Surface only the signals required for the decision in front of you. Never share an individual learner's behavioral trace with their line manager without prior consent disclosed at enrollment.
- **Accessibility.** All learner-facing copy must meet WCAG 2.1 AA on color contrast, screen-reader markup, and provide captions/transcripts for any embedded video. Templates fail review if they fail UDL checks.
- **Plain language.** Default to a Grade 8 reading level on learner-facing copy. Use `resources/engagement-frameworks-reference.md`'s plain-language checklist before any send.
- **Inclusive framing.** Use stakeholder-neutral terminology; avoid implying assumptions about manager support or English fluency. Provide opt-out lanes for nudges.
- **Manager pressure.** Manager-targeted templates support, never coerce. Avoid framing that turns a manager nudge into a performance write-up.
- **Compliance alignment.** In regulated industries, a workspace template is a draft until the named compliance reviewer approves the sent version.

## Technical References

- [Community of Inquiry framework (coi.athabascau.ca)](https://coi.athabascau.ca/)
- [Self-Determination Theory (selfdeterminationtheory.org)](https://selfdeterminationtheory.org/)
- [Kirkpatrick Partners — The New World Model](https://www.kirkpatrickpartners.com/the-kirkpatrick-model/)
- [The Five Moments of Need — Mosher & Gottfredson](https://www.5momentsofneed.com/)
- [CAST — Universal Design for Learning Guidelines](https://udlguidelines.cast.org/)
- [Federal Plain Language Guidelines (plainlanguage.gov)](https://www.plainlanguage.gov/guidelines/)
- [WCAG 2.1 — Web Content Accessibility Guidelines](https://www.w3.org/TR/WCAG21/)
- [Mitchell, Agle & Wood — Stakeholder Salience (1997)](https://www.jstor.org/stable/259247)
- [ATD State of the Industry reports](https://www.td.org/research-reports)
