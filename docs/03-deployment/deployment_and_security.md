# Clarity – Deployment & Security Guide

This document outlines how to deploy and secure Clarity in a development or demo environment. Clarity is an ephemeral, AI-powered research tool — no accounts, no user sessions, and no sensitive data storage.

---

## Deployment Options

### 1. Local Development (Recommended for Demo)
- Clone the repo and run locally:
  ```bash
  git clone https://github.com/your_repo/clarity.git
  cd clarity
  docker-compose up --build
  ```

- Access the app at: `http://localhost:3000`

- Backend API (FastAPI): `http://localhost:8000`
- Frontend (Next.js): `http://localhost:3000`
- Ollama models (optional): `http://localhost:11434`

---

### 2. Vercel + Fly.io Hybrid (Cloud Demo)
- Deploy frontend to Vercel for global speed
- Deploy backend to Fly.io or Railway
- Make sure `NEXT_PUBLIC_API_URL` is set in Vercel env vars
- Protect API endpoints behind rate-limiting if needed

---

## Secrets & Environment Config

`.env` variables required:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/clarity
SECRET_KEY=your_secret_key
NEXT_PUBLIC_API_URL=http://localhost:8000
```

No API keys are needed unless using external RSS services (e.g. GNews, Currents).

---

## Security Philosophy

- ✅ No user accounts → no PII exposure
- ✅ No long-term session storage
- ✅ No external social ingest (e.g. Twitter, Reddit)
- ✅ Local AI = no outbound API calls to OpenAI, Anthropic, etc.
- ✅ Ingest pipeline uses only public, licensed, or RSS-accessible sources

---

## Hardening for Production (Post-MVP)

If you plan to deploy Clarity long-term or publicly:
- Use HTTPS reverse proxy (e.g. Nginx)
- Monitor Docker containers with health checks
- Secure Postgres with role-based auth
- Remove all shell access to backend containers
- Consider `robots.txt` and caching if exposed online

---

## Logging

- Minimal logging in production
- Log ingestion errors and AI failures only
- Future option: log manipulation detection anomalies (optional)

---

## Backup

- Use pg_dump for backing up articles if needed
- Can easily re-ingest narratives on demand using keyword or query