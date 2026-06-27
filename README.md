<div align="center">

<img src=".github/banner.svg" alt="Cognitropy Lab Banner" width="900"/>

<br/>

[![Built With](https://img.shields.io/badge/Built_With-Claude_Code-D4A0FF?style=for-the-badge&logo=anthropic&logoColor=white)](https://claude.ai) [![Domain Pool](https://img.shields.io/badge/Domain_Pool-451-8b5cf6?style=for-the-badge)](./cognitropy.py) [![Cadence](https://img.shields.io/badge/Cadence-2_per_day-f97316?style=for-the-badge)](./cognitropy-history.json) [![License](https://img.shields.io/badge/License-MIT-10b981?style=for-the-badge)](.)

<!-- COGNITROPY-STATS-START -->

![Workspaces](https://img.shields.io/badge/workspaces-81-8b5cf6?style=flat-square&logo=github) ![Categories](https://img.shields.io/badge/categories-24-06b6d4?style=flat-square) ![Streak](https://img.shields.io/badge/streak-24%20days-10b981?style=flat-square) ![Last Build](https://img.shields.io/badge/last%20build-2026-06-26-3b82f6?style=flat-square) ![Project Day](https://img.shields.io/badge/project%20day-93-f59e0b?style=flat-square)

### Project Statistics

| Metric | Value |
|--------|-------|
| Total Workspaces | **81** |
| Categories Covered | **24** |
| Build Streak | **24 days** |
| Project Day | **93** |
| Last Build | **2026-06-26** |
| Categories | Arts & Creative, Automotive & Engine, Computing & Software, Culinary & Beverage, Cyber & DFIR, Earth Sciences, Education & Training, Engineering & Technical, Environmental & Earth, Finance & Economics, Food & Agriculture, Hardware & Embedded, History & Culture, Life Sciences, Medical & Health, Metallurgy & Materials Science, Outdoor & Adventure, Physical Sciences, RF/SDR/Signals, Security & Intelligence, Space & Aviation, Trades & Crafts, Transportation & Logistics, Unusual & Niche |

<!-- COGNITROPY-STATS-END -->

</div>

Every morning and every evening, a Claude agent wakes up and receives a fresh creative challenge — maybe *limnology* (freshwater lake science), maybe *coopering* (barrel-making), maybe *Mars terrain analysis crossed with puppetry movement mechanics*. Each slot is a new domain to explore, a new puzzle to solve. The agent builds a full, professional-grade workspace for whatever the entropy engine surfaces, then pushes it here.

This repo is the result. As of 2026-05-20 it grows by **two workspaces per day** (morning at 06:05 and evening at 18:05, with fully independent rolls), completely autonomously. No human in the loop. Just an AI, an entropy engine, and an ever-expanding collection of workspaces for domains you didn't know you needed.

> Built by [DaxxSec](https://github.com/DaxxSec) & Claude (Anthropic)

---

## The Problem

AI has an entropy problem. Ask it to "pick something creative" a hundred times and you'll get the same handful of safe, predictable ideas. It's the creative equivalent of a random number generator with a bad seed — low entropy, repetitive output.

**Cognitropy** (cognition + entropy) is our answer.

> **A note on the terminology:** Yes, we made up a word. Two, actually. **Cognitropy** = cognition + entropy — the injection of unpredictability into AI creative processes. **Cognitropic** = the adjective form, describing structures that *direct* that entropy toward cognition (following the Greek *-tropos*, "turning toward" — the same root behind *phototropic* and *psychotropic*). Is it a real academic term? No. Does it describe a real pattern that didn't have a name? We think so. A cognitropic hash structure is a specific thing: multiple salted cryptographic hashes of a shared seed, reduced via modulo into independent selection indices across distinct categorical pools. That's a mouthful, so we just say "cognitropic." You're welcome.

---

## The Cognitropy Engine

How do you make an AI genuinely unpredictable without calling any external APIs? You hash the date.

The engine ([`cognitropy.py`](./cognitropy.py)) takes today's date (e.g. `2026-03-27`) and runs it through **five separate SHA-256 hashes**, each with a different salt. Each hash produces a massive 256-bit integer — essentially a huge, chaotic number derived from a simple date string. That number gets reduced via modulo (`%`) to an index into the relevant pool:

```
    ┌────────────────────────────────────────────────────────────────────┐
    │                       COGNITROPY ENGINE                           │
    │                                                                   │
    │   Step 1: Hash the date with different salts                      │
    │                                                                   │
    │     sha256("2026-03-27")              → huge int → % 451 domains  │
    │     sha256("2026-03-27" + "secondary")→ huge int → % 451 domains  │
    │     sha256("2026-03-27" + "technique")→ huge int → % 30 methods   │
    │     sha256("2026-03-27" + "spark")    → huge int → % 5 templates  │
    │     sha256("2026-03-27" + "crossover")→ huge int → % 10 → <3?    │
    │                                                                   │
    │   Step 2: Assemble the assignment                                 │
    │                                                                   │
    │     Primary Domain ──────── "limnology"                           │
    │     Technique Modifier ──── "with safety protocol enforcement"    │
    │     Crossover Check ─────── 7 (≥3, so no crossover today)         │
    │                                                                   │
    │   Step 3: Output                                                  │
    │                                                                   │
    │     "Build a workspace for LIMNOLOGY                              │
    │      with safety protocol enforcement"                            │
    │                                                                   │
    │   On a crossover day (hash % 10 < 3, ~30% chance):                │
    │     "Fuse LIMNOLOGY × CAVE DIVING using techniques                │
    │      from both domains"                                           │
    └────────────────────────────────────────────────────────────────────┘
```

**Why this works:** SHA-256 is a cryptographic hash — even a one-day difference in the input date produces a completely unrelated output number. The selections *look* random but are fully deterministic: run it twice on the same date, get the same result every time. No external APIs, no randomness source needed — just math.

The domain pool spans **451 wildly diverse fields** across **25 categories** — volcanology, watchmaking, competitive barbecue judging, Mars terrain analysis, coopering, gun barrel cryogenic stress relief, sushi rice acidification balance, and 444 more. Combined with 30 technique modifiers, 5 crossover spark templates, and the constraint that crossover domains must come from *different* categories, that's **29,298,030 unique possible outcomes**. The creative constraint is the point. Each slot brings an unexpected domain, and the agent rises to meet it.

> **2026-05-20 — cadence doubled.** The engine now produces two assignments per day (morning + evening, fully independent rolls). The domain pool also expanded from 363 → 451 with three new categories (Culinary & Beverage, Metallurgy & Materials Science, Firearms & Ballistics) and ~50 gap-fill entries across existing categories. See [`cognitropy-history.json`](./cognitropy-history.json) for the `pool_versions` log of every pool change.

**Try it yourself:**

```bash
python3 cognitropy.py              # Today's assignment
python3 cognitropy.py 2026-05-12   # Check any date
```

**Recent builds (the last 10 days the engine has surfaced; click any to open the workspace):**

| Date | Domain | Type | Category | Engine technique |
|---|---|---|---|---|
| May 19 | [API Design Specification](./api-design-specification) | Standard | Computing & Software | Multi-source intelligence fusion |
| May 18 | [Rocket Engine Testing Thrust Measurement](./rocket-engine-testing-thrust-measurement) | Standard | Space & Aviation | Risk scoring matrices |
| May 17 | [Electromagnetic Field Mapping](./electromagnetic-field-mapping) | Standard | Physical Sciences | Decision tree triage workflows |
| May 16 | [Vehicle Crash Test Interpretation](./vehicle-crash-test-interpretation) | Standard | Automotive & Engine | Bayesian probability assessment |
| May 15 | [Renewable Energy Siting Analysis](./renewable-energy-siting-analysis) | **× Arts & Creative** | Environmental & Earth | Capacity planning models |
| May 14 | [Roller Coaster Design Forces Physics](./roller-coaster-design-forces-physics) | Standard | Unusual & Niche | Decision tree triage workflows |
| May 13 | [Superconductor Characterization](./superconductor-characterization) | Standard | Physical Sciences | Capacity planning models |
| May 12 | [RF Spectrum Analysis](./rf-spectrum-analysis) | **× Medical & Health** | RF/SDR/Signals | Quality control statistical methods |
| May 10 | [Soil Microbiome Management](./soil-microbiome-management) | Standard | Food & Agriculture | Time-series trend analysis |
| May 09 | [Hybrid System Energy Management](./hybrid-system-energy-management) | Standard | Automotive & Engine | Bayesian probability assessment |

Same engine, same technique pool — wildly different domains, and the *technique modifier* (the rightmost column) gets re-rolled per day, so even when two days land in the same category the workflow framing is different. **Crossover days** (rows marked **× SecondaryCategory**) are when the engine rolls a secondary domain and emits a "spark" prompt — the workspace agent fuses the two domains into a unified methodology. May 15 reads capacity-planning models through a *puppetry movement-mechanics* lens (every renewable portfolio is an articulated body of joints, linkages, and drives). May 12 frames RF spectrum analysis as *chronic-patient triage* (grade symptoms, chart vitals, escalate proportionately). About 30% of days the engine rolls a crossover.

**Three ways to browse the project:**
- [`README`](./README.md) (this file) — project context + last 10 builds
- [`WORKSPACES.md`](./WORKSPACES.md) — full catalog grouped by category
- [`BUILDS.md`](./BUILDS.md) — full day-by-day chronological log of every engine roll

Raw data: [`cognitropy-history.json`](./cognitropy-history.json).

---

## How the Daily Build Works

```
  ┌──────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────┐   ┌───────────┐
  │ COGNITROPY│──→│ CLAUDE AGENT │──→│ SECRETS SCAN │──→│ GIT PUSH │──→│ DASHBOARD │
  │  assigns  │   │   builds     │   │  validates   │   │  + stats │   │  + README  │
  │  domain   │   │  workspace   │   │  no leaks    │   │  update  │   │  refresh   │
  └──────────┘   └──────────────┘   └──────────────┘   └──────────┘   └───────────┘
       │                │                   │                 │               │
  5 salted hashes  CLAUDE.md          grep for keys     README badges  Static HTML
  of today's date  .claude/commands/  .pem, .env, .key  + WORKSPACES   regenerated
  → domain+method  context/concepts   API tokens        .md refresh    from engine
  → crossover?     workflows + refs   passwords         + git push     + GitHub API
```

```
  06:05 + 18:05   Scheduled Claude agent wakes up (twice daily, fully independent rolls)
     ↓            Pulls the cognitropy-library (private factory) and lab (public mirror)
     ↓            Runs cognitropy.py $DATE <morning|evening>  → today's slot assignment
     ↓            Anti-clustering check against the last 10 entries (5 days × 2 slots)
     ↓            Copies the hybrid skeleton, then AUTHORS bespoke content
     ↓             (.claude/commands/ × 5-10, context/concepts/workflows/references, prompts × 3-5)
     ↓            Scans for secrets leakage
     ↓            Commits to library; mirrors to lab
     ↓            Refreshes WORKSPACES.md + BUILDS.md + README badges + cognitropy-history.json
     ↓            Pushes lab; regenerates local dashboard HTML
     ↓            Cleans up the ephemeral deploy-path workspace
  Done.           Two new workspaces in the repo per day (morning + evening).
```

---

## What's a "Workspace"?

Think of it as a ready-to-go AI assistant kit for a specific job. Each workspace is a folder you can point [Claude Code](https://claude.ai/claude-code) (or any compatible AI CLI) at, and it instantly becomes an expert in that domain. It knows what questions to ask, what workflows to follow, and what commands are available.

Every workspace bundles bespoke domain commands (like `/spectrum-sweep` for an SDR workspace or `/torque-split-design` for a hybrid-powertrain workspace — never generic `/analyze` or `/triage`), substantive domain knowledge, methodology, reference tables, and reusable prompt templates. Clone one, launch your AI CLI inside it, and you're working.

Cognitropy workspaces follow a **hybrid** of two upstream Claude Code patterns: the directory shape from [`Claude-Workspace-Foundational-Plugin`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) (flat `context/`, `prompts/`, `outputs/` — no legacy ceremony), plus per-workspace `.claude/commands/` for bespoke depth. The full spec is in [WORKSPACE_SPEC.md](./WORKSPACE_SPEC.md).

```
workspace-name/
├── CLAUDE.md                      # Agent role, available commands, foundational instructions (~25-40 lines)
├── README.md                      # Human-facing showcase: what, why, quick start, refs (~50-100 lines)
├── .claude/
│   └── commands/                  # 4-8 bespoke domain commands (NO required /onboard)
│       └── <name>.md              # Each: brief purpose + Inputs / Steps / Output
├── context/
│   ├── concepts.md                # Domain knowledge — taxonomies, frameworks, failure modes (80-200 lines)
│   ├── workflows.md               # Methodology — step-by-step procedures, decision trees (50-150 lines)
│   └── references.md              # Lookup tables, cheat-sheets, links to upstream catalogues (30-100 lines)
├── prompts/                       # 2-4 bespoke reusable prompt templates
└── outputs/                       # Generated artifacts; .gitkeep at scaffold time
```

Workspaces are self-contained — no plugin install required. If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed globally, additional cross-workspace commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) work alongside the workspace's own. Without it, the bespoke `.claude/commands/` still work.

> **Older workspaces** (project days 1–34, before 2026-05-10) follow a heavier legacy structure (`/onboard` interview command, `context/{project,role,constraints}.md`, `context/for-agent/`, `planning/`, `work-log/`, `user-docs/`, `CREATION_REPORT.md`) inherited from the retired [`Claude-Agent-Workspace-Model`](https://github.com/danielrosehill/Claude-Agent-Workspace-Model) spec. They are kept as historical showcase artifacts — not retroactively migrated.

---

## Quickstart

```bash
# Clone the lab
git clone https://github.com/DaxxSec/cognitropy-lab.git
cd cognitropy-lab

# Pick a workspace — any workspace
cd wireless-protocol-re   # or phishing-kit-analyzer, hybrid-system-energy-management, ...

# Open it as a Claude Code workspace
claude
```

Inside the workspace, the agent will read `CLAUDE.md` automatically and surface the bespoke commands defined in `.claude/commands/`. For `wireless-protocol-re` that means `/spectrum-sweep`, `/decode-signal`, `/protocol-map`, `/compare-known`, `/report-findings`, `/capture-plan`. For `hybrid-system-energy-management` that means `/torque-split-design`, `/posterior-update`, `/ecms-tune`, `/wear-vs-fuel-pareto`, etc. Every workspace publishes its own command set in its `CLAUDE.md` under `## Available Commands` — no two workspaces share a command list, by design.

Each workspace is self-contained. The agent uses the repo as its memory — no cloud dependencies, no accounts to create, no API keys needed.

> **Browse all workspaces by category** → see [`WORKSPACES.md`](./WORKSPACES.md).

---

## Workspace Index

All current workspaces, grouped by category and updated daily by the build pipeline:

**→ See [`WORKSPACES.md`](./WORKSPACES.md) for the full catalog.**

Each entry links to the workspace folder and includes its tagline. The index regenerates as part of every daily build, so it stays in sync with what's actually in the repo.

## Engine Stats

| Metric | Value |
|---|---|
| Cognitropy Domain Pool | **451** |
| Domain Categories | **25** |
| Technique Modifiers | **30** |
| Crossover Sparks | **5** |
| Crossover Probability | **~30%** |
| Build Cadence | **2 / day** (morning 06:05 + evening 18:05) |
| Engine Pool Version | **v2-451d-25c** (since 2026-05-20) |
| **Total Unique Outcomes** | **29,298,030** |

> **The math:** Standard slots = 451 domains × 30 techniques = **13,530** combos. Crossover slots = 195,230 cross-category domain pairs × 30 techniques × 5 sparks = **29,284,500** combos. Total: **29,298,030** unique possible assignments. At **two workspaces per day**, that's **40,134 years** before a repeat is even *possible* — and even then, the agent would build it differently. (Cross-category pairs = 451² − Σdᵢ² = 203,401 − 8,171 = 195,230 — because the engine enforces that crossover domains come from different categories.)
>
> Pre-2026-05-20 the pool was 363 domains × 22 categories at 1 build/day → 18,863,790 outcomes / ~51,646 years. The doubling event (engine v1 → v2) is recorded in `cognitropy-history.json` under `pool_versions[]`; entries with `pool_version: "v1"` were built under the smaller pool and are NOT re-derivable by the current engine without a pool re-pin.

---

## Run Your Own Lab

The cognitropy engine is generic. Fork the repo, swap in your own domain pool, point your own scheduled agent at it.

```bash
# Fork this repo, then edit the domain pool
vim cognitropy.py   # Replace DOMAINS list with your own interests

# Check what your custom pool generates
python3 cognitropy.py 2026-04-01
python3 cognitropy.py 2026-04-02
python3 cognitropy.py 2026-04-03

# Set up a scheduled Claude agent to build workspaces daily
# (see WORKSPACE_SPEC.md for structure conventions)
```

The workspace model works for literally anything. The domains are just the fun part.

---

## About

The Cognitropy Lab is built by [DaxxSec](https://github.com/DaxxSec) & Claude (Anthropic).

Inspired by [Daniel Rosehill's Claude Code Projects Index](https://github.com/danielrosehill/Claude-Code-Projects-Index) and built on a hybrid of the (now-retired) Claude-Agent-Workspace-Model and the [`Claude-Workspace-Foundational-Plugin`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) — see [WORKSPACE_SPEC.md](./WORKSPACE_SPEC.md) for the spec.

The daily build pipeline: **Cognitropy assigns a domain → Claude agent builds the workspace → secrets scan → README stats update → push to GitHub → dashboard regeneration → local cleanup.** Fully autonomous, every morning.

The term "cognitropic" and the underlying hash-based selection pattern were coined here. If you use it elsewhere, we'd love to hear about it.
