# Clarity Reports - Project Documentation

## README.md
### High-Level Project Summary
Clarity Reports is an AI-driven financial intelligence platform that detects media manipulation, ranks news credibility, and delivers AI-generated market insights and reports. Users can access reports via a secure dashboard or API.

## project_overview.md
### Business Plan, Revenue Model & Execution Roadmap
- **Product:** AI-generated market intelligence reports.
- **Target Users:** Hedge funds, financial analysts, traders.
- **Pricing Model:** Subscription ($299-$999/mo), Custom Reports ($2K-$10K).
- **Go-to-Market:** Direct outreach, social media, content marketing.
- **Tech Stack:**
  - **Frontend:** Next.js, Tailwind (Minimal dashboard for report access)
  - **Backend:** FastAPI, PostgreSQL, Ollama (AI)
  - **AI Processing:** Multi-agent framework with task routing (summarization, contradiction detection, classification) using local models (Mistral, LLaMA3, DeepSeek Coder).
  - **Payments:** Stripe (Subscription-based report access)
 
## architecture.md
### Backend Structure, Dependencies, API Flow
- **Backend:** FastAPI for API endpoints, modular multi-agent system (summarizer, contradiction, classifier), Ollama for local LLM execution (Mistral, LLaMA3, Phi-4), PostgreSQL for news and report storage.
- **Data Pipeline:** NewsAPI, Twitter Scraper → AI Processing → Sentiment & Credibility Scoring → Report Generation.
- **Frontend (Later Phase):** Minimal UI for purchasing and scheduling reports.

## api_documentation.yaml
```yaml
openapi: 3.0.0
info:
  title: Clarity Reports API
  description: API documentation for financial intelligence reports.
  version: 1.0.0
paths:
  /fetch-news:
    get:
      summary: Fetch latest financial news
      responses:
        '200':
          description: Success
  /generate-report:
    post:
      summary: Generate an AI-powered market intelligence report
      responses:
        '200':
          description: Report generated
```

## setup_guide.md
### Installation Steps
```bash
# Clone the repository
git clone https://github.com/your_repo/clarity_reports.git clarity_reports
cd clarity_reports

# Ensure Python 3.9+ is installed
python3 --version

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r docs/requirements.txt
```

## requirements.txt
```plaintext
fastapi
uvicorn
requests
ollama
pandas
matplotlib
weasyprint
newsapi-python
```

## deployment_guide.md
### Steps to Deploy
1. **Set up PostgreSQL database**
2. **Run FastAPI server**: `uvicorn app.main:app --host 0.0.0.0 --port 8000`
3. **Schedule Report Generation** (cron job or cloud function)
4. ## Deployment Options
   - **Cloud Hosting (Backend):** Deploy FastAPI via Fly.io or DigitalOcean
   - **Frontend Hosting:** Deploy Next.js dashboard via Vercel
   - **Database:** PostgreSQL (Managed Cloud Instance)
   - **Security:** API authentication with OAuth2, rate limiting, log monitoring

## security_best_practices.md
- **API Rate Limiting**
- **Secure API Keys & Tokens**
- **Encrypt Stored Data**
- **Regular Security Audits**

## versioning.md
- **v1.0.0 (Initial Release):** Core features - news scraping, AI analysis, PDF reports.
- **v1.1.0 (Next Release):** Automated scheduling, enhanced UI.
