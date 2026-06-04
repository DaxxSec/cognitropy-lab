# HAZMAT Transportation Regulations — Core Concepts

Background the agent reads before decoding a shipment. Two halves: the **regulatory codebook** (what the symbols mean) and the **cryptanalysis mapping** (how a codebreaker exploits the codebook's redundancy to find errors). Optimised for fast recall, not exhaustive theory — defer to the live regulation for authority.

## The regulatory codebook

Dangerous goods transport is governed by a layered set of mutually-aligned regulations, all descended from the **UN Recommendations on the Transport of Dangerous Goods — Model Regulations** (the "Orange Book"):

| Mode | Regulation | Authority |
|------|------------|-----------|
| All US modes | **HMR** — 49 CFR Parts 100–185 | PHMSA / US DOT |
| Road (Europe) | **ADR** | UNECE |
| Rail (Europe) | **RID** | OTIF |
| Sea | **IMDG Code** | IMO |
| Air | **IATA DGR / ICAO Technical Instructions** | IATA / ICAO |

They differ in detail (placarding thresholds, segregation, quantity limits, documentation) but share one spine: the **Dangerous Goods List** — `49 CFR 172.101` in the US, **Chapter 3.2** in the Model Regulations. This is the codebook.

### The UN number is the key

Each regulated substance has a four-digit **UN number** (0004–~3600, assigned by the UN Sub-Committee of Experts). Given the UN number, the Dangerous Goods List deterministically returns:

- **Proper Shipping Name (PSN)** — the legally required descriptive name (not the trade name).
- **Hazard class / division** — the primary hazard (see table below).
- **Subsidiary risk(s)** — secondary hazards, shown as additional labels.
- **Packing group (PG)** — degree of danger within the class: **I** (great), **II** (medium), **III** (minor). Classes 1, 2, 5.2, 6.2, 7 do not use PGs.
- **Labels** — the diamond hazard labels required on the package.
- **Special provisions, packing instructions, limited/excepted quantities, IBC/tank codes.**
- **ERG guide number** — the response action (via the Emergency Response Guidebook).

Note: a UN number has **no internal check digit** — it is a registry key, not a self-validating code. Its validity is established by *cross-reference* to the codebook, not arithmetic. (Container numbers under **ISO 6346** *do* carry a real check digit; the freight bill of lading often does too.)

### Hazard classes 1–9

| Class | Hazard | Common divisions |
|-------|--------|------------------|
| 1 | Explosives | 1.1–1.6 (mass-explosion → very insensitive) |
| 2 | Gases | 2.1 flammable · 2.2 non-flammable/non-toxic · 2.3 toxic |
| 3 | Flammable liquids | (by flash point / boiling point → PG I/II/III) |
| 4 | Flammable solids | 4.1 flammable solid · 4.2 spontaneously combustible · 4.3 dangerous when wet |
| 5 | Oxidizing | 5.1 oxidizer · 5.2 organic peroxide |
| 6 | Toxic / infectious | 6.1 toxic · 6.2 infectious |
| 7 | Radioactive | (categories I–III-YELLOW; transport index) |
| 8 | Corrosive | (acids, bases → PG I/II/III) |
| 9 | Miscellaneous | incl. lithium batteries, environmentally hazardous substances |

### Placards, labels, and the Kemler/HIN code

- **Labels** (≈100 mm diamonds) go on packages; **placards** (≈250 mm diamonds) go on the transport unit. Both encode class by colour, symbol, and class number.
- **ADR orange plate** carries two numbers. The lower is the **UN number**. The upper is the **Hazard Identification Number (HIN, "Kemler code")**: first digit = primary hazard, following digits = secondary hazards; a **doubled digit** intensifies (33 = highly flammable liquid, flash point < 23 °C); a leading **X** means *reacts dangerously with water* (do not use water). Example: `X423 / 1428` = a flammable solid that reacts dangerously with water, sodium.
- **Marks**: UN-spec packaging codes (e.g. `4G` fibreboard box), the limited-quantity diamond, the lithium battery mark, orientation arrows, and the environmentally-hazardous-substance "dead fish/tree" mark.

### Documentation

A shipping paper / dangerous goods declaration must carry, in a prescribed order, the **UN number, PSN, hazard class, packing group** (the "basic description"), plus quantity, number/type of packages, a **24-hour emergency response telephone number**, an emergency response information source (ERG guide), and a shipper's certification. Air adds the IATA Shipper's Declaration and CAO/PAX limits; sea adds the container/vehicle packing certificate.

## The cryptanalysis mapping

The codebook's redundancy is what makes hazmat documents *attackable* in the cryptanalytic sense — the same facts are encoded several times, so an error in one encoding contradicts the others.

- **Known-plaintext / crib attack → codebook expansion.** The Dangerous Goods List is a giant known-plaintext table. Given the UN number (key), the full plaintext is fixed. Expand it and diff against the paper; any field that disagrees is a decode error. (`/codebook-crossref`)
- **Cross-field consistency = checksum.** UN ↔ PSN ↔ class ↔ subsidiary risk ↔ PG ↔ labels ↔ placards ↔ ERG guide are mutually constraining. Treat the set as a parity check: if they don't all agree, the "message" is corrupt. (`/decode-manifest`)
- **Frequency analysis.** Letter frequency breaks substitution ciphers; *code frequency* breaks complacent inspection. Profile the UN-number/class distribution for a shipper or lane; an entry far from the expected distribution (Class 1 from a produce importer) is a high-value inspection target. (`/frequency-profile`)
- **Index of coincidence / entropy.** Fabricated or copy-pasted paperwork has the wrong randomness: identical emergency-contact strings across unrelated shipments, round-number net quantities, placeholder values, repeated package counts. Low entropy where the real world is noisy is a tell. (`/anomaly-entropy`)
- **Transposition & substitution errors.** A single transposed digit (1203↔1230, 1830↔1380) silently rekeys the message to a different substance. Detect with edit distance against the valid UN space plus PSN plausibility, and validate ISO 6346 container check digits arithmetically. (`/transposition-check`)
- **Traffic analysis.** Even without "reading" each package, the *pattern* of co-loaded codes reveals risk: a combination of classes that the segregation table prohibits is a collective hazard no single-line check sees. (`/segregation-conflict`)
- **Crib-dragging.** Cryptanalysts slide a suspected plaintext fragment along the ciphertext looking for a fit. Slide known dangerous-goods cribs ("power bank" → lithium battery; "pool shock" → oxidizer; "dry ice" → UN 1845) along a plain-language goods description to expose hazards the declaration omits. (`/undeclared-crib`)

## Common failure modes

- **Misdeclaration** — wrong class/PG/UN, often to dodge cost, packaging, or a carrier embargo. Caught by cross-field consistency.
- **Undeclared dangerous goods** — hazardous goods shipped as "general cargo." The single biggest air-cargo safety problem (lithium batteries especially). Caught by crib-dragging.
- **Transcription/transposition error** — honest typo that changes the substance. Caught by edit-distance + check digit.
- **Segregation violation** — individually compliant items that may not travel together. Caught by traffic analysis.
- **Stale codebook** — decoding against a withdrawn UN number or an old ERG edition. Mitigated by recording the edition.
- **Placard/paper mismatch** — orange plate or placards don't match the declaration (load changed; wrong plate). Caught by `/placard-decipher`.

## Operating constraints

- The agent is an **advisory screen**, not an enforcement authority or a substitute for a DGSA/DG advisor.
- Decode against the **mode- and jurisdiction-correct** regulation; never blend HMR placarding with IMDG segregation.
- Cite the **codebook edition/year** in every decode; the HMR and modal regulations are revised continually.
- A statistical flag is a **lead**; escalate to documentary/physical inspection before any operational decision.
