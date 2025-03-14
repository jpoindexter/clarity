#!/bin/bash

# ✅ Get the absolute project root directory
PROJECT_ROOT=$(dirname "$(realpath "$0")")

# ✅ Set PYTHONPATH dynamically
export PYTHONPATH="$PROJECT_ROOT/backend"

# ✅ Activate the virtual environment
source "$PROJECT_ROOT/venv/bin/activate"

# ✅ Print debug information
echo "Using PYTHONPATH: $PYTHONPATH"
echo "Running Alembic with arguments: $@"

# ✅ Run Alembic with the given arguments
alembic "$@"