# vendor-rfp-spec

## Purpose

Generate a precise outsourcing specification / RFP for a digitization service bureau — the imaging standard, deliverables, metadata, fixity, handling, and SLA — so vendor output is conformant and comparable to in-house work. Use when `/model-project-cost` routes overflow lots to a vendor, for material cleared to leave the building.

## Prompt Template

```
You are preparing a digitization outsourcing spec for a service bureau.

Inputs:

- **Lots to outsource:** [MATERIAL TYPES, EST. IMAGES, ANY SIZE EXTREMES]
- **Imaging standard required:** [FADGI ?★ / METAMORFOZE / ISO 19264 LEVEL ?]
- **Deliverables:** [MASTER FORMAT, DERIVATIVES, OCR?, IIIF?]
- **Metadata & packaging:** [NAMING CONVENTION, METS/PREMIS/MIX, BAGIT?]
- **Handling / custody constraints:** [TRANSIT INSURANCE, CHAIN OF CUSTODY, RETURN CONDITION]
- **Timeline & acceptance:** [DEADLINE, QA SAMPLING RULE, REJECT/RE-DELIVER TERMS]

Please produce an RFP/spec with:
1. **Scope & volume** — lots, material, estimated images, exclusions.
2. **Capture spec** — standard/level, resolution, bit depth, color management, target-chart cadence (must be QA-verifiable on return).
3. **Deliverable spec** — master + derivative formats, naming, metadata schemas, fixity (SHA-256 manifest), packaging (BagIt).
4. **Handling & custody** — transit, insurance, environmental, chain-of-custody documentation, and any material that must NOT be accepted.
5. **Acceptance & SLA** — QA sampling method, conformance tolerances, reject/re-deliver terms, payment milestones, timeline.
6. **Comparison hooks** — what the vendor must report so output is directly comparable to in-house cost-per-image and quality.
```

## Expected Output

- A vendor-ready RFP/spec a service bureau can bid against unambiguously.
- Acceptance criteria that make vendor deliverables verifiable with the same `/audit-image-quality` and `/audit-fixity-integrity` checks used in-house.
- Explicit handling/custody terms, including any material excluded from transit.
