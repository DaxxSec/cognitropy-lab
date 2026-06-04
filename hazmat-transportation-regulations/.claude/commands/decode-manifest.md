# /decode-manifest

Decode every line of a dangerous goods declaration against the codebook and run the cross-field consistency "checksum" — the first-pass attack on a shipment's paperwork.

## Inputs

- A shipping paper / dangerous goods declaration / manifest / air waybill (text, PDF, or photo).
- The transport mode and jurisdiction (road/rail/sea/air; HMR/ADR/RID/IMDG/IATA).
- The codebook edition to decode against (49 CFR 172.101 edition or UN Model Regs / modal regulation version).

## Steps

1. Establish scope: record mode, jurisdiction, governing regulation, and codebook edition (gating — wrong regulation invalidates the decode).
2. For each line, extract the key (UN number) and the claimed basic description (PSN, class, subsidiary risk, PG).
3. Crib-expand each UN number against the codebook to its expected plaintext (delegates to `/codebook-crossref` logic).
4. Run the consistency checksum: diff expected vs claimed across PSN, class, subsidiary risk, PG, labels, placards, ERG guide; verify the 24-hour emergency phone and certification are present.
5. Mark each line `PASS` / `FAIL` / `FLAG` with the specific disagreeing field(s) and citation.

## Output

A decoded manifest table at `outputs/manifest-decode-<ref>-<date>.md`: one row per line item with claimed vs codebook-expected fields side by side, the verdict, and a summary of fails/flags. Codebook edition cited in the header.

## Notes

- The PSN may be a listed synonym, but never a trade name alone — "trade name only" is a FAIL.
- A generic "n.o.s." entry (e.g. UN 1993) requires the technical name in parentheses; its absence is a documentation FAIL.
- Treat any unresolved disagreement as the *more hazardous* interpretation until corrected.
