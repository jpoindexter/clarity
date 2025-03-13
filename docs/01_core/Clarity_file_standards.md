/clarity/                   # 🚀 Root of the entire project (Frontend + Backend + Docs)
│
├── /backend/               # 🏗️ FastAPI Backend (API + Services + DB)
│   ├── /api/               # 📡 API Endpoints
│   │   ├── __init__.py
│   │   ├── main.py         # 🚀 Main FastAPI app entry point (Uvicorn runs this)
│   │   ├── router.py       # 🌉 Central router that includes all endpoints
│   │   ├── v1/             # 📌 Versioned API (future-proofing)
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/  # 🏗️ API Route Handlers
│   │   │   │   ├── __init__.py
│   │   │   │   ├── analyze.py
│   │   │   │   ├── contradiction.py
│   │   │   │   ├── news.py
│   │   │   │   ├── search.py
│   │   │   │   └── articles.py
│   │   │   └── dependencies.py # 🛠️ Common dependencies for endpoints
│   │   └── middleware.py   # 🔄 Request handling middleware
│   │
│   ├── /services/          # 🛠️ Business Logic Layer (Processes Data, Calls APIs)
│   │   ├── __init__.py
│   │   ├── contradiction_service.py # 📊 Handles contradiction analysis
│   │   ├── financial_analysis.py    # 💰 FinBERT sentiment analysis
│   │   ├── text_analysis.py         # 📖 NLP/Text Processing Logic
│   │   ├── fetch_news.py            # 📰 Fetch & Process News Data
│   │   ├── data_cleaning.py         # 🧹 Preprocessing / Cleaning
│   │   └── ml_models.py             # 🧠 Calls AI models for processing
│   │
│   ├── /models/             # 🏛️ Pydantic + SQLAlchemy Data Models
│   │   ├── __init__.py
│   │   ├── article.py
│   │   ├── contradiction.py
│   │   ├── news.py
│   │   ├── user.py
│   │   └── metadata.py
│   │
│   ├── /schemas/            # 📝 Pydantic Request/Response Models
│   │   ├── __init__.py
│   │   ├── article.py
│   │   ├── contradiction.py
│   │   ├── news.py
│   │   ├── user.py
│   │   └── metadata.py
│   │
│   ├── /crud/               # 🔍 Database CRUD Operations
│   │   ├── __init__.py
│   │   ├── articles.py
│   │   ├── contradictions.py
│   │   ├── news.py
│   │   ├── users.py
│   │   └── metadata.py
│   │
│   ├── /database/           # 🗄️ Database Connection & Migrations
│   │   ├── __init__.py
│   │   ├── db_connection.py # 🎛️ Main DB connection
│   │   ├── db_helper.py     # 🛠️ Helper functions for DB queries
│   │   ├── migrations/      # 📜 Alembic Migrations
│   │   │   ├── env.py
│   │   │   ├── README
│   │   │   ├── script.py.mako
│   │   │   └── versions/
│   │   ├── alembic.ini
│   │   └── seed_db.py       # 🌱 Seed Initial Data
│   │
│   ├── /ai_models/          # 🤖 AI Model Checkpoints
│   │   ├── __init__.py
│   │   ├── mistral/
│   │   ├── deepseek/
│   │   ├── ollama/
│   │   ├── finbert/
│   │   └── embeddings/
│   │
│   ├── /config/             # ⚙️ Configuration & Secrets Management
│   │   ├── __init__.py
│   │   ├── settings.py      # 🛠️ App Settings (dotenv, env variables)
│   │   ├── logger.py        # 📝 Logging Config
│   │   ├── security.py      # 🔐 API Keys / Auth
│   │   └── constants.py     # 📌 Hardcoded Constants
│   │
│   ├── /logs/               # 📝 Logs (Centralized)
│   │   ├── backend.log
│   │   ├── startup/
│   │   │   ├── 2025-02-13_10-19-22.log
│   │   └── errors/
│   │       ├── api_errors.log
│   │       ├── db_errors.log
│   │       └── ai_errors.log
│   │
│   ├── __init__.py
│   ├── main.py              # 🚀 Entrypoint for FastAPI
│   ├── start.sh             # 🏁 Script to Start Backend
│   ├── requirements.txt     # 📜 Python Dependencies
│   ├── pytest.ini           # 🧪 Pytest Configuration
│   ├── detect_circular_imports.py  # 🔄 Import Debugging
│   └── README.md
│
└── /tests/                  # 🧪 Unit + Integration Tests
    ├── __init__.py
    ├── test_health.py
    ├── test_articles.py
    ├── test_contradictions.py
    ├── test_db.py
    ├── test_ml_models.py
    ├── test_endpoints.py
    ├── test_security.py
    └── /api/
        ├── test_analyze.py
        ├── test_articles.py
        ├── test_contradiction.py
        ├── test_news.py
        └── test_search.py