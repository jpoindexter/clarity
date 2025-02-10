from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from src.database.models.article import Base  # ✅ Correct import path

DATABASE_URL = "sqlite:///./test.db"  # Change if using PostgreSQL/MySQL

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = scoped_session(SessionLocal)

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# ✅ Add this function to allow dependency injection in FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
