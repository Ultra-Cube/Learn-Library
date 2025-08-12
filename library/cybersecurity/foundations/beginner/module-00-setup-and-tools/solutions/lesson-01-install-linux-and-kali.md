# Solutions — Install Linux and Kali Linux

## Exercises

1. Install path justification
   - VM: Safe, reversible, snapshot support, minimal risk to host. Recommended for most learners.
   - Bare Metal: Best performance, but higher risk for daily use; requires backups.
   - WSL: Fast to set up for dev tasks; limited GUI/lab parity by default.

2. Steps (example: VM + Ubuntu/Kali)
   - Download ISO, verify checksum
   - Create VM (2–4 CPU, 4–8 GB RAM), attach ISO
   - Install OS, apply updates, install guest additions
   - Create snapshot “clean-base”

## Puzzle

Prefer a VM for Kali; keep browsing on a separate OS/profile. Use snapshots before risky tests.
