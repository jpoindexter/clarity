import os
import importlib
import sys
import traceback
from datetime import datetime
from pathlib import Path

# Define the correct project root and log directory
PROJECT_ROOT = "/Users/jasonpoindexter/Documents/GitHub/clairity/src"
LOG_DIR = "/Users/jasonpoindexter/Documents/GitHub/clairity/logs/scan"

# Ensure the log directory exists
Path(LOG_DIR).mkdir(parents=True, exist_ok=True)

# Generate a timestamped log file
log_filename = f"debug_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
LOG_FILE = os.path.join(LOG_DIR, log_filename)

# Set Python Path dynamically
sys.path.insert(0, PROJECT_ROOT)

# Modules to check
modules_to_check = [
    "api.main",
    "api.endpoints.news",
    "api.endpoints.articles",
    "database.db_connection",
    "database.crud.news",
    "models.article",
    "schemas.articles",
]


def log_message(message):
    """Write message to log file and print it."""
    with open(LOG_FILE, "a") as log:
        log.write(message + "\n")
    print(message)


def check_missing_init():
    """Check for missing __init__.py files."""
    log_message("\n🔍 Checking for missing __init__.py files...")
    missing_files = []

    for root, dirs, files in os.walk(PROJECT_ROOT):
        if "__pycache__" in root:
            continue  # Skip pycache folders
        if "__init__.py" not in files:
            missing_files.append(root + "/__init__.py")

    if missing_files:
        log_message("❌ Missing __init__.py files detected!\n")
        for file in missing_files:
            log_message(f"  - {file}")
        log_message("\n⚠️ Fix: Run this to create missing files:")
        log_message("  find src -type d -exec touch {}/__init__.py \\;\n")
    else:
        log_message("✅ All required __init__.py files are present.\n")


def check_imports():
    """Check import errors."""
    log_message("\n🔍 Checking imports...\n")
    for module in modules_to_check:
        try:
            importlib.import_module(module)
            log_message(f"✅ {module} - OK")
        except ModuleNotFoundError as e:
            log_message(f"❌ {module} - {e}")
        except Exception as e:
            log_message(f"❌ {module} - Import Error!\n{traceback.format_exc()}")


def check_circular_imports():
    """Check for circular imports (short summary)."""
    log_message("\n🔍 Checking for circular imports...\n")
    try:
        result = os.popen(f"python -m trace --trace {PROJECT_ROOT}/api/main.py").read()
        if "ImportError" in result or "cannot import" in result:
            log_message("❌ Circular import detected!")
        else:
            log_message("✅ No circular imports detected.\n")
    except Exception as e:
        log_message(f"❌ Circular Import Check Failed: {e}")


def test_uvicorn():
    """Run a quick test to see if Uvicorn can start."""
    log_message("\n🚀 Running Uvicorn test...\n")
    try:
        os.system("uvicorn api.main:app --port 9000 --reload --no-access-log")
    except Exception as e:
        log_message(f"❌ Uvicorn failed to start: {e}")


if __name__ == "__main__":
    # Clear old log file
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

    log_message(f"\n🚀 Running Debug Script at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    log_message(f"📂 Project Root: {PROJECT_ROOT}")
    log_message(f"📂 Log File: {LOG_FILE}")

    check_missing_init()
    check_imports()
    check_circular_imports()
    test_uvicorn()

    log_message("\n✅ Debugging complete! Check the log file for full details.")
