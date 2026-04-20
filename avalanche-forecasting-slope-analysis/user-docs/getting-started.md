# Getting Started (User-Facing)

## First Run

1. `git clone https://github.com/DaxxSec/cognitropy-lab.git`
2. `cd cognitropy-lab/avalanche-forecasting-slope-analysis`
3. `claude`
4. In the session: `/onboard`

The agent will walk you through zone, role, data sources, and reporting cadence.

## Daily Workflow

1. Start the day with `/daily-forecast`. Paste in overnight telemetry and the last 24 h observations.
2. As snowpits come in, run `/snowpack-analysis` on each.
3. Before sending guides or patrollers into a specific zone, run `/slope-check`.
4. Weekly: run `/mitigation-plan` to refresh the PM schedule.
5. After any incident: `/incident-review` in peer-review mode.

## What the Agent Will NOT Do

- Publish a bulletin directly.
- Issue a fire order for explosives.
- Use the word "safe."
- Auto-retire a PWL.
- Absolve you of the call.

## Troubleshooting

- If a slash command fails, check that `/onboard` has been run and the context files are populated.
- If bulletin drafts feel generic, enrich `context/for-agent/environment.md` with your specific station + observation ecosystem.
