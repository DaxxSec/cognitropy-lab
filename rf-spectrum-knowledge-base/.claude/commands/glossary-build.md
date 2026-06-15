# /glossary-build — Maintain the Controlled-Vocabulary Glossary

Extract and maintain the controlled vocabulary / lightweight ontology of RF terms used across the knowledge base, so entries, the FAQ, and queries all speak the same language.

## Inputs

- The KB at `outputs/kb/`, the FAQ, and the query log (sources of terms in actual use)
- The existing `outputs/glossary.md` if present
- `context/references.md` for canonical definitions and unit conventions

## Steps

1. **Harvest terms.** Pull candidate terms from entry fields and prose: modulation/access schemes (FSK, GFSK, OFDM, DSSS, FHSS), measurement terms (occupied bandwidth, duty cycle, PSD, noise floor, ENBW), services, and acronyms.
2. **Canonicalize.** For each term pick one preferred label and register variants/abbreviations as `see also` aliases (e.g. "frequency-hopping spread spectrum" ↔ "FHSS"). Resolve casing and unit conventions (Hz/kHz/MHz, dBm vs. dBμV).
3. **Define and relate.** Write a one-line definition per term; add lightweight relations (`broader`/`narrower`/`related`) — e.g. GFSK `narrower-of` FSK. This is the ontology backbone retrieval and dedup lean on.
4. **Reconcile usage.** Flag entries/FAQ answers using a non-preferred label or an undefined term; suggest edits so the corpus converges on the controlled vocabulary.
5. **Write the glossary.** Emit alphabetized terms with definitions, aliases, and relations, plus a "new this pass" section.

## Output

`outputs/glossary.md` — alphabetized controlled vocabulary with definitions, aliases, and relations; an inconsistency list (non-preferred or undefined terms found in the corpus) routed back to `/emitter-entry-author` and `/faq-generate`.

## Notes

- The glossary powers `/kb-query` normalization — an analyst asking about "freq hopping" should hit FHSS entries; that only works if the alias is registered.
- Keep definitions tight and cite a standard (ITU-R, IEEE) where one exists; the glossary is a controlled vocabulary, not an encyclopedia.
- New terms should mostly arrive via this command, not be invented ad hoc inside entries — that's how vocabulary drift starts.
