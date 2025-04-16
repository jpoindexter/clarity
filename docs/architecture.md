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

To ensure high-reliability text extraction from online articles, Clarity implements a multi-layer content fallback system known internally as the **Clarity Content Ladder**. Each layer attempts to extract usable article text and only falls through when the previous layer fails.

#### 🧠 Content Ladder Flow

1. **Newspaper3k** – Standard structured extractor.
2. **Trafilatura** – Fast, lightweight extractor with user-agent spoofing.
3. **BeautifulSoup** – Raw HTML paragraph text fallback.
4. **RSS Summary Fallback** – Uses entry summary if all scrapers fail.
5. *(Coming Soon)*: AMP variant, Wayback Archive lookup, News APIs, Playwright browser automation.

This ensures that every article passed to the AI agents contains readable, high-signal content — even if protected, JS-rendered, or blocked.

The fallback system is centralized in `article_fetcher.py` and automatically wired into the `/articles/ingest` FastAPI route.