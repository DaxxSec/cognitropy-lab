# Domain Knowledge — Course Facilitation Engagement

This file is the agent's working theory of engagement. Anything you draft draws from it: a template's purpose, a cadence's rationale, a sponsor readout's framing.

## What "Engagement" Actually Means in a Cohort

Engagement is observable behavior **plus** interior motivation. Behavior alone (login counts, video completes) is leading indicator and easy to game; motivation alone is invisible. The strongest signal is the convergence of the two.

We use a four-layer model when reading or writing about a learner state:

| Layer | What It Is | How It Surfaces |
|------:|-----------|-----------------|
| 1. Logistical | Did the learner show up at all? | Attendance, login frequency, asset opens |
| 2. Behavioral | Did they take the requested action? | Submission rate, forum posts, peer-review completion |
| 3. Cognitive | Did they actually grapple with the material? | Question quality, reflection depth, applied artifact quality |
| 4. Affective | Do they feel connected and supported? | Pulse-survey sentiment, free-text reflection, peer mentions |

A template that only fixes Layer 1 (a reminder) will not move Layer 4 (belonging). Match the template to the layer that is actually slipping.

## Stakeholder Taxonomy

A "course" has more participants than just the people in the seats. The default register for a corporate cohort:

| ID | Stakeholder | Primary Interest | Power Over Course | Salience Default |
|----|-------------|------------------|-------------------|------------------|
| LRN | Learner | Skill development, certification, time well spent | Low (individual), High (collective) | Definitive |
| MGR | Line manager | Team capability, ROI on time off the floor | Medium | Dominant |
| SPN | Executive sponsor | Strategic capability building, business outcome | High | Definitive |
| FAC | Facilitator | Effective delivery, professional reputation | Medium-High | Dominant |
| PRO | Producer / TA | Smooth operations, learner support | Low | Discretionary |
| ADM | L&D admin | Logistics, completion records, compliance evidence | Medium | Dependent |
| SME | Subject-matter expert / guest | Content fidelity, professional reputation | Medium | Discretionary |
| MTR | Mentor / coach | Learner growth in their charge | Low | Dependent |
| ALM | Alumni | Network identity, ongoing development | Low (individual), Medium (collective) | Discretionary |
| CMP | Compliance / risk | Regulatory exposure, evidence trail | High in regulated contexts | Definitive in scope |
| ACC | Accessibility / DEI | Equitable access, inclusion outcomes | Medium | Dominant |
| ITP | IT / platform support | Tooling reliability | Medium during incidents | Dependent |

"Salience Default" follows Mitchell-Agle-Wood (1997): combinations of power, legitimacy, and urgency. Definitive = all three; Dominant = power + legitimacy; Dependent = legitimacy + urgency; Discretionary = legitimacy only. Triage cadence depth and approval flow against salience, not just role title.

## Communication Phases

A cohort has a predictable rhythm. Templates and triggers are organized along it.

### Phase 1 — Pre-launch (T–30 to T–1)
Goal: secure attention, surface logistics, set expectations across all stakeholder lanes before kickoff.

| T- | Stakeholder | Intent | Example template |
|----|-------------|--------|------------------|
| T-30 | Sponsor | Inform | Confirm scope, dates, attendees, what they will receive |
| T-21 | Learner | Invite | Save-the-date with course pitch and goals |
| T-21 | Manager | Inform | Heads-up: your team member is enrolled, here's what to expect |
| T-14 | Learner | Invite (formal) | Calendar invite + pre-work + welcome video |
| T-14 | Manager | Nudge | Suggested 1:1 prompts to brief their report on goals |
| T-7  | Learner | Remind | Pre-work due, joining details, prep checklist |
| T-3  | Admin | Inform | Final cohort manifest + access provisioning |
| T-1  | Learner | Remind | Tomorrow's joining details, time zone, what to bring |
| T-1  | Facilitator | Inform | Cohort dossier: learners, roles, accessibility notes |

### Phase 2 — During (D0 → D-end)
Goal: maintain Community of Inquiry presence balance; reinforce manager/sponsor; respond to triggers.

Cadence per module (a module spans the time between two synchronous sessions):
- **Module preview** (T-2 of session): learner — preview the topic, frame the question
- **Live session** (T0): facilitator + producer running, calendar already in flight
- **Module recap** (T+1): four-audience pack (learner, manager, facilitator log, sponsor highlight if Definitive)
- **Mid-module nudge** (T+3): learner — peer-prompt, optional office hours
- **Manager reinforcement nudge** (T+4 to T+5): manager — 1:1 prompts that map to module objectives
- **Continuous**: triggered messages whenever a signal trips (see "Engagement Signals" below)

### Phase 3 — Midpoint pulse
Goal: surface signal early enough to act on it before the back half of the cohort.

