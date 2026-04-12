# Creation Report: Curriculum Design Peer Review

## Assignment
- **Date:** 2026-04-12 (Day 18)
- **Category:** Education & Training
- **Domain:** Curriculum Design Learning Objectives
- **Technique:** Using Peer Review Workflows
- **Crossover:** No

## Rationale

Education & Training is a domain that benefits enormously from structured AI assistance. Curriculum design — specifically the craft of writing measurable, aligned learning objectives — is a skill gap across all educational levels. Many instructors write objectives that are vague ("students will understand…"), misaligned with assessments, or disconnected from standards frameworks.

Peer review is the technique assigned by the Cognitropy engine, and it maps naturally to curriculum design: the iterative feedback loop of submit → review → revise is exactly how high-quality curricula are developed in well-resourced programs. Most educators lack access to dedicated instructional designers or peer review structures. This workspace fills that gap.

## Design Decisions

1. **Backward Design as the spine** — Wiggins & McTighe's UbD framework provides the structural backbone. Every command flows from outcomes to evidence to activities.

2. **Bloom's Revised Taxonomy integration** — The agent enforces measurable verb usage in all learning objectives, with a built-in reference for cognitive process dimensions.

3. **Structured peer review protocol** — Rather than freeform feedback, the `/peer-review` command follows a criteria-based rubric covering alignment, rigor, clarity, and inclusivity.

4. **Standards-agnostic flexibility** — The `/align-standards` command supports multiple frameworks (Common Core, NGSS, ISTE, etc.) without being locked to any one system.

5. **Rubric generation** — The `/rubric-gen` command closes the loop by producing assessment rubrics directly from the learning objectives, ensuring alignment throughout.

## Domain Knowledge Sources

- Bloom's Revised Taxonomy (Anderson & Krathwohl, 2001)
- Understanding by Design (Wiggins & McTighe, 2005)
- Webb's Depth of Knowledge framework
- Quality Matters rubric standards for online learning
- Universal Design for Learning (UDL) guidelines

## What Makes This Workspace Useful

An educator can clone this workspace, run `/onboard`, and immediately start designing curriculum units with built-in quality assurance through the peer review workflow. The agent serves as both a knowledgeable collaborator and a structured reviewer, catching misalignment and suggesting improvements at every stage.
