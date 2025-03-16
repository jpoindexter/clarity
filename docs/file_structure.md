# Clarity Reports - Project File Structure

## 1. Overview
This document defines the industry-standard file structure for Clarity Reports. It ensures maintainability, scalability, and modularity.

---

## 2. Directory Layout

```
clarity_reports/
│── backend/               # Core backend services (FastAPI)
│   ├── api/               # API endpoints
│   ├── models/            # Database models (SQLAlchemy)
│   ├── services/          # Business logic (AI processing, credibility scoring)
│   ├── utils/             # Helper functions and utilities
│   ├── main.py            # FastAPI entry point
│── data/                  # Storage for raw and processed news data
│── reports/               # Generated AI-powered PDF reports
│── docs/                  # Project documentation
│   ├── README.md          # High-level project summary
│   ├── project_overview.md # Business model and execution plan
│   ├── architecture.md    # System architecture and dependencies
│   ├── api_documentation.yaml # OpenAPI standard for API endpoints
│   ├── setup_guide.md     # Installation and setup instructions
│   ├── requirements.txt   # List of Python dependencies
│   ├── deployment_guide.md # Deployment procedures
│   ├── security_best_practices.md # Security and compliance best practices
│   ├── versioning.md      # Change log and version control strategy
│   ├── file_structure.md  # This document
│── scripts/               # Automation scripts, including web scrapers, scheduled AI processing tasks, and data ingestion workflows.
│── venv/                  # Virtual environment for Python dependencies
│── requirements.txt        # Global dependencies list
│── .gitignore              # Specifies which files should be ignored in version control. Typically includes `.env`, `venv/`, `__pycache__/`, logs, and other sensitive or unnecessary files.
│── README.md               # Main project readme
```

---

## 3. Explanation of Key Directories

- **backend/** → FastAPI-based backend API with AI integration.
- **data/** → Stores raw news data before processing.
- **reports/** → Stores AI-generated PDF reports.
- **docs/** → Contains all project documentation.
- **scripts/** → Houses automation scripts for scraping and AI task scheduling.
- **venv/** → Virtual environment for dependency isolation.

---

## 4. Best Practices

- Keep all **API logic inside `backend/api/`** to maintain separation of concerns.
- Store **all data models in `backend/models/`** for database consistency.
- Write **reusable AI processing logic inside `backend/services/`** for modularity.
- Place **all automation scripts in `scripts/`** to avoid cluttering the backend.
- Never store **API keys, credentials, or secrets in the codebase**—use `.env` files.
- Ensure the `.env` file is stored in the root directory and contains all sensitive credentials, such as API keys and database URLs. This file should never be committed to version control.

🚀 **This structure is designed for maximum efficiency, scalability, and maintainability.**
