# HAZMAT Transportation Regulations — Workflows and Methodology

How the agent actually *works* a shipment. Everything here is built around the engine technique for this build — **standardized inspection checklists** — so that decoding is a numbered, repeatable, pass/fail procedure rather than a freeform read. `concepts.md` says what the symbols mean; this file says what the agent does with them.

## The standardized documentation-inspection pipeline

Five phases, run in order. Each phase emits checklist line items with an explicit verdict (`PASS` / `FAIL` / `FLAG` / `N/A`) and a citation to the codebook edition used. The pipeline mirrors how a cryptanalyst attacks a message: collect → key → decode → cross-check → exploit.

### Phase 1 — Collect & scope
Capture the artifact (shipping paper, manifest, air waybill, placard photo). Record **mode** (road/rail/sea/air), **jurisdiction**, and therefore the **governing regulation** (HMR / ADR / RID / IMDG / IATA). Record the **codebook edition** you will decode against. Wrong regulation = wrong decode, so this is a gating item.

### Phase 2 — Key extraction
For each line, extract the **UN number** (the key) and the claimed basic description (PSN, class, PG). If the UN number is missing, illegible, or implausible, route to `/transposition-check` before proceeding — you cannot decode without a valid key.

### Phase 3 — Codebook decode
Run the known-plaintext expansion (`/codebook-crossref`): for each UN number, retrieve the *expected* PSN, class, subsidiary risk, PG, labels, placards, special provisions, and ERG guide from the Dangerous Goods List.

### Phase 4 — Cross-field consistency (the checksum)
Diff the expected plaintext against the paper (`/decode-manifest`). The fields are mutually constraining; any disagreement is a corrupt message:
- PSN must match the UN number's listed name (synonyms allowed; trade names are not PSNs).
- Class/division and subsidiary risk must match the labels and placards.
- PG must be one the class permits (and present only when the class uses PGs).
- ERG guide must be the one the UN number maps to.
- The 24-hour emergency phone and emergency-information source must be present and plausible.

### Phase 5 — Collective & exploit checks
The message is more than its lines. Run traffic analysis across the whole load (`/segregation-conflict`), crib-drag the goods descriptions for undeclared hazards (`/undeclared-crib`), and — for a corpus — run frequency and entropy screening (`/frequency-profile`, `/anomaly-entropy`). Then assemble the standardized record (`/inspection-checklist`).

## Workflow 1: Single-shipment decode-and-verify

**Goal:** Determine whether one shipment's paperwork is internally consistent and codebook-correct.

### Steps
1. Run Phase 1 (scope + codebook edition).
2. Extract keys (Phase 2); transposition-check any doubtful UN number.
3. `/codebook-crossref` each UN number for its expected plaintext.
4. `/decode-manifest` to run the cross-field consistency checksum and list every disagreement.
5. `/placard-decipher` if a placard/orange-plate photo exists; reconcile with the paper.
6. Assemble the record with `/inspection-checklist`; write to `outputs/`.

### Decision points
- If the UN number resolves to a *different* substance than the PSN → **FAIL** (misdeclaration or transposition); record both candidates and the ERG-guide divergence.
- If labels/placards contradict the class → **FAIL**; the visible hazard governs an inspector's safety response.
- If a required field (emergency phone, PG where required, certification) is absent → **FAIL** (incomplete documentation).
- If everything reconciles → **PASS**, with the codebook edition cited.

## Workflow 2: Corpus screening to target inspections

**Goal:** Out of many manifests, find the few worth a human's time.

### Steps
1. Build/refresh the baseline with `/frequency-profile` (class, UN, PG, shipper, lane distributions).
2. Run `/anomaly-entropy` across the batch for fabrication tells (duplicate strings, round quantities, placeholder fields).
3. Rank shipments by combined outlier + anomaly score.
4. Route the top of the ranked list into Workflow 1.

### Decision points
- If a shipment is a frequency outlier *and* carries an entropy tell → top priority for physical inspection.
- If it is a frequency outlier but the codebook decode is clean → likely a legitimate one-off; note and de-prioritise.
- If the whole corpus's entropy is uniformly low → suspect a template-generated set; widen the sample.

## Workflow 3: Undeclared-goods crib hunt

**Goal:** Expose dangerous goods hidden inside a benign-sounding description.

### Steps
1. Tokenise the plain-language goods/commodity description.
2. Crib-drag against the known-hazard crib list in `references.md` ("power bank" → UN 3480; "aerosol" → UN 1950; "pool shock" → 5.1 oxidizer; "dry ice" → UN 1845; "perfume/nail polish" → UN 1266).
3. For each hit, check whether the declaration actually declares that UN number / class.
4. Where a crib hits but nothing is declared → **FLAG undeclared**; cite the mode's rule (e.g. air transport of lithium batteries) and escalate to physical verification.

### Decision points
- If the crib is ambiguous (could be exempt — e.g. small consumer quantities) → FLAG with the exemption to verify, not a hard FAIL.
- If the commodity is a known embargo-dodge target (lithium batteries, fireworks, fuel) → escalate regardless of declared quantity.

## Out-of-service / escalation decision tree

Standardized checklists carry an out-of-service (OOS) concept (CVSA). Map findings to action:
- **Documentation OOS-equivalent** — missing/contradictory basic description, no emergency phone, undeclared DG, prohibited segregation: shipment **must not move** until corrected; record as FAIL with the regulatory citation.
- **FLAG (verify)** — frequency outlier, entropy tell, ambiguous crib, placard/paper mismatch pending re-check: hold for documentary or physical inspection; not yet a violation.
- **PASS** — full cross-field reconciliation against a cited codebook edition; no segregation conflict; no undeclared crib hit.

Always record: codebook edition, checklist version, the exact items checked, and the verdict — so a second inspector reproduces the result.
