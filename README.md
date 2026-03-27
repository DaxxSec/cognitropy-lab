# The Cognitropy Lab

**An AI agent builds one new workspace every day, on a topic it never gets to choose.**

Every morning, a Claude agent wakes up and gets assigned a random domain — maybe *limnology* (freshwater lake science), maybe *coopering* (barrel-making), maybe *Mars terrain analysis crossed with EVA procedure planning*. It doesn't get to pick. It has to build a full, professional-grade agent workspace for whatever it's handed, then push it here.

This repo is the result. It grows by one workspace daily, completely autonomously. No human in the loop. Just an AI, an entropy engine, and an ever-expanding collection of workspaces for domains you didn't know you needed.

---

## What's a "Workspace"?

Think of it as a ready-to-go AI assistant kit for a specific job. Each workspace is a folder you can point [Claude Code](https://claude.ai/claude-code) (or any compatible AI CLI) at, and it instantly becomes an expert in that domain. It knows what questions to ask, what workflows to follow, and what commands are available.

Every workspace includes agent instructions, slash commands you can run (like `/triage` or `/analyze`), reference materials, prompt templates, and structured workflows. Clone one, run `/onboard`, and you're working.

They all follow the [Agent Workspace Model](https://github.com/danielrosehill/Claude-Agent-Workspace-Model) by Daniel Rosehill.

---

## How the Daily Build Works

```
  6:00 AM    Cognitropy engine seeds today's domain from the date
     ↓
  9:04 AM    Scheduled Claude agent wakes up
     ↓       Clones this repo
     ↓       Runs cognitropy.py → gets today's assignment
     ↓       Builds the full workspace (CLAUDE.md, commands, workflows, resources...)
     ↓       Scans for secrets leakage
     ↓       Updates this README index
     ↓       Commits and pushes
     ↓       Cleans up local files
  Done.      One new workspace in the repo. Every day.
```

---

## The Cognitropy Engine

Here's where it gets fun.

AI has an entropy problem. Ask it to "pick something creative" a hundred times and you'll get the same handful of safe, predictable ideas. It's the creative equivalent of a random number generator with a bad seed — low entropy, repetitive output.

**Cognitropy** (a portmanteau of "cognition" and "entropy") is our solution. It's a self-contained Python engine ([`cognitropy.py`](./cognitropy.py)) that uses the current date as a cryptographic seed to deterministically select from a pool of **200+ wildly diverse domains** — everything from volcanology to watchmaking to competitive barbecue judging.

The agent doesn't get to choose. It gets *assigned*. And it has to make it work.

**How it works:**

- `sha256(today's date)` → index into a pool of 200+ domains
- A technique modifier is selected (e.g., "with decision tree triage workflows" or "using Bayesian probability assessment")
- ~30% of days are **Crossover Days** where two unrelated domains get fused together (e.g., "cave diving × hazmat transportation" or "Mars terrain analysis × EVA procedure planning")
- The output is a plain-text assignment — the agent builds the workspace around it

**Try it yourself:**

```bash
python3 cognitropy.py              # Today's assignment
python3 cognitropy.py 2026-04-05   # Check any date
```

**Sample 30-day schedule (the agent has no say in this):**

| Date | Domain | Type |
|---|---|---|
| Mar 27 | Limnology | Standard |
| Mar 28 | Aquaponics | Standard |
| Mar 30 | Engraving | Standard |
| Mar 31 | Heraldry | Standard |
| Apr 05 | Hazmat Transportation × Cave Diving | Crossover |
| Apr 09 | Coopering × Storm Chasing | Crossover |
| Apr 11 | Mars Terrain Analysis × EVA Procedure Planning | Crossover |
| Apr 22 | Roller Coaster Design | Standard |
| Apr 24 | Mushroom Foraging | Standard |

The diversity is the point. A workspace for mushroom foraging uses the same structured methodology as one for malware analysis — triage, evidence collection, documentation, reporting. The patterns transfer. The domains are just the fun part.

---

## Workspace Index

### Cybersecurity & DFIR

| Workspace | Description |
|---|---|
| [Firmware RE Workspace](./firmware-re-workspace) | Firmware reverse engineering assistant — extract, disassemble, analyze, and document embedded firmware images to uncover architecture, attack surface, vulnerabilities, and hardcoded secrets. |
| [Phishing Kit Analyzer](./phishing-kit-analyzer) | Phishing kit analysis specialist — dissect, reverse-engineer, and extract intelligence from phishing kits deployed on compromised infrastructure. |

### Automotive & Engine Tuning

| Workspace | Description |
|---|---|
| [ECU Tune & Engine Build](./ecu-tune-engine-build-workspace) | Performance tuning and engine build assistant — ECU calibration, datalog analysis, engine modification planning, and build documentation. |

### Development & Debugging

| Workspace | Description |
|---|---|
| [Expo Debugger](./expo-debugger-workspace) | Senior React Native / Expo debugging specialist — systematic triage, diagnosis, and fix for Expo-managed apps with Railway backends. |

---

## Using a Workspace

1. **Clone this repo** (or just the workspace folder you want)
2. **Point Claude Code at it:** `cd workspace-name && claude`
3. **Run `/onboard`** — the agent interviews you to customize the workspace for your specific situation
4. **Start working** — use the slash commands, ask questions, let the agent guide you

Each workspace is self-contained. The agent uses the repo as its memory — no cloud dependencies, no accounts to create, no API keys needed.

---

## Workspace Structure

Every workspace follows the same proven pattern:

| Component | What It Does |
|---|---|
| `CLAUDE.md` | Agent's brain — role, instructions, command list (kept lightweight) |
| `context/` | Your project details, role, constraints (populated by `/onboard`) |
| `context/for-agent/` | Deep workflows and environment config the agent reads on demand |
| `.claude/commands/` | Slash commands — repeatable, domain-specific workflows |
| `resources/` | Reference materials, cheat sheets, checklists |
| `prompts/` | Reusable prompt templates for common tasks |
| `work-log/` | Session history — the agent logs what it did and found |
| `outputs/` | Generated reports, analysis results, exports |

---

## Stats

- **Total Workspaces:** 4
- **Categories:** 3
- **Cognitropy Domain Pool:** 200+
- **Last Updated:** 2026-03-26
- **Build Streak:** Day 1

---

## About

The Cognitropy Lab is built by [DaxxSec](https://github.com/DaxxSec). Inspired by [Daniel Rosehill's Claude Code Projects Index](https://github.com/danielrosehill/Claude-Code-Projects-Index) and the [Agent Workspace Model](https://github.com/danielrosehill/Claude-Agent-Workspace-Model).

The daily build pipeline: **Cognitropy assigns a domain → Claude agent builds the workspace → secrets scan → index update → push to GitHub → local cleanup.** Fully autonomous, every morning.

Want to run your own lab? The cognitropy engine is generic — fork the repo, swap in your own domain pool, point your own scheduled agent at it. The workspace model works for literally anything.
