# Stakeholder Template Library

Forty-plus parameterized message templates organized by `<phase>-<stakeholder>-<intent>-<channel>`. Each entry carries: ID, header metadata, body, framework anchors. The agent renders by substituting the variable set in `context/for-agent/domain-knowledge.md`.

> Variable convention: anything in `{{double_braces}}` is filled per render. Never leave braces in a sent message.

---

## Phase 1 — Pre-launch

### `pre-sponsor-inform-email`
- Stakeholder: SPN | Phase: pre | Intent: inform | Channel: email
- CoI: teaching | SDT: competence | Approver: sponsor-CoS | Send: T-30 09:00 sponsor TZ

> Subject: {{course_name}} — {{cohort_name}} kickoff on {{cohort_start_date}}
>
> {{sponsor_first_name}},
>
> Quick brief on {{cohort_name}}, which begins {{cohort_start_date}} and runs through {{cohort_end_date}}.
>
> What we're committing to:
> - {{n_learners}} learners across {{role_mix}}
> - {{n_modules}} modules over {{duration_weeks}} weeks
> - Engagement targets: {{completion_target}}% completion, pulse ≥ {{pulse_target}}, observable behavior change at D+30 on {{l3_metric}}
>
> What you will receive:
> - A recap pack after each module (≤200 words)
> - A midpoint pulse summary at week {{midpoint_week}}
> - A Kirkpatrick-aligned readout at D+30
>
> One ask: confirm by {{sponsor_response_deadline}} that the D+30 readout slot ({{readout_date}}) is on your calendar.
>
> {{facilitator_first_name}}

### `pre-learner-invite-email`
- Stakeholder: LRN | Phase: pre | Intent: invite | Channel: email
- CoI: social + teaching | SDT: relatedness + autonomy | Approver: facilitator | Send: T-21 mid-morning learner TZ

> Subject: You're in — {{course_name}} starts {{cohort_start_date}}
>
> Hi {{learner_first_name}},
>
> Welcome to {{cohort_name}}. Over {{duration_weeks}} weeks we'll work through {{n_modules}} modules with a small cohort of {{n_learners}} colleagues. The program goal: {{program_objective}}.
>
> What to expect:
> - Live sessions: {{session_cadence}}, {{session_length}} each
> - Asynchronous work: roughly {{async_hours}} per week
> - A peer cohort that will be your second source of insight (often more useful than mine)
>
> Your one action this week: open the prework — {{prework_url}} — and tell us in the welcome thread what you most want to leave with. We'll shape the first session around what we hear.
>
> If now is not the right time, reply and we'll move you to a later cohort — no fuss.
>
> Looking forward,
> {{facilitator_first_name}}, {{facilitator_role}}

### `pre-manager-inform-email`
- Stakeholder: MGR | Phase: pre | Intent: inform | Channel: email
- CoI: teaching | SDT: competence | Approver: facilitator | Send: T-21

> Subject: Heads-up: {{learner_first_name}} is joining {{course_name}}
>
> Hi {{manager_first_name}},
>
> {{learner_full_name}} is enrolled in {{course_name}}, running {{cohort_start_date}} → {{cohort_end_date}}. The program is {{one_sentence_program_summary}}.
>
> What this means for you:
> - {{learner_first_name}} will need ~{{weekly_hours}} per week, with {{session_count}} live sessions
> - You will get a short module-by-module nudge with 1:1 prompts you can use
> - You will get a D+30 manager check-in to capture what changed
>
> No action needed yet — the first nudge arrives at T-14 with prompts you can use to brief {{learner_first_name}} ahead of kickoff.
>
> {{facilitator_first_name}}

### `pre-manager-nudge-email`
- Stakeholder: MGR | Phase: pre | Intent: nudge | Channel: email
- CoI: teaching | SDT: relatedness | Approver: facilitator | Send: T-14

> Subject: Three prompts to brief {{learner_first_name}} for {{course_name}}
>
> Hi {{manager_first_name}},
>
> Kickoff is in two weeks. The single biggest predictor of cohort outcomes is a 15-minute manager 1:1 before the first session.
>
> Three prompts that work:
> 1. "What is one thing you want this course to change about how you work?"
> 2. "What is the experiment you'd like to try at week 3, and how can I support it?"
> 3. "What can I take off your plate during the {{duration_weeks}} weeks so you can show up for it?"
>
> No artifacts to read. Just the conversation.
>
> {{facilitator_first_name}}

### `pre-learner-invite-calendar`
- Stakeholder: LRN | Phase: pre | Intent: invite | Channel: calendar
- CoI: teaching | SDT: competence | Approver: facilitator | Send: T-14

