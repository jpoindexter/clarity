import os
import sys
from pathlib import Path
from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from alembic import context

# ✅ Debugging Output
print(f"🔥 ALEMBIC DEBUG - SYS.PATH BEFORE: {sys.path}")

# ✅ Ensure Python Can Find `backend/`
BASE_DIR = Path(__file__).resolve().parents[2]
BACKEND_DIR = BASE_DIR / "backend"

if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))  # Ensures backend/ is first
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))  # Ensures project root is included

print(f"🔥 ALEMBIC DEBUG - SYS.PATH AFTER: {sys.path}")

# ✅ Load Alembic Config
config = context.config

# ✅ Get DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL") or config.get_main_option("sqlalchemy.url")

if not DATABASE_URL or DATABASE_URL == "${DATABASE_URL}":
    raise ValueError(
        "❌ ERROR: DATABASE_URL is not set. Export it or check alembic.ini.")

# ✅ Configure Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ✅ Import Base Model
try:
    from backend.models import Base
    print("✅ SUCCESS: Imported `backend.models`")
except ImportError as e:
    print(f"❌ DEBUG: sys.path={sys.path}")  # Print paths for debugging
    raise ImportError("❌ ERROR: Could not import `backend.models`. "
                      "Ensure PYTHONPATH is correctly set.") from e

# ✅ Set `target_metadata`
target_metadata = Base.metadata

# 🔹 **Offline Migrations**


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# 🔹 **Online Migrations**


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = create_engine(DATABASE_URL, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


# ✅ Ensure the Correct Mode is Used
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
