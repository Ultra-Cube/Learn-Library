---
id: CYB-RED-BEG-002
title: Passive Reconnaissance
domain: Cybersecurity
track: Red Team
level: Beginner
module: Reconnaissance Fundamentals
duration: 45m
prerequisites: 
  - Completed Red Team basics lesson
  - Basic understanding of networking
tags: 
  - reconnaissance
  - osint
  - information-gathering
  - passive-scanning
sources:
  - OSINT Framework
  - SANS OSINT Summit presentations
  - Bellingcat's Online Investigation Toolkit
---

## Overview

Learn how to gather information about targets without directly interacting with their systems.

## Learning Objectives

- Understand passive vs active reconnaissance
- Learn OSINT (Open Source Intelligence) techniques
- Practice using search engines for intelligence gathering
- Identify social media reconnaissance methods

## Passive Reconnaissance Overview

Passive reconnaissance involves gathering information about a target without directly interacting with their systems or networks. This approach reduces the risk of detection while still providing valuable intelligence.

### Key Principles

1. **No Direct Contact**: Never interact directly with target systems
2. **Public Sources Only**: Use publicly available information
3. **Stealth**: Avoid leaving digital footprints
4. **Documentation**: Keep detailed records of findings

## Common Techniques

### Search Engine Intelligence

- Google dorking/hacking
- Bing and specialized search engines
- Image search and reverse image search
- Cached page analysis

### Social Media Intelligence

- LinkedIn for organizational structure
- Facebook for personal information
- Twitter for real-time information
- Instagram for location data

### Public Records

- Domain registration information (WHOIS)
- Business registrations
- Patent filings
- Court records

## Tools and Resources

### Search Engines
- Google Advanced Search
- Shodan (Internet-connected device search)
- Censys (Internet scanning platform)
- Have I Been Pwned (breach database)

### OSINT Frameworks
- OSINT Framework website
- Maltego (link analysis)
- theHarvester (email/subdomain gathering)
- Recon-ng (reconnaissance framework)

## Practical Exercise

### Exercise: Company Intelligence Gathering

**Target**: A fictional company "SecureTech Solutions"

**Tasks**:
1. Find the company website and key personnel
2. Identify email format and potential email addresses
3. Discover subdomains and related domains
4. Locate social media profiles
5. Find any public documentation or presentations

**Tools to Use**:
- Google advanced search operators
- LinkedIn
- WHOIS lookup tools
- Subdomain enumeration tools

## Challenge

Research a real cybersecurity company (like CrowdStrike, FireEye, or Rapid7) using only passive techniques. Create a brief intelligence report including:

- Company structure and key personnel
- Technology stack indicators
- Physical locations
- Recent news or press releases
- Social media presence

**Time Limit**: 30 minutes
**Format**: 1-2 page report

## Solution

A comprehensive intelligence report should include:

### Company Profile
- Business focus and services
- Size and revenue (if public)
- Key executives and departments
- Corporate hierarchy

### Technical Footprint
- Website technologies used
- Subdomains and related domains
- Email patterns and formats
- Cloud services and platforms

### Physical Presence
- Office locations
- Data center locations (if applicable)
- Regional presence

### Digital Presence
- Social media accounts
- Recent publications
- News mentions
- Industry participation

## Ethics and Legal Considerations

### Ethical Guidelines
- Only use publicly available information
- Respect privacy boundaries
- Don't attempt social engineering
- Follow responsible disclosure principles

### Legal Boundaries
- Understand local laws regarding OSINT
- Avoid accessing private systems
- Don't violate terms of service
- Document sources for accountability

## Summary

Passive reconnaissance is the foundation of ethical penetration testing and red team operations. By mastering these techniques, security professionals can:

- Understand their organization's external exposure
- Identify potential attack vectors
- Improve security awareness training
- Develop better defensive strategies

## Additional Resources

- [SANS OSINT Summit presentations](https://www.sans.org)
- [OSINT Framework](https://osintframework.com)
- [Bellingcat's Online Investigation Toolkit](https://docs.google.com/spreadsheets/d/18rtqh8EG2q1xBo2cLNyhIDuK9jrPGwYr9DI2UncoqJQ)
- [Intel Techniques OSINT Tools](https://inteltechniques.com/tools)

## Next Steps

In the next lesson, we'll explore active reconnaissance techniques and learn how to safely interact with target systems for information gathering.
