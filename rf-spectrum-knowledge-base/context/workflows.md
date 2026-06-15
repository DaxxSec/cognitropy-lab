# Workflows — The Spectrum Knowledge-Base Lifecycle

The defining technique of this workspace is **knowledge base and FAQ generation**. That technique is not a single step — it's a lifecycle that turns transient sweeps into a durable, self-correcting corpus. The phases below run in a loop; each daily/weekly cycle adds knowledge and pays down knowledge debt.

```
   ┌──────────────────────────────────────────────────────────────┐
   │                                                                │
   ▼                                                                │
[1 INGEST] → [2 IDENTIFY] → [3 AUTHOR] → [4 CURATE] → [5 PUBLISH]  │
                                                          │          │
                                                          ▼          │
                                                    [6 MAINTAIN] ────┘
                                                  (gap-scan feeds the
                                                   next ingest's targets)
```

## Phase 1 — Ingest

**Goal:** every capture becomes structured drafts, nothing is lost to a forgotten PNG.

1. Run a sweep (or import a `hackrf_sweep` / `rtl_power` CSV / IQ recording) **with full capture metadata**.
2. `/kb-ingest-sweep` — threshold against the noise floor, cluster detections, measure each, match against existing entries.
3. Each detection becomes a **draft** in `outputs/kb/_drafts/`: an `update` to an existing entry, or a `new` (often `unidentified`) draft.

**Decision — new vs. update:** does the detection's frequency range overlap an existing entry's, with compatible bandwidth? Yes → update (note any parameter drift). No → new draft.

## Phase 2 — Identify & enrich

**Goal:** move drafts up the confidence ladder.

1. For each draft, work cheap → expensive cues (see `concepts.md`): allocation → waterfall shape → parameters → decode.
2. Match the fingerprint against catalogs (sigidwiki) and against existing `/signature-card`s.
3. Rule out **receiver artifacts first** — image, harmonic, intermod, spur — before treating a detection as a real new emitter.

**Decision — identification routing:**
- Decoded identifier or unambiguous signature → `confirmed`.
- Fits allocation / partial signature only → `probable`.
- Nothing fits → keep `unidentified`, and let `/gap-scan` queue it for a targeted recapture or research.

## Phase 3 — Author the canonical entry

**Goal:** a schema-compliant, cited, canonical entry.

1. `/emitter-entry-author` — fill every required schema field, set confidence to match the evidence, attach provenance and citations.
2. `/signature-card` — generate the recognition card for the top of the entry, with at least one discriminator vs. a look-alike.
3. `/band-plan-sync` (periodically) — reconcile the entry's service/region against the authoritative allocation; resolve discrepancies.

**Rule:** no entry above `unidentified` without a citation; confidence language must match evidence; updates append history, never overwrite.

## Phase 4 — Curate (pay down knowledge debt)

**Goal:** keep the corpus coherent as it grows.

1. `/entry-dedup-merge` — collapse duplicate drafts promoted twice; link variants rather than merging them; leave tombstone redirects for absorbed entries.
2. `/glossary-build` — harvest new terms into the controlled vocabulary, register aliases, flag non-preferred usage.
3. `/kb-audit` — schema, citation integrity, contradictions, staleness. Treat uncited `confirmed` and broken citations as **blocking**; fix before publishing.

## Phase 5 — Publish & answer

**Goal:** the KB becomes useful to humans.

1. `/faq-generate` — cluster the query log by topic, draft grounded answers (cite entries), structure into sections, mark unanswerable questions OPEN.
2. `/kb-query` — answer individual questions grounded in the KB, with citations or an explicit abstain. Every exchange is logged to seed the next FAQ.

**Decision — answer vs. abstain (the core discipline):**
```
retrieve entries by frequency overlap, then service/keyword
   │
   ├─ entries sufficiently support the answer? ── yes ─→ answer + inline citations + confidence
   │
   └─ no / partial ─→ ABSTAIN: state what is/isn't known,
                       emit an OPEN question → /gap-scan
                       (never fill from general knowledge)
```

## Phase 6 — Maintain (and close the loop)

**Goal:** stop silent rot; aim the next cycle.

1. `/gap-scan` — tile the coverage target, mark `covered`/`thin`/`dark`; collect `unidentified`/`probable` entries, stale entries past `review_by`, and OPEN questions; prioritize by `impact × tractability`.
2. The top **dark-band** gaps and unresolved unknowns become the **priority frequencies for the next Phase-1 sweep** — closing the loop.
3. Re-run `/kb-audit` periodically and track the health-score trend; a rising defect count means curation isn't keeping pace with ingest.

## Cadence guidance

| Activity | Trigger / cadence |
|----------|-------------------|
| `/kb-ingest-sweep` | Every capture session |
| `/emitter-entry-author`, `/signature-card` | Per identified draft |
| `/entry-dedup-merge` | After every large ingest |
| `/band-plan-sync` | Weekly, or when allocations change |
| `/faq-generate` | After any significant ingest |
| `/gap-scan` | Weekly — produces next sweep's targets |
| `/glossary-build`, `/kb-audit` | Weekly, and always before external sharing |
