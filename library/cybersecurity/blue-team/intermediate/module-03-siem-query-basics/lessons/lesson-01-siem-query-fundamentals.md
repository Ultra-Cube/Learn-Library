---
id: CYB-BLT-INT-007
title: SIEM Query Fundamentals (Data, Fields, Filters, Time)
domain: Cybersecurity
track: Blue Team
level: Intermediate
module: SIEM Query Basics
duration: 45m
prerequisites: [CYB-BLT-INT-003]
tags: [siem, queries, kql, splunk, detection]
sources:
  - https://learn.microsoft.com/azure/sentinel/kusto-query-language
  - https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/WhatsInThisManual
  - https://www.elastic.co/guide/en/kibana/current/kuery-query.html
---

## Overview

Learn the core pieces common to most SIEM query languages: selecting data sources, filtering by fields and time, projecting columns, and aggregating counts.

## Learning objectives

- Understand log tables and common fields (timestamp, host/user/ip)
- Use time windows and filters to scope investigations
- Project/select fields and compute simple aggregations

## Key terms

- Time window — the period of data a query scans (e.g., last 24h)
- Projection — selecting specific columns/fields to display
- Aggregation — summarizing data (count, sum) often grouped by fields

## Explanation

Most SIEMs provide similar building blocks even if syntax differs:

- Choose a dataset (table/index), e.g., process events, auth logs, DNS, proxy
- Filter rows with conditions (by time, user, process, IP, status)
- Select output fields and compute new ones if needed
- Aggregate to spot outliers or patterns

Examples across popular syntaxes (concepts are equivalent):

- KQL (Microsoft Sentinel):

```kusto
SecurityEvent
| where TimeGenerated >= ago(24h)
| where EventID in (4624, 4625)
| summarize logons = count() by Account, bin(TimeGenerated, 1h)
| order by logons desc
```

- Splunk SPL:

```text
index=security sourcetype=wineventlog:security (EventCode=4624 OR EventCode=4625) earliest=-24h
| bin _time span=1h
| stats count AS logons by Account _time
| sort - logons
```

- Elastic KQL (+ Lens or ESQL):

```text
index = "winlogbeat-*" and event.code : (4624 or 4625) and @timestamp >= now()-24h
```

## Exercises

1. Identify the time filter in each example and rewrite it for a 7-day window.
2. Add a filter to only include failed logons (4625) and show top 5 accounts.
3. Change the time bin from 1h to 15m and explain when finer bins help.

## Challenges & Activities

- Activity (10m): Project only Account, Computer, and EventID from the dataset. Explain why reducing columns can speed analysis.
- Challenge (20m): Count logons per SourceIP and highlight any IPs with > 100 attempts in 24h.
- Stretch: Group by both Account and SourceIP; what patterns do you see?

## Puzzle

You see an unusual spike of logons to a single host between 02:00–03:00. Which aggregation and binning choices will best reveal the account(s) and source IPs involved, and why?

## Further reading

- Sentinel KQL docs — [learn.microsoft.com](https://learn.microsoft.com/azure/sentinel/kusto-query-language)
- Splunk Search Reference — [docs.splunk.com](https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/WhatsInThisManual)
- Elastic KQL — [elastic.co](https://www.elastic.co/guide/en/kibana/current/kuery-query.html)
