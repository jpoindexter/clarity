# Clarity Reports - Project Documentation

## architecture.md 
### **System Architecture & Tech Stack**

### **1. Overview**
Clarity Reports is an **AI-powered financial intelligence platform** that processes financial news, detects contradictions, analyzes sentiment, and generates structured reports. Users can access insights via a secure **dashboard and API**.

### **2. Tech Stack**
- **Frontend:** Next.js (React) for the user dashboard (report access & management).
- **Backend:** FastAPI (Python) for API services.
- **AI Processing:** Multi-agent architecture using Ollama (Mistral, LLaMA3, Phi-4, DeepSeek Coder). Agents handle summarization, contradiction detection, classification, tagging, and future tone analysis.
- **Database:** PostgreSQL (storing processed news credibility data).
- **Data Pipeline:** NewsAPI, Twitter Scraper → AI Processing → Sentiment & Credibility Scoring → Report Generation.
- **Report Generation:** WeasyPrint (PDF creation for intelligence reports).
- **Task Automation:** Cron Jobs or Celery for scheduled AI processing.
- **Deployment:** Docker & AWS (future scaling to cloud infrastructure).
- **Frontend Hosting:** Vercel (Next.js dashboard for user access)

---

### **3. Core Architecture Components**
```
clarity_reports/
│── frontend/           # Next.js Dashboard (User Portal)
│   ├── pages/          # Dashboard Pages
│   ├── components/     # UI Components
│   ├── services/       # API Client (Fetching Reports)
│   ├── public/         # Static Assets
│   ├── styles/         # Tailwind CSS Styles
│   ├── package.json    # Frontend Dependencies
│── backend/            # FastAPI Backend Services
│   ├── api/            # API Endpoints
│   ├── models/         # Database Models (PostgreSQL)
│   ├── services/       # Business Logic (AI Processing, Data Analysis)
│   ├── agents/         # Multi-agent dispatcher, prompts, and task-specific LLM logic
│   ├── utils/          # Helper Functions & Utilities
│── data/               # Raw & Processed News Data
│── reports/            # Generated PDF Reports
│── docs/               # Project Documentation
│── scripts/            # Automation Scripts (Scrapers, AI Jobs)
│── venv/               # Virtual Environment
│── requirements.txt    # Python Dependencies
│── .gitignore          # Git Ignore File
│── README.md           # Project Summary
```

---
 
### **4. API Workflow**
1️⃣ **Data Ingestion**: Scrape financial news from multiple sources (NewsAPI, Twitter, Reddit, RSS feeds). Store raw data in a structured database.  
2️⃣ **AI Processing**: Run NLP models (Mistral/LLaMA3/Phi-4/DeepSeek) to summarize & detect contradictions.  
3️⃣ **Sentiment & Credibility Scoring**: Apply VADER NLP for bias detection.  
4️⃣ **Report Generation**: Convert AI-driven insights into structured reports (PDF and JSON formats) for clients. Future support planned for API-based real-time retrieval.  
5️⃣ **Client Access**:
      - **Dashboard:** Users log in to manage & download reports (Next.js frontend).
      - **API:** Institutional clients can programmatically access reports via FastAPI endpoints.

---

### **5. API Endpoints Overview**

---

### 6. Article Ingestion Fallback Strategy

To ensure maximum resilience when extracting article content, Clarity uses a tiered mesh known internally as the **Clarity Content Ladder**. This multi-layer system guarantees usable input for AI summarization — even when sources are blocked, paywalled, JavaScript-rendered, or unavailable.

#### 🧠 Content Ladder Flow

1. **Newspaper3k** – Structured parser, fast and effective for basic HTML articles.
2. **Trafilatura** – Lightweight extractor with user-agent spoofing.
3. **BeautifulSoup** – Raw paragraph scanner for minimal HTML fallback.
4. **RSS Summary Fallback** – Uses `entry.summary` if all scrapers fail.
5. *(Coming Soon)*:
     - **AMP Variant** – Attempts to load the `/amp` version of article URL.
     - **Wayback Machine** – Pulls archived versions via Internet Archive.
     - **Free News APIs** – Fallback to NewsData, GNews, or other summarization endpoints.
     - **Playwright Automation** – Last-resort JS-rendered scrape (e.g. for NYT or Reuters).

Each extraction attempt is logged, and the fallback tier used is optionally stored in the database for transparency. The pipeline enforces a minimum text threshold before allowing AI agents to process content.

The full ladder lives inside `article_fetcher.py` and connects directly to `/articles/ingest`. This ensures every article routed to the summarizer has a fallback mechanism to guarantee signal, not silence.

### 7. Frontend Display Gaps & Timeline Roadmap

As of Batch 14, article ingestion, AI enrichment, and database storage are all live. However, the frontend (particularly the Timeline tab) currently has critical display limitations:

#### ❌ Known Display Gaps
- Articles shown after ingest disappear when tab is changed.
- Timeline tab is not yet wired to pull from the `summarized_articles` table.
- No frontend-side article limit (`load more` or pagination missing).
- Fallback tier (e.g. RSS summary, BS4) is not visually surfaced.
- Links within cards can overflow and break layout.
- Cards vary in size due to summary length, causing layout jitter.
- Chips (tags) are inconsistently rendered and overflow on wrap.
- "Classification of the text" and similar verbose phrases reduce clarity.

#### ✅ Planned Fixes (Batch 15+)
- DB-driven TimelineView (query summaries from backend)
- Unified card height with `line-clamp` and max-width
- Standardized chip rendering (truncated tags + color scale)
- Fallback tier badges (e.g. `via RSS`, `via AMP`)
- Tone/filter dropdowns
- Dark mode visual audit
- UI cleanup: less verbose phrasing, tighter spacing

These changes will bring the frontend into alignment with the AI processing power and resilience already present in the ingest pipeline.