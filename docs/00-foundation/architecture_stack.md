# Clarity – Architecture & Stack

This document outlines the system architecture of the Clarity narrative intelligence platform.

## Overview

Clarity is a dark-mode, analyst-grade web application built to analyze and visualize how media narratives evolve over time. It is composed of a FastAPI backend, a Next.js frontend, and a PostgreSQL database. All AI enrichment is handled through locally running LLMs via Ollama (DeepSeek, Mistral).

---

## System Components

### 1. Frontend (Next.js + Tailwind)
- Route-driven layout (`/explore`, `/timeline/:topic_id`, `/investigation/:article_id`)
- Sidebar = navigation only (no filters)
- FilterBar = top-aligned, contextual to Timeline view
- ResultCards display tone, rhetoric, risk badge, and summary

### 2. Backend (FastAPI)
- Endpoints: `/ingest`, `/timeline/{topic_id}`, `/investigation/{article_id}`
- Sessionless, query-based data retrieval
- Agents run synchronously during ingestion
- JSON schema validated output for frontend use

### 3. Database (PostgreSQL)
- Tables:
  - `summarized_articles`: stores enriched metadata and timestamps
  - `topic_clusters`: maps articles to topic_id and human-readable topic_title
- Alembic used for migrations

---

## AI Agents (via Ollama)
- **Summarizer**: Condenses article content
- **NarrativeAnalysisAgent**: Returns tone, rhetoric, fallacies, manipulation_score, and rationale
- Output Example:
```json
{
  "tone": "critical",
  "rhetoric": ["emotional", "economic"],
  "fallacies": ["slippery slope"],
  "manipulation_score": 0.78,
  "summary_rationale": "Framing emphasizes urgency with emotionally loaded language and no counterpoint."
}
```

---

## Data Ingest Mesh

- Query-triggered fetch from Google News RSS
- Background enrichment via Common Crawl and GDELT
- Ingest agent assigns topic_id using zero-shot prompt
- All content processed locally

---

## Future Considerations

- Tauri wrapping for offline/desktop mode
- Optional GPU offload for AI processing
- Embedding layer for long-term topic linking