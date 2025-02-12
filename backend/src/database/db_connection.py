import os
import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# ✅ Load environment variables from backend/.env
dotenv_path = os.path.join(os.path.dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

# ✅ Retrieve database URL or use default
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL is not set. Check your .env file!")

# ✅ Create database engine
engine = create_engine(DATABASE_URL)

# ✅ Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ Import models to ensure database tables are created
try:
    from models.article import Base  # ✅ FIXED: Removed `src.` from import
except ModuleNotFoundError:
    from backend.src.models.article import Base  # ✅ Fallback if `src` is required

# ✅ Ensure tables are created if they don’t exist
try:
    Base.metadata.create_all(bind=engine)
    logging.info("✅ Database tables created successfully")
except Exception as e:
    logging.error(f"❌ Failed to create tables: {e}")

# ✅ Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
