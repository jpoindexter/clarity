 
# Clarity – AI Agents

This document outlines the local AI agents used within Clarity to process and enrich media narratives.

---

## Overview

Clarity does not rely on cloud AI APIs. Instead, it uses **locally hosted language models** via Ollama (DeepSeek, Mistral, Phi-2) to perform summarization, narrative analysis, and rhetorical classification. This approach preserves privacy, speeds up iteration, and aligns with the project’s long-term vision of being fully local and offline-capable.

---

## Agents in Use

### 🧠 1. Summarization Agent

**Model:** DeepSeek or Mistral (depending on local setup)

**Purpose:** Reduces full article content into a short, readable summary.

**Output:**
- `summary` (2–4 sentences)
- `tags` (topics extracted from the text)

---

### 🧠 2. NarrativeAnalysisAgent

**Model:** DeepSeek (preferred for reasoning tasks)

**Purpose:** Analyzes article structure to detect manipulation signals.

**Prompt Template:**
```
Analyze the article below. Return a JSON object with:
- tone: (neutral, critical, supportive)
- rhetoric: list of rhetorical techniques (e.g. emotional, fear-based)
- fallacies: logical fallacies present (if any)
- manipulation_score: 0.0–1.0
- summary_rationale: short explanation of why manipulation score was assigned.
```

**Output:**
```json
{
  "tone": "critical",
  "rhetoric": ["emotional", "national security framing"],
  "fallacies": ["slippery slope"],
  "manipulation_score": 0.82,
  "summary_rationale": "Uses urgency, emotional appeals, and no opposing viewpoint."
}
```

---

## Execution

Agents are triggered during ingest via FastAPI routes (`/ingest`), and their output is stored directly in the `summarized_articles` table. All AI outputs are validated against a strict schema using Pydantic before display.

---

## Extensibility

Future agents may include:
- **ClusteringAgent** for topic grouping
- **FramingShiftDetector** for time-based tone/rhetoric evolution
- **NarrativeComparator** for comparing articles with different tones on the same event