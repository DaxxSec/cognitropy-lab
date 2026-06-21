# Concepts — Immunology Antibody Engineering (run as an apprenticeship)

Domain knowledge for engineering therapeutic/research antibodies, plus the competency-progression vocabulary that organizes how a trainee engineer is brought from supervised to independent practice. The two halves are deliberately interleaved: every engineering competency below maps to a rung on the apprenticeship ladder.

## 1. Antibody architecture

- **IgG topology.** Two heavy + two light chains; each chain has a variable (V) and constant (C) region. The antigen-binding fragment (**Fab**) carries VH+CH1 and VL+CL; the **Fc** (CH2–CH3) drives effector function and FcRn-mediated half-life. The **Fv** (VH+VL) is the minimal binding unit.
- **CDRs and framework.** Each V domain has three complementarity-determining regions (CDR1/2/3) on a framework (FR) scaffold. **CDR-H3** is the most diverse and usually dominates specificity; the other five CDRs adopt a limited set of **canonical conformations** set by a few key framework/CDR residues.
- **Numbering schemes.** Kabat (sequence-based), Chothia (structural loops), Martin/enhanced-Chothia, IMGT (unique, gap-aware), AHo. The scheme sets CDR boundaries — always state which one. Tools: ANARCI, AbNum, IMGT/DomainGapAlign.
- **Isotypes & subclasses.** IgG1/2/3/4, IgA, IgM, IgE, IgD. IgG subclasses differ in hinge length and FcγR/C1q engagement → different ADCC/CDC/ADCP. Subclass and Fc engineering choices (effector-silent vs effector-enhanced) follow from mechanism of action.
- **Vernier zone.** Framework residues underlying the CDRs that tune loop conformation — the prime back-mutation targets in humanization.

## 2. Discovery routes (where a candidate comes from)

- **Hybridoma** — immunize (usually mouse), fuse B cells with myeloma, screen. Produces non-human antibodies needing humanization.
- **Display (in vitro)** — phage, yeast, or ribosome display of antibody libraries; pan against antigen. Naïve, immune, or synthetic libraries. Full sequence control and the native home of affinity maturation.
- **Single B-cell** — sort antigen-specific memory B / plasma cells, amplify natively paired VH/VL. Source of many fully-human leads.
- **Transgenic animals** — mice with humanized Ig loci (VelocImmune-type, XenoMouse-type) yield human sequences directly.
- **Computational / de novo** — structure- and ML-guided design (strong for redesign and affinity, still maturing for de novo binders).

## 3. Humanization

Reduce immunogenicity of a non-human antibody while preserving affinity:

- **CDR grafting** (Winter) — transplant the six CDRs onto human germline frameworks chosen for canonical-class match.
- **Back-mutations** — restore parental framework residues (Vernier, canonical-determining, VH/VL-interface) where the human framework costs affinity. The art is the *minimal* set.
- **Resurfacing/veneering** — mutate only solvent-exposed framework residues; lighter touch for stable scaffolds.
- **Humanness scoring** — T20, Z-score, OASis identity (BioPhi), Hu-mAb — proxies for how "self" the sequence looks to a human repertoire.

## 4. Affinity maturation

Improve KD by diversify-and-select:

- **Diversification** — targeted CDR libraries (NNK/NNS or trinucleotide soft-randomization, hotspot-focused), chain shuffling, error-prone PCR, DNA shuffling, or in-silico/DMS-guided design.
- **Selection** — display panning with decreasing antigen, **off-rate (kinetic) selection** with competitor for koff-limited leads, counter-selection against poly-reactivity/off-target.
- **Epistasis & the affinity ceiling** — good single mutations don't always combine; below a target KD further affinity is clinically pointless and raises specificity/developability risk. Set a target, not "as tight as possible".

## 5. Developability

Will the molecule survive expression, purification, formulation, storage, and dosing?

