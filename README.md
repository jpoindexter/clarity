# clarity

AI-powered intelligence and narrative analysis platform. Detects contradictions, narrative shifts, and misinformation in real-time data streams. Built for independent researchers and anyone tracking information integrity across sources.

## What it does

- Ingests news and RSS feeds continuously
- Runs contradiction detection across articles and sources
- Flags narrative manipulation and misinformation patterns
- Adaptive learning difficulty for different research contexts
- FastAPI backend with local LLM inference via Ollama

## Stack

**Backend**
- FastAPI
- PostgreSQL + SQLAlchemy
- Alembic (migrations)
- Ollama (local LLMs: Mistral, DeepSeek, LLaMA)
- Whisper (speech-to-text input)

**Frontend**
- Next.js (in progress)

## Setup

```bash
# Copy env template
cp .env.example .env

# Run migrations
alembic upgrade head

# Start backend
uvicorn backend.main:app --reload
```

Requires Python 3.11+ and a running PostgreSQL instance. Ollama must be installed and running locally with at least one supported model pulled.

## Project structure

```
backend/    FastAPI app, routes, AI pipeline, database models
docs/       Architecture, vision, and roadmap documentation
alembic/    Database migration config
```

## Status

MVP. Backend functional, frontend rebuild in progress.
