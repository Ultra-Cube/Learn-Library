---
id: CYB-BLT-INT-010
title: Feedback Loops and Rule Lifecycle (Metrics, Suppressions)
domain: Cybersecurity
track: Blue Team
level: Intermediate
module: Alert Tuning & False Positive Reduction
duration: 45m
prerequisites: [CYB-BLT-INT-009]
tags: [detections, lifecycle, feedback, metrics]
sources:
  - https://learn.microsoft.com/azure/sentinel/detections#best-practices
  - https://attack.mitre.org/
  - https://www.elastic.co/guide/en/security/current/detection-engine-overview.html
---

## Overview

Operationalize a simple detection lifecycle with feedback from triage, metrics tracking, and scheduled reviews.

## Learning objectives

- Capture triage outcomes to drive tuning
- Track rule health with KPIs (volume, precision, MTTR)
- Use suppressions safely and expire them

## Key terms

- KPI — key performance indicator (e.g., precision, volume, MTTR)
- Suppression — temporary mute for a known noisy condition
- Review cadence — scheduled time to re-evaluate rules

## Explanation

- Add a triage outcome field (TP/FP/Benign) and sample context to each alert
- Weekly: review top noisy rules and action tuning items; Monthly: rule efficacy review
- Define KPIs per rule; alert when KPIs drift out of bounds (too noisy or too quiet)
- Time-bound suppressions with owners and expiry dates; avoid permanent blind spots

## Exercises

1. Draft three KPIs for a failed-logon rule and target ranges.
2. Design a 30-day review checklist with inputs from triage notes.

## Challenges & Activities

- Activity (10m): Create a suppression template with owner, scope, and expiry.
- Challenge (25m): Write a rule lifecycle doc outline: creation -> deploy -> evaluate -> tune -> retire.
- Stretch: Propose a lightweight A/B approach for threshold testing.

## Puzzle

Your precision drops sharply after a rule update while volume doubles. What metrics and logs do you pull to diagnose, and how do you roll back safely?

## Further reading

- Sentinel best practices — [learn.microsoft.com](https://learn.microsoft.com/azure/sentinel/detections#best-practices)
- MITRE ATT&CK — [attack.mitre.org](https://attack.mitre.org/)
- Elastic detection engine — [elastic.co](https://www.elastic.co/guide/en/security/current/detection-engine-overview.html)
