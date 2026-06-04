# /codebook-crossref

Crib-expand a single UN number into its complete expected plaintext from the Dangerous Goods List, then diff it against what the paper claims — a known-plaintext attack on one entry.

## Inputs

- One UN number (the key).
- The claimed basic description for that entry (PSN, class, PG) as written on the paper.
- Codebook edition / modal regulation.

## Steps

1. Look up the UN number in the Dangerous Goods List for the governing regulation.
2. Retrieve the full expected plaintext: PSN, hazard class/division, subsidiary risk(s), packing group, labels, placards, special provisions, packing instructions, limited/excepted quantity, and ERG guide number.
3. Diff each expected field against the paper's claim.
4. Classify each field: `match`, `synonym-ok`, `mismatch`, or `missing`.
5. If any mismatch changes the hazard profile (class, subsidiary risk, ERG guide), state both the declared and the codebook substance explicitly.

## Output

A single-entry crossref card at `outputs/crossref-UN<num>-<date>.md`: the full codebook plaintext, the paper's claim, the per-field diff, and a verdict line. Suitable for pasting into an inspection record.

## Notes

- A UN number has no check digit; its only validation is this codebook cross-reference plus PSN plausibility.
- If the UN number is not in the list at all, route to `/transposition-check` before concluding it is invalid.
