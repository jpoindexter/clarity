# 🧠 Clarity Intelligence Platform

Clarity is an AI-powered intelligence and narrative analysis platform designed to detect contradictions, misinformation, and narrative manipulation in real-time data streams. Built for neurodivergent learners, independent researchers, and anyone seeking truth through clarity.

---

## 🚀 Project Structure

- `backend/` – FastAPI-based backend (news, contradictions, AI inference, database)
- `docs/` – Project documentation (vision, architecture, roadmap, PMF, etc.)
- `alembic/` – Database migration config (via Alembic + SQLAlchemy)
- `node_modules/` – Local frontend deps (Next.js to be rebuilt)

---

## 🛠️ Tech Stack

- **Backend**: FastAPI, PostgreSQL, Alembic, SQLAlchemy
- **AI**: Ollama (local LLMs: Mistral, DeepSeek, LLaMA, etc.)
- **Frontend**: [Coming Soon] Next.js (to be rebuilt)
- **Infra**: Python 3.11+, pgAdmin 4, Alembic migrations

---

## 🧪 Local Dev Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/jpoindexter/clairity.git
   cd clarity
   ```

2. Create `.env` based on `.env.example`

3. Run Alembic migrations:
   ```bash
   alembic upgrade head
   ```

4. Start the backend:
   ```bash
   uvicorn backend.main:app --reload
   ```

---

## 📌 MVP Phase Goals

- Log contradictions in news articles
- Summarize impact & highlight misinformation
- Build real-time red flag alert system
- Serve frontend visualizations via Next.js

---

## 🔐 Status

> Internal MVP — not yet deployed.  
> For dev use only.  