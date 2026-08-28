<div align="center">

# 🤖 Embodied AI & Physical Intelligence Pipeline
### Autonomous Research Ingestion, Taxonomy-Weighted Scoring & Executive Dashboard

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![arXiv API](https://img.shields.io/badge/arXiv-API%20Ingestion-B31B1B?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-00D26A?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-000000?style=for-the-badge)](https://github.com/psf/black)

<p align="center">
  <b>A production-ready ETL pipeline designed to monitor, filter, rank, and publish frontier preprints in Humanoid Robotics, Embodied AI, Tactile Sensing, and Reinforcement Learning.</b>
</p>

</div>

---

## ⚡ Overview & Architecture

Modern academic repositories are inundated with high-volume preprints daily. This autonomous system functions as an **Intelligence Radar**, applying domain-specific semantic heuristics to filter signal from noise and deliver executive-grade insights.

```text
  ┌───────────────────────┐
  │   arXiv REST API      │ ──► [ CS.RO / Artificial Intelligence Preprints ]
  └──────────┬────────────┘
             │ (Raw Atom XML Stream)
             ▼
  ┌───────────────────────┐
  │   1. Ingestion Engine │ ──► Resilient HTTP extraction with auto-retry
  └──────────┬────────────┘
             │
             ▼
  ┌───────────────────────┐
  │   2. Scoring & Rank   │ ──► Domain Taxonomy Matching (Multidimensional Weights)
  └──────────┬────────────┘
             │
             ▼
  ┌─────────────────────────────────────────────────────────────┐
  │   3. Multi-Format Output Layer                              │
  │   ├── Markdown Briefing (DAILY_INTELLIGENCE.md)             │
  │   └── Dark-Mode Interactive Dashboard (index.html)          │
  └─────────────────────────────────────────────────────────────┘
