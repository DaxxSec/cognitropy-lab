# Curriculum Design Peer Review Workspace

A Claude agent workspace for designing, aligning, and iteratively improving educational curricula through structured peer review workflows. Built on evidence-based instructional design principles including backward design, Bloom's Revised Taxonomy, and Webb's Depth of Knowledge.

## Why This Workspace Exists

Curriculum design is often done in isolation — a single instructor or designer drafts objectives, builds assessments, and creates activities without structured feedback loops. Research consistently shows that peer review improves alignment, reduces blind spots, and produces more rigorous learning experiences. This workspace operationalizes that research by embedding peer review directly into the curriculum design workflow.

The agent acts as both a design collaborator and a peer review facilitator, helping educators move from vague goals to measurable, standards-aligned learning objectives with matched assessments and activities.

## Getting Started

1. **Clone this workspace** into your Claude agent environment
2. **Run `/onboard`** to configure your teaching context, subject area, learner demographics, and institutional standards
3. **Start designing** with `/design-unit` or bring existing curriculum materials for review with `/peer-review`

### Prerequisites

- A clear sense of your subject area and learner audience
- Any institutional standards or frameworks you need to align with (Common Core, NGSS, ISTE, AP, IB, etc.)
- Existing curriculum documents (optional — you can start from scratch)

## Command Reference

| Command | Purpose | Input | Output |
|---------|---------|-------|--------|
| `/onboard` | Initialize workspace context | Interactive interview | Populated context files |
| `/design-unit` | Create a new curriculum unit | Topic, duration, learner level | Unit plan with objectives, assessments, activities |
| `/peer-review` | Run peer review on materials | Curriculum document or unit plan | Structured feedback with revision recommendations |
| `/align-standards` | Map objectives to frameworks | Learning objectives list | Standards alignment matrix |
| `/rubric-gen` | Generate assessment rubrics | Learning objectives + assessment type | Analytic or holistic rubric |

## Directory Structure

```
curriculum-design-peer-review/
├── CLAUDE.md                    # Agent identity and command index
├── README.md                    # This file
├── CREATION_REPORT.md           # Build rationale and domain notes
├── context/
│   ├── project.md               # Course/program details (via /onboard)
│   ├── role.md                  # Your role and institution (via /onboard)
│   ├── constraints.md           # Design boundaries and preferences
│   └── for-agent/
│       ├── domain-knowledge.md  # Instructional design frameworks
│       ├── workflows.md         # Peer review and design workflows
│       ├── environment.md       # Toolchain and platform details
│       └── tools.md             # Recommended integrations
├── .claude/commands/            # Slash commands
│   ├── onboard.md
│   ├── design-unit.md
│   ├── peer-review.md
│   ├── align-standards.md
│   └── rubric-gen.md
├── prompts/                     # Reusable prompt templates
│   ├── bloom-objective-writer.md
│   ├── constructive-feedback.md
│   └── backward-design-planner.md
├── resources/
│   ├── blooms-taxonomy-verbs.md
│   ├── webbs-dok-guide.md
│   └── peer-review-checklist.md
├── planning/                    # Active design plans
├── outputs/                     # Generated curriculum artifacts
├── user-docs/                   # Reference documentation
├── work-log/                    # Session tracking
└── .gitkeep files               # Preserve empty directories
```

## Core Design Frameworks

### Backward Design (Wiggins & McTighe)
The workspace follows the Understanding by Design (UbD) framework:
1. **Identify desired results** — What should learners know and be able to do?
2. **Determine acceptable evidence** — How will we know they learned it?
3. **Plan learning experiences** — What activities will get them there?

### Bloom's Revised Taxonomy
All learning objectives are drafted using measurable verbs from Bloom's cognitive process dimensions: Remember, Understand, Apply, Analyze, Evaluate, Create.

### Peer Review Workflow
The structured peer review process follows four phases:
1. **Submission** — Designer submits unit plan or objectives
2. **Criteria-based review** — Reviewer evaluates against alignment checklist
3. **Feedback synthesis** — Actionable recommendations with evidence
4. **Revision cycle** — Designer iterates based on feedback

## Example Use Cases

- **K-12 teacher** building a new unit on climate science aligned to NGSS
- **University instructor** redesigning a course for active learning
- **Corporate L&D designer** creating competency-based training modules
- **Curriculum committee** reviewing and standardizing department-wide objectives
- **Instructional designer** ensuring QM (Quality Matters) rubric compliance for online courses

## Recommended MCP Servers / Tools

- **Filesystem MCP** — Read/write curriculum documents locally
- **Google Docs MCP** — Collaborate on shared curriculum drafts
- **Notion MCP** — Track curriculum mapping in database views
- **Git MCP** — Version control curriculum iterations

## Ethical Considerations

- Learning objectives should be inclusive and avoid cultural bias
- Peer review must be constructive, never punitive
- Assessment design should accommodate diverse learner needs (UDL principles)
- AI-assisted curriculum design should be transparent to stakeholders
- This workspace supports human designers — it does not replace professional judgment

## License

This workspace template is open source. Curriculum content you create with it belongs to you.
