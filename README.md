# Digital Process Optimization – Postrückläufer Case Study

A back-office process optimization project: identifying a real inefficiency in
handling undeliverable mail ("Postrückläufer") at a bank, redesigning the
process, and rebuilding it here as a small Python data-analysis project with
fully synthetic data.

**Note on the data:** every dataset in this repository is synthetic, generated
by `src/generate_data.py` to match the *pattern* of the real process. No real
customer, account or employer data is used or reproduced anywhere here.

## Background

While working a Werkstudent role in bank back-office operations, I noticed two
compounding problems in how undeliverable mail was handled:

1. **No free contact attempt before a paid address lookup.** Every eligible
   case went straight to an external, paid address-lookup service — even
   though research showed 80–90% of affected clients had online banking and
   could likely be reached for free first.
2. **No synchronization between teams.** A separate team handling client
   messages sometimes already had a client's updated address sitting unread,
   while the back-office team ran (and paid for) a lookup anyway — creating
   duplicate work and fee-reversal tasks.

## The redesign

I proposed and helped implement a new process: log every incoming case
centrally, split the work into two roles (logging vs. filtering/eligibility),
contact eligible clients for free via online banking first, and only escalate
genuine non-responders to a paid lookup. I also produced written and video
guides so the process could be run by rotating junior/temporary staff without
pulling in a permanent employee to train each new person.

## This project

This repository rebuilds that process as a small, from-scratch Python project:

- `src/generate_data.py` — simulates case-level data for the old ("before") and
  new ("after") process, based on the real mechanics above with illustrative
  probabilities (documented in the code)
- `analysis/` — KPI analysis (cost, resolution rate, workload) comparing before
  vs. after
- `process/` — before/after process diagrams
- `dashboard/` — a simple visual summary of the results
- `presentation/` — a short write-up suitable for sharing

**Status:** in progress — data generation logic is currently being built.

## Technology

- Python (standard library + pandas + matplotlib for analysis/charts)
- GitHub

## Why this project exists

I'm learning Python by building this from scratch, one concept at a time,
rather than generating it wholesale — the commit history reflects that.