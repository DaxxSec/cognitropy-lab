# Prompt: Predictive-Maintenance Overdue Brief

Scan `resources/pm-schedule-template.md` and any maintenance logs. Produce:

1. Overdue items (past target cadence) with days overdue
2. At-risk items (within 2 days of cadence expiry)
3. Pre-storm readiness gap - given the 72 h weather outlook, which items MUST be current before storm onset that are not
4. Proposed schedule window for each overdue item given access feasibility

Order by operational criticality.
