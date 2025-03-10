import os
import sys
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

# ✅ Fix `ModuleNotFoundError` by adding backend to sys.path
BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../..")
)
sys.path.insert(0, BASE_DIR)  # ✅ This **must** come **before** importing backend

# ✅ Import AFTER sys.path modification (Fixes `E402`)
from backend.src.database.db_connection import Base  # ✅ Ensure all models are included

# ✅ Load Alembic config
config = context.config

# ✅ Load logging configuration
if config.config_file_name:
    fileConfig(config.config_file_name)

# ✅ Ensure DATABASE_URL is set
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    config.get_main_option("sqlalchemy.url")
)

# ✅ Correct potential database name typo
if DATABASE_URL and "clarrity" in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("clarrity", "clarity")

# ✅ Validate DATABASE_URL exists
if not DATABASE_URL:
    raise ValueError(
        "❌ ERROR: DATABASE_URL is missing! Define it in the environment "
        "or alembic.ini"
    )

# ✅ Set the database URL dynamically
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# ✅ Set target metadata for migrations
target_metadata = Base.metadata


def run_migrations_offline():
    """🔹 Run migrations in 'offline' mode (without a live database connection)."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """🔹 Run migrations in 'online' mode (with a live database connection)."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


# ✅ Determine migration mode
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
