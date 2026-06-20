# /contingency-tree

Generate the contingency decision tree for the trip — medical, hostile action, civil disturbance, vehicle failure, comms loss — with protocol-triggered actions per branch.

## Inputs

- **Trip configuration** — venues, routes, motorcade config, jurisdictions.
- **Threat tier** + threat-stream summary.
- **Available assets** — own CAT, medical asset, host-nation QRF, embassy MSG.
- **Communication channels** — primary + alternate + emergency frequencies + sat-comm backup.
- **Hospital pre-positioning** — primary trauma centre + alternate per route.
- **Diplomatic channels** — Embassy DCM, host-nation MOI liaison, FAA / counterpart for airspace.

## Steps

1. Read `context/concepts.md` "Contingency doctrine" + `context/workflows.md` "Contingency activation".
2. Build the decision tree by category, each starting at a documented trigger and branching to specific actions:
   - **Medical** — protectee injured / staff injured / mass-casualty / vehicle accident
   - **Hostile action** — small-arms attack / IED / VBIED / kidnapping attempt / armed standoff
   - **Civil disturbance** — protest in path / hostile crowd / venue siege
   - **Vehicle failure** — primary VIP vehicle disabled / motorcade vehicle disabled / armoured vehicle damage
   - **Comms loss** — primary comms down / sat-comm fail / runner protocol activated
   - **Host-nation event** — coup / national emergency / sudden border closure / sudden visa revocation
3. Per branch, document:
   - Trigger condition (specific, observable)
   - Immediate actions (first 30 seconds — who does what)
   - Short-term actions (1-5 minutes — formation change, evac route, comms escalation)
   - Sustained actions (beyond 5 minutes — embassy notification, host-nation request, family notification)
   - Decision authority — who decides to continue trip vs. abort
4. Cross-reference with route recon for evac-route specifics per branch.
5. Cross-reference with motorcade config for formation-change protocols.
6. Identify named POCs in jurisdiction matrix who must be notified per branch.
7. Generate a one-page summary for detail leader carry; full tree in `outputs/contingency-trees/<trip-id>/contingency-tree.md`.
8. Walk the team through the tree in pre-trip rehearsal.

## Output

A markdown contingency tree at `outputs/contingency-trees/<trip-id>/contingency-tree.md` plus a one-page carry-summary for detail leader. Tree branches keyed to triggers; actions sequenced by timeline; POCs and decision authorities named.

## Decision points

- **If a branch has no clear evac route from a venue** → that's a venue-survey gap; remediate before trip OR cancel that increment.
- **If decision authority is unclear (RSO vs. Detail Leader vs. Ambassador)** → resolve in pre-trip rehearsal; ambiguity in the moment is the failure mode.
- **If host-nation response time exceeds protocol maximum on a branch** → request augmentation OR pre-position own assets to compensate OR reduce time-in-vulnerable-segment.

## Notes

- Tree must be walked through with the team in pre-trip rehearsal; reading it in the moment is too late.
- Branches should be specific enough to action without re-deliberation. "Move to hard room" is actionable; "respond appropriately" is not.
- Document the team's role-specific actions per branch (CAT lead, driver, agent, family escort, medical) — each role has specific moves.
- Update tree after any significant pre-trip change (threat-tier shift, new intel, jurisdictional update).
