---
id: CYB-BLT-INT-008
title: From Exploration to Detection (Baselines, Aggregations, Thresholds)
domain: Cybersecurity
track: Blue Team
level: Intermediate
module: SIEM Query Basics
duration: 50m
prerequisites: [CYB-BLT-INT-007]
tags: [siem, detections, baselining, thresholds, alerts]
sources:
  - https://learn.microsoft.com/azure/sentinel/detections
  - https://docs.splunk.com/Documentation/ES/latest/User/Correlationsearches
  - https://www.elastic.co/guide/en/security/current/detections-ui-exceptions.html
---

## Overview

Turn ad-hoc queries into detections by creating a baseline, choosing grouping keys, and setting thresholds or statistical conditions.

## Learning objectives

- Baseline normal behavior to reduce false positives
- Use group-by keys and windowed aggregations
- Set thresholds and create alert-friendly outputs

## Key terms

- Baseline — reference of expected behavior (per host/user/hour)
- Threshold — rule limit that triggers an alert when exceeded
- Entity — the key subject of the detection (user, host, ip, process)

## Explanation

A reliable detection comes from a stable query + sensible threshold. Steps:

1) Pick a clear behavior to detect (e.g., excessive failed logons)
2) Establish baseline over prior N days and pick grouping keys
3) Decide on numeric threshold or use statistics (mean + k*stddev)
4) Emit concise fields for triage (entity, counts, sample values, links)

Concept example (KQL-style):

```kusto
let window = 24h;
let threshold = 50;
SecurityEvent
| where TimeGenerated >= ago(window)
| where EventID == 4625
| summarize fails = count(), sampleHosts = make_set(Computer, 3) by Account
| where fails > threshold
| project TimeGenerated=max(TimeGenerated), Account, fails, sampleHosts
```

And Splunk-ish:

```text
index=security sourcetype=wineventlog:security EventCode=4625 earliest=-24h
| stats count AS fails, values(Computer) AS sampleHosts by Account
| where fails > 50
| table _time Account fails sampleHosts
```

## Exercises

1. Replace the static threshold with a dynamic one using average + 3*stddev computed over 7 days.
2. Switch the entity from Account to SourceIP. How does this change the baseline?
3. Add a “TopProcesses” field for a process-focused detection.

## Challenges & Activities

- Activity (10m): Emit only the fields needed for an alert: Time, Entity, Count, Sample. Justify your selection.
- Challenge (25m): Design a detection for rare admin logons after hours. Define the baseline, grouping, and threshold.
- Stretch: Add a suppression/exception list for known scanners or batch accounts.

## Puzzle

You want to reduce false positives from a high-fails detection caused by a noisy service account. Which baselining or exception techniques will keep signal while excluding the noise?

## Further reading

- Microsoft Sentinel detections — [learn.microsoft.com](https://learn.microsoft.com/azure/sentinel/detections)
- Splunk ES correlation searches — [docs.splunk.com](https://docs.splunk.com/Documentation/ES/latest/User/Correlationsearches)
- Elastic Security detections and exceptions — [elastic.co](https://www.elastic.co/guide/en/security/current/detections-ui-exceptions.html)
