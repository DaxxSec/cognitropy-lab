# Domain Knowledge — Comparative Anatomy & Standardized Inspection

*Reference document for the agent. Read on demand when conducting inspections, comparisons, or trait coding. Do not load eagerly — pull the section relevant to the task.*

## 1. What Comparative Anatomy Is (and Isn't)

Comparative anatomy is the study of similarities and differences in the anatomical structures of organisms, framed against their phylogenetic relationships. Its fundamental claim — descent with modification — means structural similarity has two possible explanations: **shared ancestry (homology)** or **convergent functional response to similar environmental pressure (analogy / homoplasy)**.

The discipline is **not** taxonomy (the art of classification) and **not** functional anatomy (the study of how form maps to performance), though it informs both. Modern comparative anatomy is heavily phylogenetic — descriptions are routinely paired with character-state codings for cladistic analysis.

## 2. Homology, Analogy, Homoplasy — The Central Distinction

| Term | Definition | Example |
|---|---|---|
| **Homology** | Shared structure due to common ancestry. Diagnostic: same topological position, same ontogenetic origin. | Forelimbs of bat, whale, human, bird — all derived from the tetrapod forelimb. |
| **Analogy** | Similar structure due to similar function, no shared ancestry of the structure itself. | Wings of bird and insect. |
| **Homoplasy** | Independent acquisition of similar character state in unrelated lineages — convergence (independent origin under similar selection) or parallelism (independent origin from similar precursor) or reversal (loss-then-regain). | Camera-eye in cephalopods and vertebrates (convergent). Streamlined body in tuna and dolphin (convergent). |

Homology operates at multiple levels — **historical homology** (shared ancestry) is the inferential prize; **biological / structural homology** (correspondence by topology + ontogeny) is the empirical evidence. They're correlated but not identical: a serial homologue (e.g. a vertebra) is structurally homologous to other vertebrae in the same animal but has the same historical homology relation only with serial homologues in other species.

**Operational test for homology** (Patterson 1982 + later refinement):
1. **Similarity of position** (topology) — does the candidate occupy the same place relative to invariant landmarks?
2. **Similarity of structure** — same composition, ontogeny, innervation, vascularization?
3. **Congruence** — does treating it as homologous yield a consistent phylogeny when combined with other characters?

Failing any one of these doesn't kill the homology hypothesis but downgrades it.

## 3. Vertebrate Body Plans (Bauplan)

The vertebrate body plan is conserved in broad strokes and elaborated/reduced lineage-specifically.

### Skeletal organization

- **Axial skeleton:** skull, vertebral column, ribs, sternum
- **Appendicular skeleton:** pectoral girdle + forelimb; pelvic girdle + hindlimb
- **Visceral / branchial skeleton:** jaw, hyoid, gill arches (varies dramatically across gnathostomes)

### Major regional body partitions (post-cranial)

cervical → thoracic → lumbar → sacral → caudal

Counts vary wildly — 7 cervicals in mammals (a near-universal constraint with rare exceptions: manatees 6, two-toed sloth ~5–8); variable in non-mammalian amniotes. Vertebral count is a routinely-coded comparative character.

### Major organ systems

| System | Diagnostic structures | Cross-vertebrate variation |
|---|---|---|
| Integumentary | epidermis (keratinized in tetrapods), dermis, derivatives (scales, feathers, fur, glands) | enormous; integument is one of the most lineage-diagnostic systems |
| Muscular | epaxial / hypaxial / appendicular | conserved gross plan; details (e.g. mammalian diaphragm) clade-specific |
| Skeletal | as above | radiations especially in jaws, limbs, postcranial axial |
| Cardiovascular | heart (chambered), aorta, systemic + pulmonary circulation | 2-chambered (fishes) → 3-chambered (anamniote tetrapods, most reptiles) → 4-chambered (mammals, archosaurs) |
| Respiratory | gills (water-breathers), lungs (air-breathers), parabronchi (birds) | foundational adaptive radiation |
| Digestive | mouth → pharynx → esophagus → stomach → intestine → cloaca/anus | dietary specialization drives gut length, stomach chambering, dentition |
| Urogenital | kidney type (pronephros / mesonephros / metanephros depending on stage and clade), gonadal arrangement | dramatic clade differences |
| Nervous | CNS (brain + spinal cord), PNS, autonomic | brain region elaboration is highly clade-diagnostic |
| Sensory | eye, ear, lateral line, olfactory, electroreception, magnetoreception | varies by ecological niche |

