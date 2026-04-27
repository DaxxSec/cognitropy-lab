# Creation Report: Microeconomics Supply & Demand — Risk Scoring Matrix Workspace

## Why This Workspace Exists

Built by the Cognitropy daily build pipeline on **2026-04-27** (Day 33), this workspace pairs **microeconomic supply-and-demand analysis** with **risk-scoring matrices** — two disciplines that produce useful artifacts in isolation but that practitioners rarely combine. Microeconomics gives precise vocabulary (elasticity, surplus, equilibrium) but no decision-grade outputs. Risk matrices give widely-understood, GRC-tool-compatible outputs but are typically populated by gut feel.

The pairing solves both problems at once: the matrix imposes a scoring discipline, while microeconomic primitives become the *evidence* that makes each cell defensible. A demand-elasticity range becomes a likelihood-of-volume-response range; a stress-test surplus delta becomes a calibrated impact tier; the resulting risk register row is auditable in a way that purely qualitative scoring isn't.

## Build Seed

- **Category:** Finance & Economics
- **Domain:** microeconomics supply demand
- **Technique:** using risk scoring matrices
- **Crossover:** no
- **Anti-clustering:** none triggered (Finance & Economics 0× in last-5 entry window)

## Distinctive Choices

- **Elasticity-as-bridge** is the workspace's central design move. Three reference tables (`resources/elasticity-reference.md`) and a tier-threshold mapping (`resources/risk-matrix-templates.md`) make the bridge concrete.
- **Calibration is enforced.** `/calibrate-scale` is a hard prerequisite — the agent refuses to score uncalibrated. This is the single most-skipped step in real-world risk programs and the most expensive omission.
- **Antitrust hard line.** The workspace explicitly refuses to recommend cross-firm price coordination, a constraint baked into both `context/constraints.md` and the relevant slash commands.
- **Honest about partial equilibrium.** `README.md` and the stress-test command both flag that this is partial-equilibrium analysis and point to CGE / multi-sector models for general-equilibrium questions.
- **Citation discipline.** Every elasticity prior in `resources/elasticity-reference.md` carries a full citation. The agent is expected to refuse "AI-detected" elasticity values not traceable to either user data or a literature source.

## Reference Bar

Modeled after the quality of `wireless-protocol-re` (the canonical workspace cited in the daily-build skill) and the prior Finance & Economics workspace `forensic-accounting-fraud-detection`. Domain-knowledge depth, command specificity, and resource substance match the bar in those references.
