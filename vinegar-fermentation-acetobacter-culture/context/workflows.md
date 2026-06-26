# Vinegar Fermentation & Acetobacter Culture — Workflows and Methodology

How an expert actually runs the ferment *and* the knowledge loop. The commands in `.claude/commands/` automate slices of these.

---

## A. The ferment lifecycle (end to end)

1. **Substrate prep.** Start from a fermented base (cider, wine, diluted spirit, rice wash). Target **5–9% ABV** — dilute anything above ~12% so it stays within strain ethanol tolerance. Record starting Brix/ABV.
2. **Inoculate.** Add a healthy mother + live raw vinegar of the same style (10–20% by volume is generous and de-risks the lag phase). Larger inoculum = shorter lag = less spoilage risk.
3. **Aerate.** Surface method: maximize air-liquid surface area, keep the vessel breathable (cloth + band). Submerged: run continuous fine-bubble aeration. **Never** seal the vessel — AAB are obligate aerobes.
4. **Hold temperature** at ~28–32 °C. Cooler is safe but slow; hotter stresses the culture.
5. **Monitor.** Titrate acidity on a cadence (e.g. weekly for surface, daily for fast methods). Plot acidity rising and residual ethanol falling.
6. **Harvest at the knee.** Pull the batch when acidity plateaus *and* residual ethanol is low but **non-zero** (~0.2–0.5%). Waiting past zero invites overoxidation.
7. **Finish.** Optionally filter, pasteurize (~60–65 °C hold to stabilize for sale), bottle. Decide whether to keep it "raw with the mother" or stabilized.
8. **Capture.** Run `/culture-log` for the mother and write the batch outcome (numbers + lessons) into the KB via `/kb-ingest`.

---

## B. Method selection (decision)

```
Volume small (≤20 L) AND aroma/complexity prized?      → Orleans (surface)
Mid volume, want speed without an acetator?            → Generator (beechwood trickle)
Large volume OR need high acidity fast & repeatable?   → Submerged (Frings-style acetator)
No aeration hardware, learning?                        → Orleans, small batch, big inoculum
```
Cross-check against equipment, time budget, and whether the style depends on slow barrel character. `/method-select` formalizes this with tradeoffs.

---

## C. Stalled / off-batch troubleshooting tree

```
Acidity not rising?
├─ Sealed or low surface area?        → restore aeration; never seal
├─ Temp < ~20 °C?                      → warm to 28–32 °C
├─ Starting ABV > ~12%?               → dilute; ethanol toxic to AAB above tolerance
├─ Inoculum tiny / no live culture?    → back-slop with raw same-style vinegar
└─ Culture old / chlorinated water?    → fresh mother; use dechlorinated water

Acidity rose then FELL?
└─ Overoxidation: ethanol hit zero     → harvest immediately; next time leave residual / use Komagataeibacter

Surface film, wrinkled/dull, off-smell?
├─ Kahm/film yeast                     → skim, raise acidity, improve sanitation
└─ Fuzzy colored mold                  → discard batch; acidity was too low to protect

Cloudy with tiny wriggling threads?
└─ Vinegar eels (harmless)             → filter + pasteurize before sale
```
`/troubleshoot-batch` walks this and **writes the resolution back to the KB** so the next occurrence is a lookup.

---

## D. Acidity & yield computation

1. **Project before brewing:** ~1% ABV → ~1% acetic acid at good efficiency. A 7% ABV cider targets ~6–7% vinegar; verify it clears the regulatory floor with margin.
2. **Titrate to measure:** `acidity % (w/v) = (V_NaOH × N_NaOH × 6.005) / V_sample_mL`. (6.005 = milliequivalent weight of acetic acid × 100 conversion; see `references.md`.)
3. **Track GK** = `% acetic acid + % residual ethanol`; in fast methods hold GK roughly steady and harvest on residual-ethanol approach to (but not) zero.
4. **Flag risks:** below the jurisdiction's floor → not legally vinegar; residual ethanol ≈ 0 with an overoxidizing strain → harvest now.
`/acidity-calc` does steps 1–4 and records the worksheet to `outputs/`.

---

## E. Mother-culture maintenance cadence

- **Feed / back-slop** when acidity stops climbing or before a new batch: transfer a portion of vigorous culture into fresh diluted substrate.
- **Lineage:** assign each mother a strain/generation ID; record splits, feeds, and vigor (pellicle thickness, acidity-rise rate) each event via `/culture-log`.
- **Storage:** keep cultures lightly fed and aerobic; long-dormant mothers lose vigor and lengthen lag.
- **Health checks:** translucent forming pellicle + steady acidity rise = healthy; sunken inert mass + flat acidity = vitality problem (see tree above).

---

## F. KB ingestion pipeline (`/kb-ingest`)

1. **Read** the source (PDF, notebook, thread, paper).
2. **Extract atomic claims** — one fact/topic per candidate entry; don't bundle.
3. **Canonicalize** each into the KB schema (title, body, taxonomy tag(s), provenance, confidence). Confidence is set by source type: own batch = `measured`, authoritative source = `published`, forum/anecdote = `practitioner-lore`, agent reasoning = `inferred`.
4. **Deduplicate / merge** against existing entries; if a new claim contradicts an old one, keep both and flag for `/kb-audit`.
5. **Write** entries under `outputs/kb/<top-level-tag>/` and update the related-links index.

---

## G. FAQ generation (`/faq-generate`)

1. **Pick the audience** (home fermenter / craft producer / educator) — sets depth and tone.
2. **Cluster** KB entries by user intent into candidate questions, phrased the way that audience asks.
3. **Answer** each question *only* from KB entries; cite the supporting entries inline.
4. **Tag** each answer with the confidence of its weakest supporting entry; soften or omit anything resting solely on `practitioner-lore`/`inferred` for safety-critical questions.
5. **Flag gaps:** questions with no backing entry are listed as "KB gaps" at the end, not answered from thin air.
6. **Write** `outputs/faq/<audience>-YYYY-MM-DD.md`. Regenerate (don't hand-edit) after KB changes.

---

## H. KB audit (`/kb-audit`)

Periodically, or before publishing a FAQ:
- **Coverage:** which taxonomy areas are thin or empty?
- **Contradictions:** entries that disagree (flagged during ingest) — resolve or annotate.
- **Staleness:** `measured` entries from old batches that newer data supersedes.
- **Sourcing:** entries missing provenance, or `practitioner-lore` that should be promoted to `measured` once your own batches confirm it.
- **Orphans:** FAQ answers whose supporting entries were edited/removed.
Output: `outputs/audits/kb-audit-YYYY-MM-DD.md` with a prioritized fix list.
