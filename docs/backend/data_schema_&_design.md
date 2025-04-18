# Clarity Intelligence Platform – Data Schema & Design

## 1. Core Schema Overview

Clarity operates as an AI-driven intelligence platform for contradiction detection, misinformation tracking, and narrative intelligence. 

- ✅ No user-generated content or engagement tracking.
- ✅ Strictly focused on real-time intelligence processing.
- ✅ Designed for speed, accuracy, and automation.

## 2. Primary Data Structures

- **SummarizedArticles Table**  
  Stores all successfully ingested and enriched articles, including:
  - `id` (int): Primary key
  - `title` (str): Original article title
  - `url` (str): Canonical link
  - `summary` (text): AI-generated abstract
  - `tags` (array or JSON): AI-classified topics
  - `tone` (str): AI-evaluated sentiment
  - `source` (str): "rss", "url", etc.
  - `timestamp` (datetime): Ingestion time
  - `raw_text` (text): Extracted article body

- **Contradictions Table**  
  Tracks AI-identified contradictions between articles and sources over time.

- **Source Reputation Table**  
  Tracks credibility signals and longitudinal scoring for all source domains.

## 3. Data Ingestion Pipeline 

Ingests data from major news sources, government reports, and finance feeds.

AI processes incoming data in real time.

Contradictions & misinformation tracked across multiple narratives.

- ✅ No user accounts or engagement tracking.
- ✅ Strict focus on AI-driven intelligence analysis.
- ✅ Optimized for speed, automation, and large-scale ingestion.

## 4. Next Steps

- Validate schema against current ingestion process.

- Ensure contradiction detection runs at high accuracy.

- Confirm AI credibility scoring method is optimized.

- Expand financial & geopolitical intelligence tracking.

This schema reflects Clarity's AI-driven intelligence model with no user-based interaction or bias tracking.