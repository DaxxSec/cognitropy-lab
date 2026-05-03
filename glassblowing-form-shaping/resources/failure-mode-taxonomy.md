# Failure-Mode Taxonomy — Glassblowing Form Shaping

The diagnostic decision tree used by `/post-mortem`. Five primary modes plus secondary contributors. Each mode lists its (When, Where, How) signature, the typical physical cause, and the corrective action.

## Decision Tree

```
Q1 — When did the failure occur?
├── During working (at the bench)             → Mode 1: Cold Check
├── Immediately on transfer to lehr           → Mode 2: Thermal Shock
├── During the anneal cycle (ramp segment)    → Mode 3: Anneal Crack
├── Within 24h after lehr complete            → Mode 4: Residual Strain
├── Days to weeks after                       → Mode 5: COE Mismatch (slow cracker)
└── Months later, no clear trigger            → Mode 6: Storage Thermal Shock
                                                   or Coldwork-Induced Stress

Q2 — Where did the crack initiate?
├── Punty mark                                → Cold punty (Mode 1) or pickup ΔT (Mode 2)
├── Color/cane interface                      → COE incompatibility (Mode 5)
├── Wall thickness inflection                 → Anneal crack at gradient (Mode 3)
├── Surface inclusion or bubble               → Cord / devit / contamination (secondary)
├── Through body, no clear initiation         → Residual strain (Mode 4)
└── Coldwork edge or grind line               → Surface stress concentration (Mode 6)

Q3 — Fracture surface character
├── Smooth conchoidal                         → Clean stress crack (Modes 3, 4, 5, 6)
├── Crystalline / cloudy at the surface       → Devit-driven (secondary; surface tensile strength reduced)
├── Branching / radial                        → High-energy thermal shock (Mode 2 confirmed)
└── Single straight crack at a feature line   → Anneal crack (Mode 3 confirmed)
```

## Primary Failure Modes

### Mode 1 — Cold Check
- **Signature:** (A1, B1, C1) most often; bench-time cracking
- **Physical cause:** Working glass below working point (10⁴ poise), or contact with a cold tool that locally crashed surface T below strain point
- **Corrective action:** Reheat sooner; pre-heat punty in glory hole; warm jacks if first use of the day
- **Apprentice tip:** Watch for the "drag" feel as glass stiffens — operating past that is when most cold checks initiate

### Mode 2 — Thermal Shock (Lehr Load)
- **Signature:** (A2, varies, C3 — branching/radial); crack appears within seconds to minutes of lehr loading
- **Physical cause:** Surface ΔT > ~80 °C between the piece and the lehr interior at moment of load. Tensile stress at the surface exceeds tensile strength.
- **Corrective action:** Pre-heat lehr to within 50 °C of the piece's measured surface temperature; use a slower load (open door briefly, place, close, allow ramp); for thick pieces, consider an intermediate "transfer kiln" at ~600 °C
- **Recovery:** none — the crack is propagated. Document and move on.

### Mode 3 — Anneal Crack
- **Signature:** (A3, B3, C4); discovered when lehr is unloaded
- **Physical cause:** Anneal-to-strain ramp rate too fast for the wall thickness; core stays hotter than surface, generating tensile stress at the surface that exceeds tensile strength
- **Corrective action:** Reduce anneal-to-strain rate per `/cool-curve`'s formula `K / thickness²`; for pieces with thickness inflections, slow the ramp to the worst case
- **Recovery:** Re-fire the cracked piece to anneal point, hold for 50% longer than original, slow-ramp at half the original rate. Cracks initiated at this stage sometimes "heal" (surfaces re-fuse) but the residual seam is visible.

### Mode 4 — Residual Strain (Insufficient Hold)
- **Signature:** (A4, B5, C1); piece survives lehr unload but cracks within 24h
- **Physical cause:** Hold at anneal point too short, OR strain-to-100 °C ramp too fast
- **Corrective action:** Increase hold time per the table in `glass-viscosity-reference.md`; double the strain-to-100 °C ramp segment if not already at controller minimum
- **Recovery:** Re-anneal with longer hold + slower ramp. Often successful for Mode 4 specifically.

### Mode 5 — COE Mismatch (Slow Cracker)
- **Signature:** (A5, B2, C1); crack at color-glass / base-glass interface, days to months
- **Physical cause:** Differential contraction during cool. The strain accumulates and propagates a crack through the interface as temperature cycles or load is applied.
- **Corrective action:** Pull the suspect rod lot from rotation. Run `/lineage-trace` Mode A on the lot to identify all affected pieces. Pretest before re-introducing.
- **Recovery:** None at the piece level; the structural mismatch is permanent.

### Mode 6 — Storage Thermal Shock / Coldwork Stress
- **Signature:** (A6, B6, C1); crack with no apparent trigger, often at a coldworked edge or after a storage temperature swing
- **Physical cause:** Either: a temperature swing in the storage area created surface stress that found a defect, OR coldwork (grinding, polishing) introduced microcracks that propagated under existing residual strain
- **Corrective action:** Monitor storage area temperature; for coldworked pieces, consider a post-coldwork reanneal at anneal point for 30 min; check ambient cycling near the storage area
- **Recovery:** None.

## Secondary Contributors

### Devitrification (Devit)
- **Visible:** Crystalline haze on the surface, often dull or matte where the rest of the piece is glossy
- **Cause:** Glass held in the devit window (700–900 °C for soda-lime, 1100–1200 °C for borosilicate) for extended time. The most common trigger is long bench operations without reheats.
- **Effect:** Devit reduces surface tensile strength and provides crack initiation sites. A piece can survive anneal but crack later through a devit zone.
- **Corrective action:** Shorter operations between reheats. Some studios use boric acid or anti-devit sprays; these have tradeoffs and the agent should defer to the studio's existing practice.

### Cord
- **Visible:** Visible streaks or striations in the body of the glass, often refracting differently than the surrounding glass
- **Cause:** Compositional inhomogeneity in the melt (incomplete mixing of cullet additions, devitrified material remixed in)
- **Effect:** Cord lines are stress concentrators and can initiate cracks under modest load
- **Corrective action:** This is upstream of form work; flag the melt batch ID in the lineage record. Repeated cord on the same melt batch indicates a furnace operation issue.

### Bubble Inclusions
- **Visible:** Trapped bubbles in the glass body
- **Cause:** Air trapped during gathering, or outgassing from cullet additions
- **Effect:** Cosmetic at small scale; structural problem if large enough to act as a stress concentrator
- **Corrective action:** Slower gather; let the gather "soak" briefly in the furnace before withdrawing; check cullet for organic contamination

## Known-Bad Pairings (Studio-Specific Append List)

(Populated as `/lineage-trace` Mode A surfaces strong-signal correlations. Each entry is a documented compatibility failure that should not be re-attempted.)

| Date documented | Glass A | Lot A | Glass B | Lot B | Failure rate | Notes |
|-----------------|---------|-------|---------|-------|--------------|-------|
| | | | | | | |

## Versioning

Append a row when a new mode is added or an existing mode's corrective action is updated based on studio findings:

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-05-03 | Initial taxonomy seeded |
