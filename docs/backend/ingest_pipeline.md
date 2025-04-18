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

To maximize the chances of extracting usable content from protected, expired, or highly dynamic sources, Clarity uses a multi-layer fallback mesh known internally as the **Clarity Content Ladder**. This pipeline ensures that even if scraping fails, we can still route content to the AI agent with meaningful signal.

### 🔁 Fallback Tiers (in order of execution)

1. **Newspaper3k** — standard HTML parser; fast and effective on older or simple article layouts.
2. **Trafilatura** — lightweight, customizable parser with spoofed user-agent.
3. **BeautifulSoup** — fallback using raw HTML paragraph scanning.
4. **RSS Summary** — if all scrapers fail, use the RSS feed’s summary field.
5. **(Planned)**: AMP variant resolution, Wayback Machine archival fallback, free news API summaries (e.g. NewsData), and Playwright JS rendering.

Each layer must meet a minimum text threshold (usually 200 characters) to proceed. All fallback attempts are logged with debug flags, and the tier that succeeded can be optionally recorded in the database.

The full ladder is implemented in `article_fetcher.py` and called directly inside `/articles/ingest`. The goal is always: **signal, not silence**.

## Notes

- `article_fetcher.py` contains all content ladder logic.
- Errors or missing content are logged for post-analysis.
- Future improvements include article caching, deduplication, and dynamic priority scoring.

## Data Persistence

After successful ingestion and AI enrichment, each article is stored in the `summarized_articles` database table. This table serves as the system’s persistent memory and enables timeline generation, filtering, and downstream analytics.

### Fields Stored:
- `title`: The article’s original title
- `url`: Canonical source URL
- `summary`: AI-generated abstract
- `tags`: List of key topics extracted from the content
- `tone`: Sentiment signal (e.g. neutral, urgent, biased)
- `source`: `"rss"` or `"url"` to indicate ingest type
- `timestamp`: Ingest time (UTC)
- `raw_text`: The full body content used to generate summary + tags 

The persistence logic is handled in `save_summarized_article()` inside `crud/articles.py` and is invoked directly within the `/articles/ingest` endpoint once all enrichment agents have run successfully.

## 4. Proposed Additions

To better support UI filtering, visibility control, and fallback tier transparency, the following schema additions are under consideration:

- `fallback_tier_used` (str): Indicates which extraction method was successful (e.g. `newspaper3k`, `trafilatura`, `bs4`, `rss_summary`, `amp`, `wayback`).
- `should_display` (bool): Marks if the article should appear on the frontend timeline by default (enables soft-hiding stale or low-signal entries).
- `ingest_origin` (str): Optional label to distinguish system-generated entries (e.g. `manual_upload`, `rss`, `api_test`, `replay`).
- `visibility_flags` (json): Future support for hiding/surfacing based on user or filter preferences (e.g. `hide_if_tags=['finance']`).

These fields are optional but recommended for scalable UI and graph logic. They support narrative filtering, timeline customization, and debug auditing.

## UI Integration Status

As of Batch 14, the ingest pipeline and storage layer are operational, but the frontend interface is not yet fully connected to persistent AI summaries. The following display issues and behavior gaps have been observed:

### Current Gaps:
- Articles shown immediately after ingest disappear when navigating away from the tab.
- Timeline tab does not pull from the `summarized_articles` database.
- There is no frontend-side limit or pagination of rendered article cards.
- Cards vary in height due to summary length; line clamping not enforced.
- Chips (tags) have inconsistent padding, wrapping, and styling.
- Links can overflow card width if too long.
- "Classification of the text" headings appear unnecessarily verbose.
- No visual indicator of fallback tier used (e.g. RSS, BS4, AMP).

### Planned Fixes:
- Timeline will load saved summaries from the database.
- Card sizing and clamping will be normalized.
- Chips will use a unified style component.
- Source tier badge (e.g. `via RSS summary`) will be shown.
- Filtering by tone, tag, and ingest tier will be implemented.