- **Sequence (chemical) liabilities** — deamidation (NG ≫ NS/NH/NT), isomerization (DG/DS/DT/DH), Met/Trp oxidation, N-glycosylation sequons (N-X-S/T, X≠P), unpaired cysteines, Asp-Pro fragmentation. Risk = motif rate × location (CDR worst) × solvent exposure.
- **Biophysical / colloidal** — thermostability (Tm/Tonset by nanoDSF), aggregation (%monomer by SEC, Tagg by DLS), self-association (AC-SINS), viscosity (high-concentration), hydrophobicity (HIC), poly-reactivity (PSR, baculovirus-particle ELISA).
- **In-silico structural flags — TAP (Therapeutic Antibody Profiler)** five metrics: total CDR length, patches of surface hydrophobicity (PSH), patches of positive charge (PPC), patches of negative charge (PNC), structural Fv charge symmetry (SFvCSP). Scored against the clinical-stage mAb distribution.
- **Immunogenicity** — MHC-II binding prediction (NetMHCIIpan), T-cell epitope content, Tregitopes, anti-drug-antibody (ADA) risk.

## 6. Formats

Full IgG, Fab/F(ab')2, scFv, VHH/nanobody (camelid single-domain), bispecifics (knobs-into-holes, CrossMab, DVD-Ig, BiTE/DART), Fc fusions, antibody–drug conjugates (ADCs). Format follows mechanism, half-life, and tissue-penetration needs.

## 7. Characterization

- **Kinetics/affinity** — SPR (Biacore) and BLI (Octet) for kon/koff/KD; ELISA for relative binding. **Avidity** from bivalent display inflates apparent affinity — measure intrinsic KD with monomeric antigen in a 1:1 orientation.
- **Epitope mapping** — competition/binning (sandwich, premix, tandem) for relative bins; HDX-MS, crystallography, cryo-EM, and AlphaFold-Multimer for residue-level epitopes.
- **Integrity/PTMs** — intact and peptide-map mass spec, SEC-MALS, capillary electrophoresis.

## 8. Apprenticeship & competency model (the organizing methodology)

Engineering antibodies is a craft learned by supervised practice. This workspace runs that learning as **competency-based progression**, borrowing the validated structure of apprenticeship and competency-based professional education:

- **Dreyfus model of skill acquisition** — Novice → Advanced Beginner → Competent → Proficient → Expert. Progress is a shift from rule-following to pattern-based intuition.
- **Miller's pyramid** — Knows → Knows How → Shows How → Does. Credentialing must reach "Does" (real work), not stop at "Knows".
- **Entrustment / supervision scale** — 1: observe only → 2: act under direct supervision → 3: act under indirect (on-call) supervision → 4: act independently → 5: supervise others. Entrustment is the unit of a sign-off.
- **Entrustable activities** — discrete, observable units of professional work (here: "humanize a standard IgG", "QC a kinetics run", "triage developability") entrusted as a whole.
- **Cognitive apprenticeship** (Collins & Brown) — modeling, coaching, scaffolding, articulation, reflection, exploration: the moves a mentor makes at each tier.
- **Evidence portfolio & workplace-based assessment** — competence is shown by accumulated real artifacts and direct observation, not by exam. Every command in this workspace tags the competency its output demonstrates, so the logbook *is* the portfolio.

### The eight core competencies

Sequence-liability assessment · humanization · affinity-maturation design · developability triage · binding-kinetics QC · epitope mapping · format/engineering strategy · regulatory & IP awareness. Each is tracked on the Dreyfus scale and gated by an entrustment level; see `context/references.md` "Competency ladder".

## 9. Common failure modes

- **Avidity mistaken for affinity** — the single most common kinetics error.
- **Over-humanization** — stripping back-mutations to maximize humanness, losing affinity.
- **Affinity won at developability's expense** — a CDR mutation that tightens KD but adds an aggregation patch or an NG liability.
- **Tier inflation** — advancing a trainee on a single good result or on hours rather than independent reps; corrupts the ladder.
- **Observation logged as competence** — watching ≠ doing; only independent reps count toward entrustment.

## 10. Operating constraints

- This is research/engineering tooling, **not clinical or medical advice**. Engineered antibodies require full preclinical and clinical evaluation before any human use.
- Wet-lab work touches biosafety (recombinant DNA / institutional biosafety committee), animal ethics (immunization → IACUC), and antibody-sequence IP / freedom-to-operate.
- Antibody sequences are often proprietary — treat candidate sequences as confidential and keep them out of any external service that retains data.
