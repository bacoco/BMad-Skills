# Reference — Performance Optimization

## Key Metrics
- **Backend:** P50/P95/P99 latency, error rate, throughput, CPU load, memory usage, queue depth.
- **Frontend:** Largest Contentful Paint, First Input Delay, CLS, TTI, bundle size, hydration time.
- **Data:** Query latency, lock contention, cache hit rate, replication lag.
- **Infrastructure:** Autoscaling events, network latency, disk IOPS, container restarts.

## Useful Tools
- **Load Testing:** k6, Locust, JMeter, Artillery, Vegeta.
- **Profiling:** Pyinstrument, Py-spy, perf, go tool pprof, flamebearer, Chrome DevTools, Lighthouse.
- **Monitoring:** Prometheus + Grafana, Datadog, New Relic, Elastic APM, OpenTelemetry.
- **Database:** EXPLAIN/ANALYZE, pg_stat_statements, MySQL performance schema, Redis MONITOR.

## Diagnostic Prompts
- "Which endpoint or component is violating the SLA?"
- "How does performance change with concurrent users or data volume?"
- "What changed recently (deployments, migrations, configuration updates)?"
- "Is the bottleneck CPU, I/O, or network bound?"
- "What instrumentation exists to validate improvements?"

## Optimization Patterns
- **Backend:** Connection pooling, asynchronous processing, caching, batching, query tuning, pagination.
- **Frontend:** Code splitting, prefetching, critical CSS, memoization, virtualization, image optimization.
- **Data:** Indexing, read replicas, partitioning, caching layers, denormalization with verification.
- **Infrastructure:** Autoscaling policies, CDN utilization, edge caching, container sizing, circuit breakers.

## Anti-Patterns
- Optimizing without baseline metrics.
- Blindly increasing infrastructure size without addressing code bottlenecks.
- Running load tests against production without safety measures.
- Ignoring cost implications of scaling decisions.
- Deploying optimizations without regression monitoring.
