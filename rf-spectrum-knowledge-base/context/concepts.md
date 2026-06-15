# Concepts — RF Spectrum Analysis as a Knowledge Base

This workspace sits at the intersection of two disciplines: **RF spectrum analysis** (measuring and identifying what occupies the radio spectrum) and **knowledge engineering** (turning observations into a structured, citable, maintainable corpus with FAQ generation on top). The first half below covers the spectrum; the second covers the knowledge system that captures it.

---

## Part 1 — RF Spectrum Analysis

### What we measure

A spectrum survey characterizes signals along a handful of axes:

- **Frequency** — center frequency and the band it sits in. The spectrum is conventionally divided ELF → VLF → LF → MF → HF → VHF → UHF → SHF → EHF (3 kHz to 300 GHz), each decade a band.
- **Bandwidth** — how wide the signal is. Reported as **occupied bandwidth** (the span containing 99 % of power) or by a relative threshold (e.g. −20 dB from peak). Necessary bandwidth depends on modulation and symbol rate.
- **Power / level** — peak and mean power, usually in **dBm** (power) or as **power spectral density** (dBm/Hz). Always relative to the measurement chain (antenna, cable loss, LNA gain, resolution bandwidth).
- **Noise floor** — the baseline power with no signal present, set by thermal noise (kTB ≈ −174 dBm/Hz at 290 K), receiver noise figure, and resolution bandwidth. Detections are defined *relative to* the floor, not absolutely.
- **Modulation & access** — how information rides the carrier (AM/FM/PM; ASK/FSK/GFSK/PSK/QAM; OFDM; spread-spectrum DSSS/FHSS) and how a channel is shared (FDMA/TDMA/CDMA/OFDMA).
- **Temporal structure** — continuous carrier vs. bursty vs. hopping; **duty cycle** (fraction of time active); burst length and period.
- **Occupancy** — over a window, the fraction of time/frequency a band is in use. The key metric for "is this band busy?"

### The measurement chain (and why provenance matters)

Measured power is the *true* emission minus antenna pattern, cable loss, plus LNA gain, shaped by the receiver's noise figure and the chosen resolution bandwidth (RBW). Change the gain or antenna and the same emitter reads at a different level. **This is why every KB entry must carry its capture settings**: a future "the level changed" claim is meaningless without knowing the chain was identical.

Resolution bandwidth also sets the noise floor: narrower RBW → lower floor → weaker signals visible, but slower sweeps. The classic time/sensitivity/span trade-off governs every survey.

### Emitter identification

Identifying an unknown signal proceeds from cheap cues to expensive ones:

1. **Where** — frequency + band-plan allocation narrows the candidate set enormously (a signal at 1090 MHz is almost certainly ADS-B).
2. **Shape** — the waterfall fingerprint: continuous, bursty, hopping, FSK "rails", OFDM block, chirp.
3. **Parameters** — bandwidth, channel spacing, symbol/hop rate, duty cycle.
4. **Decode** — demodulate and read a protocol identifier (the only path to a `confirmed` identity).

Catalogs like the **Signal Identification Wiki (sigidwiki)** index these fingerprints; matching against them is the workhorse of identification.

### Common failure modes in spectrum analysis

- **Receiver artifacts mistaken for real signals.** Images (`2·LO ± f`), harmonics (`n·f`), intermodulation products, and ADC spurs all appear as "emitters." Rule these out before logging.
- **Front-end overload.** A strong nearby transmitter desensitizes the receiver and spawns false products across the band. Symptom: signals that vanish when you add attenuation.
- **Aliasing / under-resolved bins.** Bin width too coarse blurs adjacent narrowband signals into one detection.
- **Floor drift read as signal change.** Temperature, gain drift, or ambient noise move the floor; SPC-style baselining separates that from real change.

---

## Part 2 — Knowledge Engineering for the Spectrum

### The KB entry — the atomic unit

Each identified (or candidate) emitter is one entry with a fixed schema (full field list in `references.md`): identity, measured parameters, service/allocation, region, confidence, lifecycle dates, and — non-negotiably — **provenance** (who observed it, when, with what) and **citations**. The schema is what makes the corpus queryable and auditable rather than a pile of notes.

### Provenance and confidence

Every claim is traceable to a capture or an external source. Confidence is graded, and the language must match the evidence:

- `unidentified` — detected, not named.
- `probable` — fits an allocation or partial signature; no decode.
- `confirmed` — decoded identifier or unambiguous signature match.

Writing "confirmed" for a band-plan guess is the cardinal sin; `/kb-audit` treats an uncited `confirmed` as a blocking defect.

### Controlled vocabulary & lightweight ontology

A glossary of preferred terms with aliases (FHSS ↔ "frequency hopping") and relations (`broader`/`narrower`/`related`) lets entries, FAQ, and queries converge on one language. Without it, "freq hopping", "FH", and "FHSS" become three un-joinable silos. This is the ontology backbone that retrieval and dedup depend on.

### Retrieval grounding (and abstaining)

Answering questions is **retrieval-augmented**: pull the relevant entries, answer *from them*, cite them. The discipline that makes the KB trustworthy is the **abstain path** — when retrieval finds insufficient support, the answer is "not in the KB" plus a logged gap, never a confident guess from general knowledge. Grounding + abstention is the whole point.

### FAQ generation

A FAQ is a *generated view* of the KB plus reference material, organized by the questions people actually ask (mined from the query log). It is never a second source of truth: if a FAQ answer and its cited entry disagree, the entry wins and the FAQ is regenerated. High-frequency question clusters become FAQ entries; unanswerable ones become OPEN gaps.

### Entry lifecycle, staleness, and contradiction

Entries are born as drafts, promoted to canonical, and age: `active` → `intermittent` → `historical`. A `review_by` date forces re-verification before claims silently rot. Two failure modes mirror each other: a band we **stopped looking at** (coverage gap) vs. an emitter that **legitimately disappeared** (mark `historical`) — opposite fixes. Contradiction detection finds overlapping entries asserting incompatible identities, the inevitable result of multiple analysts ingesting independently.

### Knowledge-base failure modes

- **Silent rot.** A KB that only grows looks healthy while half its entries go stale. Staleness gaps matter as much as missing ones.
- **Duplicate proliferation.** Repeated ingests promote the same emitter twice under different names; without dedup the corpus fragments.
- **Vocabulary drift.** Terms invented ad hoc inside entries instead of through the glossary fragment retrieval.
- **Ungrounded answers.** The KB exists precisely so answers are cited; an answer with neither citation nor abstention defeats the workspace.

## Standards & catalogs worth citing

- **ITU Radio Regulations** and the **ITU-R Table of Frequency Allocations** — the authoritative global allocation framework (Regions 1/2/3).
- National regulators — **FCC/NTIA** (US), **Ofcom** (UK), **BNetzA** (DE), etc.
- **ITU-R recommendations** — e.g. SM-series on spectrum monitoring and measurement.
- **Signal Identification Wiki (sigidwiki.com)** — community catalog of signal fingerprints.
- **IEEE / 3GPP / ETSI** standards for specific systems when decoding for a `confirmed` ID.
