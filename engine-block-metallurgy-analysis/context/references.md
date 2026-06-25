# Engine Block Metallurgy Analysis — Reference Tables

Lookup data the agent reaches for during tasks. Compact by design — defer to upstream sources for full specs.

## Common block-material composition windows (wt %)

| Grade | C | Si | Mn | P (max) | S (max) | Other | UTS (MPa) |
|---|---|---|---|---|---|---|---|
| Gray A48 Cl.35 | 3.1–3.4 | 1.9–2.3 | 0.6–0.9 | 0.15 | 0.12 | — | ~250 |
| CGI ISO GJV-450 | 3.5–3.8 | 2.1–2.4 | 0.2–0.5 | 0.04 | 0.01 | Mg 0.008–0.015; Ti control | ≥450 |
| Ductile A536 65-45-12 | 3.5–3.9 | 2.2–2.8 | 0.2–0.5 | 0.05 | 0.02 | Mg 0.03–0.05 | ≥448 |
| Al A319 | — | 5.5–6.5 | 0.8 max | — | — | Cu 3.0–4.0, Fe 1.0 max | ~185 (T5) |
| Al A356 | — | 6.5–7.5 | 0.35 max | — | — | Mg 0.20–0.45, Fe 0.20 max | ~230 (T6) |
| Al A390 (hypereut.) | — | 16–18 | 0.10 max | — | — | Cu 4.0–5.0, Mg 0.45–0.65 | ~280 (T6) |

Carbon equivalent: `CE = %C + (%Si + %P)/3`; eutectic ≈ 4.3. Engine gray irons ≈ 3.8–4.2.

## Graphite classification quick-ref (ASTM A247 / ISO 945-1)

| Type | Form | Significance |
|---|---|---|
| I / II | Nodular / irregular nodular | Ductile iron target |
| III | Vermicular (compacted) | CGI target |
| IV / V | Aggregate / crab | Degenerate — process problem |
| VI / VII | Irregular flake / flake | Gray iron (or Mg-fade reversion in SG iron) |

Flake **distribution** A (random, best) · B (rosette) · C (kish, hypereutectic) · D (interdendritic random) · E (interdendritic preferred, worst). Size 1 (coarse) → 8 (fine). Nodularity: ductile ≥80–90%; CGI a controlled low-nodule window.

## Etchants (cast iron & aluminium)

| Etchant | Composition | Reveals |
|---|---|---|
| Nital | 2% HNO₃ in ethanol | Ferrite/pearlite matrix, martensite |
| Picral | 4% picric acid in ethanol | Pearlite, carbides (less grain-boundary attack) |
| Stead's reagent | CuCl₂ + MgCl₂ + HCl | Phosphorus segregation (steadite) |
| Keller's | HF + HCl + HNO₃ + water | Aluminium alloys, general structure |
| 0.5% HF | dilute HF in water | Al-Si: primary/eutectic silicon |

## Hardness method quick-ref

| Method | Use | Standard |
|---|---|---|
| Brinell HBW 10/3000 | Bulk iron blocks (averages over graphite) | ASTM E10 |
| Rockwell B/C | Quick bulk checks | ASTM E18 |
| Vickers microhardness HV | Phase-level, traverses, thin zones | ASTM E384 |

Indent must span several graphite features for cast iron — micro-indents between flakes read the matrix, not the bulk.

## Likelihood-ratio interpretation scale (for the Bayesian update)

| LR range | Verbal weight | Effect on log-odds |
|---|---|---|
| 1–2 | Barely worth mentioning | ~0 to +0.3 |
| 2–5 | Weak support | +0.3 to +0.7 |
| 5–10 | Moderate support | +0.7 to +1.0 |
| 10–100 | Strong support | +1.0 to +2.0 |
| >100 | Decisive | >+2.0 |
| ≈1 | **Non-diagnostic — do not move the verdict** | 0 |

(Use the reciprocal for evidence favoring the alternative hypothesis.)

## Indicative prior base rates (starting points — adjust per case)

| Scenario | Tilt the prior toward |
|---|---|
| Near-zero-hours warranty failure | Casting/material defect |
| High-mileage field return | Service cause (overheat, fatigue, wear) |
| Cluster from one lot/date code | Process escape (composition, nodularity) |
| Single part, abuse history | Mechanical overload / detonation |

## Upstream catalogues

- **ASM Handbook Vol. 11 — Failure Analysis and Prevention** — https://dl.asminternational.org/handbooks — canonical FA methodology & case library.
- **ASM Handbook Vol. 9 — Metallography and Microstructures** — https://dl.asminternational.org/handbooks — prep, etching, image reference atlas.
- **ASTM standards portal** — https://www.astm.org — A247, A48, A536, E3, E407, E10, E384, E562, E1245, E2567.
- **ISO cast-iron standards** — https://www.iso.org — 945 (graphite), 16112 (CGI), 6892 (tensile).
- **MatWeb** — https://www.matweb.com — searchable composition & property database.
- **SinterCast (CGI process)** — https://www.sintercast.com — CGI metallurgy & process-control background.
