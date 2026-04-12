# /compare-known — Compare Against Known Protocols

Compare captured signal characteristics against known protocol databases.

## Required Inputs
- Signal params: frequency, bandwidth, modulation, symbol rate
- Frame structure if decoded: preamble, sync word, payload length

## Steps

### 1. Build Fingerprint
Extract comparison vector from frequency, modulation, rate, frame structure, CRC, duty cycle.

### 2. Database Search
Check: rtl_433 protocol list (200+), known-protocol-signatures.md, ISM band conventions, FCC ID database.

### 3. Similarity Scoring
For each candidate:
- freq: 1.0 exact, 0.5 within ISM band
- mod: 1.0 exact type+params, 0.5 same type
- rate: 1.0 within 5%, 0.5 within 20%
- frame: 1.0 sync match, 0.5 structure similar
- total = freq*0.15 + mod*0.25 + rate*0.25 + frame*0.35

### 4. Validate
For scores > 0.6: attempt known decoder, check CRC, compare fields. Confidence: HIGH >0.85, MEDIUM 0.6-0.85, LOW <0.6.

### 5. Report
Ranked candidates with scores and confidence. Novel protocol classification if no match.
