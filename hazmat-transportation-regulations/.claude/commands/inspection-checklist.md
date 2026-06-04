# /inspection-checklist

Assemble the standardized, mode-specific dangerous-goods documentation inspection checklist, run it, and record an auditable pass/fail result — the technique that turns every decode into a numbered, reproducible, CVSA-style line item.

## Inputs

- The shipment under inspection and any decode artifacts already produced (`/decode-manifest`, `/codebook-crossref`, `/placard-decipher`, `/segregation-conflict`, `/undeclared-crib` outputs).
- Mode and jurisdiction (selects the checklist template).
- Inspector identity / reference and codebook + checklist version.

## Steps

1. Select the mode-specific checklist template (road/rail/sea/air) and stamp the codebook edition and checklist version.
2. Populate the standardized items in order: basic description complete & correctly ordered; UN/PSN/class/PG cross-field consistent; subsidiary risks shown; labels/placards match; emergency phone present & plausible; ERG/emergency info correct; segregation compatible; no undeclared crib hits; certification signed.
3. For each item, record the verdict (`PASS` / `FAIL` / `FLAG` / `N/A`) with the supporting evidence and citation.
4. Apply the out-of-service mapping: any documentation-OOS-equivalent FAIL means the shipment must not move until corrected.
5. Produce the signed, dated inspection record with an overall disposition.

## Output

A standardized inspection record at `outputs/inspection-<ref>-<date>.md`: the full checklist with per-item verdicts, evidence, citations, the OOS determination, and an overall disposition (`CLEARED` / `HOLD` / `OUT OF SERVICE`). Designed so a second inspector re-running the same checklist reproduces the result.

## Notes

- The checklist is the *deliverable* — a decode that isn't recorded as a checklist item didn't happen, for audit purposes.
- Keep the item order fixed across inspections so records are comparable over time and across inspectors.
- Cite versions: a record is only reproducible if the codebook edition and checklist version are on it.
