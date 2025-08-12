# Solution — Lesson 01: SIEM Query Fundamentals

- Time window: change `ago(24h)` to `ago(7d)` (KQL), `earliest=-7d` (SPL), or `now()-7d` (KQL/Elastic)
- Failed logons only: add `EventID == 4625` (KQL), `EventCode=4625` (SPL), `event.code: 4625` (Elastic)
- Top 5 accounts: `summarize count() by Account | top 5 by count_` (KQL); `stats count by Account | sort - count | head 5` (SPL)
- 15m bins: `bin(TimeGenerated, 15m)` (KQL); `bin _time span=15m` (SPL)

Notes

- Finer bins reveal bursty behavior and timing patterns; coarser bins smooth noise.
