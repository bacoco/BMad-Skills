# Workflow — Observability Readiness

1. **Discovery & Scope**
   - Understand business-critical journeys and SLAs.
   - Review existing monitoring stack and ownership.
   - Document pain points (missing data, noisy alerts, manual debugging).

2. **Current State Assessment**
   - Audit logging levels, formats, and retention.
   - Map available metrics to golden signals (latency, traffic, errors, saturation).
   - Inspect tracing coverage across services and queues.
   - Evaluate dashboard usefulness and incident response maturity.

3. **Design Future State**
   - Define instrumentation requirements for metrics, logs, events, and traces.
   - Establish data governance: retention, PII handling, compliance constraints.
   - Propose toolchain updates or integrations (OpenTelemetry, Grafana, Datadog, Honeycomb, etc.).

4. **SLO & Alert Framework**
   - Collaborate with stakeholders to define SLIs/SLOs per journey.
   - Draft alert policies, routing, escalation, and maintenance windows.
   - Outline runbook expectations and training needs.

5. **Backlog & Rollout Plan**
   - Convert instrumentation work into prioritized stories.
   - Sequence milestones (foundational metrics → tracing → dashboards → alert tuning).
   - Identify dependencies on infrastructure or platform teams.

6. **Handover & Validation**
   - Deliver observability plan, backlog, and dashboard specs.
   - Coordinate with `bmad-performance-optimization` and `bmad-security-review` for shared telemetry needs.
   - Recommend follow-up reviews post-implementation to validate signal quality.

## Resources
- Templates in `assets/` for observability plans, dashboards, and backlog exports.
- `REFERENCE.md` contains metric taxonomies and logging/tracing standards.
