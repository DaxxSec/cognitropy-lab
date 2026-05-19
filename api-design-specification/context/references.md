# API Design Specification — Reference Tables

Lookup data the agent reaches for during tasks. Compact by design; defer to upstream sources for fuller specs.

## HTTP Status Codes (Operational Subset)

| Code | Name | Typical API usage |
|------|------|-------------------|
| 200 | OK | Successful `GET` / non-creating `POST`. |
| 201 | Created | Resource created. Include `Location` header. |
| 202 | Accepted | Async work queued; not yet processed. |
| 204 | No Content | Successful `DELETE` / `PUT` with no body. |
| 206 | Partial Content | Range request fulfilment. |
| 301 | Moved Permanently | Permanent URL change. Update clients. |
| 304 | Not Modified | Conditional-GET cache hit (`If-None-Match`). |
| 307 | Temporary Redirect | Preserve method; transient redirect. |
| 308 | Permanent Redirect | Preserve method; permanent redirect. |
| 400 | Bad Request | Malformed syntax — body unparseable, missing required header. |
| 401 | Unauthorized | Missing / invalid authentication. Include `WWW-Authenticate`. |
| 403 | Forbidden | Authenticated but not permitted. |
| 404 | Not Found | Resource absent or hidden by ACL. |
| 405 | Method Not Allowed | Verb not supported on this URL. Include `Allow`. |
| 406 | Not Acceptable | Cannot satisfy `Accept`. |
| 409 | Conflict | State conflict (e.g. version mismatch, duplicate). |
| 410 | Gone | Permanent removal. |
| 412 | Precondition Failed | `If-Match` / `If-Unmodified-Since` mismatch. |
| 415 | Unsupported Media Type | Bad `Content-Type`. |
| 422 | Unprocessable Content | Syntactically valid but semantically wrong (validation failure). |
| 425 | Too Early | Replay protection for 0-RTT. |
| 428 | Precondition Required | Server requires `If-Match` (RFC 6585). |
| 429 | Too Many Requests | Rate-limited. Include `Retry-After`. |
| 451 | Unavailable for Legal Reasons | Censorship / legal removal. |
| 500 | Internal Server Error | Unhandled server fault. |
| 502 | Bad Gateway | Upstream returned invalid response. |
| 503 | Service Unavailable | Overload / maintenance. Include `Retry-After`. |
| 504 | Gateway Timeout | Upstream timeout. |

**400 vs 422 — house rule.** 400 for syntactic / structural problems (unparseable JSON, missing required field). 422 for semantic / business-rule violations (valid shape, invalid combination). Either is legal per RFC 7231 / RFC 4918; pick one rule per surface and enforce.

## OpenAPI 3.1 — Top-Level Cheat Sheet

| Field | Required | Purpose |
|-------|----------|---------|
| `openapi` | yes | Must be `3.1.x`. |
| `info` | yes | `title`, `version`, optional `summary`, `description`, `contact`, `license`. |
| `servers` | no | Base URLs with variable templating. |
| `paths` | one of paths/webhooks/components | URL templates → operations. |
| `webhooks` | one of paths/webhooks/components | Outbound events (3.1-native). |
| `components` | one of paths/webhooks/components | Reusable definitions. |
| `security` | no | Default security across operations; per-op overrides. |
| `tags` | no | Grouping for documentation rendering. |
| `externalDocs` | no | Outbound documentation link. |
| `jsonSchemaDialect` | no | Defaults to `https://spec.openapis.org/oas/3.1/dialect/base`. |

## JSON Schema 2020-12 Validation Keywords (Common Use)

| Category | Keywords |
|----------|----------|
| Type | `type`, `enum`, `const` |
| String | `minLength`, `maxLength`, `pattern`, `format` |
| Numeric | `minimum`, `maximum`, `exclusiveMinimum`, `exclusiveMaximum`, `multipleOf` |
| Array | `items`, `prefixItems`, `contains`, `minItems`, `maxItems`, `uniqueItems`, `minContains`, `maxContains` |
| Object | `properties`, `patternProperties`, `additionalProperties`, `unevaluatedProperties`, `required`, `propertyNames`, `minProperties`, `maxProperties` |
| Composition | `allOf`, `anyOf`, `oneOf`, `not` |
| Conditional | `if`, `then`, `else`, `dependentRequired`, `dependentSchemas` |
| References | `$ref`, `$dynamicRef`, `$defs` |
| Annotations | `title`, `description`, `examples`, `default`, `readOnly`, `writeOnly`, `deprecated` |

## RFC Index (Most-Cited)

