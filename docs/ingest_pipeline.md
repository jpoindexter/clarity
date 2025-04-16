# Clarity Ingest Pipeline

This document outlines the step-by-step flow for how Clarity ingests, processes, and analyzes article data. It includes technical notes on both the backend architecture and the AI enhancement pipeline.

## Overview

The ingest system is triggered via the `/articles/ingest` endpoint and accepts input from either a single URL or an RSS feed.

### Input Types
- `source: "url"` — a single article
- `source: "rss"` — a full feed containing multiple articles

## Flow Breakdown

1. **Parse Input**
   - If `rss`, feed is parsed into entries.
   - If `url`, a single article is processed.

2. **Fetch Content**
   - Clarity attempts to extract readable content from the article’s URL using the **Content Ladder** system.

3. **Run AI Agents**
   - `summarize_article()` → generates a readable summary
   - `extract_tags()` → identifies key concepts
   - `detect_contradictions()` (optional) → flags conflicting claims
   - `analyze_tone()` → sentiment or narrative signal

4. **Return Results**
   - Articles are returned with full metadata: title, summary, tags, tone, and source URL.

## 🧠 Clarity Content Ladder

To maximize the chances of extracting usable content from protected or unreliable sources, Clarity uses a tiered fallback system:

1. **Newspaper3k** — fast, structured extraction
2. **Trafilatura** — flexible with custom user-agent
3. **BeautifulSoup** — raw HTML text from `<p>` tags
4. **RSS Summary Fallback** — if all else fails, use summary from the feed
5. *(Planned)* AMP pages, Archive.org lookups, Free APIs, and Playwright scraping

Each layer only runs if the one before it fails. Minimum content length is enforced before results are sent to the AI agent.

## Notes

- `article_fetcher.py` contains all content ladder logic.
- Errors or missing content are logged for post-analysis.
- Future improvements include article caching, deduplication, and dynamic priority scoring.