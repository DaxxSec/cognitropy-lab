# /verify-extraction

Verify the integrity and completeness of an acquisition: hash the image, cross-validate critical findings with a second tool, and check what the extraction actually unwrapped against the keybag.

## Inputs

- The acquired image/backup and its acquisition log (tool, version, timestamps).
- The expected class coverage from `/plan-extraction`.
- A second parsing/extraction tool for cross-validation.

## Steps

1. **Hash** the image/backup (SHA-256) at acquisition and again before analysis; record both and confirm they match (integrity).
2. **Completeness vs keybag** — determine which Data Protection classes were unwrapped; compare against the plan's expected coverage. Note any class that stayed sealed and why (e.g. BFU, no passcode).
3. **Dual-tool cross-validation** — parse a sample of critical artifacts (e.g. `sms.db` rows, timeline events) with a second tool; confirm the interpretations agree, and document any divergence.
4. **Schema/version sanity** — confirm the parser matches the device's iOS artifact schema (epoch handling, table layout) so timestamps aren't silently wrong.
5. **Record limitations** — anything not acquired or not validated goes in writing; an unverified finding is not a finding.

## Output

`outputs/verification-YYYY-MM-DD.md`: acquisition + pre-analysis hashes (matched Y/N), class-coverage completeness vs plan, dual-tool cross-validation results, schema notes, and an explicit limitations list.

## Notes

- Hashes prove the image didn't change; they say nothing about completeness — both checks are required.
- A single tool's parse of a key artifact is a hypothesis; cross-validation is what tests it.
