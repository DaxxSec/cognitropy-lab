# Getting Started

## Prerequisites
- Claude Code or compatible Claude agent environment
- Dam information (type, height, hazard classification, jurisdiction)
- Instrumentation data in CSV format (for anomaly detection features)

## Quick Start

### 1. Orient the Agent
Run `/onboard` to initialize the agent and provide your dam's basic information. The agent will configure itself for your dam type and regulatory context.

### 2. Generate an Inspection Checklist
Run `/inspect` and provide your dam profile. You'll receive a comprehensive, dam-type-specific inspection checklist suitable for field use.

### 3. Analyze Instrumentation Data
Run `/analyze-readings` and provide your instrumentation data (CSV with timestamp, instrument_id, reading columns). The agent will perform automated anomaly detection and produce a severity-ranked findings report.

### 4. Review Your EAP
Run `/eap-review` and provide your Emergency Action Plan. The agent will check it against FEMA 64 requirements and identify gaps.

### 5. Generate Reports
Use the prompts in `prompts/` to produce condition assessment reports, anomaly analysis reports, or failure mode screening documents.

## Data Format Tips
- CSV headers should include: timestamp, instrument_id, reading, unit
- Include reservoir_elevation if available (significantly improves anomaly detection accuracy)
- Monthly or more frequent data works best; quarterly data will limit trend detection capability
- Include at least 2 years of historical data for reliable baseline statistics

## Important Notes
- This workspace assists analysis; it does not replace licensed Professional Engineer judgment
- Always review agent recommendations with qualified dam safety personnel
- When the agent flags a finding, treat it as warranting investigation until a qualified engineer determines otherwise
