# Expo App Debugger Workspace

A Claude agent workspace purpose-built for debugging React Native apps built with the Expo framework and Railway backends. Designed to take you from cryptic error message to working fix with minimal frustration.

## What This Workspace Does

This workspace turns Claude into a dedicated debugging partner for your Expo app. Instead of copy-pasting errors into generic chat sessions, you get structured triage, root cause analysis, and tested fix patterns specific to the React Native / Expo / Railway stack.

**The agent can help you:**

- Triage any error, crash, or unexpected behavior and rate its severity
- Walk through interactive debugging sessions step-by-step
- Generate complete, copy-paste-ready fixes with verification steps
- Audit your dependencies for version conflicts and known issues
- Debug Railway backend problems (deployment failures, API issues, env vars)
- Analyze crash reports and stack traces end-to-end
- Run health checks across common issue categories before you ship

## Getting Started

### 1. Clone and Open

```bash
git clone <this-repo>
cd expo-debugger-workspace
```

Open this folder in Claude Code (or your Claude-enabled editor).

### 2. Run Onboarding

```
/onboard
```

The agent will ask you about your app, your environment, and your tech stack so it can give you targeted help from the start.

### 3. Start Debugging

The fastest path from error to fix:

```
/triage
```

Paste your error. The agent will classify it, explain the root cause, and tell you how urgent it is. Then:

```
/fix
```

Get the actual code changes you need to make.

## Command Reference

| Command | When to Use |
|---------|-------------|
| `/onboard` | First time setup — tell the agent about your app |
| `/triage` | You have an error and need to understand what's going on |
| `/debug` | You need a full interactive debugging session |
| `/fix` | You know the bug — you want the code fix |
| `/health-check` | Pre-flight check before a build or TestFlight push |
| `/railroad` | Something is wrong on the Railway backend side |
| `/crash-report` | You have a crash log or stack trace to analyze |
| `/deps` | Check for dependency version conflicts or known issues |

## Directory Structure

```
expo-debugger-workspace/
├── CLAUDE.md              # Agent identity and command reference
├── README.md              # This file
├── context/
│   ├── project.md         # Your app details (populated by /onboard)
│   ├── role.md            # Your experience level and preferences
│   ├── constraints.md     # What the agent should/shouldn't do
│   └── for-agent/
│       ├── environment.md # Your dev environment specifics
│       └── workflows.md   # Detailed debugging methodologies
├── .claude/commands/       # All slash commands
├── work-log/              # Session-by-session debugging history
├── planning/              # Active debugging plans
├── user-docs/             # Guides the agent writes for you
├── prompts/               # Reusable prompt templates
├── resources/             # Error references, checklists, guides
└── outputs/               # Generated fixes, reports, patches
```

## Recommended MCP Servers

For the best experience, consider connecting:

- **filesystem** — Let the agent read your actual project files
- **github** — Pull issues, PRs, and code context directly
- **fetch** — Check Expo/React Native docs and Railway status in real-time

## Tips

- **Be specific with errors**: Paste the full stack trace, not just the error message. Include the command you ran and what you expected to happen.
- **Use `/triage` before `/fix`**: Understanding the root cause first prevents whack-a-mole debugging.
- **Check `/deps` regularly**: Half of React Native bugs are dependency version mismatches.
- **Review `work-log/`**: The agent tracks every session. If a bug comes back, the history is there.

## Tech Stack This Workspace Covers

- React Native (Expo managed workflow)
- Expo SDK, EAS Build, EAS Submit
- Railway (backend hosting, PostgreSQL, Redis)
- TypeScript / JavaScript
- Common libraries: React Navigation, Expo Router, AsyncStorage, Axios/Fetch, etc.
