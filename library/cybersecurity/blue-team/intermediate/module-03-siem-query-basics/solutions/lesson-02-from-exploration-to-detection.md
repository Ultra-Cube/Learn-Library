# Solution — Lesson 02: From Exploration to Detection

- Dynamic threshold: compute `avgFails` and `stdFails` over 7d; alert when `fails > avgFails + 3*stdFails`
- Entity pivot: when using SourceIP, consider NAT egress and shared IPs; include secondary keys like Account or Host
- TopProcesses: use `make_set(Process, 5)` (KQL) or `values(process) AS TopProcesses` (SPL equivalent)

Reducing noise

- Add an exception list (service accounts, scanners)
- Baseline per-entity and per-hour to respect diurnal patterns
- Require multiple signals (fails + unusual geolocation or host)
