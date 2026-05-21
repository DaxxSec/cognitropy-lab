# Biomechanical Engineering — Prosthetics — Core Concepts

Background the agent should read before acting on prosthetics-fitting, gait-analysis, fatigue-testing, or outcome-trend tasks. Tuned for fast recall, not exhaustive theory.

## Prosthetic Taxonomy

### Lower-limb amputation levels (proximal → distal)

| Level | Common abbreviation | Notes |
|---|---|---|
| Hip disarticulation | HD | Hip joint required in prosthesis; very high energy cost |
| Transfemoral | TF / AKA | Above-knee; ischial-containment or sub-ischial socket; mechanical or microprocessor knee |
| Knee disarticulation | KD | Through-knee; long lever, end-bearing on femoral condyles |
| Transtibial | TT / BKA | Below-knee; PTB or TSB socket designs dominate; most common amputation level |
| Syme's | — | Through-ankle; preserves distal tibia + fibula; partial end-bearing |
| Partial foot | PF | Chopart, Lisfranc, transmetatarsal; high preservation, often shoe-fit issues |

### Upper-limb amputation levels

Shoulder disarticulation → transhumeral → elbow disarticulation → transradial → wrist disarticulation → partial-hand. Each level reduces functional restoration potential and increases prosthesis complexity (body-powered → external-powered → myoelectric → targeted muscle reinnervation).

### Socket designs (lower-limb)

| Design | Indication | Suspension method |
|---|---|---|
| **PTB** (Patellar Tendon Bearing) | Classic TT design | Supracondylar / strap |
| **TSB** (Total Surface Bearing) | TT, even pressure distribution | Pin-lock / suction / sleeve |
| **Ischial Containment** | TF, lateralised proximal trim | Sub-ischial pubic ramus or anterior wall |
| **Sub-Ischial** | TF, comfort-prioritised | Vacuum / pin-lock |
| **Sym Suspension** | Syme's | End-bearing with proximal trim |
| **CAT-CAM** (Contoured Adducted Trochanteric–Controlled Alignment Method) | TF historical | Sub-ischial precursor |

### Component classes (lower-limb)

- **Feet/ankles:** SACH (solid-ankle cushion-heel), single-axis, multi-axis, dynamic-response (carbon-fibre), microprocessor-controlled (Proprio Foot, Empower).
- **Knees:** single-axis, polycentric, weight-activated stance control, pneumatic, hydraulic, microprocessor (C-Leg, Genium, Rheo Knee, Power Knee).
- **Liners:** silicone, urethane, mineral-oil-based gel; with/without pin distal; sleeve suspension.
- **Sockets:** thermoplastic check sockets (test fit), laminated carbon/fibreglass definitive sockets, 3D-printed sockets (emerging).

## Gait Analysis Fundamentals

### Gait cycle phases

| Phase | % of cycle | Key events |
|---|---|---|
| Initial contact (IC) | 0% | Heel strike (sound side) or prosthetic-foot contact |
| Loading response | 0-12% | Weight acceptance, peak vertical GRF (~1.1-1.3 BW typical) |
| Mid-stance | 12-31% | Single-limb support, body passes over standing limb |
| Terminal stance | 31-50% | Heel-off, COG forward |
| Pre-swing | 50-62% | Toe-off, second peak GRF |
| Initial swing | 62-75% | Foot clearance, knee flexion |
| Mid-swing | 75-87% | Limb advancement |
| Terminal swing | 87-100% | Deceleration into next IC |

Reference: Perry & Burnfield, *Gait Analysis: Normal and Pathological Function* (2nd ed.).

### Standard kinematic / kinetic variables tracked in P&O gait labs

- **Spatiotemporal**: cadence (steps/min), velocity (m/s), step length (m), stride length (m), step width (m), single-limb support time (s), stance/swing ratio.
- **Kinematics** (joint angles): peak hip flexion (stance ~30°), peak hip extension (terminal stance ~10°), peak knee flexion in swing (60-65° in normal, less in TT prosthesis), peak ankle dorsiflexion (10° stance) / plantarflexion (toe-off ~15°), trunk lean (sagittal + coronal).
- **Kinetics** (joint moments/powers): peak vertical GRF (1.1-1.3 BW), braking + propulsive impulses, peak knee extension moment, peak hip extension moment, hip + knee + ankle joint powers.

### Marker sets

- **Helen Hayes (Plug-in-Gait)** — workhorse for clinical gait analysis; 15 markers lower body.
- **Oxford Foot Model** — multi-segment foot; important for partial-foot and Syme's analysis.
- **Cleveland Clinic / IOR** — alternative marker sets; choose for consistency with reference data.

## QC Statistical Methods

### Statistical Process Control (SPC) charts

| Chart | Use case | Data type |
|---|---|---|
| **I-MR** (Individuals + Moving Range) | Single observations per time point | Continuous, rational subgroup of 1 |
| **X-bar-R** | Multiple observations per subgroup | Continuous, subgroup size 2-10 |
| **X-bar-S** | Larger subgroups | Continuous, subgroup size >10 |
| **p chart** | Proportion defective | Attribute (pass/fail), variable subgroup size |
| **np chart** | Number defective | Attribute, constant subgroup size |
| **c chart** | Count of defects per unit | Attribute, constant opportunity |
| **u chart** | Defects per unit (variable opportunity) | Attribute |
| **EWMA** (Exponentially Weighted Moving Average) | Detect small shifts | Continuous |
| **CUSUM** | Detect persistent small shifts | Continuous |

