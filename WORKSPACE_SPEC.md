# Cognitropy Workspace Spec — Hybrid Model

Cognitropy workspaces use a **hybrid** of two upstream Daniel Rosehill specs, optimised for the cognitropy use case (daily public-showcase artifacts seeded by an entropy engine):

- **Foundational shape** — flat directory tree, no legacy ceremony — from `danielrosehill/Claude-Workspace-Foundational-Plugin`.
- **Bespoke depth** — per-workspace `.claude/commands/` and rich `context/` substance — from the retired `danielrosehill/Claude-Agent-Workspace-Model` spec, which originally seeded cognitropy.

Neither pure form fits cognitropy alone. The foundational plugin is too thin (5-line README, no per-workspace commands) for a public-showcase artifact; the legacy model is too heavy (`/onboard`, `planning/`, `work-log/`, `user-docs/`, `CREATION_REPORT.md`) for one-shot showcase pieces. The hybrid keeps what each does well.

## Required Directory Structure

```
workspace-name/
├── CLAUDE.md                # Lightweight: identity + role + commands table + plugin-primitives note
├── README.md                # Comprehensive showcase intro: what / why / quick start / commands / refs
├── .claude/
│   └── commands/            # 5-10 bespoke domain commands (NO required /onboard)
│       └── <name>.md        # Each: brief purpose + Inputs / Steps / Output
├── context/
│   ├── concepts.md          # Domain knowledge — taxonomies, frameworks, failure modes (80-200 lines)
│   ├── workflows.md         # Methodology — step-by-step procedures, decision trees (50-150 lines)
│   └── references.md        # Lookup tables, cheat-sheets, links to upstream catalogues (30-100 lines)
├── prompts/                 # 3-5 bespoke reusable prompt templates
│   └── <name>.md            # Each: Purpose / Prompt Template (parameterised) / Expected Output
└── outputs/                 # Generated artifacts; .gitkeep at scaffold time
    └── .gitkeep
```

## File Guidelines

### CLAUDE.md (~25-40 lines)

Loaded with every prompt, so stays compact. Sections:

- `# <Domain> Workspace` header
- One-paragraph agent role tied to today's domain
- `## Context References` — stubs pointing to `context/concepts.md`, `context/workflows.md`, `context/references.md`, `prompts/`
- `## Available Commands` — markdown table listing the 5-10 commands in `.claude/commands/`
- `## Foundational Instructions` — 3-5 numbered items (repo-as-memory, legal/ethical reminders, reproducibility, etc.)
- `## Optional plugin primitives` — one-line note that `/workspace-foundational:context-sweep` and `/workspace-foundational:find-template` are available **if** the user has the foundational plugin installed; the workspace works without them.

### README.md (50-100 lines)

This is the public-facing showcase. Sections:

- Short tagline (one sentence under `>`)
- What this workspace is and why it exists
- Getting started — prerequisites + numbered quick-start steps
- Full command reference table (when to use each)
- Directory structure tree
- 3-5 example use cases
- Recommended MCP servers / tools
- Legal & ethical considerations if applicable
- Technical references with real links

### .claude/commands/<name>.md × 5-10 (natural floor > forced ceiling)

Bespoke per today's domain. Each command file: brief purpose sentence, then `## Inputs`, `## Steps` (numbered procedure), `## Output`.

If today's domain genuinely only yields 5-6 substantive bespoke commands, stop at the natural number — padding to hit the upper bound with generic commands is worse than honoring the floor. Conversely, rich domains can comfortably hit 10 and should.

**Anti-patterns:**
- Generic command names (`/analyze`, `/triage`, `/report`, `/summarize`) reused across domains.
- The legacy `/onboard` interview command (retired — workspaces are showcase artifacts, not personal projects to interview the user about).
- Padding the command count past the natural depth of the topic.

### context/concepts.md (80-200 lines)

Real domain knowledge: key concepts, taxonomies, common failure modes, formulas/methods. Cite real standards, papers, specs where they apply.

### context/workflows.md (50-150 lines)

Step-by-step workflows tied to today's `technique` field from the engine. Decision trees, methodology phases, expert know-how.

### context/references.md (30-100 lines)

Lookup tables, cheat-sheets, links to upstream catalogues. Compact lookup data, not prose.

### prompts/<name>.md × 3-5

Reusable prompt templates for recurring tasks in today's domain. Each: `## Purpose`, `## Prompt Template` (parameterised slots in `[brackets]`), `## Expected Output`. Natural floor applies here too — 3 substantive prompts beats 5 padded ones.

## Key Principles

1. **Foundational shape, legacy depth.** Three flat dirs (`context/`, `prompts/`, `outputs/`) like the foundational plugin; per-workspace `.claude/commands/` like the legacy model.
2. **Self-contained.** Workspace works without any plugin install — clone-and-go.
3. **Foundational plugin is an *optional* enhancer**, not a dependency. CLAUDE.md mentions it; nothing breaks without it.
4. **No `/onboard` requirement.** Workspaces are showcase artifacts; there's no user to interview.
5. **No `planning/`, `work-log/`, `user-docs/`, `CREATION_REPORT.md`, `context/{project,role,constraints}.md`, `resources/`, `context/for-agent/` subdir.** All retired with the legacy spec.
6. **Bespoke per topic.** Two consecutive daily workspaces should never share command names. Generic command sets across domains is the failure mode this exists to prevent.

## Migration history

- **2026-04-01 → 2026-05-09** — workspaces followed the legacy `danielrosehill/Claude-Agent-Workspace-Model` spec verbatim (`.claude/commands/onboard.md`, `context/for-agent/`, `planning/`, `user-docs/`, `work-log/`, `CREATION_REPORT.md`, `resources/`). The upstream Claude-Agent-Workspace-Model repo was retired by the author and superseded by `Claude-Workspace-Foundational-Plugin`. The 32 workspaces from this period remain in `files/workspaces/` with the legacy shape — they are showcase artifacts of that era and are not retroactively migrated.
- **2026-05-10 (briefly)** — two workspaces were built in pure-foundational shape (`hybrid-system-energy-management`, `soil-microbiome-management`) during a misfired migration. Same-day regeneration in the hybrid shape (this commit and the next).
- **2026-05-10 → 2026-05-19** — hybrid model with **one build per day** at 06:05 local.
- **2026-05-20 → present** — **doubled cadence: morning (06:05) + evening (18:05)** builds per day, fully-independent rolls per slot. Engine pool expanded 363 → 451 domains and 22 → 25 categories (added Culinary & Beverage + Metallurgy & Materials Science + Firearms & Ballistics). Per-workspace command range bumped from 4-8 to 5-10 (natural floor > forced ceiling), prompts from 2-4 to 3-5. Engine now emits `slot`, `pool_version` fields; history schema additive. Pool version: `v2-451d-25c`.

## Upstream references

- `danielrosehill/Claude-Workspace-Foundational-Plugin` — https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin (vendored at `skills/cognitropy-daily-build/templates/foundational/` for reference; not used by the build).
- `danielrosehill/Claude-Agent-Workspace-Model` — retired; the spec it described is preserved partially in this hybrid (`.claude/commands/`, deep `context/` substance) and partially abandoned (`/onboard`, `planning/`, `work-log/`, `user-docs/`, `CREATION_REPORT.md`).
