# /standards-alignment

Measure a drafted spec's conformance to current standards (OpenAPI 3.1, JSON Schema 2020-12, RFC 9457, RFC 8288, RFC 7234/9111) and produce a remediation list. Runs before every internal review and before publishing externally. Designed to catch unconscious drift, not to overrule deliberate adjudications.

## Inputs

- **Spec file** path — e.g. `outputs/spec/orders-v3.yaml`. Accepts a directory to scan a whole catalogue.
- **Adjudication directory** — `outputs/adjudication/` — used to whitelist deliberate deviations.

## Steps

1. **Parse the spec.** Confirm `openapi: 3.1.x`. If the file is 3.0.x, flag immediately — `nullable: true` and other 3.0 idioms cannot be checked under 3.1 rules.
2. **OpenAPI 3.1 conformance.** Run Spectral with the `oas` ruleset (or Redocly's lint), capture findings. Particularly check:
   - `nullable: true` usage (3.0 vestige; should be `type: ["x", "null"]`).
   - `openapi` version field.
   - Required `info.title` and `info.version`.
   - At least one of `paths`, `webhooks`, `components` populated.
   - `$ref` targets resolve.
3. **JSON Schema 2020-12 alignment.** For each schema:
   - `$schema` declared correctly (if present).
   - Composition keywords used per 2020-12 semantics (`unevaluatedProperties` rather than the 3.0 workaround).
   - `discriminator` paired with `oneOf` / `anyOf` where polymorphism is intended.
4. **Error envelope (RFC 9457).** For each `4xx` / `5xx` response, confirm content-type `application/problem+json` and schema with required `type`/`title`/`status`/`detail`/`instance` fields. Flag legacy hand-rolled envelopes (`{ code, message }`) unless an adjudication memo explicitly overrides.
5. **Pagination (RFC 8288 if used).** If `Link` header pagination is in use, confirm relation types are from the IANA registry. If cursor/offset is used, confirm consistency across the surface.
6. **Caching (RFC 9111).** For each `GET`, check for `Cache-Control` documented response header where appropriate. Conditional-request headers (`ETag`, `Last-Modified`) checked on resources where corpus convention applies.
7. **HTTP method semantics (RFC 9110).** Confirm idempotent methods only have `2xx`/`3xx`/`4xx` for non-side-effecting paths; `POST` allowed `200/201/202/204`; sanity-check status code choice against the operation summary.
8. **Whitelist adjudicated deviations.** For each finding, check whether an adjudication memo in `outputs/adjudication/` covers it. If yes, demote to `note`; if no, keep as `finding`.
9. **Emit the report.** Write `outputs/standards-alignment/<spec>-<date>.md` listing findings sorted by severity (`error` / `warning` / `note`), each with: rule, location (JSONPath), excerpt, suggested remediation, whitelisting status.

## Output

`outputs/standards-alignment/<spec>-<date>.md` — the remediation list. Designed to be triaged into a PR or a backlog ticket.

## Notes

- This command does not auto-fix. Findings often look like simple fixes but reflect intentional adjudications upstream; review before patching.
- Run this command quarterly as the hygiene pass (Workflow 5), not just on draft.
- If a finding is rejected as a permanent deviation, write a fresh adjudication memo and re-run; the second run will whitelist it.
- A spec with zero findings is suspicious unless the surface is trivial; either the linter is mis-configured or someone is silently auto-fixing.
