---
id: CYB-BLT-INT-002
title: Intro to Network Threat Hunting
domain: Cybersecurity
track: Blue Team
level: Intermediate
module: Incident Detection
duration: 50m
prerequisites: [CYB-FND-BEG-001]
tags: [network, hunting, zeek]
sources:
  - https://docs.zeek.org/en/current/
  - https://www.crowdstrike.com/cybersecurity-101/threat-hunting/
---

## Overview

Form hunting hypotheses and test them with network metadata (e.g., Zeek logs).

## Learning objectives

- Formulate hypotheses (“If attacker… then we’d see…”)
- Use DNS, HTTP, and connection metadata to validate
- Summarize hunt results and next steps

## Key terms

- Zeek — a network security monitor producing rich metadata
- Beaconing — periodic connections suggesting C2
- JA3 — TLS client fingerprinting

## Explanation

- Start with a question: anomalous DNS, rare user-agents, long-lived connections.
- Review conn.log, dns.log, http.log (or equivalent) for patterns and outliers.
- Triangulate with endpoints for confirmation.

## Exercises

1. Write two hunting hypotheses using DNS or HTTP metadata.
2. Define one simple beaconing heuristic you could test.

## Challenges & Activities

- Activity (10m): Identify the top talkers and rare user-agents from a sample dataset.
- Challenge (20m): Sketch a query to find domains with high NXDOMAIN rates and justify why it might be suspicious.
- Stretch: Outline how you’d pivot from a rare JA3 to host triage.

## Puzzle

You find periodic DNS queries to a random-looking domain every 10 minutes from one host. What could this indicate and what’s your next step?

## Further reading

- Zeek docs — [docs.zeek.org](https://docs.zeek.org/en/current/)
- Threat hunting overview — [crowdstrike.com](https://www.crowdstrike.com/cybersecurity-101/threat-hunting/)
