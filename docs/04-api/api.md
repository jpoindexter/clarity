# Clarity – API Reference

This document outlines the current and planned API endpoints for the Clarity narrative intelligence platform. These routes support ingest, timeline rendering, and investigation queries.

---

## 🔗 Base URL

```
http://localhost:8000
```

---

## 🔍 `/ingest` (POST)

**Purpose:** Ingest articles by topic query and trigger AI enrichment

**Body:**
```json
{
  "topic": "tiktok ban"
}
```

**Returns:**
- 200 if ingest was successful
- Triggers summarization and narrative analysis

---

## 📚 `/timeline/:topic_id` (GET)

**Purpose:** Retrieve list of AI-enriched articles for a narrative

**Returns:**
```json
[
  {
    "title": "U.S. Considers TikTok Ban",
    "source": "Reuters",
    "published_at": "2025-04-10",
    "tone": "critical",
    "rhetoric": ["national security", "emotional"],
    "manipulation_score": 0.72,
    "summary": "...",
    "topic_id": "tiktok-ban"
  }
]
```

---

## 🧠 `/investigation/:article_id` (GET)

**Purpose:** Full detail view for a specific article

**Returns:**
```json
{
  "tone": "critical",
  "rhetoric": ["emotional", "economic"],
  "fallacies": ["slippery slope"],
  "manipulation_score": 0.78,
  "summary_rationale": "Frames urgency with emotionally loaded language",
  "summary": "..."
}
```

---

## Planned Routes (v1.2+)

| Endpoint | Description |
|----------|-------------|
| `/compare/:topic_id` | Show cross-source tone/rhetoric comparison |
| `/playback/:topic_id` | Time-scrubbed version of narrative |
| `/tags/:tag_name` | Explore all articles using a tag |
| `/clusters` | List of topics with emerging tone shifts |

---

## Notes

- All endpoints return JSON
- Backend uses FastAPI and Pydantic validation
- Frontend is powered by these endpoints via `getArticles()`, `getAnalysis()`, and `getTimeline()`