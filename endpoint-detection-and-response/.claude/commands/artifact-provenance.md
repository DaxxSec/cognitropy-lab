# /artifact-provenance — Trace an Artifact's Lineage & Find-Context

Establish where a single endpoint artifact came from, how it arrived, and its lineage — the EDR equivalent of sourcing an extant garment and documenting its find-context.

## Inputs

- The artifact: a file path + hash, a process (PID/GUID), a registry key, or a scheduled task.
- Available telemetry sources (Sysmon, Amcache, Prefetch, EDR backend) and the investigation time window (UTC).
- Optional: the host's known baseline / gold image for comparison.

## Steps

1. **Identify the artifact** unambiguously: SHA-256, full path, signer, and the first-seen timestamp across every available source (Amcache, Prefetch, EDR first-execution).
2. **Walk the lineage backward**: parent process → grandparent → … to the initial-access vector (browser, mail client, archive, remote service). Record each link's evidence and a confidence tag.
3. **Establish find-context**: which user/session, which path, was it dropped/downloaded/copied, and what touched it immediately before and after.
4. **Compare to baseline**: is this artifact expected on a gold-image host? Note presence/absence and path legitimacy.
5. **Score provenance confidence** per link (`CONFIRMED` / `INFERRED` / `CONJECTURE`) and flag any link that rests on a single uncorroborated source.

## Output

A provenance chain written to `outputs/provenance-<artifact>-<date>.md`: ordered lineage from initial access to the artifact, each link tagged with confidence and backing telemetry, plus a "find-context" header and a baseline-deviation note.

## Notes

- A provenance link with no corroboration is conjecture; say so explicitly rather than drawing the arrow solid.
- Resolve and hand off to `/anachronism-sweep` before treating any first-seen timestamp as fact.
