# References — Antibody Engineering & Apprenticeship Lookup

Compact lookup data. Defer to the upstream catalogues for full specs.

## Numbering & CDR definitions

| Scheme | Basis | Notes |
|--------|-------|-------|
| Kabat | Sequence variability | Classic; insertion letters (e.g. 100A–K in CDR-H3) |
| Chothia | Structural loops | Canonical-class framework |
| Martin (enhanced Chothia) | Hybrid | Common in tools |
| IMGT | Unique, gap-aware | Default for ANARCI; consistent across species |
| AHo | Structural, 149-position | Good for VH/VL alignment |

Tools to number: **ANARCI** (SAbDab), **AbNum**, **IMGT/DomainGapAlign**.

## Sequence-liability motif table

| Liability | Motif | Relative risk | Worst location |
|-----------|-------|---------------|----------------|
| Deamidation | NG | High | CDR |
| Deamidation | NS, NH, NT | Moderate | CDR |
| Isomerization | DG | High | CDR |
| Isomerization | DS, DT, DH | Moderate | CDR |
| Oxidation | exposed Met (M) | Moderate–high | CDR / Fc (M252, M428) |
| Oxidation | exposed Trp (W) | Moderate | CDR |
| N-glycosylation | N-X-S/T (X≠P) | Context-dependent | CDR (usually unwanted) |
| Fragmentation | DP (Asp-Pro) | Low–moderate | Hinge/linker |
| Free thiol | unpaired Cys | High (aggregation) | Anywhere |

Risk weighting: motif rate × location (CDR > Vernier/FR > constant) × solvent accessibility.

## Affinity & kinetics reference ranges

| Regime | KD | Comment |
|--------|----|---------|
| Weak | µM | Early hits / naïve libraries |
| Moderate | 1–100 nM | Typical un-matured leads |
| Strong | 0.1–1 nM | Common therapeutic target range |
| Very strong | < 100 pM | KD measurement becomes assay-limited; often off-rate-limited |

- KD = koff / kon. Diffusion-limited kon ceiling ≈ 10^6–10^7 M⁻¹s⁻¹.
- **Avidity caution:** bivalent display inflates apparent affinity by orders of magnitude — use monomeric antigen, 1:1 orientation, for intrinsic KD.

## Developability thresholds (orientation, not absolutes)

| Metric | Method | Watch-out |
|--------|--------|-----------|
| Tm / Tonset | nanoDSF / DSF | Fab Tm typically ≥ ~65 °C; low Tonset → aggregation risk |
| %monomer | SEC | High-monomer preferred; HMW species = aggregation |
| Self-association | AC-SINS | Red-shift → viscosity/PK risk at high conc |
| Viscosity | high-conc rheology | Critical for ≥100 mg/mL subcutaneous |
| Poly-reactivity | PSR / BVP-ELISA | Predicts fast clearance / off-target |
| TAP flags | SAbPred/TAP | PSH, PPC, PNC, SFvCSP, total CDR length vs clinical mAbs |

## Supervision / entrustment scale

| Level | Meaning |
|-------|---------|
| 1 | Observe only |
| 2 | Act under direct (over-the-shoulder) supervision |
| 3 | Act under indirect (on-call) supervision |
| 4 | Act independently |
| 5 | Supervise / teach others |

## Competency ladder (8 core competencies × Dreyfus tier)

| Competency | Carried by command(s) | Entrustment gate for "lead engineer" |
|------------|----------------------|--------------------------------------|
| Sequence-liability assessment | `/sequence-liability-scan` | 4 |
| Humanization | `/humanize-candidate` | 4 |
| Affinity-maturation design | `/affinity-maturation-plan` | 4 |
| Developability triage | `/developability-triage` | 4 |
| Binding-kinetics QC | `/binding-kinetics` | 4 |
| Epitope mapping | `/epitope-binning` | 3 |
| Format/engineering strategy | (cross-command judgment) | 3 |
| Regulatory & IP awareness | (cross-command judgment) | 3 |

Dreyfus tiers: Novice → Advanced Beginner → Competent → Proficient → Expert. Advance only on consistent multi-rep evidence + a mentor entrustment event.

## WHO antibody nomenclature (INN stems)

- Legacy: `-ximab` chimeric, `-zumab` humanized, `-umab` human, source-segment before `-mab`.
- 2021 revision drops `-mab`; new stems: `-tug` (unmodified), `-bart` (artificial), `-mig` (multi-specific), `-ment` (fragment).

## Upstream catalogues & tools

- **IMGT** — https://www.imgt.org/ — reference numbering, germlines, gene nomenclature.
- **OAS (Observed Antibody Space)** — https://opig.stats.ox.ac.uk/webapps/oas/ — billions of repertoire sequences; humanness baselines.
- **SAbDab / Thera-SAbDab** — https://opig.stats.ox.ac.uk/webapps/sabdab-sabpred/ — structures + therapeutic antibody database; hosts TAP.
- **BioPhi** — https://biophi.dichlab.org/ — OASis humanness + Sapiens humanization.
- **ANARCI** — antibody numbering (pip-installable).
- **ImmuneBuilder / ABodyBuilder2** — fast Fv structure prediction.
- **NetMHCIIpan** — https://services.healthtech.dtu.dk/ — MHC-II epitope / immunogenicity prediction.
- **Hu-mAb** — humanness scoring (random-forest).

## Key papers

- Schoch-independent: Jones et al. 1986 (CDR grafting); Winter & Milstein 1991 (humanization).
- Raybould et al. 2019, *Five computational developability guidelines (TAP)*, PNAS.
- Dreyfus & Dreyfus 1980/1986 — skill-acquisition model.
- ten Cate 2005; ten Cate & Scheele 2007 — entrustable professional activities / entrustment.
- Collins, Brown & Newman 1989 — cognitive apprenticeship.
- Miller 1990, *The assessment of clinical skills/competence/performance* (Miller's pyramid).
