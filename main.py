"""
Embodied AI & Robotics Intelligence Pipeline (arXiv Global Tracker)
-------------------------------------------------------------------
Author: Deyi 
License: MIT
Description: Automated ETL pipeline that scrapes, scores, ranks, and renders
             frontier AI/Robotics research papers from arXiv into executive-ready
             Markdown digests and interactive dark-mode HTML dashboards.
"""

from datetime import datetime, timezone
from typing import Any, Dict, List, Tuple
import xml.etree.ElementTree as ET
import requests

# =====================================================================
# 1. STRATEGIC INTELLIGENCE TAXONOMY (GLOBAL EMBODIED AI FOCUS)
# =====================================================================
STRATEGIC_WEIGHTS: Dict[str, int] = {
    "embodied ai": 50,
    "humanoid": 45,
    "world model": 40,
    "sim2real": 40,
    "bipedal": 35,
    "quadruped": 35,
    "reinforcement learning": 30,
    "dexterous manipulation": 30,
    "tactile sensing": 30,
    "locomotion": 25,
    "diffusion policy": 35,
    "vision-language-action": 45,
    "vla": 40,
    "actuator": 20,
    "teleoperation": 20,
}


# =====================================================================
# 2. EXTRACT ENGINE (arXiv API Ingestion)
# =====================================================================
def fetch_raw_arxiv_papers(
    category: str = "cs.RO", max_results: int = 20
) -> List[Dict[str, Any]]:
    """Fetches the latest preprints from arXiv API for a given category."""
    endpoint = (
        f"https://export.arxiv.org/api/query?"
        f"search_query=cat:{category}&"
        f"start=0&max_results={max_results}&"
        f"sortBy=submittedDate&sortOrder=descending"
    )

    print(f"[*] Ingesting top {max_results} preprints from arXiv ({category})...")

    try:
        response = requests.get(
            endpoint,
            timeout=20,
            headers={"User-Agent": "EmbodiedAI-IntelligencePipeline/1.0"},
        )
        response.raise_for_status()
    except requests.RequestException as err:
        print(f"[!] Network extraction error: {err}")
        return []

    root = ET.fromstring(response.content)
    namespace = {"atom": "http://www.w3.org/2005/Atom"}
    papers: List[Dict[str, Any]] = []

    for entry in root.findall("atom:entry", namespace):
        title_el = entry.find("atom:title", namespace)
        summary_el = entry.find("atom:summary", namespace)
        id_el = entry.find("atom:id", namespace)
        published_el = entry.find("atom:published", namespace)

        if title_el is None or summary_el is None or id_el is None:
            continue

        title = " ".join(title_el.text.strip().split())
        summary = " ".join(summary_el.text.strip().split())
        link = id_el.text.strip()
        published = (
            published_el.text.strip()[:10] if published_el is not None else "N/A"
        )

        authors = [
            a.find("atom:name", namespace).text.strip()
            for a in entry.findall("atom:author", namespace)
            if a.find("atom:name", namespace) is not None
        ]

        # Format author list concisely
        author_str = (
            ", ".join(authors[:3]) + (" et al." if len(authors) > 3 else "")
            if authors
            else "Unknown Authors"
        )

        papers.append(
            {
                "title": title,
                "summary": summary,
                "link": link,
                "pdf_link": link.replace("/abs/", "/pdf/"),
                "published": published,
                "authors": author_str,
            }
        )

    return papers


# =====================================================================
# 3. TRANSFORM & SCORING ENGINE (Semantic Scoring & Ranking)
# =====================================================================
def score_paper(
    title: str, summary: str, weights: Dict[str, int]
) -> Tuple[int, List[str]]:
    """Calculates multidimensional strategic importance score based on domain taxonomy."""
    base_score = 50
    corpus = f"{title} {summary}".lower()
    matched_tags: List[str] = []

    for keyword, weight in weights.items():
        if keyword in corpus:
            base_score += weight
            matched_tags.append(keyword)

    return base_score, matched_tags


def process_and_rank_papers(
    papers: List[Dict[str, Any]], weights: Dict[str, int]
) -> List[Dict[str, Any]]:
    """Enriches paper records with score and sorts them in descending order."""
    for paper in papers:
        score, tags = score_paper(paper["title"], paper["summary"], weights)
        paper["score"] = score
        paper["tags"] = tags

    papers.sort(key=lambda x: x["score"], reverse=True)
    return papers


