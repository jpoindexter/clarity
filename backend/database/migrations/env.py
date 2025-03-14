import sys
import os
from pathlib import Path
from sqlalchemy import create_engine, pool
from sqlalchemy.engine.url import make_url
from alembic import context
print("ALEMBIC DEBUG - SYS.PATH:", sys.path)
from backend.models import Base  # ✅ Corrected Import Path

# ✅ Fix Import Path Issue (Ensures `backend/` is available before imports)
BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BASE_DIR / "backend"))

# ✅ Debugging Output (Only use for troubleshooting)
print("SYS.PATH DEBUG:", sys.path)


# ✅ Load Alembic configuration
config = context.config

# ✅ Get the correct database URL from .env or alembic.ini
DATABASE_URL = os.getenv("DATABASE_URL") or config.get_main_option(
    "sqlalchemy.url"
)

if not DATABASE_URL or DATABASE_URL == "${DATABASE_URL}":
    raise ValueError(
        "❌ ERROR: DATABASE_URL is not set in the environment or alembic.ini"
    )

# ✅ Ensure DATABASE_URL is correctly formatted
DATABASE_URL = str(make_url(DATABASE_URL))

# ✅ Create an engine with proper pooling
connectable = create_engine(
    DATABASE_URL,
    poolclass=pool.NullPool,
    echo=True,
    future=True,
)

# ✅ Set target metadata for autogeneration
target_metadata = Base.metadata


# 🔹 **Offline Mode Migration**


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


# 🔹 **Online Mode Migration**


def run_migrations_online():
    """Run migrations in 'online' mode."""
    try:
        with connectable.connect() as connection:
            context.configure(
                connection=connection,
                target_metadata=target_metadata,
            )

            with context.begin_transaction():
                context.run_migrations()

    except Exception as e:
        raise RuntimeError(
            f"❌ ERROR: Unable to connect to the database. "
            f"Check database settings.\n\n{e}"
        )


# ✅ Ensure the correct migration mode is executed


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

# ✅ Added a newline at the end to fix Flake8 warning (W292)
