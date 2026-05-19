# /trace-provenance

Given any element in an existing OpenAPI document — a path, method, parameter, response, schema — produce the source chain that justifies it. Used for internal review, audit response, and incoming-engineer onboarding.

## Inputs

- **Spec file** path — e.g. `outputs/spec/orders-v3.yaml`.
- **Element JSONPath** — e.g. `paths./v3/orders.post.responses.422`, `components.schemas.Order.properties.status`, `paths./v3/orders.parameters[?(@.name=='cursor')]`.

## Steps

1. **Resolve the element.** Walk the JSONPath; if the element doesn't exist, abort with the closest match and let the caller correct the path.
2. **Collect the `x-provenance` chain.** Start at the element; walk upwards (operation → path → tag → document) collecting every `x-provenance` block. Apply most-specific first.
3. **Resolve `$ref` chains.** If the element is a `$ref`, traverse the reference and collect provenance from the target as well.
4. **De-duplicate.** Multiple ancestors may have cited the same source; report each source class once with the union of the contributing claims.
5. **Look up source-class details.** Cross-reference each claim against the source dossier (`outputs/sources/<surface>-<date>.md`) for that surface to print the reliability rating and access path.
6. **Find related adjudications.** If the element is mentioned in any `outputs/adjudication/*.md`, link them.
7. **Emit the report.** Markdown with header `# Provenance trace: <jsonpath>`, then sections per source class with claim → source-handle → rating → adjudication-link.

## Output

`outputs/traces/<spec>-<element-slug>-<date>.md` containing:

- The element value (extracted from the spec).
- The provenance chain (most-specific → most-general).
- Each contributing claim with rating and source handle.
- Linked adjudications (if any).
- A "Gaps" section listing any elements in the chain that lacked `x-provenance`.

## Notes

- A gap in the chain (no `x-provenance`) on a recent element points at tooling that stripped extensions; investigate the pipeline.
- A gap on a legacy element pre-dating fusion is expected; mark for re-fusion in the next hygiene sweep (Workflow 5).
- If an element's most-specific provenance contradicts an ancestor's, the most-specific wins for the trace; flag the contradiction at the bottom of the report.
- This command should run in seconds. If your spec is so large that traces are slow, split the spec into per-resource files (see notes on `/spec-draft-openapi`).
