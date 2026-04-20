# Constraints

## Data handling
- **No real PII in committed files.** All examples and templates use placeholder IDs (SUBJ-NNNN), placeholder dates, and generic locations.
- **CUI / FOUO markings** — if the user pastes in CUI material for analysis, output must be marked accordingly and stored under `outputs/` (git-ignored in practice for real use).
- **No authoritative system integration.** Do not suggest, generate, or attempt code that talks to DISS, NBIS, Scattered Castles, or equivalent. This workspace is a reasoning aid only.
- **Attorney-client and privilege considerations** — if the user is adjudicating or coordinating with general counsel on a specific case, flag that draft output may become discoverable. Recommend consulting counsel before generating a final memo.

## Authority boundaries
- The agent **suggests**; the human **decides**.
- Adjudicative determinations are reserved to the cognizant adjudicative authority.
- Nothing produced here substitutes for a Statement of Reasons, the subject's Reply, or Personal Appearance.
- Continuous Vetting alerts may trigger action, but the action taken is always the human's call under the governing EOs and agency policy.

## Technical constraints
- Keep CLAUDE.md lightweight (<50 lines). Everything substantive goes under `context/for-agent/`.
- Use structured (YAML/JSON) artifacts where downstream tooling or trending will read them.
- Never embed secrets, tokens, API keys, or real subject identifiers in any file that could be pushed to a public repo.

## Modeling constraints
- Risk scores are **analyst guidance**, not determinations.
- The rubric in `resources/risk-scoring-rubric.md` is editable per agency. Document any changes in `work-log/`.
- When trending, preserve a history of at least 8 scans per subject so drift is visible.
