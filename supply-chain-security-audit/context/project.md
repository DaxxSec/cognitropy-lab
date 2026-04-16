# Project Context

## Purpose
This workspace provides a structured, repeatable approach to software supply chain security auditing. It serves both point-in-time assessments and ongoing monitoring programs.

## Scope
- Software dependency analysis (direct and transitive)
- Build pipeline integrity assessment
- Vendor/supplier security posture evaluation
- SBOM generation, validation, and drift tracking
- Knowledge base maintenance for organizational learning

## Target Environments
- Web applications (Node.js, Python, Go, Rust, Java, .NET)
- Container images and base image supply chains
- CI/CD platforms (GitHub Actions, GitLab CI, Jenkins, CircleCI)
- Infrastructure-as-code dependencies (Terraform modules, Helm charts)
- Hardware/firmware supply chains (when vendor documentation is available)

## Success Criteria
- Complete dependency inventory with risk scores
- Prioritized finding list using the triage methodology
- Actionable remediation plan with quick wins identified
- Generated SBOM meeting NTIA minimum elements
- Stakeholder-appropriate documentation (technical report + executive summary)