For invertebrate phyla, the body-plan reference depends entirely on the phylum (annelid metamerism vs. arthropod tagmosis vs. molluscan torsion vs. echinoderm pentaradial symmetry vs. cnidarian polyp/medusa). When working in invertebrate zoology, replace this section with the phylum-specific reference (Brusca & Brusca, Ruppert et al., or phylum monograph).

## 4. Anatomical Position & Directional Terminology

| Term | Meaning | Notes |
|---|---|---|
| Anterior / Posterior | toward head / tail | "rostral / caudal" in many vertebrate texts |
| Dorsal / Ventral | toward back / belly | invariant across most vertebrates |
| Medial / Lateral | toward midline / away | midline = midsagittal plane |
| Proximal / Distal | toward attachment / away | for limbs and projecting structures |
| Cranial / Caudal | toward head / tail | preferred over anterior/posterior for quadrupeds |
| Superior / Inferior | upward / downward | only meaningful in upright human; avoid in non-human vertebrates |
| Superficial / Deep | toward skin / interior | self-explanatory |

**Reference planes:** sagittal (left/right), coronal (= frontal; dorsal/ventral), transverse (= horizontal in a quadruped; cranial/caudal). For invertebrates and asymmetric organisms, define the planes the work uses up front.

## 5. Standardized Inspection — Core Methodology

A standardized inspection is the application of a pre-defined checklist to a specimen, recording **presence/absence**, **measurements**, **state codings**, and **provenance** in a structured form. The checklist serves four functions:

1. **Completeness anchor** — forces the inspector through every system and every diagnostic structure, even ones outside the immediate question.
2. **Vocabulary anchor** — every named structure uses the agreed convention; states are coded against pre-defined categories.
3. **Reproducibility anchor** — another worker applying the same checklist to the same specimen should produce concordant records.
4. **Provenance anchor** — specimen ID, locality, holding institution, and inspector ID are non-optional fields, not afterthoughts.

The vertebrate body-plan checklist for this workspace lives at `resources/vertebrate-body-plan-checklist.md`. Adapt it per taxon (a bird inspection won't traverse mammary glands; a fish inspection won't traverse a diaphragm); record adaptations in the inspection output, not by silently dropping checklist items.

### Inspection record structure

Every per-specimen inspection produces a markdown file under `outputs/inspections/<specimen-id>__<system>.md` with sections:

```
# Inspection Record

## Provenance
specimen_id: <institutional accession>
taxon: <binomial + author>
sex: <M / F / unknown>
age_class: <neonate / juvenile / subadult / adult / unknown>
preservation: <fluid / dry / mount / fossil / imaged-only>
locality: <coarse>
holding_institution: <accession-bearing institution>
inspector: <user OR "Comparative Inspector workspace">
inspection_date: <YYYY-MM-DD>
checklist_version: <e.g. "vertebrate-body-plan-checklist v1.0">

## System: <system-name>

### Per-structure record
- structure_name (TA/NAV/NAA): ...
- presence: <present / absent / damaged-uncertain>
- count (if applicable): ...
- measurement(s): ... (units, instrument)
- character_state (if coded): <state ID + description>
- notes: ...
- citations / cross-refs: ...
```

Aggregate across systems = full-specimen inspection.

## 6. Phylogenetic Context (for Trait Coding)

