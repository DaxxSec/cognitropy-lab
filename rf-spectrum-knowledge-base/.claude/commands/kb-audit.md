# /kb-audit — QA the Knowledge Base for Integrity

Run a full quality-assurance pass over the knowledge base: schema compliance, citation integrity, internal contradictions, and staleness. The gate that keeps the KB trustworthy.

## Inputs

- The KB at `outputs/kb/`, FAQ, glossary, and query log
- The entry schema and controlled vocabulary from `context/references.md` and `outputs/glossary.md`

## Steps

1. **Schema check.** For every entry verify all required fields are present and well-typed (frequencies numeric + plausibly ordered `low ≤ center ≤ high`, dates ISO-8601, `confidence` in the allowed set, provenance non-empty).
2. **Citation integrity.** Confirm every claim above `unidentified` has a citation; resolve internal `[kb:…]` links and external references; flag dangling links and entries asserting `confirmed` with no source.
3. **Contradiction scan.** Find entries that overlap in frequency/region but assert incompatible services or identities; find FAQ answers that disagree with their cited entry; find glossary terms used inconsistently.
4. **Staleness & lifecycle.** Flag entries past `review_by`, `active` entries not seen in recent sweeps, and drafts in `_drafts/` older than a threshold (stuck triage).
5. **Score and report.** Compute a KB health score (weighted defect counts) and write a prioritized fix list, distinguishing blocking defects (broken schema, uncited "confirmed") from advisory ones (mild staleness).

## Output

`outputs/kb-audit-<date>.md`: defect table (entry, defect class, severity, fix), the health score with trend vs. the previous audit, and a "fix first" shortlist. Exit-style summary line: `AUDIT: <n> blocking, <m> advisory`.

## Notes

- Treat an uncited `confirmed` identity as a blocking defect — it's exactly the unsupported-confidence failure this workspace exists to prevent.
- Run before any FAQ publication or external sharing; a contradiction shipped to stakeholders is expensive to walk back.
- Track the health score over time — a slowly rising defect count signals the curation cadence isn't keeping up with ingest.
