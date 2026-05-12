# Getting Started — CI Motive Analysis Workspace

This guide gets you from a fresh clone of this workspace to a peer-reviewed CI motive finding. It is written for a CI analyst, insider-threat program officer, or corporate security investigator who already has the authority to conduct the inquiry. The workspace cannot grant authority; it formalizes the analytic chain that turns indicators into a defensible finding.

## Prerequisite Reminder

Before any other step, confirm the lawful basis for the inquiry:
- An opened CI investigation with a case number
- An insider-threat program charter section that covers this subject
- An executive-branch order or its analog in your jurisdiction
- A signed engagement letter for private-sector work

If none of those apply to this subject, **stop**. The workspace is for authorized analysis. It is not a tool for inquiring about people.

## First Pass — From Onboarding to Finding (One Working Session, Best Case)

In a clean case with a focused source packet, the full chain can be completed in one analytic session. In practice, indicator gaps and source acquisition usually stretch the work across multiple sessions. Either way, the chain is the same:

### 1. `/onboard`
Capture analyst authority, jurisdiction, classification level, subject category, source inventory, reporting chain. The agent will refuse to proceed without authority confirmation. Output lands in `context/project.md`, `context/role.md`, `context/for-agent/environment.md`, and `planning/plan.md`.

### 2. `/indicator-checklist`
Run the 5-domain inspection checklist against the first source packet. Output lands in `outputs/<date>-indicator-checklist.md`. Expect to iterate this command as new sources arrive — treat the checklist as a versioned artifact, not a one-shot.

### 3. `/build-motive-profile`
Once the checklist is at least 70% populated, map indicators onto MICE-RC. Output lands in `outputs/<date>-motive-profile-draft.md`. Expect this draft to evolve as the source base evolves.

### 4. `/timeline-correlate`
Once you have at least 3 timestamped indicators, build the chronology. Output lands in `outputs/<date>-timeline.md` and an updated motive profile section. Causation hypotheses live here.

### 5. `/recruit-vector-assessment` (conditional)
Run only if the indicator pattern includes foreign-contact or external-influence markers. Output lands in `outputs/<date>-recruit-vector.md`. If the indicator pattern is purely internal, skip this command and document the skip.

### 6. `/peer-review-checklist`
Mandatory before any finding leaves the workspace. Walks ICD 203 standards, builds the ACH matrix, runs the bias inventory, and confirms civil-liberties and source-protection. Output lands in `outputs/<date>-ach.md` and an updated motive profile sign-off block.

### 7. `/produce-ci-finding`
Generate the final ICD 203-compliant finding. Output lands in `outputs/<date>-finding.md`. The analyst transmits to the recipient; the agent does not.

## Workspace Hygiene

- **Work log first.** Every command appends to `work-log/session-log.md` (or a date-named file per session). The log is a discoverable record. Treat it as such.
- **Outputs are versioned.** Multiple iterations of the indicator checklist over a case are normal. Suffix filenames with date and version number rather than overwriting.
- **Planning is alive.** `planning/plan.md` evolves as gaps close and new questions appear. It is not a one-time document.
- **Classification matches source.** If a source packet is classified above the workspace's stated level, do not ingest it into this workspace. Re-host or summarize-down per applicable procedures.
- **Civil-liberties checks are not optional.** They are run at onboarding, at every command's predication step, and at peer review. If any check fails, work stops.

## Common First-Time Pitfalls

| Pitfall | Why it happens | Avoidance |
|---|---|---|
| Skipping `/onboard` because "the case is obvious" | Eagerness to get to the analysis | Onboarding sets the predication and constraints; without it, the agent has nothing to refuse-on |
| Building a motive profile from one domain | Source packet was domain-specific | Acquire cross-domain sources before profiling; or call the result "indicator pattern of concern, not motive finding" |
| Skipping the null hypothesis | Confirmation bias | The peer-review checklist requires the null in the ACH matrix |
| Naming a specific service from contact-pattern alone | Tradecraft pattern + media coverage of recent cases | Resist; vector type only, attribution is a separate evidentiary chain |
| Including protected-class characteristics as indicators | Pattern matching against historical cases | Re-read constraints; rule out the protected-class shortcut |
| Treating the agent's draft as the final finding | Speed pressure | The agent drafts; the analyst signs; the cognizant office reviews |

## When to Pause and Escalate

The agent will pause and require analyst input when:
- Authority is unclear
- Source material falls outside scope
- Indicator pattern requires a step (interview, subpoena, technical pull) outside analyst authority
- Analytic step would rest predominantly on protected-class characteristics
- Coercion indicators are corroborated (escalate to operational leadership immediately)
- Civil-liberties or source-protection check fails during peer review

Pausing is the correct behavior. The analyst's job is to clear the obstacle (acquire sources, consult counsel, escalate operationally) and re-run the relevant command. The finding is built once, correctly.

## Beyond the First Case

Standard CI doctrine encourages re-application of the inspection checklist across cleared populations on a periodic basis. This workspace is designed to scale: copy it per subject, retain the templates, and let the indicator-taxonomy and MICE-RC checklist resources stay constant across the whole program. The case-specific files (`context/project.md`, `context/role.md` — when role for *this* analyst differs by case, `outputs/`, `work-log/`) live per-case; the doctrinal layer is shared.