> Title: {{course_name}} — {{module_n}} {{module_title}}
>
> Description:
> Welcome — this is the calendar invite for the {{module_n}} session of {{cohort_name}}.
>
> Joining: {{join_url}}
> Time zone shown: {{learner_time_zone}}
> Live captions: yes
> Recording: posted within 24h to {{lms_url}}
>
> Pre-work (≤30 min): {{prework_url}}
> Welcome video (3 min): {{welcome_loom_url}}
>
> If a conflict comes up, reply and we'll find a way.
>
> {{facilitator_first_name}}

### `pre-learner-remind-email`
- Stakeholder: LRN | Phase: pre | Intent: remind | Channel: email
- CoI: teaching | SDT: competence | Approver: facilitator | Send: T-7 and T-1

> Subject: One week to {{cohort_name}} — prep checklist
>
> {{learner_first_name}},
>
> Quick reminder: {{cohort_name}} begins {{cohort_start_date}} at {{module_session_time}} {{learner_time_zone}}.
>
> Three things to check before kickoff:
> - You can join {{join_url}} from your usual setup
> - You've skimmed the prework: {{prework_url}}
> - You're free for the {{session_length}} window without distractions
>
> Anything in the way? Reply directly — I read every one.
>
> {{facilitator_first_name}}

### `pre-admin-inform-email`
- Stakeholder: ADM | Phase: pre | Intent: inform | Channel: email
- CoI: teaching | SDT: competence | Approver: facilitator | Send: T-3

> Subject: Final manifest — {{cohort_name}} starts {{cohort_start_date}}
>
> {{admin_first_name}},
>
> Final cohort manifest for {{cohort_name}} attached. Please confirm by EOD {{admin_deadline}}:
> - LMS access provisioned for all {{n_learners}} learners
> - Calendar invites accepted by ≥{{accept_threshold}}%
> - Recording / captioning enabled on the conferencing platform
> - Help-channel and pulse instrument live
>
> Anything you need from me to close the gaps?
>
> {{facilitator_first_name}}

---

## Phase 2 — During (per module)

### `during-learner-invite-email`
- Stakeholder: LRN | Phase: during | Intent: invite | Channel: email
- CoI: cognitive | SDT: autonomy | Approver: facilitator | Send: T-2 of session

> Subject: {{module_n}} {{module_title}} — what we'll work on
>
> {{learner_first_name}},
>
> {{module_n}} is on {{module_session_date}} at {{module_session_time}} {{learner_time_zone}}.
>
> What we'll work on: {{module_focus_question}}.
>
> Two things to bring:
> - {{prework_artifact}}
> - One real situation from your work where {{module_topic}} would land
>
> If you can't make it live, the recording goes to {{lms_url}} within 24h. Forum thread: {{forum_url}}.
>
> {{facilitator_first_name}}

### `during-learner-recap-email`
- Stakeholder: LRN | Phase: during | Intent: recap | Channel: email + LMS
- CoI: cognitive + social | SDT: relatedness + autonomy | Approver: facilitator | Send: T+1

> Subject: {{module_n}} recap — and one thing to try this week
>
> {{learner_first_name}},
>
> Yesterday we worked on {{module_focus_question}}. Three points worth re-reading:
> 1. {{point_1}}
> 2. {{point_2}}
> 3. {{point_3}}
>
> Try this: {{application_prompt}} — five minutes, this week, not perfect.
>
> If you want a thinking partner, drop it in {{forum_url}} or join office hours: {{office_hours_url}}.
>
> {{facilitator_first_name}}
>
> P.S. If the cadence is too much right now, here's the lighter-touch lane: {{opt_in_lighter_url}}.

### `during-learner-nudge-slack`
- Stakeholder: LRN | Phase: during | Intent: nudge | Channel: slack
- CoI: social | SDT: relatedness | Approver: producer | Send: T+3

> {{learner_first_name}}, halfway between sessions — how is the application going? Drop a sentence here, even if it's "not yet". I'll match you with one cohort-mate working on the same thing.

### `during-manager-nudge-email`
- Stakeholder: MGR | Phase: during | Intent: nudge | Channel: email
- CoI: teaching | SDT: relatedness | Approver: facilitator | Send: T+1

> Subject: 1:1 prompts after {{module_n}} for {{learner_first_name}}
>
> Hi {{manager_first_name}},
>
> {{learner_first_name}} just finished {{module_n}} {{module_title}}. Two prompts that work this week:
> 1. {{prompt_1}}
> 2. {{prompt_2}}
>
> Listen for: {{listen_for}}.
>
> No reply needed. If you want the recap learners got, here it is: {{recap_url}}.
>
> {{facilitator_first_name}}

