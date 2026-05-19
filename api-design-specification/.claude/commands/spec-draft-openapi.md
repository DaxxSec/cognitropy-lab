# /spec-draft-openapi

Convert a resolved fusion brief into an OpenAPI 3.1 specification, preserving per-element provenance as `x-provenance` annotations. Runs after `/fuse-requirements` and any required `/contradiction-resolve` rounds.

## Inputs

- **Fusion brief** path — e.g. `outputs/fusion/orders-v3.md`.
- **All resolved adjudications** for any `CONFLICT` blocks in the brief.
- **Target spec file** path — default `outputs/spec/<resource>.yaml`.
- **Target OpenAPI version** — default `3.1.0`.

## Steps

1. **Verify resolution.** Walk the brief's conflict register. If any conflict is still `OPEN`, refuse to draft and emit the unresolved list. Do not produce a half-fused spec.
2. **Stub the document.** Emit `openapi: 3.1.0`, `info`, `servers`, `tags`, then empty `paths` + `components` + `security` blocks.
3. **Draft each path operation.** For each path/method in the brief's Phase 4 table:
   - Emit `summary`, `description`, `operationId`, `tags`, `parameters`, `requestBody`, `responses`, `security`.
   - Attach `x-provenance` listing the contributing claims (compact form: `[{source, reliability, claim_ref}]`).
   - Attach `x-fusion-reliability: <aggregate A1/B2/etc.>` summarising the operation's confidence.
4. **Draft schemas under `components.schemas`.** Each schema gets its own `x-provenance` and `x-fusion-reliability`. Use `$ref` aggressively — don't inline duplicate schemas.
5. **Draft error envelopes.** Default to RFC 9457 Problem Details (`application/problem+json`) unless an adjudication memo explicitly overrides. Add the type-URI registry stub if the surface has one; link from each error response.
6. **Security schemes.** Stamp the agreed schemes under `components.securitySchemes` and reference per operation.
7. **Lint preview.** Run a quick syntactic check (e.g. `redocly lint <file>` or `spectral lint <file> --ruleset base`). Note any failures inline in the spec as `# TODO:` comments — do not silently fix linter findings; they may reflect real adjudications.
8. **Cross-link back to the brief.** At the top of the YAML, add a header comment: `# fusion-brief: outputs/fusion/<resource>.md` and `# generated: <date>`.

## Output

`outputs/spec/<resource>.yaml` — a valid OpenAPI 3.1 document with every operation, schema, and response carrying `x-provenance`. The file is review-ready; the fusion brief and adjudication memos are the supporting evidence.

## Notes

- **Never strip `x-*` extensions in downstream tooling.** Pin the doc generator / merger to one that preserves vendor extensions. The provenance trail is the workspace's value proposition.
- For very large surfaces, emit `paths` as `$ref` to per-resource files (e.g. `paths.yaml#/...`) so the diff for any single resource stays small.
- Webhooks land under top-level `webhooks` (3.1 native), not `paths`. Same provenance discipline applies.
- If the brief specifies an unusual content-type (`text/event-stream`, `multipart/mixed`), emit it explicitly and double-check the linter understands it (Spectral does; older tooling may not).
