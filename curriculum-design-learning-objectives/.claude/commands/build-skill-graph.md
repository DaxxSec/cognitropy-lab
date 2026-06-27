# /build-skill-graph

Construct the prerequisite skill graph — a Bayesian-network DAG — that links the objectives and
drives both sequencing and remediation routing.

## Inputs
- An objective set (from `/draft-objectives` or supplied).
- Optional: known prerequisite constraints, instructor intuitions about dependence strength.

## Steps
1. Create one node per objective/skill.
2. Draw a directed edge A→B only when mastering A is genuinely required before B is learnable;
   justify each edge in one line. Reject "nice to have" edges — keep the DAG sparse.
3. Check for cycles (a prerequisite loop is a design error) and resolve them.
4. For each edge, record a dependence strength that seeds the conditional probability table:
   `P(child mastered | parents mastered)` vs. `| parents not mastered`.
5. Identify roots (entry points) and leaves (terminal objectives); note the critical path.
6. Emit a `pgmpy`-style structure (nodes + edges + CPT stubs) the quantitative commands can load.

## Output
A DAG description: edge list with rationales, CPT stubs, root/leaf annotations, and a text or
Mermaid diagram. Saved to `outputs/skill-graph-<topic>.md`.
