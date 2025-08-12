---
id: CYB-BLT-INT-001
title: Windows Event Log Triage Basics
domain: Cybersecurity
track: Blue Team
level: Intermediate
module: Incident Detection
duration: 45m
prerequisites: [CYB-FND-BEG-001]
tags: [windows, event-logs, detection]
sources:
  - https://learn.microsoft.com/windows/security/threat-protection/auditing/basic-audit-policy-recommendations
  - https://attack.mitre.org/
---

## Overview

Triage common Windows events to spot authentication anomalies and suspicious process activity.

## Learning objectives

- Know key event IDs for logon/logoff and process creation
- Baseline normal vs. anomalous patterns
- Document findings reproducibly

## Key terms

- Event ID — a numeric identifier for a Windows audit event
- EID 4624/4625 — logon success/failure
- EID 4688 — process creation

## Explanation

- Enable auditing and collect Security logs; ensure 4688 includes command lines.
- Review EID 4624/4625 for brute-force patterns or impossible travel (workstation/local domain context).
- Inspect 4688 for unexpected parent-child relationships and suspicious command lines.

## Exercises

1. List three red flags across 4624/4625 patterns.
2. Show two suspicious 4688 command-line examples.

## Challenges & Activities

- Activity (10m): Baseline normal logon types and typical source addresses in your lab.
- Challenge (20m): Create two basic detection rules (pseudo-logic) for failed login spikes and encoded PowerShell.
- Stretch: Map findings to MITRE ATT&CK techniques.

## Puzzle

You see many 4625 failures from localhost followed by a single 4624 and then 4688 launching `rundll32`. What story could explain this?

## Further reading

- Windows audit policy — [learn.microsoft.com](https://learn.microsoft.com/windows/security/threat-protection/auditing/basic-audit-policy-recommendations)
- MITRE ATT&CK — [attack.mitre.org](https://attack.mitre.org/)
