---
id: SWD-DBG-BEG-003
title: Error Monitoring and Observability Foundations
module: Debugging Basics
track: Foundations
level: Beginner
duration: 20m
author: UltraCube Software Engineering Team
last_updated: 2025-09-02
prerequisites:
  - lesson-01-introduction-to-debugging.md
  - lesson-02-debugging-tools-and-techniques.md
learning_objectives:
  - Distinguish logging, metrics, tracing, and profiling
  - Interpret basic time-series metrics (latency, error rate, saturation)
  - Configure alert thresholds using SLO + error budget concepts
  - Use trace spans to follow a user request across services
  - Establish minimal observability checklist for new features
---

## Error Monitoring and Observability Foundations

> Bridging runtime feedback signals to actionable insights.

## 1. Core Pillars and Their Questions

| Signal | Core Question | Example Tools |
|--------|---------------|---------------|
| Logs | What happened? | Loki, ELK, CloudWatch |
| Metrics | How is it trending quantitatively? | Prometheus, Datadog, New Relic |
| Traces | Where is time spent across components? | Jaeger, Zipkin, Tempo |
| Profiles | What code paths consume resources? | eBPF tools, PySpy, JFR |

## 2. Golden Signals (Baseline)

- Latency (response time distribution, not just averages)
- Traffic (RPS/QPS, concurrent sessions)
- Errors (rate & classification)
- Saturation (resource utilization: CPU, memory, queue depth)

Augment with: Availability, Cost per transaction, Tail latency (p95/p99), Retry storm indicators.

## 3. Instrumentation Minimal Viable Set

| Layer | Must Have | Rationale |
|-------|-----------|-----------|
| HTTP/API | Request/response timing, status code, route | User experience + error patterns |
| DB | Query duration & errors | Bottleneck & slow queries |
| Cache | Hit/miss rate | Capacity planning |
| Queue | Lag/backlog size | Throughput health |
| Feature Flag | Flag state in events | Debugging config-induced behavior |

## 4. Error Monitoring Workflow

1. Alert fires (threshold breach or anomaly)
2. Triage: confirm signal validity (noise vs real)
3. Correlate: related recent deploys, incidents, config changes
4. Scope: impacted endpoints / users / regions
5. Drill: trace slow span or error stack
6. Mitigate: rollback, circuit-break, feature flag off
7. Learn: create post-incident summary & preventative task

## 5. SLOs and Error Budgets (Intro)

- Service Level Indicator (SLI): Quantitative measure (e.g., successful request ratio)
- Service Level Objective (SLO): Target (e.g., 99.5% success over 30 days)
- Error Budget: 1 - SLO (allowed failure window)
- Policy: If burn rate > threshold, freeze deploys and prioritize resilience

Basic burn rate heuristic: (Errors in window / Total requests) / (1 - SLO) > 2 → Investigate.

## 6. Alert Design Principles

- Multi-window multi-burn (fast + slow) to reduce noise
- Page only on user-visible impact, not internal counters
- Include runbook link + diagnostic queries in alert description
- Prefer ratio-based alerts over raw counts
- Suppress during maintenance windows / controlled experiments

## 7. Tracing Essentials

- Root Span: Entry (e.g., HTTP request handler)
- Child Spans: DB query, external API call, queue publish
- Trace Context Propagation: HTTP headers (traceparent), messaging metadata
- Tags / Attributes: user_id (privacy safe), endpoint, cache_status
- Logs In Context: Correlate via trace_id for deep dives

## 8. Observability Checklist for a New Endpoint

- [ ] Structured logs with correlation IDs
- [ ] Latency histogram (not just average)
- [ ] Error rate metric (5xx + defined business failures)
- [ ] Critical external calls traced with spans
- [ ] Feature flag state emitted
- [ ] Default dashboard created (latency, error, traffic, saturation)
- [ ] Alert for high error burn rate
- [ ] Runbook link documented

## 9. Anti-Patterns

| Anti-Pattern | Consequence | Remedy |
|--------------|-------------|--------|
| Log Everything at DEBUG | Storage cost & signal dilution | Define field schema & sampling |
| Alert on CPU 70% | Noise from normal spikes | Alert on saturation + error correlation |
| Single-Window Threshold | Misses slow burns or spikes | Multi-window strategy |
| Missing Trace Context | Fragmented analysis | Enforce propagation library |
| No Postmortems | Repeat incidents | Lightweight template & SLA |

## 10. Quick Practice

1. Draft an SLO: 99.0% successful checkout requests over 7 days. Compute error budget percentage and list two burn scenarios.
2. Given latency p95 jumped while RPS steady—list three hypotheses.
3. Design one actionable alert (include condition + runbook pointer).

---

**Next Lesson Suggestion**: Practical Profiling & Optimization (to be created).
