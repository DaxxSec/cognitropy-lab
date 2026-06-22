# Upholstery Frame Restoration — Core Concepts

Background the agent reads before acting. Two domains meet here: the **craft of restoring upholstered furniture frames** (the bare wooden carcass under the padding) and **statistical quality control (SQC)** — the discipline of telling stable, expected variation apart from a real, assignable problem. They are joined by one idea: a restoration shop is a **process**, and a frame is its **unit of output**, even when the batch size is one.

## 1. What "the frame" is

An upholstered chair or sofa is built in layers. From the inside out: the **frame** (load-bearing wooden skeleton), the **suspension** (webbing, coil or sinuous springs, spring ties), the **padding** (burlap, stuffing, foam, batting), and the **cover** (fabric/leather). Frame restoration is the bottom layer — once the upholstery is stripped, the carcass is exposed, repaired, re-squared, and made structurally sound before anything is built back on top. Everything above it inherits the frame's geometry, so a frame that is out of square or racks under load telegraphs through every later layer and shortens the life of the finished piece.

Key members:

- **Rails** — the horizontal members forming the seat box: front rail, back rail, two side rails. The **seat frame** is the load path for the sitter.
- **Stiles / posts** — vertical members (back posts, arm posts) carrying the back and arms.
- **Stretchers** — lower cross-members tying legs together for racking resistance.
- **Corner blocks** — triangular glue blocks screwed/glued into the inside corners of the seat box; the single most important anti-racking element and the most common failure point.
- **Slip tongues / dowels / tenons** — the joinery connecting members.

## 2. Frame joinery and how it fails

| Joint | Where used | Primary failure mode |
|---|---|---|
| Mortise & tenon | rail-to-post seat joints | tenon shoulder gap, glue-line failure, shrinkage-loosened fit |
| Dowel joint | factory-built 20th-c. frames | doweled joint "rocking" as glue fails; sheared dowels |
| Corner block (glued + screwed) | inside seat corners | block detached, split, or screws stripped → racking |
| Lap / bridle | arms, some backs | fastener loosening, splits along grain |
| Butt + fastener | cheap/modern frames | the joint relied on a screw or staple, not wood-to-wood |

The dominant frame failure is **racking** — the rectangular seat box deforming into a parallelogram under repeated off-axis load. Racking is what makes a chair "wobbly." It is resisted by the joints' moment stiffness and, above all, by intact corner blocks. The second failure is **joint-line opening** from old animal-glue (hide glue) crystallizing and releasing, often accelerated by wood movement.

## 3. Wood movement and moisture (the hidden process input)

Wood is hygroscopic: it gains and loses moisture with ambient relative humidity, and it moves **anisotropically** — far more across the grain (tangential > radial) than along it. Movement is governed by **Equilibrium Moisture Content (EMC)**, the moisture the wood reaches for a given temperature and RH.

- Furniture is built and lives at roughly **6–9% MC** (indoor EMC at ~35–50% RH).
- Gluing wood that is too wet (>~12%) means it will shrink after glue-up and open the joint; too dry means it can swell and crush fibers later.
- Hide glue and PVA both want mating surfaces near service EMC at glue-up.

Moisture is therefore a **process input variable** — the single uncontrolled factor most likely to put a joint-gap control chart out of control. This is why `/moisture-spc` exists: chart MC against the safe window before committing to joinery.

## 4. Conservation ethics (the constraint that overrides "in spec")

Restoration of an antique or significant piece is governed by conservation principles, codified for US practitioners in the **AIC (American Institute for Conservation) Code of Ethics & Guidelines for Practice**:

- **Minimal intervention** — do only what the object needs; do not over-restore.
- **Reversibility** — prefer treatments that can be undone (hide glue is reversible with heat/moisture; modern epoxies and PVA largely are not).
- **Retention of original material** — repair original timber before replacing it; document and retain what must be removed.
- **Documentation** — every treatment recorded (this is also good SQC: the traveler *is* the conservation record).

The tension this workspace must hold: SQC pushes toward conformance and replacement of out-of-tolerance parts; conservation pushes toward retaining original, slightly-imperfect material. **Ethics gate the spec** — a sound original rail that is 2 mm out of nominal is kept, not re-cut to hit a control limit.

## 5. Variation — the central SQC idea

Every measured characteristic varies. SQC's foundational distinction (Shewhart, 1924; Deming) is between two kinds of variation:

- **Common cause (chance / random)** — the inherent, stable noise of a process in control. Many small influences. You *cannot* fix it by reacting to individual points; you change the process to reduce it.
- **Special / assignable cause** — a specific, identifiable disturbance (a new restorer, a worn jig, a wet board, a different glue lot). It shows up as a signal on a control chart. You *find and remove* it.