Comparative claims are conditioned on a phylogeny. Even if you're not running a tree analysis, your descriptions should be reconcilable with a published phylogeny.

- Use a recent, peer-reviewed tree (e.g. for mammals: Upham et al. 2019; for birds: Jetz et al. 2012 with caveats; for tetrapods broadly: Pyron & Wiens 2011 + updates; for fishes: Betancur-R et al. 2017).
- Distinguish **synapomorphy** (shared derived character) from **plesiomorphy** (shared ancestral character) — only synapomorphies define clades.
- **Autapomorphy** = unique derived character of one taxon.
- **Symplesiomorphy** = shared ancestral character — useless for resolving relationships.
- Character polarity is determined by **outgroup comparison** — a state present in the outgroup is plesiomorphic for the ingroup.

## 7. Common Failure Modes & How To Avoid Them

| Failure | Symptom | Fix |
|---|---|---|
| Naming inconsistency | Same structure called "X" in one record, "Y" in another | Lock the convention in `role.md`; agent must check before naming |
| Missing structure | A character that turns out to matter wasn't recorded | Run the full checklist always; don't skip systems even if "irrelevant" |
| Lost provenance | Specimen referred to by partial label, museum number missing | Provenance section is mandatory; halt if incomplete |
| Implicit homology | Trait matrix has "humerus length" as a column without justifying that all rows have a homologous humerus | Every column requires a homology statement in the matrix notes |
| Range invention | "Adult body length 1.5–2.0 m" without citation | Halt; demand citation or restate as "specimen-X length: N cm" |
| Convergent → "homologous" slip | Camera-eye described as "homologous between cephalopods and vertebrates" | Vocabulary discipline; agent re-reads constraints.md before homology assertions |
| Quantitative imprecision | "Large skull" instead of CBL = 88.2 mm | Always prefer measurement; "large" is unrecoverable from text |

## 8. Vocabulary Cheat Sheet — Borrowed Terms Frequently Misused

- **Cusp** (dentistry) — projection on a tooth crown, named (paraconid, protoconid, metaconid, etc.) per the tribosphenic nomenclature
- **Foramen** (osteology) — natural opening in a bone, transmitting nerve/vessel; name + identify what passes through
- **Process** (osteology) — a projection; specify its base location
- **Tubercle** vs. **Tuberosity** — small/large bony prominence respectively
- **Fossa** — depression
- **Sulcus** — groove; identify what occupies/produces it
- **Synapomorphy** ≠ **shared character**. A state shared with the outgroup is symplesiomorphy, not synapomorphy.
- **Suture** — fibrous joint between bones (cranial); distinct from "synchondrosis" (cartilaginous) or "synostosis" (fused)

## 9. References

- Patterson, C. 1982. "Morphological characters and homology." In *Problems of Phylogenetic Reconstruction*.
- Hall, B.K. 1994. *Homology: The Hierarchical Basis of Comparative Biology.*
- Wagner, G.P. 2014. *Homology, Genes, and Evolutionary Innovation.*
- Romer, A.S., Parsons, T.S. 1986. *The Vertebrate Body* (6th ed.).
- Kardong, K.V. 2018. *Vertebrates: Comparative Anatomy, Function, Evolution* (8th ed.).
- Liem, K.F., Bemis, W.E., Walker, W.F., Grande, L. 2001. *Functional Anatomy of the Vertebrates* (3rd ed.).
- Bookstein, F.L. 1991. *Morphometric Tools for Landmark Data.*
- *Terminologia Anatomica* (TA2, FIPAT 2019).
- *Nomina Anatomica Veterinaria* (6th ed., 2017).
- Brusca, R.C., Brusca, G.J. 2003. *Invertebrates* (3rd ed.).
- Ruppert, E.E., Fox, R.S., Barnes, R.D. 2004. *Invertebrate Zoology* (7th ed.).