### `during-manager-reinforce-email`
- Stakeholder: MGR | Phase: during | Intent: reinforce | Channel: email
- CoI: teaching | SDT: competence | Approver: facilitator | Send: T+5

> Subject: A 5-minute reinforcement for {{learner_first_name}}
>
> Hi {{manager_first_name}},
>
> If the team has a stand-up or 1:1 this week, here's a 5-minute reinforcement: ask {{learner_first_name}} what they tried from {{module_title}}, and what got in the way. The trying matters more than the success.
>
> {{facilitator_first_name}}

### `during-facilitator-recap-internal`
- Stakeholder: FAC | Phase: during | Intent: recap | Channel: internal doc
- CoI: teaching | SDT: competence | Approver: facilitator (self) | Send: T+1

Internal log — never sent to learners or managers. Sections:
- Attendance, on-time, polls, forum thread count
- Engagement temperature 1–5
- What worked / what dragged
- Named at-risk learners + rationale
- Adjustments to next module
- Content escalations to curriculum owner

### `during-sponsor-recap-email`
- Stakeholder: SPN | Phase: during | Intent: recap | Channel: email
- CoI: teaching | SDT: competence | Approver: sponsor-CoS | Send: T+1, Definitive only

> Subject: {{cohort_name}} — module {{module_n}} highlight
>
> {{sponsor_first_name}},
>
> A short note from {{module_n}} {{module_title}}.
>
> What stood out: {{anonymized_story}}.
> Cohort signal: completion {{module_completion_pct}}%, pulse trend {{pulse_trend}}.
> What you can do this week: {{specific_amplification_ask}}.
>
> Full data when you want it: {{recap_url}}.
>
> {{facilitator_first_name}}

### `during-learner-pulse-email`
- Stakeholder: LRN | Phase: during | Intent: invite | Channel: email + LMS
- CoI: social + teaching | SDT: autonomy | Approver: facilitator | Send: midpoint

> Subject: 3-minute pulse — what should I change?
>
> {{learner_first_name}},
>
> We're at the cohort midpoint. Three minutes, anonymous, 5 questions:
>
> {{pulse_url}}
>
> What I commit to: I will publish what I'm changing in response within 5 working days, with names off and themes on.
>
> Deadline: {{pulse_deadline_iso}} {{learner_time_zone}}.
>
> {{facilitator_first_name}}

### `during-learner-pulse-recap-email`
- Stakeholder: LRN | Phase: during | Intent: recap | Channel: email + LMS
- CoI: social + teaching | SDT: relatedness | Approver: facilitator | Send: pulse + 5 working days

> Subject: What you said in the pulse — and what changes next
>
> {{learner_first_name}},
>
> Thank you. {{pulse_response_n}} of {{n_learners}} responded.
>
> The top theme: {{top_theme}}.
> Next two: {{theme_2}}, {{theme_3}}.
>
> What changes for the back half:
> - {{change_1}} — by {{date_1}}, owner {{owner_1}}
> - {{change_2}} — by {{date_2}}, owner {{owner_2}}
>
> What I'm not changing and why: {{not_changing}}.
>
> {{facilitator_first_name}}

---

## Phase 3 — Triggered Outreach

### `trigger-learner-nudge-email`
- Stakeholder: LRN | Phase: trigger | Intent: nudge | Channel: email
- CoI: social | SDT: autonomy | Approver: facilitator | Send: T+0 from signal

> Subject: A check-in — no pressure
>
> {{learner_first_name}},
>
> I noticed it's been a bit since the last log-in. No pressure, and no judgement — life happens.
>
> If you want to pick up: the next module's preview is here {{module_preview_url}}, and the recordings live at {{lms_url}}.
>
> If now is not the right time, reply with one word ("pause", "drop", "later") and I'll act on it. We can always restart in a future cohort.
>
> {{facilitator_first_name}}

### `trigger-learner-remind-sms`
- Stakeholder: LRN | Phase: trigger | Intent: remind | Channel: sms
- Approver: facilitator | Send: T-24h of deadline, opted-in only

> {{cohort_name}}: heads-up — {{deadline_artifact}} is due tomorrow {{deadline_date}}. Submit at {{submit_url}}, or reply STOP to opt out.

