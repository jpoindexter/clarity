 
# Clarity – Frontend UX & Layout System

This document defines the user interface and layout rules that govern Clarity’s frontend, modeled after modern intelligence tools like Palantir, Splunk, and Recorded Future.

---

## 🔧 UX Foundations

- **Dark theme only**: All UI is built for high-contrast readability, supporting analyst-grade focus.
- **No onboarding fluff**: Users land directly on a search-driven Explore interface.
- **Split navigation & filters**: Sidebar = navigation only; filters appear above timelines or as contextual panels.
- **Semantic structure**: Everything is driven by topic, tone, and time.

---

## 🧭 Core Views

### 1. Explore (`/`)
- Search box front and center
- Optional chip-based topic suggestions
- Clicking "search" routes to `/timeline/:topic_id`

### 2. Timeline View (`/timeline/:topic_id`)
- Narrative summary block at top
- Scrollable ResultCards below
- Top-aligned FilterBar with tone, rhetoric, date slider
- Tone/risk/rhetoric chips embedded in each card
- Time groupings optional

### 3. Investigation View (`/investigation/:article_id`)
- Article summary + full rationale
- Risk score detail
- Expandable rhetorical breakdown

---

## 🔲 UI Components

| Component | Description |
|----------|-------------|
| `SearchBox` | Used in Explore mode |
| `ResultCard` | Article display with tone, tags, source, manipulation chip |
| `FilterBar` | Top-aligned filters, never in sidebar |
| `TimelineSlider` | Optional mini scrub bar for playback / range |
| `SidebarNav` | Minimal, includes Explore, Timeline, (future: Compare) |
| `RiskBadge` | Visual indicator (LOW, MEDIUM, HIGH) in top-right of card |

---

## 🧠 UX Inspiration Models

- **Splunk SOAR** – Timeline blocks + sidebar nav + contextual severity chips
- **Palantir Gotham** – Investigation depth and explainability layers
- **Perplexity** – Search-driven start, no fluff
- **ResearchRabbit** – Topic graph exploration (optional post-MVP)

---

## Future Features

- Toggle between “timeline” and “compare” mode
- Visualize shifts in tone across time per topic
- Hover-to-expand manipulation rationale on ResultCard