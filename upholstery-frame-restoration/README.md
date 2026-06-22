# Upholstery Frame Restoration Workspace

> Restore the wooden carcass under the padding — and run the bench as a measured, statistically-controlled process, not a guess.

## What This Workspace Does

When an upholstered chair or sofa is stripped to its bare wooden frame, the restorer faces a structural problem (loose joints, racking, split rails, detached corner blocks) *and* a quality problem: how do you know the rebuilt frame is right when every job is one-off, the wood is moving, and the work disappears forever under fabric? This workspace pairs **upholstery frame restoration** with **statistical quality control (SQC)**. It treats each restored frame as a unit of process output and gives the bench the tools to measure the characteristics that matter, chart them over time, and separate normal craft variation from a real, fixable cause.

The SQC lens is adapted for craft realities. Restoration is usually **one frame at a time (n = 1)**, so the default chart is the **Individuals & Moving-Range (I-MR)** chart, with **DNOM** (deviation-from-nominal) for mixed frame types — not the high-volume X̄-R chart from a factory floor. Before any frame data is trusted, the workspace insists on a **gage R&R** study, because in a hand-measured shop the measurement method is often the biggest source of variation. And throughout, **conservation ethics gate the spec**: reversibility, minimal intervention, and retention of original material (AIC Code of Ethics) always override "in tolerance."

The result is a bench that can say, with evidence, *"this joint-gap creep is real and the new glue lot is the cause"* — or *"that's just hand-to-hand variation, leave it alone."*

## Why This Workspace Exists

Frame restoration quality is invisible after re-upholstery, so problems surface as customer callbacks months later — a wobble, a reopened joint, a chair that rocks. The usual response is to "adjust" after each slightly-off frame, which (per Deming) *adds* variation. This workspace codifies the discipline that prevents that: measure with a validated gauge, chart for stability, judge capability only on a stable process, and target improvement at the vital few defect causes — while never letting the statistics push toward harming an original object.

## Getting Started

### Prerequisites

- Claude Code (or any agent that reads `CLAUDE.md` + `.claude/commands/`).
- A way to record measurements: digital caliper, a diagonal/squareness method, and a **moisture meter** (pin or pinless, species-correctable).
- Basic frame-shop materials referenced by the repair specs: hot/liquid hide glue (conservation) or PVA (utility), clamps, hardwood for corner blocks/dowels.
- No coding required; the commands produce markdown reports saved to `outputs/`.

### Quick Start

1. Clone this workspace and open it with your agent.
2. Strip a frame and run the **`frame-intake-assessment`** prompt to get the measurement + SQC plan for the piece.
3. Open a job traveler with **`/restoration-traveler`**, then validate your gauges with **`/gage-rr`** before trusting any numbers.
4. Inspect geometry with **`/frame-square-check`** and grade joints with **`/joint-integrity-grade`**; feed each value into **`/control-chart`**.
5. Once a characteristic's chart is in control, judge **`/process-capability`**; at batch close, run **`/defect-pareto`** and the `batch-quality-review` prompt.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/frame-square-check` | Dimensional conformance (squareness, seat opening, leg spread) vs. tolerance | After stripping, to measure frame geometry |
| `/joint-integrity-grade` | Grade joints for gap/racking and assign keep/repair/replace | Assessing structural soundness of each joint |
| `/control-chart` | Build/update an I-MR or DNOM chart; flag out-of-control signals | Every measured value, to read it in process context |
| `/process-capability` | Cp/Cpk vs. tolerance, on an in-control process only | After a chart is stable, to judge the bench |
| `/defect-pareto` | Rank defect causes by count/cost; find the vital few | At batch close, to target improvement |
| `/gage-rr` | Measurement-system analysis on a gauge/jig | Before trusting any new characteristic's data |
| `/sampling-plan` | ANSI/ASQ Z1.4 acceptance sampling for a batch | Incoming trade frames or a finished joint batch |
| `/moisture-spc` | Chart wood MC vs. the glue-up window | Before committing any joinery |
| `/joint-repair-spec` | Method/adhesive/reinforcement/clamp spec for a graded joint | After grading, to plan the repair |
| `/restoration-traveler` | Per-frame traceability + conservation record | At intake, as the job's single source of truth |

## Directory Structure

```
upholstery-frame-restoration/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # 10 bespoke domain commands
├── context/
│   ├── concepts.md           # Frame anatomy, wood/moisture, conservation ethics, SQC fundamentals
│   ├── workflows.md          # Intake→chart→capability pipeline, gage R&R, OCAP, sampling, DMAIC
│   └── references.md         # Control-chart constants, WE rules, Cpk bands, Z1.4, EMC, joints/adhesives
├── prompts/                  # 4 reusable prompt templates
└── outputs/                  # Generated charts, capability studies, travelers, Pareto reports
```

## Example Use Cases

### A wobbly chair that "looks fine"
Strip it, grade the joints — discover two detached corner blocks driving the racking, not the joints that *look* open. Spec reversible re-gluing + new hardwood blocks, re-test racking, and feed the result to the chart.

### Joint gaps creeping up across the week
The I-MR chart shows 9 consecutive frames below center on joint gap. The OCAP traces it to a humidity drop pushing wood below the glue-up window; the fix is a moisture gate (`/moisture-spc`), not re-clamping every frame.

### A batch of trade frames from a new supplier
A `/sampling-plan` (Z1.4, AQL 2.5) sets n and Ac/Re; the rejected lot's defects feed a `/defect-pareto`, revealing that 80% of failures are one joint type — a single conversation with the supplier.

## Recommended MCP Servers / Tools

- **Filesystem MCP** — persist control-chart data, travelers, and capability studies in `outputs/` so the chart history survives between jobs.
- **Spreadsheet / CSV tooling** — hold the measurement series and moving ranges; control charts are only as good as their retained data.
- **Camera/photo workflow** — intake/disposition photos are required conservation documentation; link them from the traveler.

## Legal & Ethical Considerations

- **Conservation ethics bind the work.** Follow the AIC Code of Ethics: minimal intervention, reversibility, retention of original material, and full documentation. Statistical conformance never justifies harming an original object.
- **Repair before replace.** Sound original timber that is slightly off-nominal is kept and documented, not re-cut to a control limit.
- **Don't sample the irreplaceable.** Acceptance sampling is for replaceable batches; antique/significant pieces are inspected 100%.

## Technical References

- [AIC Code of Ethics & Guidelines for Practice](https://www.culturalheritage.org/about-conservation/code-of-ethics) — conservation principles governing disposition.
- [NIST/SEMATECH e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/) — control charts, capability, acceptance sampling (free).
- [ANSI/ASQ Z1.4 acceptance sampling](https://asq.org/quality-resources/z14-z19) — attributes sampling (successor to MIL-STD-105E).
- [AIAG MSA Reference Manual](https://www.aiag.org/) — gage R&R methodology.
- [Forest Products Laboratory *Wood Handbook* (FPL-GTR-282)](https://www.fpl.fs.usda.gov/products/publications/) — equilibrium moisture content and wood movement.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
