import os
from dotenv import load_dotenv
load_dotenv()
import logging
import time  # ✅ Added missing import
from contextlib import contextmanager
from sqlalchemy import create_engine, inspect, event
from sqlalchemy.orm import sessionmaker, scoped_session
from backend.models import Base
  
# ✅ Configure Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
  
# ✅ Load DATABASE_URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    logger.error("❌ DATABASE_URL is not set. Please define it in the environment.")
    raise ValueError("❌ DATABASE_URL is not set. Please define it in the environment.")

# ✅ Configure PostgreSQL engine with efficient pooling
engine = create_engine(
    DATABASE_URL,
    pool_size=10,          # ✅ Maintain up to 10 active connections
    max_overflow=20,       # ✅ Allow 20 additional temporary connections
    pool_timeout=30,       # ✅ Max time to wait for connection
    pool_recycle=1800,     # ✅ Prevents stale connections
    echo=False,            # ✅ Disables excessive SQL logging
    connect_args={"connect_timeout": 10}  # ✅ Ensure timeout handling
)

# ✅ Add support for retry logic to handle transient DB failures


def with_retry(session_func, retries=3):
    """Retries a database session function if it fails due to a transient error."""
    for attempt in range(retries):
        try:
            return session_func()
        except Exception as e:
            logger.warning(
                f"❌ Database operation failed, retrying ({attempt+1}/{retries}): {e}"
            )
            if attempt == retries - 1:
                raise
            time.sleep(2 ** attempt)  # Exponential backoff




# ✅ Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Session = scoped_session(SessionLocal)


# ✅ Ensure tables exist before first request
try:
    with engine.connect() as connection:
        inspector = inspect(connection)
        tables_to_check = ["articles", "users", "summarized_articles"]  # ✅ Ensure all tables are checked
        for table in tables_to_check:
            if not inspector.has_table(table):  # ✅ Fix for has_table()
                logger.info(f"Creating missing table: {table}")
                Base.metadata.create_all(bind=engine)
except Exception as e:
    logger.error(f"❌ Database Initialization Failed: {e}")


# ✅ Dependency Injection for FastAPI
def get_db():
    """✅ Provide database session with proper cleanup."""
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.error(f"❌ Database Session Error: {e}")
    finally:
        db.close()  # ✅ Ensuring session closes properly


# ✅ Context manager for manual session handling (if needed outside FastAPI)
@contextmanager
def get_session():
    """✅ Provides a session and ensures it closes properly."""
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        logger.error(f"❌ Session Transaction Failed: {e}")
        raise e
    finally:
        db.close()
