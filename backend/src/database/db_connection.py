from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models.article import Base  # Import Article model

DATABASE_URL = "sqlite:///./test.db"  # Change if using PostgreSQL/MySQL

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)
