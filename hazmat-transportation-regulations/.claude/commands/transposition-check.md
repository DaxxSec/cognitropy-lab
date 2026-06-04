# /transposition-check

Detect digit-transposition and substitution errors in UN numbers and container numbers — the codebreaker's edit-distance attack on a transcription error that silently rekeys the message to a different substance.

## Inputs

- A UN number (and the named substance / PSN on the paper), and/or an ISO 6346 container number.
- The governing regulation / codebook edition.

## Steps

1. For a UN number: confirm it exists in the Dangerous Goods List. If it does, check that its codebook substance matches the named PSN.
2. If it does not exist, or the substance disagrees with the PSN, enumerate the **edit-distance-1 neighbours** (single transposition or single-digit substitution) that *do* exist.
3. For each neighbour, test PSN plausibility against the named substance (e.g. paper says "gasoline," 1230=methanol, neighbour 1203=gasoline → transposition found).
4. For a container number: compute the ISO 6346 check digit (letters A=10…Z=38 skipping ÷11; weights 2^position; sum mod 11, 10→0) and compare to the stated check digit.
5. Report the most plausible intended value with the evidence, or confirm no transposition.

## Output

A transposition report at `outputs/transposition-<ref>-<date>.md`: the suspect value, the edit-distance neighbours considered, the PSN/check-digit evidence, and the most-likely-intended value (or "no error found").

## Notes

- A transposition that lands on another *valid, plausible* UN number is the dangerous case — it passes a naive existence check but means the wrong substance and ERG guide.
- Quantity fields transpose too (1,200 ↔ 2,100 kg); flag round-trip-implausible quantities for confirmation.
