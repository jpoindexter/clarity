import os
import shutil
import subprocess

# 📌 Directories to reset
DIRECTORIES = [
    "backend/api",
    "backend/crud",
    "backend/schemas",
    "backend/database"
]

# 📌 Backup Directory (before deleting)
BACKUP_DIR = "backend_backup"

def backup_files():
    """Backup existing files before deletion."""
    if os.path.exists(BACKUP_DIR):
        shutil.rmtree(BACKUP_DIR)
    os.makedirs(BACKUP_DIR, exist_ok=True)
    for directory in DIRECTORIES:
        if os.path.exists(directory):
            shutil.copytree(directory, os.path.join(BACKUP_DIR, os.path.basename(directory)))

def delete_files():
    """Delete broken backend files."""
    for directory in DIRECTORIES:
        if os.path.exists(directory):
            shutil.rmtree(directory)

def recreate_structure():
    """Rebuild clean backend structure with correct imports."""
    # 📌 Recreating API structure
    os.makedirs("backend/api/endpoints", exist_ok=True)
    os.makedirs("backend/crud", exist_ok=True)
    os.makedirs("backend/schemas", exist_ok=True)
    os.makedirs("backend/database", exist_ok=True)

    # ✅ main.py (entry point)
    with open("backend/api/main.py", "w") as f:
        f.write('''from fastapi import FastAPI
from backend.api.router import include_routers

app = FastAPI()

# ✅ Ensure routes are registered
include_routers(app)

@app.get("/")
def root():
    return {"message": "Clarity API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}
''')

    # ✅ router.py (central API router)
    with open("backend/api/router.py", "w") as f:
        f.write('''from fastapi import APIRouter
from backend.api.endpoints.news import router as news_router
from backend.api.endpoints.articles import router as articles_router
from backend.api.endpoints.search import router as search_router
from backend.api.endpoints.contradictions import router as contradictions_router

router = APIRouter()

# ✅ Correct API paths
router.include_router(news_router, prefix="/api/news", tags=["news"])
router.include_router(articles_router, prefix="/api/articles", tags=["articles"])
router.include_router(search_router, prefix="/api/search", tags=["search"])
router.include_router(contradictions_router, prefix="/api/contradictions", tags=["contradictions"])

def include_routers(app):
    app.include_router(router)
''')

    # ✅ news.py (endpoint)
    with open("backend/api/endpoints/news.py", "w") as f:
        f.write('''from fastapi import APIRouter, Depends
from backend.schemas.news import NewsSchema
from backend.crud.news import news_crud
from backend.database.db_connection import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/news", tags=["news"])

@router.get("/", response_model=list[NewsSchema])
def fetch_news(db: Session = Depends(get_db)):
    return news_crud.get_all_news(db)
''')

    # ✅ news_crud.py (CRUD logic)
    with open("backend/crud/news.py", "w") as f:
        f.write('''from sqlalchemy.orm import Session
from backend.schemas.news import NewsSchema
from backend.models.news import News

class NewsCRUD:
    def get_all_news(self, db: Session):
        return db.query(News).all()

news_crud = NewsCRUD()
''')

    # ✅ schemas/news.py (Pydantic models)
    with open("backend/schemas/news.py", "w") as f:
        f.write('''from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NewsSchema(BaseModel):
    id: int
    title: str
    content: str
    source: str
    url: str
    published_at: Optional[datetime]
''')

    # ✅ database/db_connection.py (Fix `get_db`)
    with open("backend/database/db_connection.py", "w") as f:
        f.write('''from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
''')

def run_lint_fix():
    """Run Flake8 & auto-fix formatting issues."""
    print("\n🔧 Running Flake8 & Auto-fixing formatting issues...\n")
    subprocess.run(["black", "backend"], check=False)
    subprocess.run(["flake8", "backend"], check=False)

def run_uvicorn_test():
    """Start the server to validate everything works."""
    print("\n🚀 Running server test...\n")
    subprocess.run(["uvicorn", "backend.api.main:app", "--reload"], check=False)

def main():
    print("\n🚀 Resetting Backend...\n")
    backup_files()
    delete_files()
    recreate_structure()
    run_lint_fix()
    print("\n✅ Backend reset complete! Restarting API...\n")
    run_uvicorn_test()

if __name__ == "__main__":
    main()