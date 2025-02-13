import logging
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# ✅ Import Base metadata so Alembic can detect models
from src.database.db_connection import Base  

# Alembic Config object, which provides access to values within the .ini file in use
config = context.config

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ✅ Set the correct metadata reference
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    try:
        url = config.get_main_option("sqlalchemy.url")
        context.configure(
            url=url,
            target_metadata=target_metadata,
            literal_binds=True,
            dialect_opts={"paramstyle": "named"},
        )

        with context.begin_transaction():
            context.run_migrations()
        print("✅ Offline migrations completed successfully.")

    except Exception as e:
        print(f"❌ Error running offline migrations: {e}")  # ✅ Fixed f-string formatting

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    try:
        connectable = engine_from_config(
            config.get_section(config.config_ini_section, {}),
            prefix="sqlalchemy.",
            poolclass=pool.NullPool,
        )

        with connectable.connect() as connection:
            context.configure(
                connection=connection, target_metadata=target_metadata
            )

            with context.begin_transaction():
                context.run_migrations()
            print("✅ Online migrations completed successfully.")

    except Exception as e:
        print(f"❌ Error running online migrations: {e}")  # ✅ Fixed f-string formatting

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
