# Clarity – Tagging System

This document outlines the tagging system used in Clarity to classify articles and surface meaningful themes for filtering and exploration.

---

## Purpose

Tags are used in Clarity to:
- Describe **what** an article is about (topics)
- Reveal **how** it’s framed (rhetorical styles, tone, framing lenses)
- Allow users to filter, cluster, and explore content across narratives

---

## Types of Tags

### 🏷️ Topical Tags
- Generated from AI summarization (e.g. “TikTok Ban”, “Crypto Crash”)
- Used for assigning `topic_id`
- Displayed in ResultCards and Timeline headers

### 🧠 Rhetorical/Framing Tags
- Derived from NarrativeAnalysisAgent output
- Examples:
  - `emotional`
  - `national security framing`
  - `economic framing`
  - `authoritative tone`

### ⚠️ Manipulation Signals
- Rendered as tag-style chips like:
  - `high risk`
  - `urgency framing`
  - `logical fallacy: slippery slope`

---

## Tag Generation Flow

1. AI Summarizer parses full article and returns a list of key phrases
2. Rhetorical classifier maps tone/rhetoric/fallacy into predefined tag pool
3. System deduplicates and maps tag → visual chip with category and style

---

## Tag Display

Tags are shown in:
- **ResultCards**: at the bottom of each article block
- **Timeline Filters**: as top-aligned chips for quick filtering
- **Investigation View**: fully expanded, grouped by category

---

## Design Guidelines

- Tag text = lowercase, short (1–3 words)
- No political tags (e.g. no “left-wing”, “liberal”, “conservative”)
- Tags must represent framing, not identity or agenda
- Color-coded by category (topic, rhetoric, risk)

---

## Future Features

- Tag impact weighting (e.g. tag strength by frequency)
- Time-filtered tag appearance (“when did ‘fear-based’ emerge?”)
- Tag clustering / co-occurrence graphs