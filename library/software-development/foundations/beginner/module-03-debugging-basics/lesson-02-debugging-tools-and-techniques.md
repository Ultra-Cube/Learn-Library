---
id: SWD-DBG-BEG-002
title: Debugging Tools and Techniques
module: Debugging Basics
track: Foundations
level: Beginner
duration: 25m
author: UltraCube Software Engineering Team
last_updated: 2025-09-02
prerequisites:
  - lesson-01-introduction-to-debugging.md
learning_objectives:
  - Use breakpoints effectively in an IDE
  - Differentiate logging levels and apply structured logging
  - Perform call stack and variable state inspection
  - Apply binary search and hypothesis-driven isolation for defects
  - Utilize watch expressions and conditional breakpoints
---

## Debugging Tools and Techniques

> Practical instruments to accelerate root cause identification while avoiding guesswork.

## 1. Categories of Debugging Tools

| Category | Purpose | Examples |
|----------|---------|----------|
| Interactive Debugger | Step through code, inspect state | VS Code, PyCharm, IntelliJ |
| Logging Framework | Persist execution context | Winston, Log4j, Python logging |
| Profiler | Measure performance hotspots | perf, cProfile, VisualVM |
| Tracing | Correlate distributed calls | OpenTelemetry, Jaeger |
| Memory Analyzer | Detect leaks/retentions | Valgrind, Eclipse MAT |

## 2. Breakpoints Beyond the Basics

**Types**:

- Line breakpoints
- Conditional breakpoints (expression-driven)
- Logpoints (non-interrupting)
- Exception breakpoints (first/uncaught)
- Function / method breakpoints

**Best Practices**:

- Start broad → refine condition
- Remove obsolete breakpoints before committing
- Prefer logpoints in collaborative sessions to avoid halting teammates' flow

## 3. Strategic Logging

| Level | Typical Use | Avoid Overuse For |
|-------|-------------|-------------------|
| TRACE | Extremely detailed path tracing | Production high-throughput paths |
| DEBUG | Internal state, branching decisions | Sensitive data dumps |
| INFO  | High-level lifecycle events | Loop-iteration noise |
| WARN  | Recoverable anomaly | Normal control flow |
| ERROR | Failed operation needing attention | User typos (unless recurring) |
| FATAL | Process-ending failure | Any recoverable scenario |

**Structured Logging Fields**:

- timestamp
- correlation_id / trace_id
- component / subsystem
- event / action
- key parameters
- result / status

## 4. Hypothesis-Driven Isolation

1. Observe the failure (inputs, outputs, environment)  
2. Form a minimal plausible cause hypothesis  
3. Design an experiment (instrumentation, added assertion)  
4. Run and collect evidence  
5. Refine or discard hypothesis  
6. Iterate until root cause converges  

Common Mistakes: jumping to code changes before evidence; modifying multiple variables at once; ignoring environment drift.

## 5. Call Stack & State Inspection

Focus points:

- Entry arguments vs mutated state
- Off-by-one indexes in loops
- Null / None vs empty collection distinctions
- Race conditions (inspect thread state where supported)

Use watch expressions for evolving values; snapshot complex objects (serialize if needed) to diff later.

## 6. Performance-Oriented Debugging

When a bug manifests as slowness:

- Confirm: Is it latency (one action) or throughput (many)?
- Capture baseline metrics (wall time, CPU, memory) before changes
- Use sampling profiler first (low overhead) before instrumenting
- Examine: N+1 queries, redundant serialization, blocking I/O

## 7. Minimal Reproduction Crafting

Checklist:

- Narrow input set (strip unrelated parameters)
- Remove side-effects (stub network / file I/O)
- Freeze timing sources (fixed seeds, time mocks)
- Document reproduction steps (copy/paste ready)

Benefits: Amplifies collaboration, accelerates code review, improves regression test creation.

## 8. Debugging in Distributed Systems

Tactics:

- Correlate logs via trace IDs across services
- Capture request + dependency timing waterfall
- Use chaos tools (small, controlled fault injection) to validate assumptions
- Snapshot configuration versions (feature flags, env vars)

## 9. Tool Selection Matrix

| Scenario | First Tool | Supplement |
|----------|------------|-----------|
| Crash at startup | Exception breakpoint | Stack trace logging |
| Intermittent null ref | Conditional breakpoint | Focused logging |
| Memory growth | Heap profiler | Allocation tracing |
| Request latency | Sampling profiler | Distributed trace viewer |
| Data corruption | Watch expressions | Serialization diff script |

## 10. Exit Criteria for a Debugging Session

You should be able to state succinctly:

- Root cause (single sentence)
- Impacted scope (modules/components)
- Fix strategy (patch, refactor, config)
- Regression tests added/updated
- Preventative measure (lint rule, guard clause, metric)

## ✅ Quick Practice

1. Set a conditional breakpoint that only triggers when `attempts > 5 && status === 'RETRY'`.
2. Convert three noisy DEBUG log lines into a structured single INFO event.
3. Create a minimal reproduction for a hypothetical function that intermittently sorts incorrectly when given duplicate keys.

---

**Next Lesson Suggestion**: Error Monitoring & Observability Foundations (to be created).
