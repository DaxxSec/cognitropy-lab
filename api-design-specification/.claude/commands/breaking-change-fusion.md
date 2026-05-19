# /breaking-change-fusion

Decide and stage a breaking change to an existing operation by fusing the four most-decisive sources for sunset decisions: telemetry (who calls it), tickets (who is hurt), standards (does the replacement align), corpus (is the replacement consistent). Outputs a deprecation + migration plan with an impact table.

## Inputs

- **Target operation** — JSONPath or `METHOD path` form (e.g. `GET /v1/users/{id}/legacy-prefs`).
- **Proposed replacement** — the operation or surface the change moves traffic to.
- **Time window** for telemetry / ticket pull — default trailing 90 days; 180 days if the surface has long-tail enterprise traffic.

## Steps

1. **Direction.** Restate the operation, the proposed replacement, and the explicit reason for the change (security, simplification, standards alignment, performance, etc.).
2. **Telemetry pull.** Aggregate by client ID: call_count_30d, call_count_90d, last_call_at, dominant request-shape signature, dominant response status. Persist as `outputs/breaking-change/<op>-clients.csv`.
3. **Ticket pull.** Filter for tickets touching the target operation in the window. Categorise: contract confusion, missing field, edge-case bug, doc gap. Count.
4. **Standards check.** Cite the standard (RFC, OpenAPI section, peer convention) the replacement aligns with. If the replacement does *not* clearly align with current standards, abort: re-design before deprecating.
5. **Corpus consistency check.** Confirm the replacement is consistent with the rest of the surface (status codes, pagination, error envelope, auth). Mismatches are spec debt that should be fixed before the sunset, not after.
6. **Fuse.** Run the standard fusion analysis on the *replacement* operation per `/fuse-requirements`, but with telemetry as a primary input rather than a tie-breaker.
7. **Impact tier the client list.** Tag each client_id with tier (enterprise / SMB / unknown), activity (active / inactive / dormant 30+), migration cost estimate (S / M / L from request-shape complexity).
8. **Sunset window.** Default 90 days. Extend to 180 if >100 distinct active clients touch the operation, or if a tier-1 enterprise is in the list. Shorten to ≤30 only if <5 clients touch it in the trailing 30 days.
9. **Outreach list.** Top-N by call volume, with tier; carve out the inactive long tail (separate notification template).
10. **Migration snippet.** Side-by-side request/response showing the dominant v(N) → replacement translation.
11. **HTTP signalling.** Emit `Deprecation` (draft-ietf-httpapi-deprecation-header) and `Sunset` (RFC 8594) header values to be added to the target operation immediately, before the sunset date.
12. **Emit plan.** Write `outputs/breaking-change/<op>-<date>.md` with all of the above; link to the impact CSV.

## Output

- `outputs/breaking-change/<op>-clients.csv` — the per-client impact table.
- `outputs/breaking-change/<op>-<date>.md` — the full plan: direction, telemetry summary, ticket summary, standards alignment, corpus consistency, sunset window + rationale, outreach list, migration snippet, header signalling.
- A pull request to add the `Deprecation` + `Sunset` headers to the target operation's spec entry, citing the plan.

## Notes

- No deprecation lands without telemetry evidence. Opinion-driven sunsets break customers and erode API-team credibility.
- If the impact list contains a tier-1 customer, account-team alignment is a hard prerequisite; pause and route.
- Default to **soft deprecation** (headers + docs + outreach) for one full sunset window before any 410 Gone response. The 410 should be the last act, not the first.
- For surfaces with formal SLAs, check the contract before setting the sunset window; some SLAs mandate ≥180 days for any breaking change.
