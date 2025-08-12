# Module Challenges — SIEM Query Basics

Use any SIEM you have access to (or a lab) and adapt syntax accordingly.

1. Top talkers in the last 24h

- Count events by SourceIP and list top 10 with counts
- Add a filter to exclude private ranges

1. Brute-force-like behavior

- Failed logons per Account and SourceIP in 1h bins
- Flag any Account with > 30 fails from a single IP in 1h

1. Rare processes

- Processes seen less than 5 times per host over 7 days
- Return CommandLine and hash fields where available

1. After-hours admin logons

- Logons by admin users between 20:00–06:00 local time
- Compare against their typical hours and flag anomalies

Deliverables

- Paste your query, a screenshot of results, and 2–3 sentence analysis
