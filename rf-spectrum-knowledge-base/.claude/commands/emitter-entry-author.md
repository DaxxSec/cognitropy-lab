# /emitter-entry-author — Author or Update a Canonical KB Entry

Author a new canonical knowledge-base entry for an identified emitter, or update an existing one, enforcing the entry schema and provenance rules.

## Inputs

- A draft entry (from `/kb-ingest-sweep`) or a manual description of the emitter
- Identification evidence: matched signature, decoded protocol, band-plan allocation, or an external reference (e.g. a Signal Identification Wiki entry)
- The existing canonical entry if this is an update

## Steps

1. **Resolve identity.** Decide whether the emitter is `confirmed`, `probable`, or `unidentified`. State the basis (signature match, band-plan allocation, decoded ID) and require at least one citation for anything above `unidentified`.
2. **Fill the schema.** Complete every required field from `context/references.md`: `id`, `name`, `freq_center`, `freq_range`, `bandwidth`, `modulation`, `access` (FDMA/TDMA/etc. if known), `service`, `region`, `occupancy`, `identification`, `confidence`, `provenance`, `citations`, `first_seen`, `last_seen`, `status`.
3. **Reconcile.** Cross-check the allocation against the band plan (suggest `/band-plan-sync` if the service/region looks inconsistent) and against the controlled vocabulary in `outputs/glossary.md` (add new terms via `/glossary-build`).
4. **Set lifecycle fields.** `first_seen` / `last_seen` from provenance; `status` = `active` | `intermittent` | `historical`; a `review_by` date proportional to how volatile the band is.
5. **Write and link.** Save to `outputs/kb/<freq>-<slug>.md`, remove the promoted draft from `_drafts/`, and add bidirectional `related` links to neighbouring or harmonically-related entries.

## Output

A canonical entry file in `outputs/kb/` that passes `/kb-audit`, plus a one-line changelog appended to the entry's history block (`created` or `updated: <field> <old>→<new>`).

## Notes

- Confidence language must match evidence: do not write "confirmed" for a band-plan guess. Reserve `confirmed` for a decoded identifier or an unambiguous signature match.
- An update must preserve history — append, don't overwrite, so drift over time stays visible.
- If two candidate identities fit, record both as `probable` alternatives rather than silently picking one.
