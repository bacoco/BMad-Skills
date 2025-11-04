# Reference — Observability Readiness

## Metric Taxonomy
- **Golden Signals:** Latency, Traffic, Errors, Saturation.
- **Reliability Metrics:** Uptime, mean time to detect, mean time to recover.
- **Business KPIs:** Conversion rate, checkout success, revenue per minute, active sessions.
- **Resource Metrics:** CPU, memory, disk, network, queue depth, thread pools.

## Logging Standards
- Use structured formats (JSON) with consistent keys (timestamp, level, service, request_id).
- Redact or hash PII/PCI data at the source.
- Include correlation identifiers to link logs with traces.
- Define retention/rotation policy aligned with compliance.

## Tracing Practices
- Adopt OpenTelemetry instrumentation libraries where available.
- Ensure span naming follows `{service}.{operation}` convention.
- Capture key attributes: user_id, order_id, region, experiment flag.
- Limit span cardinality to avoid storage explosions.

## Alerting Principles
- Tie alerts to SLO burn rates or symptom-based triggers.
- Provide actionable context: hypothesis, impacted customers, suggested runbook.
- Avoid duplicate alerts by using grouping, suppression, and maintenance windows.
- Route to owners with clear escalation chain.

## Tooling Resources
- OpenTelemetry Collector deployment templates.
- Grafana dashboard starter packs (Golden Signals, Infrastructure, Business KPIs).
- Alertmanager configuration examples with routing and silencing rules.
- Runbook template stored in `assets/runbook-template.md.template`.
