import os
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

from backend.src.database.db_connection import \
    Base  # ✅ Ensure all models are included

# ✅ Load Alembic config
config = context.config

# ✅ Load logging configuration
if config.config_file_name:
    fileConfig(config.config_file_name)

# ✅ Ensure DATABASE_URL is set and corrected
DATABASE_URL = os.getenv("DATABASE_URL", config.get_main_option("sqlalchemy.url"))

# ✅ Fix the database name if incorrectly set
if DATABASE_URL and "clarrity" in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("clarrity", "clarity")

# ✅ Validate DATABASE_URL exists
if not DATABASE_URL:
    raise ValueError(
        "❌ ERROR: DATABASE_URL is not set. Define it in the environment or alembic.ini"
    )

# ✅ Set the database URL dynamically
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# ✅ Set target metadata for autogeneration
target_metadata = Base.metadata


def run_migrations_offline():
    """🔹 Run migrations in 'offline' mode (no database connection)."""
    context.configure(
        url=DATABASE_URL, target_metadata=target_metadata, literal_binds=True
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


# ✅ Determine if running offline or online
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
