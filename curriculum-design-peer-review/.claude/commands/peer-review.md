# Peer Review

Run a structured peer review cycle on curriculum materials.

## Input
Ask the user to provide or point to the curriculum document to review. This can be:
- A unit plan (from `/design-unit` or external)
- A set of learning objectives
- A syllabus or course outline
- An assessment or rubric

## Review Protocol

### Phase 1: Alignment Check
- [ ] Every learning objective uses a measurable Bloom's verb
- [ ] Every objective is assessed by at least one assessment item
- [ ] Every activity supports at least one objective
- [ ] Objectives map to stated standards (if applicable)
- Flag any orphaned objectives, assessments, or activities

### Phase 2: Rigor Analysis
- Map each objective to its Bloom's level (Remember through Create)
- Map each objective to Webb's DOK level (1-4)
- Check: Is there cognitive complexity progression across the unit?
- Check: Are higher-order objectives adequately supported by scaffolding?
- Flag: Objectives clustered at DOK 1-2 with no higher-order thinking

### Phase 3: Clarity & Measurability
- Flag vague verbs: understand, know, learn, appreciate, be aware of
- Check: Can each objective be observed and measured?
- Check: Are conditions and criteria specified where needed?
- Provide rewritten alternatives for any flagged objectives

### Phase 4: Inclusivity & Accessibility
- Check for UDL compliance across engagement, representation, action/expression
- Flag examples or scenarios that may carry cultural bias
- Verify multiple assessment pathways exist
- Check that materials are accessible (alt text, transcripts, flexible formats)

### Phase 5: Feedback Synthesis
Organize all findings into three tiers:
1. **Critical** — Alignment gaps, unmeasurable objectives, missing assessments
2. **Important** — Rigor concerns, inclusivity gaps, structural issues
3. **Suggested** — Polish items, additional resources, enhancement ideas

For each finding, provide:
- The issue (specific and quoted)
- The framework/principle it violates
- A concrete revision suggestion with before/after comparison

## Output
Save review report to `outputs/review-[document-name]-[date].md`