# =====================================================================
# 4. LOAD & RENDER ENGINE (Markdown + Modern Dark UI Dashboard)
# =====================================================================
def export_markdown_report(
    papers: List[Dict[str, Any]], filename: str = "DAILY_INTELLIGENCE.md", top_k: int = 5
) -> None:
    """Exports top-k papers into a clean, GitHub-ready Markdown digest."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    selected = papers[:top_k]

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# 🤖 Embodied AI & Robotics Frontier Briefing ({today})\n\n")
        f.write(
            "> *Automated Intelligence Briefing generated via custom ETL scoring pipeline. "
            "Prioritizes foundation models, manipulation, locomotion, and physical AI systems.*\n\n---\n\n"
        )

        for rank, p in enumerate(selected, 1):
            tags_display = (
                " ".join([f"`#{t}`" for t in p["tags"]])
                if p["tags"]
                else "`#general-frontier`"
            )
            f.write(f"### Top {rank}: {p['title']}\n")
            f.write(
                f"- **Priority Score**: `{p['score']} pts` | **Published**: `{p['published']}`\n"
            )
            f.write(f"- **Focus Tracks**: {tags_display}\n")
            f.write(f"- **Key Authors**: {p['authors']}\n")
            f.write(
                f"- **Direct Access**: [arXiv Abstract]({p['link']}) | [PDF Fulltext]({p['pdf_link']})\n\n"
            )
            f.write(f"**Executive Abstract**:\n> {p['summary']}\n\n")
            f.write("---\n\n")

    print(f"[✓] Markdown briefing compiled: {filename}")


def export_html_dashboard(
    papers: List[Dict[str, Any]], filename: str = "index.html", top_k: int = 8
) -> None:
    """Generates an executive-grade, responsive dark-mode HTML dashboard with instant search."""
    today = datetime.now(timezone.utc).strftime("%B %d, %Y")
    selected = papers[:top_k]

    cards_markup = ""
    for rank, p in enumerate(selected, 1):
        badges = "".join([f'<span class="badge">#{tag}</span>' for tag in p["tags"]])
        if not badges:
            badges = '<span class="badge badge-muted">#frontier</span>'

        cards_markup += f"""
        <article class="paper-card" data-title="{p['title'].lower()}" data-summary="{p['summary'].lower()}">
            <div class="card-meta-top">
                <span class="rank-tag">TOP #{rank}</span>
                <div class="score-badge">
                    <span class="score-label">Priority Index</span>
                    <span class="score-value">{p['score']}</span>
                </div>
            </div>
            
            <h2 class="paper-title">{p['title']}</h2>
            
            <div class="author-row">
                <span>🗓️ {p['published']}</span>
                <span>✍️ {p['authors']}</span>
            </div>
            
            <div class="badge-cluster">
                {badges}
            </div>
            
            <p class="paper-summary">{p['summary']}</p>
            
            <div class="card-action-bar">
                <a href="{p['pdf_link']}" target="_blank" rel="noopener noreferrer" class="btn btn-secondary">
                    View PDF
                </a>
                <a href="{p['link']}" target="_blank" rel="noopener noreferrer" class="btn btn-primary">
                    arXiv Page &rarr;
                </a>
            </div>
        </article>
        """

    html_document = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Embodied AI & Robotics Intelligence Digest — {today}</title>
    <style>
        :root {{
            --bg-base: #080c14;
            --surface-1: #0f172a;
            --surface-2: #1e293b;
            --border-color: rgba(255, 255, 255, 0.08);
            --border-hover: rgba(56, 189, 248, 0.4);
            --cyan-glow: #38bdf8;
            --purple-accent: #a855f7;
            --text-heading: #f8fafc;
            --text-muted: #94a3b8;
            --text-body: #cbd5e1;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            background-color: var(--bg-base);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            color: var(--text-body);
            padding: 40px 20px;
            line-height: 1.5;
            display: flex;
            justify-content: center;
        }}

        .wrapper {{
            max-width: 900px;
            width: 100%;
        }}

        /* Header section */
        header {{
            margin-bottom: 32px;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 28px;
        }}

        .pill-brand {{
            display: inline-block;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 1.8px;
            text-transform: uppercase;
            color: var(--cyan-glow);
            margin-bottom: 12px;
        }}

        h1 {{
            font-size: 32px;
            font-weight: 800;
            color: var(--text-heading);
            letter-spacing: -0.8px;
            line-height: 1.2;
            margin-bottom: 8px;
        }}

        .subtitle {{
            font-size: 14px;
            color: var(--text-muted);
        }}

        /* Search input */
        .controls {{
            margin-top: 20px;
        }}

        .search-box {{
            width: 100%;
            background: var(--surface-1);
            border: 1px solid var(--border-color);
            padding: 12px 16px;
            border-radius: 10px;
            color: var(--text-heading);
            font-size: 14px;
            outline: none;
            transition: all 0.2s ease;
        }}

        .search-box:focus {{
            border-color: var(--cyan-glow);
            box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.15);
        }}

        /* Paper cards */
        .paper-card {{
            background: var(--surface-1);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
            transition: all 0.25s ease;
        }}

        .paper-card:hover {{
            border-color: var(--border-hover);
            transform: translateY(-2px);
        }}

        .card-meta-top {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 14px;
        }}

        .rank-tag {{
            font-size: 11px;
            font-weight: 800;
            color: var(--cyan-glow);
            background: rgba(56, 189, 248, 0.08);
            border: 1px solid rgba(56, 189, 248, 0.25);
            padding: 3px 8px;
            border-radius: 6px;
            letter-spacing: 0.5px;
        }}

        .score-badge {{
            display: flex;
            align-items: center;
            gap: 8px;
            background: linear-gradient(135deg, #6366f1, #a855f7);
            padding: 4px 12px;
            border-radius: 20px;
            color: #fff;
            box-shadow: 0 4px 14px rgba(168, 85, 247, 0.25);
        }}

        .score-label {{
            font-size: 10px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            opacity: 0.9;
        }}

        .score-value {{
            font-size: 14px;
            font-weight: 800;
        }}

        .paper-title {{
            font-size: 20px;
            font-weight: 700;
            color: var(--text-heading);
            line-height: 1.35;
            margin-bottom: 12px;
        }}

        .author-row {{
            display: flex;
            flex-wrap: wrap;
            gap: 16px;
            font-size: 13px;
            color: var(--text-muted);
            margin-bottom: 14px;
        }}

        .badge-cluster {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 16px;
        }}

        .badge {{
            font-size: 11px;
            font-weight: 600;
            padding: 3px 8px;
            border-radius: 6px;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.08);
            color: var(--cyan-glow);
        }}

        .badge-muted {{
            color: var(--text-muted);
        }}

        .paper-summary {{
            font-size: 13.5px;
            line-height: 1.65;
            color: var(--text-body);
            background: rgba(0, 0, 0, 0.25);
            padding: 14px 18px;
            border-radius: 8px;
            border-left: 3px solid var(--cyan-glow);
            margin-bottom: 20px;
        }}

        .card-action-bar {{
            display: flex;
            justify-content: flex-end;
            gap: 12px;
        }}

        .btn {{
            display: inline-flex;
            align-items: center;
            font-size: 13px;
            font-weight: 600;
            padding: 8px 16px;
            border-radius: 8px;
            text-decoration: none;
            transition: all 0.2s;
        }}

        .btn-secondary {{
            color: var(--text-heading);
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-color);
        }}

        .btn-secondary:hover {{
            background: rgba(255, 255, 255, 0.1);
        }}

        .btn-primary {{
            color: #000;
            background: var(--cyan-glow);
            font-weight: 700;
        }}

        .btn-primary:hover {{
            background: #7dd3fc;
            box-shadow: 0 0 15px rgba(56, 189, 248, 0.4);
        }}
    </style>
</head>
<body>
    <div class="wrapper">
        <header>
            <span class="pill-brand">Autonomous Research Intelligence</span>
            <h1>Embodied AI & Physical Frontier Briefing</h1>
            <p class="subtitle">Compiled on {today} • Ranked top {len(selected)} strategic breakthroughs out of incoming preprints.</p>
            
            <div class="controls">
                <input type="text" id="filterInput" class="search-box" placeholder="Filter papers by keywords (e.g. humanoid, tactile, diffusion)...">
            </div>
        </header>

        <main id="paperList">
            {cards_markup}
        </main>
    </div>

    <script>
        const filterInput = document.getElementById('filterInput');
        const cards = document.querySelectorAll('.paper-card');

        filterInput.addEventListener('input', (e) => {{
            const query = e.target.value.toLowerCase().trim();
            cards.forEach(card => {{
                const title = card.getAttribute('data-title');
                const summary = card.getAttribute('data-summary');
                if (title.includes(query) || summary.includes(query)) {{
                    card.style.display = 'block';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }});
    </script>
</body>
</html>
"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_document)

    print(f"[✓] Interactive HTML dashboard generated: {filename}")


# =====================================================================
# 5. ORCHESTRATION PIPELINE
# =====================================================================
def run_pipeline() -> None:
    """Executes the complete end-to-end intelligence cycle."""
    print("=" * 60)
    print("🚀 Initializing Embodied AI Autonomous Intelligence Pipeline")
    print("=" * 60)

    # Step 1: Extract
    raw_preprints = fetch_raw_arxiv_papers(category="cs.RO", max_results=20)
    if not raw_preprints:
        print("[!] No papers ingested. Terminating pipeline.")
        return

    # Step 2: Transform (Score & Rank)
    ranked_preprints = process_and_rank_papers(raw_preprints, STRATEGIC_WEIGHTS)

    # Step 3: Load & Deliver
    export_markdown_report(
        ranked_preprints, filename="DAILY_INTELLIGENCE.md", top_k=5
    )
    export_html_dashboard(ranked_preprints, filename="index.html", top_k=8)

    print("=" * 60)
    print("✨ Pipeline completed successfully with zero defects.")
    print("=" * 60)


if __name__ == "__main__":
    run_pipeline()