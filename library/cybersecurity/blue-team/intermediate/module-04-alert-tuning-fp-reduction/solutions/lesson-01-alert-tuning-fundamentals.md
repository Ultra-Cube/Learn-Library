# Solution — Lesson 01: Alert Tuning Fundamentals

- Candidate exceptions: service accounts with documented behavior, vulnerability scanners, backup servers with known patterns.
- Threshold change: from >50 fails/24h to >25 fails/1h (captures bursts); expect lower volume but higher precision.
- Guardrails: time-bound exceptions, parallel detection for privileged accounts, anomaly-based secondary checks.
