# Clarity Reports - Setup Guide

## 1. Prerequisites
Before setting up Clarity Reports, ensure the following dependencies are installed:
- **Python 3.9+**
- **pip** (Python package manager)
- **Virtualenv** (for environment isolation)
- **PostgreSQL 14+** (database storage)
- **Git** (for version control)
- **Docker (optional)** (for containerized deployment)

---

## 2. Clone the Repository
```bash
git clone https://github.com/your_repo/clarity_reports.git
cd clarity_reports
```

---

## 3. Set Up Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```
(For Windows, use `venv\Scripts\activate` instead.)

---

## 4. Install Dependencies
```bash
pip install -r docs/requirements.txt
```

---

## 5. Configure Environment Variables
Create a `.env` file in the root directory and add the following:
```plaintext
DATABASE_URL=postgresql://clarity_user:your_password@localhost:5432/clarity_reports
SECRET_KEY=your_secret_key
NEWS_API_KEY=your_news_api_key
```

---

## 6. Set Up PostgreSQL Database
```bash
sudo -u postgres psql
CREATE DATABASE clarity_reports;
CREATE USER clarity_user WITH ENCRYPTED PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE clarity_reports TO clarity_user;
```

---

## 7. Apply Database Migrations
```bash
alembic upgrade head
```

---

## 8. Run the FastAPI Server
```bash
uvicorn backend.api.main:app --host 0.0.0.0 --port 8000 --reload
```

The server will be accessible at: `http://localhost:8000`

---

## 9. Verify Installation
To confirm everything is running correctly, open your browser and go to:
```bash
http://localhost:8000/docs
```
This will open the Swagger API documentation.

---

🚀 **Your system is now set up and ready to use!**
