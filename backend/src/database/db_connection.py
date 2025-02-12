from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://jpoindexter:dontforgetme@localhost/Clarity")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ Import models to ensure database tables are created
from backend.src.models.article import Base  

# ✅ Ensure tables are created if they don’t exist
Base.metadata.create_all(bind=engine)

# ✅ Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
