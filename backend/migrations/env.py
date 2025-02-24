import os
from logging.config import fileConfig

from sqlalchemy import create_engine, pool
from sqlalchemy.dialects import registry

# Fix for "Can't load plugin: sqlalchemy.dialects:driver"
registry.register("postgresql.psycopg2", "sqlalchemy.dialects.postgresql.psycopg2", "PGDialect_psycopg2")

from sqlalchemy.engine.url import make_url
from alembic import context

# Load Alembic configuration
config = context.config

# Set up logging
if config.config_file_name:
    fileConfig(config.config_file_name)

# Ensure the correct database URL is used
DATABASE_URL = config.get_main_option("sqlalchemy.url")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in alembic.ini")

# Convert to a SQLAlchemy URL object to prevent misconfiguration
DATABASE_URL = str(make_url(DATABASE_URL))

# Import models for auto-migration
from backend.src.models import Base  # Ensure this matches your actual model import

# Set target metadata for autogeneration
target_metadata = Base.metadata

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

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    from sqlalchemy.dialects import registry

    # Explicitly register the dialect (fixes NoSuchModuleError)
    registry.register("postgresql.psycopg2", "sqlalchemy.dialects.postgresql.psycopg2", "PGDialect_psycopg2")

    # Ensure the engine is created with proper pooling
    connectable = create_engine(
        DATABASE_URL.replace("postgresql+psycopg2", "postgresql"), 
        poolclass=pool.NullPool, 
        echo=True
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()