- Pulse to learners (5–7 questions max)
- Aggregate summary back to learners (closing the feedback loop is itself an engagement driver — Ledermann's reciprocity effect)
- Stakeholder-specific summary to facilitator, sponsor, admin
- Course-correction memo if any signal is below threshold

### Phase 4 — Post-cohort (D+0 to D+30)
Goal: cement transfer to the workplace and close the Kirkpatrick loop with the sponsor.

| D+ | Stakeholder | Intent |
|----|-------------|--------|
| D+0 | Learner | Celebrate (certification, peer recognition) |
| D+0 | Sponsor | Recap (Level 1 + Level 2 outcomes) |
| D+1 | Learner | Reflect (commitments, application plan) |
| D+7 | Manager | Nudge (3-question check-in: what was tried, what blocked, what they want to recognize) |
| D+14 | Learner | Apply (peer-share success-story prompt) |
| D+30 | Sponsor | Readout (Level 3 behavior signals, qualitative artifacts) |
| D+30 | Alumni | Invite (cohort alumni community) |

### Phase 5 — Long-term reinforcement (D+60 to D+180+)
Goal: sustain behavior change and feed the next cohort with alumni evidence.

- D+60 reinforcement micro-module
- D+90 manager ROI check-in
- D+180 alumni success-story collection (feeds next cohort's marketing and the program's L4 evidence)

## Template Grammar

Every template has the same shape — header metadata, body, parameters, framework tags. The parameter set is the key to scaling: a template author writes once, the agent renders for any cohort.

### Header
```
ID: <phase>-<stakeholder>-<intent>-<channel>
Stakeholder: <STAKEHOLDER>
Phase: <pre|during|post|trigger>
Intent: <inform|invite|nudge|remind|recap|escalate|celebrate|reflect>
Channel: <email|slack|lms|sms|calendar|loom>
CoI presence: <cognitive|social|teaching|mixed>
SDT driver: <autonomy|competence|relatedness|mixed>
Five-Moments-of-Need: <new|more|apply|solve|change|n/a>
Reading-level target: <grade>
Approver: <role>
Time-of-send: <relative — e.g., T-7 09:00 learner local>
```

### Body Conventions
- **Subject / opener** — concrete and outcome-focused; never "Quick update"
- **What changed / what's coming** — one paragraph
- **What we ask of you** — one sentence with one verb
- **How to engage** — one or two specific links/actions
- **Where to get help** — name the human or channel; "support@" without a name is not enough
- **Sign-off** — facilitator name + role + cohort ID

### Standard Variable Set
```
{{org_name}}             {{course_name}}            {{cohort_name}}
{{cohort_start_date}}    {{cohort_end_date}}        {{cohort_id}}
{{learner_first_name}}   {{learner_full_name}}      {{learner_email}}
{{manager_first_name}}   {{manager_full_name}}      {{manager_email}}
{{sponsor_name}}         {{sponsor_title}}          {{sponsor_email}}
{{facilitator_name}}     {{facilitator_email}}      {{producer_name}}
{{module_n}}             {{module_title}}           {{module_objectives}}
{{module_session_date}}  {{module_session_time}}    {{learner_time_zone}}
{{join_url}}             {{prework_url}}            {{recap_url}}
{{certificate_url}}      {{help_channel}}           {{office_hours_url}}
{{deadline_iso}}         {{at_risk_threshold}}      {{pulse_score}}
{{completion_pct}}       {{l3_behavior_metric}}     {{l4_business_metric}}
```

Use ISO-8601 for dates and explicit time zone names (e.g., `Europe/Dublin`) — never "next Tuesday" without a date.

### Authoring Rules
1. **One ask per message.** If you have three asks, send three messages or build a checklist asset and link to it.
2. **Lead with the why.** Adult learners (Knowles) need the relevance up front, not after a generic salutation.
3. **Concrete next step in the first 200 characters.** Mobile inbox preview length.
4. **Time-bound the ask.** "By Thursday 17:00 Europe/Dublin" beats "soon".
5. **Provide a graceful exit.** Every nudge offers a "not relevant for me right now — here's how to opt out of this nudge sequence" line.
6. **Reciprocate.** When you ask for a pulse response, commit to share back the aggregate within the next module.

## Engagement Signals and Their Sources

The agent watches a small, well-defined set of signals. Each has a source, a polling cadence, and a default threshold.

| Signal | Source | Cadence | Default trigger threshold |
|-------|--------|---------|---------------------------|
| Login frequency | LMS analytics | Daily | No login > 7 days during active phase |
| Asset open rate | LMS / video host | Per module | <60% of cohort opened the recap asset within 72h |
| Assignment submission | LMS | Per assignment | Individual missed at deadline OR cohort <80% on time |
| Forum participation | LMS / community platform | Weekly | Individual zero posts in two consecutive weeks |
| Live session attendance | Conferencing platform | Per session | <70% of cohort attended OR individual missed two in a row |
| Pulse score | Survey tool | Pulse week | Cohort mean <3.5/5 OR individual <3 with low text engagement |
| Help-channel volume | Slack/Teams | Daily | Spike >2x baseline (often a content issue, not a learner issue) |

Signals route to triggered templates via `/at-risk-outreach`. The escalation chain is always:
1. Learner (lightest, supportive, autonomy-preserving)
2. Cohort-level pattern message if the signal is collective
3. Manager (only after Step 1 has had time to land — typical 72h)
4. Sponsor (only on persistent risk to a Definitive outcome — never the first move)

## Frameworks Crib Sheet

Detailed in `resources/engagement-frameworks-reference.md`; here is the operational gloss.

### Community of Inquiry (CoI)
A cadence balanced across **cognitive presence** (questions, reflection prompts, applied tasks), **social presence** (peer prompts, photo/avatar use, named mentions), and **teaching presence** (objectives, scaffolding, direct instruction) maintains engagement. If a week is all teaching presence, learners drift; if all social, the cohort feels purposeless.

### Self-Determination Theory (SDT)
Reinforce **autonomy** (offer choice in how to apply), **competence** (timely, specific feedback), **relatedness** (peer threading and named recognition). A nudge that strips autonomy ("you must do this by Tuesday or you're out") backfires; a nudge that offers it ("Most cohort-mates are starting Tuesday — what works for you?") sustains.

### Kirkpatrick's New World Model
Four levels: Reaction → Learning → Behavior → Results. A sponsor readout that reports only Level 1 (smile sheet) signals a weak program. Build the cadence so Levels 3 and 4 are observable artifacts (manager check-ins, application plans, business-metric movement) by D+30.

### Five Moments of Need (Mosher & Gottfredson)
**New** (first encounter), **More** (deepening), **Apply** (in workflow), **Solve** (when something breaks), **Change** (when context shifts). Triggered messages should target the moment the learner is in, not the moment the calendar says.

### Power–Interest matrix (Mendelow)
Manage closely / Keep satisfied / Keep informed / Monitor. Cadence depth follows the matrix: do not over-update a low-power, low-interest stakeholder; do not under-update a high-power one.

### Stakeholder Salience (Mitchell-Agle-Wood)
Power × Legitimacy × Urgency. Salience can shift mid-cohort (a Discretionary alumni group becomes Definitive when their success-story is needed for the sponsor readout). Re-rank on each phase boundary.

### UDL — Universal Design for Learning
Provide multiple means of **representation** (text, audio, visual), **action and expression** (write, record, build), and **engagement** (choice, relevance, challenge). Channel mix should reflect this, not default to email-only.

### Knowles' andragogy
Adults learn best when: they know the why, can leverage their experience, are problem-centered, and can apply immediately. Every learner-facing template should pass an "adult-respecting" check.

### Plain-language guidelines (plainlanguage.gov)
Active voice, short sentences, common words, "you" and "we", explicit calls to action, clear navigation. Run every send through the plain-language checklist in `resources/engagement-frameworks-reference.md`.

## Common Failure Modes (and the Right Template Response)

| Failure mode | Wrong response | Right response |
|--------------|---------------|----------------|
| Learner missed kickoff | Mark absent, defer | `trigger-learner-nudge-email` + warm reschedule offer; CC manager only if learner opts in |
| Cohort-wide silence after Module 2 | Add another reminder | Run `silent-cohort-revival.md` — pulse + format change + facilitator self-disclosure |
| Sponsor goes quiet | Send the same monthly update | Re-rank salience; deliver `during-sponsor-recap-email` with a Level-3 signal, not Level-1 |
| Manager forwards nudge as a write-up | Stop CC'ing the manager | Replace coercive phrasing in template; add a manager FAQ asset |
| Pulse score drops mid-cohort | Defend the design | Run `/pulse-check` deep-dive; publish the change you will make in response within 48h |
| Accessibility complaint | One-off fix | Re-audit the template library against UDL; document the change; loop the ACC stakeholder into approval |

## What This Workspace Is Not

- **Not curriculum design.** Module objectives, assessment design, and content authoring are upstream.
- **Not marketing.** Pre-cohort recruitment is a separate funnel; this workspace begins at "the cohort is enrolled".
- **Not HR or performance management.** Engagement signals are not performance evidence; templates do not feed disciplinary systems.
- **Not a one-to-one chat assistant.** The agent drafts; the facilitator reviews and sends. Bulk auto-send breaks the trust model.
