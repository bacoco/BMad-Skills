# Workflow — Performance Optimization

1. **Clarify Goals**
   - Capture target metrics (TTFB, P95 latency, RPS/QPS, FPS, memory budgets).
   - Align on environments to test (staging vs. prod) and acceptable risk envelope.

2. **Collect Evidence**
   - Pull metrics from APM dashboards, tracing tools, and infrastructure monitors.
   - Gather profiling outputs (CPU flamegraphs, heap snapshots, query plans).
   - Note recent releases, infra changes, or incidents affecting performance.

3. **Diagnose Hotspots**
   - Map call chains and resource usage to identify slowest components.
   - Evaluate caching strategy, database indexes, queue backlogs, client bundle weight.
   - Quantify impact of each issue to focus on high-leverage fixes.

4. **Design Benchmark Plan**
   - Choose tooling (k6, JMeter, Locust, Artillery, Lighthouse, WebPageTest, Playwright).
   - Define workloads for baseline, stress, spike, soak, and failover scenarios.
   - Specify metrics to capture, acceptable thresholds, and rollback triggers.

5. **Plan Optimizations**
   - Recommend code, configuration, and infrastructure changes.
   - Highlight prerequisites (e.g., schema migrations, feature flags, CDN updates).
   - Sequence work into short-, medium-, and long-term initiatives.

6. **Communicate & Integrate**
   - Deliver performance brief and backlog.
   - Sync with `bmad-story-planning` for story creation and `bmad-test-strategy` for regression coverage.
   - Define follow-up validation cadence post-implementation.

## Tooling Shortcuts
- Profilers: `pyinstrument`, `perf`, `clinic.js`, Chrome DevTools, `go tool pprof`.
- Load testing: k6 scripts, Locust tasks, JMeter test plans stored in `assets/`.
- Frontend metrics: Lighthouse CI, Web Vitals, bundle analyzer templates.
