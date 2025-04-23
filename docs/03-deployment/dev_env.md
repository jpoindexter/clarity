# Clarity – Developer Environment Setup

This document provides a full development environment guide for contributors or local deployment of the Clarity narrative intelligence platform.

---

## 🧠 Overview

Clarity is a query-based narrative investigation platform using:
- FastAPI (backend)
- Next.js (frontend)
- PostgreSQL (storage)
- Ollama + local LLMs (AI enrichment)

---

## 🔧 Backend Setup (FastAPI)

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start the backend server:
```bash
uvicorn main:app --reload
```

3. Alembic for DB migrations:
```bash
alembic upgrade head
```

4. Optional: run in Docker:
```bash
docker-compose up --build
```

---

## 🎨 Frontend Setup (Next.js)

```bash
cd frontend
npm install
npm run dev
```

---

## 🧪 Testing

```bash
pytest
```

- Ensure `pytest-asyncio` is installed
- Add test cases to `tests/` directory

---

## 🌐 Environment Variables (`.env`)

```env
DATABASE_URL=postgresql://user:password@localhost:5432/clarity
SECRET_KEY=your_secret_key
NEXT_PUBLIC_API_URL=http://localhost:8000
```

---

## 🤖 AI Agents (via Ollama)

Install Ollama: [https://ollama.ai](https://ollama.ai)

```bash
ollama run deepseek
```

Optionally preload:
- `deepseek`
- `mistral`
- `phi`

Models run on `http://localhost:11434` unless changed.

---

## 🛠️ Recommended Tooling

- Postgres (via pgAdmin or CLI)
- VS Code (with Pylance + Tailwind IntelliSense)
- Docker Desktop (optional)
- Makefiles or `.task` runners if desired

---

## 🔄 Sync Notes

- Frontend uses `getArticles`, `getTimeline`, `getAnalysis`
- Backend must expose: `/ingest`, `/timeline/:topic_id`, `/investigation/:article_id`
- Agents must return valid JSON per schema

For any errors, check `uvicorn` logs and DeepSeek response logs.