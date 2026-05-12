# Tools & Integrations

## Learning Management Systems

### Canvas (Instructure)
- Engagement signals: course-level analytics 2 API for login, page views, submissions, communication
- Announcements: REST `/courses/:course_id/announcements`
- Best paired with: Canvas Studio for video, Canvas Catalog for cross-org enrollment
- Quirk: page-view granularity is daily, not per-asset; cross-reference with the video host for asset-level signal

### Moodle
- Engagement signals: `report_log`, `report_loglive`, plus the `tool_dataprivacy` log for consented exports
- Announcements: forum subscription pattern (Announcements forum) — every cohort uses this
- Best paired with: H5P for interactive content, Big Blue Button for live sessions
- Quirk: completion tracking must be enabled at course level; default Moodle setup is "off"

### Cornerstone OnDemand
- Engagement signals: ILT roster, transcripts, training plan completion via Reporting 2.0
- Announcements: Inbox + Connect community combined
- Best paired with: Cornerstone Content (paid library content), Connect (the community module)
- Quirk: signal export is batch-oriented — set up a daily export to a sheet for real-time-ish dashboards

### Docebo
- Engagement signals: Discover, Coach & Share metrics; learning intelligence dashboards
- Announcements: in-app notifications + email digest
- Quirk: AI tagging on user content can mislabel skill associations — review before relying on the auto-tag

### Workday Learning
- Engagement signals: limited learner-level granularity; cohort-level reporting via Workday reports
- Announcements: typically tied to email, not in-platform
- Quirk: integrates tightly with HRIS data — strong choice when manager hierarchy is the cadence backbone

### 360Learning
- Engagement signals: Reactions, Comments, Skills built (collaborative learning model)
- Announcements: in-platform feed + email
- Quirk: collaborative model treats forum activity as a first-class signal — privilege it accordingly

## Email

### Gmail / Google Workspace
- Sending tools: Gmail mail merge, Apps Script, third-party (Mailmeteor, YAMM)
- Best practice: send from a delegated alias, not the facilitator's personal account
- Tracking: opt-in tracking per send; never track learners who have not consented

### Microsoft Outlook / 365
- Sending tools: Power Automate flows, Word mail merge to Outlook
- Best practice: shared mailbox with delegate access for handoff continuity
- Tracking: avoid Outlook read-receipts on learner sends; use a single tracked anchor link instead

### Transactional ESPs (SendGrid, Postmark, Mailgun, Amazon SES)
- Use only when volume justifies it (>500 cohort members) and DKIM/SPF/DMARC alignment is in place
- Suppression list management is a hard requirement — audit before each cohort

## Messaging

### Slack
- Channels: `<cohort-id>-cohort`, `<cohort-id>-facilitators`, `<cohort-id>-help`
- Bot pattern: a workflow builder template per cadence event is more maintainable than custom Slack apps
- DM policy: never bulk-DM; DMs are reserved for individualized nudges with a named human as the sender

### Microsoft Teams
- Cohort team with channels for learners, facilitators, optional manager-only channel
- Tabs: pin the LMS course, the calendar, and the planning calendar
- Approvals app is useful for cadence-step gates; send-on-approve patterns reduce friction

### Discord (community-led cohorts)
- Roles: `learner`, `alumni`, `facilitator`, `mentor`
- Channels per module + a #help channel
- Engagement signal: presence + reaction count, less reliable than thread-reply count

## Calendar

### Google Calendar
- Use rich event description for joining details, prework links, accessibility provisions
- Insert events with `sendUpdates=all` for first send, `none` for subsequent edits to avoid alert fatigue

### Microsoft Outlook
- Use a shared facilitator mailbox to send invites; avoids individual-facilitator dependency
- Honor working-hours so cross-time-zone invites land politely

## Survey / Pulse

### Typeform
- One-question-at-a-time UX is high completion; pair with conditional logic for stratified pulses
- Webhook to your sheet of record after each response for near-real-time aggregates

### Qualtrics
- Strongest for institution-grade pulses; supports advanced anonymity controls
- Use the Branch logic to deliver stakeholder-specific summaries from one survey

### Microsoft Forms
- Integrates cleanly with Teams; weak on analytics — pair with Power BI

### Google Forms
- Free, fast, and aggregates straight to Sheets; weak on anonymity controls — be careful with consent framing

## Video / Conferencing

### Zoom
- Recording cloud + transcript; download for retention; auto-share with the cohort within 24h
- Polls for in-session quick pulses; export to CSV for the cadence record

### Microsoft Teams
- Live captions on by default; recordings live in Stream/SharePoint; respect retention policy

### Loom
- The agent's primary asynchronous video tool — short (3–5 min) facilitator-personal recaps
- Native captions are usable; clean up on long recordings

## Analytics & Dashboards

### LMS-native dashboards
- Use first; fight for engagement-data export rights at procurement time

### Power BI / Looker / Tableau
- One pane of glass across LMS + survey + email signals
- Engagement scorecard template should live here once the cohort scales past one cohort at a time

### Sheets / Excel
- Single source for the cohort register, the cadence calendar, and the engagement scorecard for cohorts <100 learners
- Use a workbook per cohort, not a sheet per cohort, for easier rollover

## Accessibility & Plain-language Tooling

- **WAVE** (wave.webaim.org) — quick page-level accessibility audit
- **axe DevTools** — browser extension for WCAG checks
- **Hemingway Editor** — readability-grade check; aim for Grade 8 on learner copy
- **Microsoft Editor / Grammarly business** — voice and inclusive-language pass
- **Color Oracle** — colorblind preview for any chart or visual

## MCP Servers (recommended)

- **filesystem** — read/write rendered templates and the planning calendar
- **gmail / outlook (or smtp)** — draft email sends; the agent drafts, the user reviews and sends
- **slack / teams** — channel posts and DM nudges
- **lms-specific (canvas / moodle / docebo)** — pull engagement signals, post announcements
- **calendar (google / microsoft)** — create rich-description session invites
- **sheets / airtable** — cohort register and engagement scorecard
- **browser** — for any web-based platform without a first-party MCP
