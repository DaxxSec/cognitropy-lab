# Peer-Review Disposition Language

> Recommended vocabulary for `/peer-review` dispositions. Adapted from Splunk and Elastic detection-engineering peer-review practice.

## The Four Dispositions

### `accepted`
The reviewer is satisfied that:
- The rule's `selection` correctly captures the failure pattern
- The rule's `filter` correctly excludes known benign cases
- The `tags` reference real cells in the failure-mode catalog
- The `falsepositives` list is complete enough for the rule's `level`
- The rule is fit to move from `draft` to `active` (or, if already active, to remain active after the tuning under review)

Use freely. Do not save `accepted` for unanimity-only situations — single-reviewer `accepted` is fine, the merge gate aggregates.

### `tune <field>`
The reviewer would accept the rule with one specific change. The named field is what to change.

Examples:
- `tune detection.selection.drift_from_baseline_gt` — threshold needs adjustment
- `tune detection.filter` — add a missing benign-case suppression
- `tune falsepositives` — false-positive list incomplete
- `tune level` — severity miscalibrated
- `tune description` — description does not match what the rule actually does

The author addresses the named field, then a new review pass runs. The new pass does not need to re-litigate fields the original review accepted unless they are touched by the tune.

### `reject`
The rule is fundamentally wrong-shape. Examples:
- The pattern is not actually a recurring failure (was a one-off)
- The rule encodes an aesthetic preference, not a mechanism failure
- The rule's tactic / technique tags do not exist and the proposal to add them was itself rejected
- The rule duplicates an existing active rule

Always include a written rationale; the rationale is read in future training. Rejected rules move to `outputs/rules/retired/` with their review record attached.

### `escalate`
The reviewer cannot reach a disposition at this review level. Examples:
- The rule touches a tradition-bearer's authority and a tradition-bearer is needed
- The rule touches safety; senior rigger / company lead needed
- The rule's tactic / technique addition is consequential enough to need wider review

Escalating reviewer states the named senior reviewer; the rule stays in draft until the escalation is resolved.

## Combinations and the Merge Gate

| Reviewer 1 | Reviewer 2 | Outcome |
|---|---|---|
| accepted | accepted | Move to `active` |
| accepted | tune | Stay in draft; address tune |
| accepted | reject | Stay in draft; resolve disagreement (often via third reviewer) |
| accepted | escalate | Stay in draft; senior reviewer added |
| tune | tune | Stay in draft; address both tunes |
| tune | reject | Stay in draft; resolve disagreement |
| reject | reject | Move to `retired` |
| escalate | * | Stay in draft until escalation resolved |

## Anti-Patterns

The following are common review failure modes; flag them gently.

- **"LGTM"** — a one-line "looks good to me" without engagement is not an `accepted` review. The pass must show evidence the reviewer walked the rule against the cited logs (Blue role) or constructed a counter-example (Red role).
- **Authority `accepted`** — when a senior reviewer signs off without engagement, the company has acquired a single-perspective rule disguised as peer-reviewed. The distinct-roles rule helps; the agent will additionally flag any review where the senior reviewer's comment is shorter than two sentences.
- **`tune` ping-pong** — repeated `tune <small thing>` cycles. After three rounds, escalate; the rule probably needs scope reduction or splitting.
- **Reject without rationale** — the rationale is the institutional learning. A bare `reject` is not a valid disposition.

## Phrasing for Each Color

### Red role phrasing
- "Constructed counter-example: [scenario]. Rule fires/does-not-fire as expected/unexpectedly."
- "I would expect this rule to also fire on [scenario]; it does not because [reason]. Acceptable / not."
- "False-positive list missing: [scenario]."

### Blue role phrasing
- "Walked rule against [cited log]. Fires correctly at [timestamp]."
- "Tag [tactic.id] is correct; I would have alternately considered [alt tag] but settled on [chosen] because [reason]."
- "Description matches rule behavior."

### Purple role phrasing
- "Suggest tightening [field] to [value] to remove the [scenario] false-positive."
- "Suggest adding `tradition.<x>` tag — this rule will only generalize within that tradition."
- "Suggest splitting this rule into two — one for [puppet type A], one for [puppet type B] — they have different baselines."

## Reference

- Splunk Detection Engineering: [docs.splunk.com](https://docs.splunk.com/) — for peer-review-as-code
- Elastic Detection Rules contributing guide: [github.com/elastic/detection-rules](https://github.com/elastic/detection-rules)
- Anton Chuvakin, *Detection Engineering Maturity Model* (Medium / blog series, 2022–2024)
