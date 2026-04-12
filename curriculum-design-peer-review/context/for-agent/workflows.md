# Workflows

## Workflow 1: Curriculum Unit Design (Backward Design)

### Input
- Subject area, topic, duration, learner level
- Applicable standards framework

### Steps
1. **Identify Desired Results**
   - Draft 3-5 enduring understandings (big ideas)
   - Write 2-3 essential questions
   - List specific knowledge and skills
   - Map to standards using `/align-standards`

2. **Draft Learning Objectives**
   - Write objectives using Bloom's Revised Taxonomy verbs
   - Ensure each objective is: measurable, specific, achievable, relevant
   - Format: "Students will be able to [verb] [object] [context/condition]"
   - Cross-reference DOK levels for cognitive complexity

3. **Design Assessment Evidence**
   - Create at least one performance task (authentic assessment)
   - Design formative checks for each objective
   - Ensure assessment-objective alignment (every objective is assessed)
   - Generate rubric using `/rubric-gen`

4. **Plan Learning Activities**
   - Sequence activities using WHERE TO framework
   - Include varied modalities (UDL compliance)
   - Build scaffolding from lower to higher Bloom's levels
   - Estimate time allocations

5. **Self-Review**
   - Run `/peer-review` on the completed unit
   - Address critical feedback items
   - Document iterations in `work-log/`

### Output
- Complete unit plan in `outputs/unit-[name]-v[N].md`
- Standards alignment matrix
- Assessment rubric(s)

## Workflow 2: Peer Review Cycle

### Input
- Curriculum document (unit plan, syllabus, objectives list, or assessment)

### Steps
1. **Submission Intake**
   - Identify document type and scope
   - Load applicable review criteria from `resources/peer-review-checklist.md`

2. **Alignment Analysis**
   - Check objective-assessment alignment
   - Check objective-activity alignment
   - Verify standards mapping completeness
   - Flag any unmeasurable objectives (vague verbs like "understand," "know," "learn")

3. **Rigor Analysis**
   - Map each objective to Bloom's level
   - Check DOK distribution (are objectives stuck at Level 1?)
   - Evaluate cognitive complexity progression across the unit

4. **Inclusivity Review**
   - Check for UDL compliance (multiple means of engagement, representation, expression)
   - Flag potential cultural bias in examples, contexts, or assessment scenarios
   - Verify accessibility of materials and activities

5. **Feedback Synthesis**
   - Organize findings by priority: Critical → Important → Nice-to-have
   - For each finding: state the issue, cite the framework, suggest a revision
   - Acknowledge specific strengths

6. **Revision Recommendations**
   - Provide rewritten objectives where needed
   - Suggest alternative assessments or activities
   - Offer before/after comparisons

### Output
- Review report in `outputs/review-[document-name]-[date].md`
- Revised objectives (if applicable)

## Workflow 3: Standards Alignment Mapping

### Input
- List of learning objectives
- Target standards framework(s)

### Steps
1. Identify the standards framework and retrieve relevant standards
2. Map each objective to one or more standards
3. Identify gaps (standards not addressed by any objective)
4. Identify orphans (objectives not tied to any standard)
5. Produce alignment matrix (table format)

### Output
- Alignment matrix in `outputs/alignment-[subject]-[framework].md`

## Workflow 4: Rubric Generation

### Input
- Learning objective(s)
- Assessment type (essay, presentation, project, lab report, etc.)

### Steps
1. Identify assessment criteria from the objective's verb and content
2. Define performance levels (4-point scale: Exemplary, Proficient, Developing, Beginning)
3. Write descriptors for each criterion at each level
4. Ensure descriptors are observable and measurable
5. Add scoring weights if requested

### Output
- Rubric in `outputs/rubric-[assessment-name].md`