| RFC | Title | Most relevant to |
|-----|-------|------------------|
| 9110 | HTTP Semantics | All HTTP behaviour (supersedes 7230–7235). |
| 9111 | HTTP Caching | Cache-Control, validators. |
| 9112 | HTTP/1.1 | Wire format. |
| 9113 | HTTP/2 | Wire format. |
| 9114 | HTTP/3 | Wire format. |
| 9457 | Problem Details for HTTP APIs | Error envelope. Supersedes 7807. |
| 8594 | Sunset HTTP Header | Deprecation signalling. |
| 8288 | Web Linking | `Link` header, pagination, relation types. Supersedes 5988. |
| 7234 / 9111 | HTTP Caching | (alias for completeness) |
| 6750 | OAuth 2.0 Bearer Token Usage | Auth header format. |
| 6749 | OAuth 2.0 Authorization Framework | Flows. |
| 7519 | JSON Web Token (JWT) | Token format. |
| 7591 | OAuth 2.0 Dynamic Client Registration | DCR. |
| 8414 | OAuth 2.0 Authorization Server Metadata | Discovery. |
| 6585 | Additional HTTP Status Codes | 428, 429, 431, 511. |
| 7240 | Prefer Header | Client preference signalling. |
| 5789 | PATCH Method | The PATCH verb itself. |
| 7396 | JSON Merge Patch | Simple merge-patch format. |
| 6902 | JSON Patch | Operation-list patch format. |
| 4180 | CSV media type | Tabular response media type. |
| 7159 / 8259 | JSON | (alias) |
| draft-ietf-httpapi-idempotency-key | Idempotency-Key Header | Opt-in POST/PATCH idempotency. |
| draft-ietf-httpapi-deprecation-header | Deprecation HTTP Header | Pair with Sunset. |

## Peer-Spec Catalogue (Fusion Source: Peer Specs)

| Peer | Spec source | Notes |
|------|-------------|-------|
| Stripe | https://github.com/stripe/openapi | Canonical reference for resource-oriented commerce APIs; explicit error envelope. |
| GitHub | https://github.com/github/rest-api-description | Comprehensive REST; older conventions intermixed with newer. |
| Twilio | https://www.twilio.com/docs/openapi | Telephony / messaging; webhook patterns. |
| Slack | https://api.slack.com/specs | Mix of REST + RPC; pagination conventions. |
| Square | https://github.com/square/square-openapi-specification | Commerce; idempotency-key first-class. |
| Atlassian | https://developer.atlassian.com/cloud/jira/platform/rest | Pagination, eventing. |
| Plaid | https://plaid.com/docs/api/ | Financial-data; opinionated error catalogue. |
| Shopify | https://shopify.dev/docs/api/admin-rest | Versioned resource API at scale. |

## Source Reliability — NATO STANAG 2022 (Replicated from `concepts.md` for Quick Lookup)

| Letter | Reliability | Rough API analogue |
|--------|-------------|--------------------|
| A | Completely reliable | OpenAPI 3.1 spec, IETF RFC. |
| B | Usually reliable | JSON:API, mature peer spec, internal corpus avg. |
| C | Fairly reliable | Telemetry from a recent window, single-source ticket pattern. |
| D | Not usually reliable | Outdated peer spec; small-sample telemetry. |
| E | Unreliable | Single anecdotal ticket; speculative stakeholder claim. |
| F | Reliability cannot be judged | Newly-onboarded source class. |

| Digit | Information credibility |
|-------|--------------------------|
| 1 | Confirmed by other sources |
| 2 | Probably true |
| 3 | Possibly true |
| 4 | Doubtful |
| 5 | Improbable |
| 6 | Truth cannot be judged |

## Operating Cheat-Sheets

### Pagination patterns (corpus tie-break crib)

| Pattern | When | Pros | Cons |
|---------|------|------|------|
| Cursor (`?cursor=opaque`) | Mutating sets, real-time feeds | Stable under writes; consistent | Hard to jump to arbitrary page |
| Offset (`?page=`+`?per_page=`) | Static reports, dashboards | Trivial to jump pages | Drift under concurrent writes |
| Link header (RFC 8288) | Per-standard alignment | Standards-aligned | Some clients struggle to parse |
| Keyset (`?after_id=`) | Append-only logs | Stable, fast | Requires sortable key |

### Auth scheme quick-pick

| Scheme | Use when |
|--------|----------|
| `bearerAuth` (JWT) | First-party SPAs/mobile; symmetric trust. |
| `oauth2` (authorisation_code + PKCE) | Third-party app delegation. |
| `oauth2` (client_credentials) | Service-to-service. |
| `apiKey` (header `X-API-Key` or `Authorization`) | Server-to-server, simple. |
| `mTLS` (`mutualTLS` 3.1) | High-trust B2B, regulated. |

### Idempotency rule of thumb

`POST` / `PATCH` accepting `Idempotency-Key` header → server stores the response keyed by `(idempotency_key, route, body_hash)` with a 24h TTL by default. Replays return the original response. Document the TTL in the spec.

## Upstream Catalogues

- **OpenAPI Initiative** — https://www.openapis.org/ — governance, releases, learning resources.
- **JSON Schema** — https://json-schema.org/ — drafts, tooling list.
- **IANA HTTP Status Code Registry** — https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml — authoritative codes list.
- **IANA Link Relation Registry** — https://www.iana.org/assignments/link-relations/link-relations.xhtml — `rel` values for `Link` header.
- **APIs.guru** — https://apis.guru/ — community-curated OpenAPI specs (hundreds of public APIs).
- **Spectral built-in rules** — https://docs.stoplight.io/docs/spectral/4dec24461f3af-open-api-rules — lint baseline.