### `trigger-learner-remind-email`
- Stakeholder: LRN | Phase: trigger | Intent: remind | Channel: email
- CoI: teaching | SDT: competence | Approver: facilitator | Send: T+72h of nudge if no movement

> Subject: One option that works for many — and a softer one
>
> {{learner_first_name}},
>
> Following up. If the schedule is the issue, here are two paths:
> - **The lighter touch:** complete just the {{must_do_artifact}} — that's enough to stay in.
> - **The reset:** drop me a one-line reply with what's in the way, and I'll match you to the right path.
>
> Either is fine. The cohort is better with you in it.
>
> {{facilitator_first_name}}

### `trigger-cohort-friendly-checkin-slack`
- Stakeholder: LRN (cohort-wide) | Phase: trigger | Intent: nudge | Channel: slack
- CoI: social | SDT: relatedness | Approver: facilitator | Send: cohort-scope signal

> Cohort — quiet week. Two questions, no answers expected:
> 1. What is the single biggest blocker right now?
> 2. What format would help — sprint, AMA, peer pair?
> Reply emoji or sentence. I'll act on whichever gets the most signal by {{deadline}}.

---

## Phase 4 — Post-cohort

### `post-learner-celebrate-email`
- Stakeholder: LRN | Phase: post | Intent: celebrate | Channel: email + LMS
- CoI: social | SDT: competence + relatedness | Approver: facilitator | Send: D+0

> Subject: You finished {{course_name}}
>
> {{learner_first_name}},
>
> You did it. Certificate: {{certificate_url}}.
>
> Three numbers from the cohort:
> - {{completion_pct}}% completion
> - Pulse mean {{final_pulse}}
> - {{n_artifacts}} pieces of cohort-built work
>
> One ask before you close the tab: tell us in 60 words {{reflection_prompt_url}}. Your words show up in the next cohort's invite — paid forward.
>
> Stay in the alumni community: {{alumni_url}}.
>
> {{facilitator_first_name}}

### `post-learner-reflect-email`
- Stakeholder: LRN | Phase: post | Intent: reflect | Channel: email
- CoI: cognitive | SDT: autonomy | Approver: facilitator | Send: D+1

> Subject: Three commitments — your D+30 self will thank you
>
> {{learner_first_name}},
>
> Cohort behavioral science is depressingly clear: skills not used in the first 30 days fade. Three commitments, written down, beat ten unwritten ones.
>
> Your three:
> 1.
> 2.
> 3.
>
> Reply or drop into {{reflection_url}}. We'll prompt you at D+7, D+14, and D+30 — opt-out anytime.
>
> {{facilitator_first_name}}

### `post-manager-nudge-email`
- Stakeholder: MGR | Phase: post | Intent: nudge | Channel: email
- CoI: teaching | SDT: relatedness | Approver: facilitator | Send: D+7

> Subject: 3 questions — has {{learner_first_name}} tried anything?
>
> Hi {{manager_first_name}},
>
> {{learner_first_name}} finished {{course_name}} a week ago. Three questions, no replies needed:
> 1. What did you see them try?
> 2. What got in the way?
> 3. What would you recognize publicly if you could?
>
> If question 3 has an answer, drop it in {{recognition_url}} — small, public, fast.
>
> {{facilitator_first_name}}

### `post-manager-roi-email`
- Stakeholder: MGR | Phase: post | Intent: nudge | Channel: email
- CoI: teaching | SDT: competence | Approver: facilitator | Send: D+90

> Subject: Three months in — what stuck?
>
> Hi {{manager_first_name}},
>
> Three months on from {{course_name}}, a 90-second prompt:
> - One thing that {{learner_first_name}} now does differently?
> - One thing they tried that didn't work?
> - One ask of us for the next cohort?
>
> Reply directly or {{form_url}}.
>
> {{facilitator_first_name}}

### `post-sponsor-recap-email`
- Stakeholder: SPN | Phase: post | Intent: recap | Channel: email
- CoI: teaching | SDT: competence | Approver: sponsor-CoS | Send: D+0 and D+30

> Subject: {{cohort_name}} — readout attached
>
> {{sponsor_first_name}},
>
> {{cohort_name}} closed on {{cohort_end_date}}. The 60-word version:
>
> {{n_learners}} learners, {{completion_pct}}% completion, NPS {{nps}}. Strongest behavior signal at D+30: {{l3_one_liner}}. Recommend {{continue|adjust|stop}}.
>
> Full readout: {{readout_url}}. 5-min Loom: {{loom_url}}. The one decision asked: {{decision}}.
>
> {{facilitator_first_name}}

