# Workflows

These are the detailed procedures the agent follows for each slash command. Keep deterministic, idempotent, and resumable.

## Workflow: /onboard

**Goal:** Populate `context/project.md`, `context/role.md`, `context/constraints.md`, `context/for-agent/environment.md`.

Steps:
1. Ask:
   - Agency / organization name (may be pseudonymized).
   - User's role (investigator, adjudicator, FSO, insider-threat analyst).
   - Authorities under which the user operates (EO 12968, EO 13467, NISPOM, agency-specific).
   - Caseload size and composition (approx. count by clearance level).
   - Tool stack (DISS, NBIS, JPAS legacy, Scattered Castles, internal ticketing).
   - Handling caveats (FOUO, CUI, SCI compartments — we do NOT ask for compartment names, only categories).
2. Write the answers to the four files above.
3. Produce a one-paragraph "mission statement" for the agent and save to `planning/plan.md`.
4. Log to `work-log/YYYY-MM-DD.md` as "onboard complete."

## Workflow: /intake-subject

**Goal:** Create a clean, pseudonymized baseline profile for a single subject.

Steps:
1. Assign an ID of the form `SUBJ-NNNN` — never a real name.
2. Collect (via questions):
   - Clearance level (Public Trust, Secret, TS, TS/SCI, etc.).
   - Eligibility determination date (approx. year).
   - Current investigation tier.
   - Position sensitivity / mission criticality (1-5).
   - Access programs (categories only, never names).
   - Any adverse history categories the user is already aware of (by SEAD 4 guideline letter, e.g., "F" for financial concerns).
3. Write `outputs/subjects/SUBJ-NNNN/baseline.md` with structured front-matter YAML plus narrative.
4. Seed `outputs/subjects/SUBJ-NNNN/scans/` with `scan-index.json` = [].
5. Schedule a first-pass drift scan and propose the date.

## Workflow: /drift-scan

**Goal:** Produce a point-in-time risk reading for a subject.

Steps:
1. Load baseline and prior scans under `outputs/subjects/<id>/`.
2. For each of the 13 SEAD 4 guidelines:
   a. Ask or accept input: any new information in this category?
   b. Score 0-5 per the rubric.
   c. Note evidence.
3. Compute a weighted composite health index.
4. Compare to the prior N scans; emit trend.
5. Apply decision rules from `resources/action-decision-tree.md`:
   - If composite delta ≥ threshold → recommend focused inquiry.
   - If any single guideline transitions from ≤2 to ≥4 → recommend targeted interview.
   - If all indicators trending stable below threshold → extend next scan interval.
6. Write `outputs/subjects/<id>/scans/scan-YYYYMMDD.md` with the structured result.
7. Append a row to `outputs/subjects/<id>/scans/scan-index.json`.
8. Log the action to `work-log/YYYY-MM-DD.md`.

## Workflow: /adjudicate

**Goal:** Produce an adjudicative memo draft for human review.

Steps:
1. Load the most recent drift scan and the baseline.
2. For each guideline where score ≥ 3:
   a. List the **disqualifying conditions** observed (with evidence pointers).
   b. List the **mitigating conditions** observed (with evidence pointers).
3. Walk the **whole-person factors** (nature, circumstances, frequency, age, participation, rehabilitation, motivation, coercibility, recurrence likelihood).
4. Draft a recommendation, framed as analyst lead:
   - "For analyst consideration: conditions favor continued eligibility," OR
   - "For analyst consideration: further inquiry warranted on Guideline X," OR
   - "For analyst consideration: conditions support referral to the adjudicator for potential adverse action."
5. Save as `user-docs/subjects/<id>/adjudicative-memo-YYYYMMDD.md`.
6. Never call the memo final. It's a draft for a human to refine.

## Workflow: /schedule-reinvestigation

**Goal:** Convert calendar-based reinvestigation thinking into condition-based scheduling.

Steps:
1. Load baseline and most recent scans.
2. Identify:
   - **Calendar anchor** — legacy PR due date (kept for policy compliance until superseded).
   - **Event triggers** — specific CE alerts that would force an out-of-cycle action.
   - **Condition triggers** — health-index thresholds per guideline.
3. Produce an intervention plan:
   - Next scheduled scan date (condition-based interval).
   - Sentinel events that short-circuit the schedule.
   - Minimum / maximum next action windows.
4. Save as `user-docs/subjects/<id>/reinvest-plan-YYYYMMDD.md`.
5. Optionally emit an iCal-compatible calendar file to `outputs/subjects/<id>/reinvest.ics` if the user wants calendar integration.

## Workflow: /continuous-eval

**Goal:** Triage a single CE alert end-to-end.

Steps:
1. Capture the alert:
   - Subject ID.
   - Source category (Criminal, Financial, Terrorism/foreign, Public records, Self-report, Employer).
   - Severity (low / moderate / high per `resources/continuous-vetting-triggers.md`).
   - Summary (redacted).
2. Map to SEAD 4 guideline(s).
3. Recommend an initial inquiry:
   - What records to pull.
   - What interview questions to prepare.
   - What timeline (per agency policy).
4. Propose a disposition:
   - No action / closed favorable.
   - Documented inquiry, retain in file.
   - Expanded inquiry.
   - Out-of-cycle investigation.
   - Refer to adjudicator.
5. Save as `outputs/ce-alerts/<alert-id>.md` and cross-link from the subject's folder.
