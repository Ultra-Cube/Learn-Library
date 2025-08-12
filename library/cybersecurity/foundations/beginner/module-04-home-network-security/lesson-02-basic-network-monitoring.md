---
id: CYB-FND-BEG-008
title: Basic Network Monitoring at Home
domain: Cybersecurity
track: Foundations
level: Beginner
module: Home Network Security
duration: 40m
prerequisites: [CYB-FND-BEG-001]
tags: [network, monitoring, wireshark]
sources:
  - https://www.wireshark.org/docs/
  - https://www.cisa.gov/secure-our-world
---

## Overview

Inventory devices and perform basic, safe traffic observation to understand your home network.

## Learning objectives

- Inventory devices via router UI and OS tools
- Capture a small packet sample responsibly
- Identify unusual device behavior

## Key terms

- Packet capture — recording network packets for analysis
- ARP — Address Resolution Protocol
- mDNS — multicast DNS for device discovery

## Explanation

- Inventory via router DHCP leases, OS network scans, or `arp -a`.
- Use Wireshark or tcpdump to capture on your own network; avoid sensitive sessions.
- Look for chatter/periodic beacons from IoT devices and document findings.

## Exercises

1. Produce a device inventory: hostname, MAC, vendor, purpose.
2. Capture 1–2 minutes of traffic and identify at least two protocols observed.

## Challenges & Activities

- Activity (10m): Filter traffic for a single device and summarize destinations.
- Challenge (15–20m): Detect a device with unusual traffic volume and propose an action.
- Stretch: Set up a simple DNS query log and review weekly.

## Puzzle

Your smart bulb chatters to multiple cloud endpoints every minute. What risks exist and how could network segmentation help?

## Further reading

- Wireshark Docs — [wireshark.org/docs](https://www.wireshark.org/docs/)
- CISA — [cisa.gov/secure-our-world](https://www.cisa.gov/secure-our-world)
