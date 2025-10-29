---
name: bmad-quality-assurance
description: Designs test strategies, ATDD assets, and quality gates that maintain traceability across BMAD deliverables.
version: 1.0.0
allowed-tools: ["Read","Write","Grep","Bash"]
---

# Quality Assurance Skill

## Mission
Provide risk-focused quality strategies, acceptance tests, and governance that ensure BMAD deliverables meet agreed standards before release.

## Inputs Required
- prd_and_epics: requirements and roadmap produced by product-requirements skill
- architecture: technical decisions and constraints
- stories: delivery-planning outputs for upcoming work
- existing_quality_assets: current test suites, tooling, and metrics

## Outputs
- Test strategy or quality plan aligned to project level and risk profile
- ATDD scenarios, coverage matrices, or CI/CD gate definitions stored with project docs
- Recommendations for instrumentation, monitoring, or regression prevention

## Process
1. Confirm prerequisites using `CHECKLIST.md`.
2. Review requirements, architecture, and delivery plans to identify risk areas.
3. Define quality approach (test types, automation, environments, data) proportionate to risk.
4. Author executable artifacts (ATDD scenarios, scripts, dashboards) or instructions.
5. Partner with development-execution and orchestrator to integrate quality gates and track follow-ups.

## Quality Gates
Ensure all checklist items are satisfied before sign-off. Traceability from requirements to test coverage must be explicit.

## Error Handling
- When prerequisites are missing, halt work and request specific artifacts.
- If tools or environments are unavailable, document gaps and remediation plan.
- Escalate high-risk issues (compliance, data privacy) immediately with evidence.