### Shewhart / Western Electric rules for out-of-control signals

1. One point beyond 3σ (the chart's control limit).
2. Two of three consecutive points beyond 2σ on the same side of CL.
3. Four of five consecutive points beyond 1σ on the same side of CL.
4. Eight consecutive points on the same side of CL (run rule).
5. Six consecutive points trending up or down.
6. Fourteen alternating up-down.
7. Fifteen consecutive within 1σ (over-control suspect).
8. Eight consecutive outside 1σ (mixture suspect).

### Process capability indices

- **Cp** = (USL - LSL) / (6σ) — ignores centring; measures spread vs. spec
- **Cpk** = min[(USL - μ)/(3σ), (μ - LSL)/(3σ)] — penalises off-centring
- **Pp / Ppk** — same formulae with total sigma (vs. within-subgroup sigma) — measures *performance* not *capability*
- **Cpm** (Taguchi) — penalises deviation from target T: Cpm = (USL-LSL) / (6 × √(σ² + (μ-T)²))

Standard interpretation: Cpk < 1.0 (incapable), 1.0-1.33 (marginal), 1.33-1.67 (capable), >1.67 (highly capable).

### Gauge R&R via ANOVA method

Variance decomposition: σ²_total = σ²_part + σ²_operator + σ²_part-operator-interaction + σ²_equipment

- **Repeatability (EV)** = √(σ²_equipment) — within-operator within-part noise
- **Reproducibility (AV)** = √(σ²_operator + σ²_interaction) — between-operator
- **Total R&R** = √(EV² + AV²)
- **% R&R** = 100 × R&R / Total Variation; AIAG bands: <10% acceptable, 10-30% marginal, >30% unacceptable
- **% Contribution** = 100 × R&R² / Total Variation²
- **NDC** = 1.41 × σ_part / σ_R&R; ≥5 desired

## Standards Landscape

| Standard | Scope |
|---|---|
| **ISO 10328** | Structural testing of lower-limb prostheses — static + ultimate strength |
| **ISO 22675** | Foot/ankle fatigue testing — cyclic loading 2-3M cycles |
| **ISO 22523** | External limb prostheses + orthoses general requirements |
| **ISO 14971** | Risk management for medical devices |
| **ISO 13485** | QMS for medical devices |
| **ANSI/RESNA WC-1, WC-2, WC-3** | Wheelchair and seating standards |
| **ANSI/RESNA ED-1** | Electronic devices for ADL |
| **FDA 21 CFR 820** | QSR (US Quality System Regulation) |
| **EU MDR 2017/745** | EU Medical Device Regulation (replaces MDD) |

## Outcome Measures (PROMs)

| Instrument | Domain | Scoring | Notes |
|---|---|---|---|
| **PEQ** (Prosthesis Evaluation Questionnaire) | Multi-domain (9 subscales: ambulation, social, etc.) | 0-100 per subscale | Legro et al. 1998 |
| **PEQ-MS** (Mobility Subscale) | Lower-limb mobility | 0-100 | Most-cited PEQ subscale |
| **AMP-PRO** (Amputee Mobility Predictor with Prosthesis) | Functional mobility | 0-47 | Predicts K-level |
| **AMP-noPRO** | Functional mobility without prosthesis | 0-43 | Pre-fit baseline |
| **LCI-5** (Locomotor Capabilities Index, 5-level) | Activity range | 0-56 | French-Canadian validation |
| **PROMIS-PF** | Physical function generic | T-score (μ=50, σ=10) | NIH item bank, CAT or fixed |
| **Houghton Scale of Use** | Hours/day worn, satisfaction | 0-12 | Quick screen |
| **OPUS** (Orthotics and Prosthetics Users' Survey) | Satisfaction + function | 0-100 modules | Multi-module |
| **TAPES** (Trinity Amputation and Prosthesis Experience Scales) | Psychosocial + function | Multi-scale | Adjustment + activity restriction |

## Common Failure Modes

- **Socket fit drift from limb volume change** (acute post-fit edema resolution; longitudinal atrophy; seasonal hydration; weight gain/loss). Pressure-mat readings drift; PROMs decline; refit needed.
- **Liner degradation** at 6-9 months typical wear life; suspect when distal-end pressure rises without other system changes.
- **Component fatigue failure** — usually preceded by compliance change visible in ISO 22675 cyclic testing or by sound complaints from patient.
- **Alignment drift** from socket-to-pylon attachment loosening; produces gait asymmetry signals.
- **Gauge measurement-system drift** — pressure mats lose calibration over 6-12 months; scanners drift with lighting environment; force plates drift slowly with temperature. R&R should be re-validated quarterly.
- **Phantom limb pain mistaken for fit complaint** — comorbid issue, not socket-fit failure; control charts should be normal in this case.

## Operating Constraints

- **Patient safety is sovereign.** Statistical methods inform; the licensed CPO and prescribing physician decide.
- **HIPAA / GDPR** for all patient data.
- **FDA 21 CFR 806** mandates corrections-and-removals reporting for US practices.
- **EU MDR Article 87** mandates serious-incident reporting within 2-15 day windows.
- Component recalls have legal force; documented good-faith outreach is the standard of care for affected patients.
