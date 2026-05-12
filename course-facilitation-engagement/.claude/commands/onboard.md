# /onboard — Initialize Course Facilitation Engagement Workspace

Welcome. I'll gather the course profile, cohort, stakeholders, and channel setup so the cadence and templates render correctly from day one.

## Interview Flow

### 1. Course Profile
Ask the user:
- What is the course called and what cohort or run is this? (e.g., "Manager Foundations Cohort 14")
- What is the modality — fully virtual, blended, in-person, or hybrid?
- What is the duration and module cadence (weekly, biweekly, sprint-based)?
- What are the learning objectives at the program level (Bloom-anchored is ideal)?
- What is the prior history with this program — first run, fifth run, refresh of an old course?

Save responses to `context/project.md`.

### 2. Cohort Profile
Ask the user:
- Cohort size and role mix (junior individual contributors, mid-level managers, senior leaders, mixed)
- Geographic and time-zone span
- Languages spoken; whether the course is delivered in one language or with translation
- Documented accessibility needs
- Prior cohort history if applicable (some learners returning, all new, etc.)

Save responses to `context/project.md`.

### 3. Stakeholder Roster (initial pass)
Ask the user to name, for each role that exists in their context:
- Lead facilitator and any co-facilitators
- Producer / TA
- L&D admin owning logistics
- Executive sponsor (and the chief of staff or program-management partner who reads first drafts)
- Line manager community (single named champion or the manager group at large)
- Compliance reviewer if regulated
- SME guests scheduled, with the modules they appear in
- Mentors / coaches if cohort has 1:1 support
- Alumni community or alumni champion if pre-existing

Save responses to `context/project.md` and stage the register for `/map-stakeholders`.

### 4. Channels
Ask the user:
- Which LMS, and what is your access level (announce / read-only signals / full export)?
- Which mail platform is the cohort sender, and what alias do you send from?
- Slack workspace or Teams tenant — channel naming convention and existing automation
- Calendar system and time-zone conventions
- Survey / pulse tool of choice
- Conferencing platform and recording policy

Save responses to `context/for-agent/environment.md` and `context/for-agent/tools.md`.

### 5. Voice, Compliance, Accessibility
Ask the user:
- Is there a brand voice doc? If yes, paste a 200-word excerpt or link it.
- Reading-level target? (Default: Grade 8 for learner-facing.)
- Compliance review SLA and named reviewer if applicable
- Accessibility expectations: captions, screen-reader testing, alt-format requests, time-to-fulfill

Save responses to `context/constraints.md`.

### 6. Engagement Goals
Ask the user:
- Completion-rate target (Level 0/1)
- Satisfaction or NPS target (Level 1)
- Learning-delta target if pre/post assessment is in scope (Level 2)
- Behavior-change target by D+30 (Level 3) — what observable change defines success?
- Business-outcome target (Level 4) if the program is tied to a business metric

Save responses to `context/project.md`.

### 7. Privacy & Authorization
Ask the user:
- What consent has been (or will be) obtained at enrollment about engagement-signal collection?
- What is shared by default with the line manager? With the sponsor?
- Retention policy for behavioral traces

Save responses to `context/constraints.md`.

## Post-Onboard Actions

1. Confirm `context/project.md`, `context/role.md`, `context/constraints.md`, `context/for-agent/environment.md`, and `context/for-agent/tools.md` are populated. Flag any gaps.
2. Recommend the immediate next step: `/map-stakeholders` to produce the Power–Interest matrix and RACI before any drafting.
3. Create the initial cadence stub in `planning/plan.md` with empty rows by phase × stakeholder, ready for `/draft-cadence`.
4. Open today's entry in `work-log/<YYYY-MM-DD>.md` with a single line: "Onboarded {{cohort_name}}; next: /map-stakeholders".
5. Surface any risk you saw in the answers (e.g., no compliance reviewer named for a regulated course; no opt-in language for manager visibility) for the user to resolve before drafting.
