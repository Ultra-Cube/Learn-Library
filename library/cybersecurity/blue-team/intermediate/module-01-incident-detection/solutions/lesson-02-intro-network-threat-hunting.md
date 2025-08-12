# Solutions — Intro to Network Threat Hunting

## Exercises

1. Hypotheses examples: “If exfiltration via DNS, expect large TXT/NXDOMAIN spikes”; “If C2 via HTTP, rare user-agent + long-lived connections”.
2. Beaconing heuristic: fixed-interval connections to a domain/IP over hours with small payloads and stable JA3.

## Puzzle

Periodic DNS to random domains suggests DGA/beaconing. Next step: pivot to host, check processes, resolve domains, and block/isolate as needed.
