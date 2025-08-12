---
id: CYB-FND-BEG-000
title: Install Linux and Kali Linux
domain: Cybersecurity
track: Foundations
level: Beginner
module: Setup & Tools
duration: 45m
prerequisites: []
tags: [linux, kali, install, virtualization]
sources:
  - https://ubuntu.com/download/desktop
  - https://www.kali.org/get-kali/
  - https://learn.microsoft.com/windows/wsl/install
---

## Overview

Learn safe ways to install Linux (Ubuntu as an example) and set up Kali Linux for security labs using a VM or WSL.

## Learning objectives

- Choose an install method (bare metal, VM, WSL)
- Install Ubuntu Desktop
- Install Kali Linux for lab use

## Key terms

- VM — Virtual Machine (e.g., VirtualBox/VMware)
- WSL — Windows Subsystem for Linux
- ISO — installer image for operating systems

## Explanation

Installation options:

- Bare Metal (advanced): Boot from USB and install Linux as your main OS.

- Virtual Machine (recommended for most): Install VirtualBox/VMware; import or install Linux ISO.

- WSL (Windows): Use WSL2 to run Linux user space; suitable for dev tasks (not full GUI labs by default).

Kali Linux guidance:

- Run Kali as a VM or in a dedicated environment to avoid mixing lab tools with daily browsing.

- Keep Kali off your primary account data; snapshots are useful before exercises.

## Exercises

1. Decide your install path (Bare Metal/VM/WSL) and justify the choice.
2. Create a bootable USB (bare metal) or a new VM (virtualization) or enable WSL (Windows), and document steps.

## Challenges & Activities

- Activity (10m): Verify checksums for downloaded ISOs; explain why this matters.
- Challenge (15m): For VM path, create a snapshot after base install and name it “clean-base”. For WSL, create a backup/export of the distro.
- Stretch: Configure a bridged or NAT network mode and describe trade-offs.

## Puzzle

You installed Kali on bare metal and are worried about daily browsing safety. What are safer alternatives that maintain lab capability?

## Further reading

- Ubuntu Desktop — [ubuntu.com/download/desktop](https://ubuntu.com/download/desktop)
- Kali Linux — [kali.org/get-kali](https://www.kali.org/get-kali/)
- WSL Install — [learn.microsoft.com/windows/wsl/install](https://learn.microsoft.com/windows/wsl/install)
