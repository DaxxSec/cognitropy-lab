# /band-plan-sync — Reconcile the KB Against an Authoritative Band Plan

Compare the knowledge base's emitter entries against an authoritative frequency allocation table (ITU Region, national regulator) and flag every discrepancy.

## Inputs

- Region(s) of interest (ITU Region 1/2/3, and/or a national regulator — FCC/NTIA, Ofcom, BNetzA, etc.)
- An allocation source: a band-plan table/CSV, or the reference links in `context/references.md`
- The KB at `outputs/kb/`

## Steps

1. **Load the allocation table.** Normalize it to `(freq_low, freq_high, service, region, allocation_type)` rows. Allocation type = primary / secondary / unallocated / ISM.
2. **Map each entry.** For every KB entry, find the allocation block(s) its `freq_range` falls in and the service(s) allocated there.
3. **Classify discrepancies.** For each entry flag one of: `consistent` (observed service matches allocation), `out-of-band` (emitter where nothing is allocated, or an ISM device leaking outside ISM), `service-mismatch` (e.g. an entry tagged "broadcast" sitting in an aeronautical block), `region-mismatch` (allocation differs by region and the entry's region tag is wrong), or `unallocated-activity` (signal in a guard/unallocated segment — high triage value).
4. **Explain, don't auto-edit.** For each non-consistent entry, write the conflict, the most likely benign explanation (harmonic, spur, image, mislabeled region) and the action (re-measure, re-identify, correct region tag).
5. **Emit the reconciliation report** and suggest specific `/emitter-entry-author` edits for the clear-cut corrections.

## Output

`outputs/band-plan-sync-<region>-<date>.md`: a table of every entry with its allocation, discrepancy class, and recommended action; a summary count by class; and a short list of "unallocated-activity" emitters worth investigating first.

## Notes

- Receiver artifacts masquerade as out-of-band signals: images (at `2·LO ± f`), harmonics (`n·f`), and intermodulation products. Rule these out before declaring a real out-of-band emitter.
- ISM bands (e.g. 433 MHz, 868/915 MHz, 2.4 GHz) host a crowd of unlicensed devices; expect many entries and reconcile by device class, not single allocation.
- Allocations differ by ITU region — always tag the region; the same frequency can be broadcast in one region and mobile in another.
