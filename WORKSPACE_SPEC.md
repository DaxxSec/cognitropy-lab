# Claude Agent Workspace — Canonical Structure Reference

> Source: github.com/danielrosehill/Claude-Agent-Workspace-Model
> Example implementation: github.com/DaxxSec/COSINT

## Core Development Stages

1. **SCAFFOLD** — User clones a designated workspace template
2. **PERSONALIZE** — Context is ingested via agent-led interview or manual input (`/onboard`)
3. **SUCCESS** — Repository is fully configured and ready for use

## Required Directory Structure

```
workspace-name/
├── CLAUDE.md                    # Lightweight: role, stubs, commands only
├── README.md                    # Human documentation
├── context/
│   ├── project.md               # Project definition (populated by /onboard)
│   ├── role.md                  # User's role (populated by /onboard)
│   ├── constraints.md           # Boundaries and preferences (populated by /onboard)
│   └── for-agent/               # Detailed agent instructions (read on demand)
│       ├── environment.md       # User environment details
│       └── workflows.md         # Domain-specific workflows
├── work-log/                    # Agent's daily operation tracking
│   └── .gitkeep
├── planning/                    # Active plan and pivot history
│   └── .gitkeep
├── user-docs/                   # Agent-written reference docs for the user
│   └── .gitkeep
├── .claude/
│   └── commands/                # Slash commands
│       ├── onboard.md           # REQUIRED: workspace initialization
│       └── [domain-commands].md # Domain-specific commands
├── prompts/                     # Reusable prompt templates
├── resources/                   # Reference materials, checklists, schemas
├── outputs/                     # Generated artifacts
│   └── .gitkeep
└── .mcp.json                    # Optional: MCP server configs
```

## File Guidelines

### CLAUDE.md (lightweight, ~30-50 lines)
Because CLAUDE.md is loaded with every prompt, it must stay lightweight:
- Workspace identity and template name
- Agent role (one sentence)
- Context references (stubs pointing to context/for-agent/)
- List of available slash commands with one-line descriptions
- Foundational instruction: "Use this repository as your primary memory"

### README.md (comprehensive, 100+ lines)
- What the workspace is and why it exists
- Getting started instructions
- Full command reference table
- Directory structure explanation
- Example use cases
- Recommended MCP servers or tools
- Ethical/legal considerations if applicable

### .claude/commands/onboard.md (REQUIRED)
- Gathers user context through interview-style flow
- Populates context/project.md, context/role.md, context/constraints.md
- Saves environment details to context/for-agent/environment.md

### Domain-specific commands (4-8 per workspace)
- Each command is a markdown file in .claude/commands/
- Define a clear, repeatable workflow
- Include expected inputs, steps, and output format

### context/for-agent/workflows.md
- Detailed step-by-step workflows for the agent's domain
- Decision trees, analysis frameworks, methodology

### resources/
- Checklists, schemas, reference data, templates
- At least 2-3 useful reference files

### prompts/
- Reusable prompt templates for common tasks
- At least 3 templates

## Key Principles

1. **CLAUDE.md = lightweight stubs** → context/for-agent/ = substance
2. **The repo IS the memory** — no reliance on built-in memory features
3. **/onboard is always required** — drives the Personalize stage
4. **Slash commands define workflows** — repeatable, domain-specific
5. **work-log/ tracks operations** — dated markdown files per session
6. **planning/ has exactly one plan.md** — pivots recorded in pivots/ subdirectory
7. **user-docs/ are deliverables** — polished, user-facing reference documents

## COSINT Example Features (for inspiration)

The COSINT workspace demonstrates excellence with:
- Specialized agents (evidence-processor, entity-profiler, correlation-analyst, etc.)
- Graph data system (Maltego-style entities/relationships in JSON)
- SpiderFoot integration for automated OSINT
- Evidence management with chain of custody and SHA-256 verification
- Import/migration commands for existing case files
- Recommended MCP servers for the domain
- Ethical use guidelines
