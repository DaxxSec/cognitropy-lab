# Prompt — Build the Analysis of Competing Hypotheses (ACH) Matrix

> Scaffolding to walk the analyst through constructing an ACH matrix in line with Heuer (1999) and Heuer & Pherson (2020).

## When to Use
- Required step in `/peer-review-checklist`
- Useful diagnostic any time motive is ambiguous
- Required when a single hypothesis is dominating the analyst's thinking — ACH counters confirmation bias

## Pre-Build
Have at hand:
- Populated indicator checklist (every corroborated indicator with source and date)
- Motive profile draft with at least the leading hypothesis articulated
- The list of MICE-RC categories that had any presence, even minimal

## Matrix Construction

### Step 1: Enumerate Hypotheses
List **at least 4** hypotheses, including:
- **H0 — Null:** "Indicator pattern is consistent with normal life events and ordinary internal causes for someone in this subject's role and circumstance."
- **H1 — Leading hostile motive:** the dominant MICE-RC category from the profile.
- **H2 — Close alternative motive:** the next most-supported MICE-RC category.
- **H3 — Mixed motive:** if profile shows two categories with comparable weight, treat the mix as its own hypothesis. (E.g., "Money + Ego" rather than collapsing.)
- **H4 — Coercion / target-of-attempt:** if foreign-contact indicators or external pressure markers are present.
- **H_other:** any other plausible hypothesis the analyst can articulate, even ones they think are unlikely.

A four-hypothesis matrix is the floor. Five or six is normal. Three or fewer is too few to discriminate.

### Step 2: Enumerate Evidence
List **every corroborated indicator** from the checklist as a row. Use compact identifiers (E1, E2, ...). For each, note source reliability and credibility.

Critical ACH discipline: include indicators that *do not appear to support* the leading hypothesis. These are the load-bearing rows for discrimination.

### Step 3: Score Each Cell
For each (Evidence, Hypothesis) cell, score:
- **C** — Consistent: the evidence is what we would expect if this hypothesis were true
- **I** — Inconsistent: the evidence is *not* what we would expect if this hypothesis were true (this is the critical ACH move — affirmatively look for inconsistency)
- **N** — Neutral: the evidence is not informative about this hypothesis
- **N/A** — Not applicable: the evidence has no bearing on this hypothesis

### Step 4: Weight the Inconsistencies
Heuer's key insight: *one inconsistency is much stronger negative evidence than one consistency is positive evidence*. Many things consistent with a hypothesis don't prove it; one thing inconsistent with a hypothesis seriously damages it.

Tally inconsistencies per hypothesis. The hypothesis with the **fewest inconsistencies** is the analytically dominant hypothesis, regardless of how many "C" marks it has.

### Step 5: Sensitivity Analysis
For the dominant hypothesis, identify the **diagnostic** evidence — items with high reliability that are inconsistent with all alternatives. If those items were proven incorrect, would the dominant hypothesis change?

If the dominant hypothesis depends on one or two diagnostic items, the finding is more fragile than the count suggests. Document this.

### Step 6: Document Residual Inconsistencies
For the dominant hypothesis, walk every "I" cell. State explicitly:
- Why this evidence is inconsistent with the dominant hypothesis
- What benign/alternative explanation accounts for the inconsistency
- Whether the analyst can resolve the inconsistency or must leave it as a known weakness

Acknowledged residual inconsistencies do not invalidate a finding; they calibrate confidence.

## Output Template

```markdown
# ACH Matrix — Subject [ref] — [date]

## Hypotheses
- H0: Null — indicator pattern explained by ordinary causes
- H1: [Money / Ideology / Compromise / Ego / Revenge / Coercion / Mixed]
- H2: ...
- ...

## Evidence
| ID | Indicator | Domain | Source Reliability | Credibility |
|---|---|---|---|---|
| E1 | ... | ... | ... | ... |
| E2 | ... | ... | ... | ... |
| ... |

## Matrix
| | H0 | H1 | H2 | H3 | H4 |
|---|---|---|---|---|---|
| E1 | C | I | C | N | I |
| E2 | I | C | C | I | N |
| ... |

## Inconsistency Tally
- H0: [count]
- H1: [count]
- ...

## Dominant Hypothesis
- [...] (fewest inconsistencies)
- Diagnostic evidence: [list]
- Residual inconsistencies and explanations: [list]

## Sensitivity
- If E[X] were refuted: [effect on dominant hypothesis]

## Reviewer Notes
- ...
```

## Cautions
- Do **not** drop evidence rows that complicate the leading hypothesis. The temptation is real; resist it.
- Do **not** score every cell against the leading hypothesis as Consistent by default. ACH only works if scoring is honest.
- The matrix is a tool, not the finding. The matrix's output informs the finding language (probability, confidence, alternatives), but the analyst writes the finding.
- A matrix that yields no clear dominant hypothesis is a valuable result: the finding is "ambiguous motive — current source set cannot discriminate," which is itself a valid, defensible analytic product.