**Tampering** — reacting to common-cause variation as if it were special (Deming's "Rule of the funnel") — actively *increases* variation. The whole point of a control chart is to stop the bench from adjusting a stable process after every slightly-off frame.

## 6. Control charts (and why I-MR fits a craft shop)

A control chart plots a characteristic over time against a **center line** and **upper/lower control limits (UCL/LCL)** computed from the process's own variation (typically ±3σ). In control = only common cause; out of control = a signal to investigate.

The textbook chart is **X̄-R** (subgroup average + range), but it assumes rational subgroups of n ≥ 2 produced under identical conditions. **Restoration is usually n = 1 per job** — one frame, measured once. The correct tool is therefore the **Individuals & Moving-Range (I-MR / X-MR)** chart:

- **I chart** — the individual measurement vs. limits derived from the average moving range.
- **MR chart** — the absolute difference between consecutive measurements (the short-term variation estimate).
- Limits: `UCL/LCL = X̄ ± 2.66 · M̄R` for individuals; `UCL_MR = 3.267 · M̄R`.

For short production runs of mixed frame types, **DNOM (deviation-from-nominal) charts** let dissimilar items share one chart by plotting (measured − nominal). Out-of-control rules: the **Western Electric / Nelson rules** (see references.md).

## 7. Process capability — Cp and Cpk

Once a process is *in control*, capability asks: does its natural spread fit inside the tolerance?

```
Cp  = (USL − LSL) / (6σ)              ← potential capability (spread only)
Cpk = min[(USL − X̄), (X̄ − LSL)] / (3σ)  ← actual capability (spread + centering)
```

- Cp ignores centering; Cpk penalizes a process that is on-target-width but off-center.
- Rough bands: Cpk < 1.0 incapable; 1.0–1.33 marginal; ≥ 1.33 capable; ≥ 1.67 high.
- **σ must come from an in-control chart** (use M̄R/d2 for I-MR). Capability of an unstable process is a fiction — this is the single most-violated rule in shop-floor SQC.

## 8. Measurement systems analysis (gage R&R)

Observed variation = true part variation **+ measurement-system variation**. Before trusting any of the above, quantify the measurement system (AIAG MSA manual):

- **Repeatability (EV)** — same operator, same gauge, same frame, repeated: the gauge's own noise.
- **Reproducibility (AV)** — different operators measuring the same frames: operator-to-operator bias.
- **% Gage R&R** = study variation from R&R ÷ total study variation. Rule of thumb: **<10% acceptable, 10–30% marginal, >30% unacceptable.**
- **ndc (number of distinct categories)** = 1.41 · (PV/GRR), want ≥ 5.

In a hand-measured craft shop the measurement system is frequently the dominant variance — a squareness "out of spec" is often the diagonal tape, the datum choice, or the operator, not the frame.

## 9. Acceptance sampling and Pareto

- **Acceptance sampling (ANSI/ASQ Z1.4, formerly MIL-STD-105E)** — decide accept/reject for a batch (e.g. incoming frames from a trade supplier, or a finished batch of re-glued joints) from a sample, given a lot size, AQL, and inspection level. Defines sample size `n` and acceptance number `Ac` (accept if defectives ≤ Ac).
- **Pareto principle (80/20)** — most defects come from a few causes. A Pareto chart ranks defect categories by frequency (or cost) to focus effort on the **vital few** (loose corner blocks, wet glue-ups) rather than the **trivial many**.

## 10. The coupling: a craft run as a controlled process

This is the workspace's central idea. SQC was built for high-volume manufacturing; restoration is low-volume, high-mix, one-off, irreplaceable. The bridge is to **measure the few characteristics that matter, chart them as individuals over time and across restorers, separate craft noise from real causes, and only then judge capability** — all while letting conservation ethics veto any "fix" that harms the object. The chart does not deskill the craft; it gives the restorer evidence about whether last week's joint-gap creep is just hand-to-hand variation or a sign the new glue lot, the dropped humidity, or a tired jig needs attention.

## Common Failure Modes

- **Tampering on common cause** — re-cutting/re-clamping in reaction to normal variation, which adds variation (Deming's funnel).
- **Capability on an unstable process** — quoting Cpk before the I chart is in control; the number is meaningless.
- **Trusting an unstudied gauge** — declaring a frame out of square when the *measurement* has 40% R&R.
- **Wrong subgrouping** — forcing X̄-R on n = 1 jobs instead of I-MR.
- **Spec over object** — re-machining sound original material to chase a control limit, violating reversibility/retention.
- **Ignoring moisture** — gluing up off-EMC wood, then blaming the glue when the joint opens months later.

## Operating Constraints

- **The object governs.** AIC ethics (reversibility, minimal intervention, retention) override conformance for antique/significant pieces.
- **n = 1 is normal.** Default to I-MR and DNOM short-run methods, not X̄-R.
- **Stability precedes capability precedes tolerance-tightening.** Never skip steps.
- **Wood moves.** Every dimension is a function of MC and RH at measurement time — record them or the data is uncomparable.
