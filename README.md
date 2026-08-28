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
🚀 Key FeaturesZero-Lag ETL Ingestion: Directly consumes standard Atom feeds from arXiv API with structured XML parsing.Strategic Taxonomy Scoring: Evaluates papers dynamically using domain-weighted priority indices (e.g., VLA, World Models, Dexterous Manipulation, Sim-to-Real).Dual Deliverable Formats:Markdown Report: Formatted for GitHub digests and automated email broadcasts.Interactive Dark Dashboard: Ultra-lightweight standalone HTML5/CSS3 dashboard with client-side keyword filtering and zero external JavaScript dependencies.Clean Engineering: Follows PEP 8 specifications, modular component architecture, and standard Python typing.📊 Strategic Taxonomy & Weight ModelThe scoring engine evaluates paper titles and abstracts against high-priority breakthrough vectors:Priority TrackTarget KeywordsWeight IndexFoundation & Modelsembodied ai, world model, vision-language-action (vla)+40 ~ +50 ptsLocomotion & Hardwarehumanoid, bipedal, quadruped, actuator+35 ~ +45 ptsControl & Manipulationsim2real, diffusion policy, tactile sensing, locomotion+25 ~ +40 pts⚙️ Configuration & CustomizationThe pipeline is completely data-driven. You can customize target research areas by updating STRATEGIC_WEIGHTS inside main.py:Python# Customize your personal research focus
STRATEGIC_WEIGHTS = {
    "humanoid": 50,
    "bipedal locomotion": 40,
    "reinforcement learning": 30
}
🛠️ Quickstart Guide1. PrerequisitesPython 3.10+Git2. Clone & SetupBash# Clone the repository
git clone [https://github.com/hardacrehardohgreenh06865-cell/ai-paper-daily.git](https://github.com/hardacrehardohgreenh06865-cell/ai-paper-daily.git)
cd ai-paper-daily

# Install dependencies
pip install requests
3. Run PipelineBashpython main.py
4. Output DeliverablesDAILY_INTELLIGENCE.md: Clean markdown summary suitable for team distribution.index.html: Open in any web browser (Chrome, Safari, Edge) for an interactive dashboard with instant search.
