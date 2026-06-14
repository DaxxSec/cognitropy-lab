# /provenance-trace

Reconstruct a calibration's origin story — VIN, market, calibration lineage, and reflash history — the way a conservator documents a specimen's accession record. Establishes *where this cal came from* before you decide what to do with it.

## Inputs

- VIN (and/or the module's CAL-ID + CVN)
- A specimen image or cal file of uncertain lineage
- (Optional) prior service history, an existing reference-collection match

## Steps

1. **Decode the VIN.** WMI/VDS/VIS → make, model, year, assembly plant, and **market of manufacture** (use the vPIC API or an offline decoder).
2. **Read the cal identity.** Record CAL-ID (Mode 09/04) and CVN (Mode 09/06); note OS/strategy and ECU HW/SW numbers.
3. **Compare to known-good.** Query `/reference-collection` for a matching factory CAL-ID; flag whether the CVN matches a stock value (→ untouched) or not (→ previously reflashed/edited).
4. **Infer the geography.** From VIN market + CAL-ID, determine the cal's intended **emissions regime, fuel grade, and altitude assumption**.
5. **Detect mismatches.** Flag gray-market signals (e.g. Euro-market ECU on a US-registered car), VIN↔CAL-ID inconsistencies, or evidence of a prior non-OEM flash.

## Output

A `outputs/provenance-<vin>.md` accession record: decoded VIN, identifiers, stock-vs-modified verdict, inferred origin geography, and any mismatch flags — feeding `/region-cal-map` and `/emissions-legality-gate`.

## Notes

- A non-matching CVN doesn't prove tampering by itself — but it means "this is not the untouched factory specimen," which changes the restoration baseline.
- Provenance gaps are findings, not failures: document what you *couldn't* establish.
