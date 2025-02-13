from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://jpoindexter:dontforgetme@localhost:5432/clarity"

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        print("✅ Database connection successful!")
except Exception as e:
    print(f"❌ Database connection failed: {e}")
