# Generate Rubric

Create an assessment rubric aligned to specific learning objectives.

## Input
1. The learning objective(s) being assessed
2. Assessment type (essay, presentation, project, lab report, portfolio, discussion, etc.)
3. Rubric type preference: **Analytic** (separate scores per criterion) or **Holistic** (single overall score)

## Process

1. **Extract criteria** from the objective's verb and content
   - The verb indicates the performance expected
   - The content indicates what should be demonstrated
   - Add relevant quality dimensions (accuracy, depth, organization, evidence use)

2. **Define performance levels** (4-point scale default):
   - **4 — Exemplary:** Exceeds expectations, demonstrates mastery
   - **3 — Proficient:** Meets expectations, demonstrates competence
   - **2 — Developing:** Partially meets expectations, shows progress
   - **1 — Beginning:** Does not yet meet expectations, needs support

3. **Write descriptors** for each criterion at each level:
   - Use observable, measurable language
   - Make distinctions clear between adjacent levels
   - Avoid vague qualifiers (good, poor, adequate)
   - Include specific indicators (e.g., "cites 3+ sources" vs. "cites sources")

4. **Add scoring weights** if the user requests them

5. **Review for bias** — Ensure descriptors don't inadvertently disadvantage certain learner populations

## Output
Save rubric to `outputs/rubric-[assessment-name].md`
Format as a markdown table for easy copying into LMS or document tools.
