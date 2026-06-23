# Archival Preservation Digital Scanning — Reference Tables

Compact lookup data. Defer to the upstream standards for authoritative tolerances; figures below are planning estimates the agent reaches for during a task.

## Imaging standard levels (use-case mapping)

| Use | FADGI | Metamorfoze | ISO 19264-1 | Typical reflective ppi | Bit depth |
|-----|-------|-------------|-------------|------------------------|-----------|
| Irreplaceable preservation master | 4★ | Preservation | Level A | 400–600 | 16-bit/ch |
| Standard preservation | 3★ | Light | Level B | 300–400 | 16-bit/ch |
| High-volume access | 1–2★ | Extra Light | Level C | 200–300 | 8-bit/ch |

Transmissive (negatives/slides): scale ppi to the desired output size — small 35mm negatives often need 2000–4000+ ppi to yield a usable master.

## QA metrics and what they catch

| Metric | Measures | Common failure cause |
|--------|----------|----------------------|
| SFR / MTF50 | True resolution (cycles/mm) | Focus, sensor/optics, vibration |
| OECF | Tone reproduction curve | Exposure, lamp drift |
| ΔE (mean / max) | Color accuracy vs. reference | Stale ICC profile, lamp aging, white balance |
| Illumination uniformity | Even lighting across field | Lamp placement, falloff |
| Noise / SNR | Sensor noise floor | Gain, exposure, temperature |
| Chromatic aberration | Color fringing | Optics |

## Throughput planning estimates (images/hour, in-house)

| Material | Rough rate | Notes |
|----------|-----------|-------|
| Loose sheets, copy stand | 100–300 | Highest throughput; auto-cropping helps |
| Bound volume, overhead/planetary | 40–120 | Cradle handling slows it; v-cradle for tight bindings |
| Photographs (reflective) | 60–150 | Glare control / polarization may be needed |
| Film/negatives (transmissive) | 30–80 | High ppi + dust handling |
| Glass-plate / very fragile | 10–40 | Conservator pace; safety first |

**Utilization discount:** multiply nameplate by **0.60–0.75** for realistic planning (rework, calibration, breaks, staffing gaps).

## Condition handling multipliers (applied to capture time)

| Grade | Multiplier | Capture path |
|-------|-----------|--------------|
| Pristine / Stable | 1.0 | Standard in-house |
| Fragile | 1.5–2.5 | In-house + conservator consult |
| At-risk (unique) | 2.0–3.0 | In-house only, **no transit** |
| Unstable | ∞ until stabilized | **Conservation-first** |

## Fixity & storage planning

- **Preferred checksum:** SHA-256 (MD5 legacy/fast, collision-weak — avoid for new baselines).
- **Replication:** ≥ 3 copies, ≥ 2 geographic locations, ≥ 1 different storage technology (LOCKSS-style); fewer replicas → verify more often.
- **Master size rough cut:** 16-bit RGB TIFF ≈ `pixels_w × pixels_h × 6 bytes` uncompressed. A 600 ppi capture of an A4 page (~4960 × 7016) ≈ ~200+ MB/master. Multiply by replication factor and retention years for true storage cost.
- **NDSA Levels** progress across four functional areas (storage, fixity, control, metadata) from Level 1 (know what you have, ≥ 2 copies) to Level 4 (audited, geographically + technologically diverse, regular fixity).

## Optimization quick-reference

| Decision | Model | Method | Watch for |
|----------|-------|--------|-----------|
| What to scan, in what order | 0/1 knapsack | DP (small) / greedy `V/cost` (large) | State optimality gap on greedy |
| Assign lots to stations | R\|\|Cmax makespan | LPT + local search | NP-hard; one job can dominate |
| When will we finish | M/M/c queue | stability `ρ<1`, drawdown | `ρ≥1` ⇒ no finish date |
| In-house vs. vendor | make-vs-buy | per-lot min-cost + hard gates | no-transit override |

## Upstream Catalogues & Standards

- **FADGI Technical Guidelines** — https://www.digitizationguidelines.gov/guidelines/digitize-technical.html — US federal star-rating imaging guidelines + the FADGI target/analysis tools.
- **Metamorfoze Preservation Imaging Guidelines** — https://www.metamorfoze.nl/en/digitization/guidelines — Dutch national preservation imaging standard.
- **ISO 19264-1** — https://www.iso.org/standard/79172.html — image-quality analysis for heritage capture (Levels A/B/C).
- **OAIS / ISO 14721 (CCSDS 650.0)** — https://public.ccsds.org/pubs/650x0m2.pdf — archival information package reference model.
- **PREMIS** — https://www.loc.gov/standards/premis/ — preservation metadata data dictionary.
- **METS** — https://www.loc.gov/standards/mets/ — structural metadata schema.
- **MIX / NISO Z39.87** — https://www.loc.gov/standards/mix/ — technical metadata for still images.
- **IIIF** — https://iiif.io/api/ — Image + Presentation APIs for access deliverables.
- **NDSA Levels of Digital Preservation** — https://ndsa.org/publications/levels-of-digital-preservation/ — tiered fixity/storage/metadata maturity model.
- **BagIt (RFC 8493)** — https://datatracker.ietf.org/doc/html/rfc8493 — package/transfer manifest format.
