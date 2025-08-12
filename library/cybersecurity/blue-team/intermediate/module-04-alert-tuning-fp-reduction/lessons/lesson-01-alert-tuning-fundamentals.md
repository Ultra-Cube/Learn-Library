---
id: CYB-BLT-INT-009
title: Alert Tuning Fundamentals (Noise, Precision, Exceptions)
domain: Cybersecurity
track: Blue Team
level: Intermediate
module: Alert Tuning & False Positive Reduction
duration: 40m
prerequisites: [CYB-BLT-INT-008]
tags: [detections, tuning, exceptions, precision]
sources:
  - https://learn.microsoft.com/azure/sentinel/detections#tune-analytics-rules
  - https://docs.splunk.com/Documentation/ES/latest/Admin/ReducingNotableEventNoise
  - https://www.elastic.co/guide/en/security/current/tune-detection-rules.html
---

## Overview

Learn to reduce alert noise safely by using exceptions, entity allowlists, time windows, and threshold refinement.

## Learning objectives

- Define noise vs. signal; track precision and alert volume
- Apply exceptions and entity-based tuning
- Use scoped time windows and thresholds

## Key terms

- Precision — proportion of true positives among fired alerts
- Exception list — entities temporarily or permanently excluded
- Scope — narrowing rule to relevant data (hosts, users, geos, apps)

## Explanation

- Start with a baseline: current alert volume, true/false positive rates
- Add exceptions for known-good service accounts, scanners, or batch jobs
- Adjust thresholds/time windows to reduce burst-driven noise while retaining real spikes
- Document each change and review impact after 7–14 days

## Exercises

1. List three candidate exceptions for a failed-logon spike rule; justify each.
2. Propose a threshold change and predict its impact on volume and precision.

## Challenges & Activities

- Activity (10m): Define precision and volume targets for one rule.
- Challenge (20m): Draft a tuning plan: exceptions, threshold, and scope changes + rollback criteria.
- Stretch: Add a temporary suppression during planned maintenance and schedule auto-expiry.

## Puzzle

After adding a service account exception, the alert volume drops 60% but an incident shows lateral movement using that account. What guardrails should you add to keep detection coverage?

## Further reading

- Microsoft Sentinel — [learn.microsoft.com](https://learn.microsoft.com/azure/sentinel/detections#tune-analytics-rules)
- Splunk ES — [docs.splunk.com](https://docs.splunk.com/Documentation/ES/latest/Admin/ReducingNotableEventNoise)
- Elastic Security — [elastic.co](https://www.elastic.co/guide/en/security/current/tune-detection-rules.html)
