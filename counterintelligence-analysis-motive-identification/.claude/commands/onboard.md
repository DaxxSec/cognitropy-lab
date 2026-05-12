# /onboard — Initialize the CI Motive Analysis Workspace

Welcome the analyst. Confirm authority before any other step. Authority is the first checklist item; it is not negotiable.

## Inputs
- Analyst identity / billet
- Organization and clearance level
- Case number or insider-threat program reference
- Subject category and case type
- Authority basis for the inquiry

## Steps

### 1. Authority Confirmation (gating)
Ask the analyst:
- What is the lawful basis for this inquiry? (Opened CI case number, insider-threat program charter section, executive-branch order, signed engagement letter)
- Is the subject within the scope of that basis?
- Is the subject a US Person? If yes, what minimization regime applies?

If any answer is "I'm not sure" or evasive, **stop**. Recommend the analyst consult their general counsel, ethics officer, or program manager before any further work. Do not proceed.

### 2. Analyst Identity
Capture analyst billet, organization, clearance level, years in CI/insider-threat work, primary frameworks familiar (MICE-RC, RASCLS, ICD 203, ACH, SATs). Save to `context/role.md`.

### 3. Subject Category
Capture the subject category — cleared US Person employee, cleared US Person contractor, foreign national employee, walk-in volunteer source, anonymous tip subject, other. Note: subject category determines which legal regime applies to indicator collection. Save to `context/project.md`.

### 4. Case Type
Identify whether this is insider-threat triage, periodic reinvestigation review, walk-in source vetting, contracted private-sector engagement, or sanitized academic case study. Save to `context/project.md`.

### 5. Source Inventory
Enumerate the source packets the analyst has lawful access to for this inquiry. For each: type, originating agency or system, classification level, date of information, date received. Save to `context/project.md`.

### 6. Reporting Chain
Identify where the finding will go (cognizant CI office, insider-threat hub, security adjudicator, HR/legal, FBI Field Office). The reporting chain affects USPER minimization and product framing. Save to `context/project.md`.

### 7. Classification and Storage
Confirm the workspace classification level. Default unclassified or CUI. If higher, confirm the host system is rated for that level. The agent will refuse to ingest material above the workspace's stated classification. Save to `context/for-agent/environment.md`.

### 8. Restrictions
Capture any restrictions on analyst authority for this case — systems they cannot access, steps they cannot lawfully take, supervisory review requirements. Save to `context/role.md` and `context/for-agent/environment.md`.

### 9. Civil-Liberties Affirmation
Walk the analyst through the civil-liberties constraints in `context/constraints.md`. Confirm the inquiry will not rest on protected-class characteristics absent independent corroborating behavior. Confirm whistleblower-protected disclosures are excluded from indicator scoring.

### 10. Initial Plan
Draft `planning/plan.md`:
- Investigative question (one sentence)
- Indicator-source survey plan
- Estimated checklist runs needed
- Key gaps already identified
- Reporting milestone

## Output
- Populated `context/project.md`, `context/role.md`, `context/for-agent/environment.md`
- A first entry in `planning/plan.md`
- An onboarding entry in `work-log/session-log.md` with date, analyst, subject reference (case-internal, not PII), authority basis, and constraints affirmed.

## Post-Onboard Recommendation
- Suggest running `/indicator-checklist` once the analyst has the first source packet open.
- Remind the analyst that authority and civil-liberties constraints will be re-checked at every command, not just at onboarding.
