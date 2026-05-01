# /peer-review — Run a Structured Peer-Review Pass

The gate that turns a draft rule, a tuned rule, or a post-show report into a peer-validated artifact. Adapted directly from cybersecurity detection-engineering peer-review practice (Splunk, Elastic, Panther workflows).

## Required Inputs

- `--target <path>` — one of:
  - `outputs/rules/draft/<rule>.yml` (new draft)
  - `outputs/rules/active/<rule>.yml` (tuning an active rule)
  - `outputs/reports/<report>.md` (post-show report)
- `--reviewers <name1>:<role1>,<name2>:<role2>` — at least two; **distinct roles required**.

## Steps

### 1. Validate Reviewer Distinct-Roles

Refuse to proceed if both reviewers share a role bucket. Acceptable role buckets:

- `puppeteer` (any performer-side perspective: omozukai, hidarizukai, marionettist, dalang)
- `rigger` (any mechanism-side perspective: builder, technician, animatronic engineer)
- `dramaturg` (any art-side perspective: director, movement director, dramaturg)
- `tradition-bearer` (lineage-holder for a living tradition; counts as its own bucket)
- `detection-engineer` (an external SOC perspective, useful for cross-pollination but never the only reviewer)

Two `puppeteer` reviewers → reject. One `puppeteer` and one `rigger` → accept. One `puppeteer` and one `tradition-bearer` → accept.

### 2. Walk Each Reviewer Through Their Color

#### Red — try to break the rule
- "Construct or recall a movement log where this rule should fire but does not."
- "Construct or recall a log where the rule fires but should not."
- "Is the false-positive list complete?"
- "Does the rule's threshold survive the next adverse environment (climate change, travel shock, new performer)?"

#### Blue — validate the detection covers the failure
- "Walk the rule against its stated example logs from `references:`. Does it fire?"
- "Are the tactic / technique tags from the catalog correct?"
- "Does the rule's `description:` match what the rule actually does?"

#### Purple — collaborative tuning
- "Propose one specific change — threshold, window, field, scope — that improves the rule without narrowing it past usefulness."
- "Suggest a baseline-refresh cadence if the rule keys off baselines."

### 3. Capture Dispositions

Each reviewer writes one of:

- `accepted` — rule is fit for active set; tags are correct; false-positive list is acceptable.
- `tune <field>` — change required before acceptance; the named field is what to change.
- `reject` — rule is fundamentally wrong-shape; close the draft.
- `escalate` — disposition above this review's authority; route to senior tradition-bearer or company lead.

### 4. Write the Pass Record

Output to `outputs/reviews/<YYYY-MM-DD>-<target-slug>.md`:

```markdown
# Peer Review Pass

**Target:** outputs/rules/draft/right-shoulder-stretch.yml
**Date:** 2026-05-01
**Target rule version:** 1.0
**Reviewers:**
- Lena (puppeteer, blue)
- Mateo (rigger, red)

## Lena — Blue
Walked rule against work-log/2026-04-15.md and work-log/2026-04-22.md.
Both fire correctly. Tags `tactic.string-system-drift` /
`technique.gradual-stretch` are correct.
False-positive #1 (deliberate slack pose) covers the case I was worried about.
**Disposition:** accepted.

## Mateo — Red
Constructed a hypothetical log: pre-show rebuild restrung the puppet.
Baseline not refreshed yet. Rule fires (false positive). The rule's
existing false-positive #2 ("Recently restrung; baseline not refreshed")
acknowledges this but does not fire suppression — only tells the author.
Suggest adding a filter on `puppet_metadata.baseline_age_lt: 2 days`.
**Disposition:** tune detection.filter — add baseline-age guard.

## Outcome
- Disposition aggregate: tune detection.filter
- Action: author addresses tune; new pass when ready.
- Rule remains in `outputs/rules/draft/`.
```

### 5. Apply the Merge Gate

- Both `accepted` → move target file from `outputs/rules/draft/` to `outputs/rules/active/`. Bump rule's `status:` from `experimental` to `test` if first acceptance, `stable` if second pass after at least 30 days in `test` with no firings of disposition `tune`.
- Any `tune` → target stays in draft; author addresses; new review pass required.
- Any `reject` → target moves to `outputs/rules/retired/` with a retirement rationale appended.
- Any `escalate` → review record stays open; target file untouched; senior reviewer notified.

### 6. Git Trace

Write a commit message in the form:

```
review: <slug> — <aggregated disposition>

Reviewers: <name1> (<role1>, <color1>), <name2> (<role2>, <color2>)
Target: <relative path>
Pass record: outputs/reviews/<file>.md
```

## Output

- `outputs/reviews/<date>-<target-slug>.md` — the pass record.
- File system action per the merge gate.
- Updated review record in git history.

## Failure Modes

- **Reviewers in same role bucket.** Refuse to start the pass; tell the user "two `puppeteer`s is one perspective; pick a rigger / dramaturg / tradition-bearer to pair."
- **Target rule referenced by review does not exist.** Refuse; tell the user the path is wrong.
- **Reviewer cannot reach a disposition.** Allow `escalate` and route to a third reviewer.

## Why Distinct Roles Matter

Two reviewers in the same role bucket will cluster on the same blind spots. An all-puppeteer review will accept rules that miss mechanism failures the rigger would catch; an all-rigger review will accept rules that miss dramaturgical drift the director would catch. Distinct-role pairing is the single most important invariant — it is what prevents the rule set from accumulating one-sided failures.