### `post-alumni-invite-email`
- Stakeholder: ALM | Phase: post | Intent: invite | Channel: email
- CoI: social | SDT: relatedness | Approver: facilitator | Send: D+30

> Subject: Welcome to the {{program_name}} alumni
>
> {{learner_first_name}},
>
> The cohort wraps; the network doesn't. Three places you live now:
> - {{alumni_slack}} — peer-help, drop-by hours
> - {{alumni_event_url}} — quarterly alumni session
> - {{success_story_url}} — your own success story (optional, attributed only with your okay)
>
> Lurk, post, or unsubscribe — all fine.
>
> {{facilitator_first_name}}

### `post-alumni-celebrate-email`
- Stakeholder: ALM | Phase: post | Intent: celebrate | Channel: email
- CoI: social | SDT: relatedness | Approver: facilitator | Send: D+180

> Subject: Six months on — what changed?
>
> {{learner_first_name}},
>
> Half a year since {{course_name}}. Two minutes if you have them:
>
> - One thing you do differently now?
> - One thing you'd recommend to a future cohort?
>
> Replies become next-cohort invites — attributed if you want, anonymous if you don't.
>
> {{facilitator_first_name}}

---

## Specialized & Internal Templates

### `pre-facilitator-dossier-internal`
- Stakeholder: FAC | Phase: pre | Intent: inform | Channel: internal doc
- Approver: facilitator (self) | Send: T-1

Internal doc only. Sections:
- Cohort manifest (names, roles, time zones, accessibility notes)
- Pre-work submission status
- Named at-risk-on-arrival (anyone signaling trouble pre-kickoff)
- Cohort culture notes (regulated, senior, mixed-language, etc.)
- First-session opening choice (icebreaker, dive-in, ground-laying)

### `during-learner-makeup-email`
- Stakeholder: LRN | Phase: during | Intent: invite | Channel: email
- CoI: teaching | SDT: autonomy | Approver: facilitator | Send: when session attendance is low

> Subject: Missed yesterday? Here's the path back in
>
> {{learner_first_name}},
>
> Three options, pick one:
> - 18-min recording: {{recording_url}}
> - 5-min Loom recap from me: {{loom_url}}
> - One peer-paired conversation: drop a slot at {{office_hours_url}}
>
> Whichever you choose, you're not behind.
>
> {{facilitator_first_name}}

### `during-learner-reset-email`
- Stakeholder: LRN | Phase: during | Intent: nudge | Channel: email
- CoI: teaching + social | SDT: autonomy + relatedness | Approver: facilitator | Send: silent-cohort revival

> Subject: Cohort reset — let's do less, better
>
> Cohort,
>
> The signal is that the load is too heavy right now. Three changes for the next two weeks:
> 1. {{drop_artifact}} is dropped — do it later or not at all.
> 2. The next live session is reformatted as {{new_format}}.
> 3. {{new_office_hours}} added — drop in for any reason or no reason.
>
> Tell me what else: {{pulse_url}}.
>
> {{facilitator_first_name}}

### `during-sponsor-pulse-email`
- Stakeholder: SPN | Phase: during | Intent: recap | Channel: email
- Approver: sponsor-CoS | Send: midpoint pulse + 5 working days

> Subject: {{cohort_name}} — midpoint pulse
>
> {{sponsor_first_name}},
>
> Pulse mean {{pulse_mean}} (cohort {{n}} of {{n_learners}}). The top theme: {{theme}}. What we're changing in response: {{change_one_line}}.
>
> {{facilitator_first_name}}

### `during-smex-thanks-email`
- Stakeholder: SME | Phase: during | Intent: celebrate | Channel: email
- Approver: facilitator | Send: T+1 of guest module

> Subject: Thank you for {{module_n}} {{module_title}}
>
> {{smex_first_name}},
>
> Three signals from your session:
> 1. {{signal_1}} (e.g., "23 questions in the chat — you held it")
> 2. {{signal_2}}
> 3. {{signal_3}}
>
> If you'd be open to coming back for {{cohort_name_next}}, the date is {{next_cohort_date}}. No expectation either way.
>
> {{facilitator_first_name}}

---

## Template Authoring Checklist (apply before any send)

- [ ] Reading-level target met (default Grade 8)
- [ ] One-ask rule (one verb, one deadline)
- [ ] Time-bound with ISO date + zone (no "next week")
- [ ] Plain-language pass (active voice, common words)
- [ ] UDL: alt-format available where applicable
- [ ] Graceful exit on every nudge
- [ ] Framework anchor declared
- [ ] Approver named
- [ ] No `{{placeholders}}` remaining
