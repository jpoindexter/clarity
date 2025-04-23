# Clarity – Narrative Intelligence Platform Overview

Clarity is a narrative intelligence platform designed to help analysts, journalists, researchers, and curious thinkers investigate how media stories evolve over time. Rather than acting as a traditional news feed, Clarity offers investigative tools to expose shifts in tone, rhetorical framing, and potential manipulation across sources and time.

## Purpose

Clarity exists to answer one core question: **How is this story being told — and how has that changed?**

By focusing on the language, framing, and emotional tone of news articles, Clarity helps users recognize patterns, contradictions, and information asymmetries in the media ecosystem.

## Key Principles

- **Intent-First UX**: Users begin with a topic or question, not a feed.
- **Ephemeral Sessions**: No login, no storage — every session is investigative and temporary.
- **Explainable AI**: Every manipulation signal is backed by structured agent output and rationale.
- **Analyst-Grade UX**: Inspired by tools like Splunk, Palantir, and Recorded Future.

## Core Modes

- **Explore**: A search-first entry point to investigate a narrative.
- **Timeline**: Scrollable view of AI-enriched articles, grouped by date and filterable by tone, rhetoric, and risk.
- **Investigation**: A drill-down view for detailed insight into manipulation scores and language techniques.

## Ingest Pipeline

- Topic-matching through Google News RSS
- Historical narrative arc enrichment from GDELT and Common Crawl
- Articles are processed via local AI agents (DeepSeek, Mistral)
- Agent output includes tone, rhetoric, fallacies, manipulation score, and rationale

## Output Example

```json
{
  "tone": "critical",
  "rhetoric": ["emotional", "economic"],
  "fallacies": ["slippery slope"],
  "manipulation_score": 0.82,
  "summary_rationale": "Framing is fear-driven and one-sided, emphasizing urgency without counterpoints."
}
```

## Notable Design Choices

- No social content (X, Reddit) or user-submitted URLs
- No source-level bias labels (tone/rhetoric only)
- Filters are not in the sidebar — they’re contextual to each view
- Dark theme only
- Future-proofed for Tauri desktop wrapping

Clarity is not just a project — it’s a tool for truth-seeking. Designed for insight, not headlines.
