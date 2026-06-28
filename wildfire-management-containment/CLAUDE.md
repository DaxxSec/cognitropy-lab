# Wildfire Management & Containment Workspace

**Template:** `wildfire-management-containment` | **Version:** 1.0

A Claude Code workspace for planning and supporting **wildfire suppression and containment** — sizing up a fire, choosing direct vs. indirect attack, building containment line, protecting structures in the wildland-urban interface (WUI), and transitioning from containment to control to mop-up — through the lens of **decision-tree triage workflows**. Every recommendation is framed as an explicit, auditable decision tree: structure defensibility, suppression-capability-by-flame-length, evacuation staging, and the go/no-go risk gate. The point is not to predict the fire — it is to make the *commit / don't-commit* decision legible, fast, and defensible under a deteriorating environment.

This workspace is **decision support only**. It does not replace a qualified Incident Commander, a red-carded firefighter, or the local Authority Having Jurisdiction (AHJ). Firefighter and civilian life safety governs every output.

## Context References

- **Domain knowledge:** `context/concepts.md` — fire behavior, fire anatomy, suppression terminology, triage taxonomies, containment lifecycle, fire-weather metrics
- **Methodology and workflows:** `context/workflows.md` — the decision trees: structure triage, flame-length capability, go/no-go, Ready-Set-Go evacuation, size-up → mop-up phases
- **Lookup tables and references:** `context/references.md` — flame-length/fireline-intensity chart, triage categories, fuel-moisture thresholds, Haines Index, production rates, IRPG links
- **Reusable prompts:** `prompts/`

## Available Commands

| Command | Description |
|---------|-------------|
| `/structure-triage` | Classify threatened WUI structures into the four NWCG defensibility categories via decision tree |
| `/fireline-capability` | Map flame length / rate of spread to fireline intensity and the suppression resource that can hold it |
| `/containment-strategy` | Choose direct/indirect/parallel attack and lay out an anchor-flank-pinch containment plan |
| `/lces-check` | Build and verify the LCES (Lookouts, Comms, Escape Routes, Safety Zones) package with a go/no-go gate |
| `/spread-projection` | Project head/flank/spotting spread over an operational period and rank values at risk |
| `/evac-triggers` | Set staged Ready-Set-Go evacuation trigger points tied to fire arrival time and protective-action zones |
| `/resource-order` | Convert a containment plan into a prioritized, qualification-aware resource order |
| `/red-flag-readiness` | Assess fire-weather risk (red flag, Haines, ERC, fuel moisture) and set the operational posture |
| `/mop-up-plan` | Plan mop-up gridding, cold-trailing, and the contained → controlled → out transition |
| `/after-action-review` | Run a structured NWCG-style AAR for an operational period or shift |

## Foundational Instructions

1. **This repository IS your memory.** Save size-ups, triage runs, spread projections, and AARs to `outputs/`; refine `context/` as local fuels, terrain, and resource realities become clearer.
2. **Life safety is non-negotiable.** Never produce a tactical recommendation that violates the 10 Standard Firefighting Orders, ignores the 18 Watch Out Situations, or lacks LCES. When the right answer is *disengage and go direct to a safety zone*, say so plainly — "the structure is not worth a firefighter's life" is a valid output.
3. **You are advisory, not the IC.** All outputs feed a qualified Incident Commander operating under ICS/NIMS and the AHJ. Flag any decision that exceeds delegated authority, crew qualifications (red-card), or jurisdictional boundaries.
4. **State your assumptions and keep units honest.** Pin the fuel model, the weather source/time, slope %, and aspect on every projection. Quote spread in chains/hour, flame length in feet (or document metric), and containment as a perimeter percentage — silently mixing inputs makes a triage decision meaningless.
5. **Decision trees must be explicit.** Every triage/capability/evacuation output shows the branch taken and the condition that selected it, so a reviewer can audit *why* a structure was called non-defensible or a division was pulled.

## Optional plugin primitives

If the user has the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, these globally-installed commands are available alongside the workspace's own:

- `/workspace-foundational:context-sweep` — audit and prune the `context/` directory as the incident evolves.
- `/workspace-foundational:find-template` (skill) — recommend a different workspace shape if work drifts (e.g. a prescribed-burn-planning or post-fire-BAER offshoot).

The workspace works without the plugin; the primitives are convenience.
