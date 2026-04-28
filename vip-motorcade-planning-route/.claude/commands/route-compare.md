# /route-compare — Multi-Criteria Route Comparison

Compare scored candidate routes side-by-side and pick a primary, alternate, and abort.

## Required Inputs
- At least three scored routes (each with `outputs/<route-codename>/scoring-sheet.md`)
- `planning/comparison-weights.md` (created by `/onboard`)
- Detail leader's intent for this movement window (predictability vs unpredictability, comfort, OPSEC profile)

## Procedure

### 1. Confirm the Candidate Set
- Reject the run if fewer than three scored routes exist for this origin/destination — two routes is a binary, not a comparison.
- Reject the run if any route's score is older than the threat baseline.

### 2. Compute the Comparison Vector
For each route, extract:

| Criterion | Source | Sign |
|-----------|--------|------|
| `max_residual` | scoring sheet roll-up | lower better |
| `high_plus_count` | scoring sheet roll-up | lower better |
| `total_time_min` | survey exposure profile | lower better |
| `time_variance_min` | survey exposure profile | lower better |
| `deconfliction` (1–5) | analyst rating from survey notes (traffic, parallel public events) | lower better |
| `profile_signal` (1–5) | how visible/loud the motorcade looks to outside observers on this route | usually lower better; sometimes inverted |
| `principal_comfort` (1–5) | analyst rating (vehicle changes, dwell stops, urban vibration) | lower better |

Normalize each criterion to a 0–1 scale across the candidate set so weights work.

### 3. Apply Weights
Default weights (tunable):

| Criterion | Default Weight |
|-----------|----------------|
| max_residual | 0.35 |
| high_plus_count | 0.20 |
| total_time | 0.10 |
| time_variance | 0.05 |
| deconfliction | 0.10 |
| profile_signal | 0.10 |
| principal_comfort | 0.10 |

Composite = Σ (normalized × weight). Lower composite = better choice.

### 4. Apply Hard Vetoes
- Any route with an Extreme residual segment is vetoed regardless of composite.
- Any route lacking an authorized abort variant is vetoed (we don't move without an abort).
- Any route shared >30% by length with the candidate alternate is vetoed *as the alternate* (must find a more distinct alternate).

### 5. Pick
- **Primary:** lowest composite, no veto.
- **Alternate:** second-lowest composite, distinct corridor (≥ 70% non-overlap with primary by length).
- **Abort:** specifically chosen for survivability, not comfort. Often the route to the nearest authorized safe location (embassy, hospital with security, hardened safe house). Score the abort on a *survivability* criterion set — `nearest_trauma_min`, `host_nation_compliance_quality`, `public_visibility_during_abort` — rather than the routine criteria.

### 6. Output
Write `planning/route-decision-<YYYY-MM-DD>.md`:

```
# Route Decision — <window codename> — <YYYY-MM-DD>

## Candidate set
- PRIMARY-A (composite 0.31)
- ALT-1     (composite 0.42)
- ABORT-X   (survivability-scored separately)
- (rejected) PRIMARY-B — Extreme residual on S14
- (rejected) ALT-2     — too close to PRIMARY-A (overlap 41%)

## Choice
- Primary: PRIMARY-A
- Alternate: ALT-1
- Abort: ABORT-X

## Rationale
[2–3 paragraphs — why these, what the residual ceilings are, what mitigations carry weight, what the detail leader signed off on]

## Sign-off
- Detail leader: [placeholder]
- Contracting office written sign-off: [if any High+ residual] [placeholder]
```

Log to `work-log/<YYYY-MM-DD>-route-decision.md`.

## Decision Rules

- If two routes tie on composite within 0.02: prefer the one with lower `max_residual`.
- If the detail leader's stated intent is *unpredictability* (e.g. witness movement, repeated post): reject any candidate that has been the primary in the last 7 d.
- If the principal explicitly requests a route the workspace would not otherwise pick: document the override, capture the principal's name (placeholder) and sign-off, and proceed only if the residual is ≤ ceiling.
