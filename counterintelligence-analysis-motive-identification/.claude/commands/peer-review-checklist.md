# /peer-review-checklist — Run the Structured Analytic Peer-Review Checklist

Run a structured analytic peer review against the draft motive assessment before any external dissemination. This command is a checklist by design; every item must be addressed, none may be skipped.

## Inputs
- Motive profile draft
- Indicator checklist (current version)
- Timeline (if produced)
- Recruit-vector assessment (if produced)
- ICD 203 standards reference

## Steps

### 1. ICD 203 Standards Walk
For each ICD 203 analytic standard, score the draft (Pass / Marginal / Fail) and document why:

| Standard | Pass condition |
|---|---|
| Properly describes quality and reliability of underlying sources | Every indicator citation has source reliability and credibility ratings; aggregate source-quality summary provided |
| Properly characterizes analytic confidence | Confidence reported separately from probability; ICD 203 lexicon used; confidence drivers named |
| Properly expresses and explains uncertainty | Alternatives enumerated; gaps that would change the assessment named; uncertainty not glossed |
| Distinguishes underlying intelligence from analytic judgment | Indicators (observations) are clearly separated from hypotheses (judgments); no rhetorical conflation |
| Uses clear and logical argumentation | Checklist trace shown; reasoning from indicator → motive hypothesis → confidence is explicit |
| Makes accurate judgments and assessments | No claim asserted beyond what the indicator base supports; lexicon matches the evidence weight |
| Incorporates effective visual information where appropriate | Timeline diagram, ACH matrix, or domain-coverage table included |

If any standard scores Fail, **stop**. Return to the relevant command and remediate before proceeding.

### 2. Build the Analysis of Competing Hypotheses (ACH) Matrix
Produce `outputs/<date>-ach.md`:

```markdown
# ACH Matrix — Subject [ref] — [date]

## Hypotheses
- H0: Null — indicator pattern explained by ordinary, non-hostile causes
- H1: [Leading motive hypothesis from profile]
- H2: [Close alternative]
- H3: [Less likely but plausible alternative]
- H4: [Coercion / target-of-attempt, if vector assessment supports]

## Evidence
- E1: [indicator 1, with source]
- E2: [indicator 2, with source]
- ... (every corroborated indicator from the checklist)

## Matrix
| | H0 | H1 | H2 | H3 | H4 |
|---|---|---|---|---|---|
| E1 | C / I / N / N/A | ... | ... | ... | ... |
| E2 | ... | ... | ... | ... | ... |
| ... |

(C = consistent, I = inconsistent, N = neutral, N/A = not applicable)

## Inconsistency Tally
- H0: [count of I]
- H1: [count of I]
- ...

## Dominant Hypothesis
- [The hypothesis with the FEWEST inconsistencies] — that is the analytically dominant hypothesis, regardless of consistency count.
- Reasoning for residual inconsistencies: [...]

## Sensitivity
- If E[X] were proven incorrect, would the dominant hypothesis change? [yes/no — analyze]
```

The dominant hypothesis is the one with the **fewest inconsistencies**, not the most consistencies. Confirm the motive profile's leading hypothesis is the ACH-dominant one. If not, the profile must be revised.

### 3. Bias Inventory
Walk the failure-mode table from `domain-knowledge.md`. For each potential bias, state explicitly how this analysis countered it:

- **Confirmation bias** — what would have refuted the leading hypothesis? Did the checklist examination genuinely seek that refutation?
- **Vividness bias** — was any single dramatic indicator anchoring the analysis?
- **Halo effect** — did the subject's prior reputation (positive or negative) influence indicator interpretation?
- **Single-source dependence** — were any indicators sourced only from one individual? Were they corroborated?
- **Protected-class shortcut** — does any indicator rest on protected-class characteristics absent independent corroborating behavior?
- **Outdated baseline** — are any "normal" assumptions in the analysis at least a decade out of date?

Document the answer to each.

### 4. Civil-Liberties Re-Check
Re-walk `context/constraints.md`. Confirm:
- No indicator rests on protected-class characteristics alone
- No whistleblower-protected disclosure is in the indicator base
- US Persons minimization (or equivalent) has been applied
- Source predication remains within authority

If any check fails, the finding is **withdrawn**. No degraded version is published.

### 5. Source-Protection Check
- Are any human-source identifiers present in the analytic product?
- Could a source be inferred from context (e.g., "subject's supervisor reported X" when only one supervisor exists)?

Strip identifiers before publication.

### 6. Adverse-Action Framing Check
Confirm the product is framed as analytic, not as a basis for action. The product:
- Uses neutral language ("indicator pattern is consistent with X" not "subject is X")
- Identifies recommendations for further inquiry, not adverse actions
- Notes explicitly that downstream actions (HR, adjudication, law enforcement) require their own predicate and decision-makers

### 7. Sign-off Block
Add to the bottom of the motive profile draft:

```
Peer-review checklist completed: [date]
ICD 203 standards walked: Pass
ACH dominant hypothesis: [...] (consistent with profile leading hypothesis: yes/no)
Bias inventory: complete (see above)
Civil-liberties check: pass
Source-protection check: pass
Adverse-action framing check: pass
Analyst initials: [...]
Reviewer initials (if separate): [...]
```

### 8. Save and Log
Save outputs (`outputs/<date>-ach.md`, updated motive profile draft). Append `work-log/session-log.md` with the peer-review session.

## Decision Points
- ACH reveals a tied or near-tied alternative → Finding is **"ambiguous motive — multiple hypotheses cannot be discriminated from current source set"**; recommendation is for further inquiry, not a conclusion.
- An ICD 203 standard cannot be met → Finding is downgraded to **"preliminary assessment, not for external dissemination"** until the gap is closed.
- A civil-liberties check fails → Finding is **withdrawn entirely**.
- A bias was uncovered late in review → Re-run the relevant command with the bias remediated; do not patch the finding.
