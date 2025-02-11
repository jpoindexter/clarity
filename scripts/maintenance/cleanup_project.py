import os
import re
import shutil
from pathlib import Path

# Define the project root
PROJECT_ROOT = "/Users/jasonpoindexter/Documents/GitHub/clairity/src"
LOG_DIR = "/Users/jasonpoindexter/Documents/GitHub/clairity/logs"

# File extensions to ignore
SAFE_EXTENSIONS = {".py", ".json", ".env", ".md"}

# Patterns to detect backup/old files
JUNK_PATTERNS = [
    r".*(_backup|_old|_copy|_temp)\.py$",  # Backup scripts
    r".*\.(log|tmp|bak)$",  # Log/temp/backup files
    r"^debug_.*\.txt$",  # Debug log files
]

def find_empty_folders():
    """Finds empty folders that can be deleted."""
    empty_dirs = []
    for root, dirs, files in os.walk(PROJECT_ROOT, topdown=False):
        for d in dirs:
            full_path = os.path.join(root, d)
            if not os.listdir(full_path):  # If the folder is empty
                empty_dirs.append(full_path)
    return empty_dirs

def find_orphaned_files():
    """Finds Python files not imported anywhere in the project."""
    all_py_files = set()
    imported_modules = set()

    # Collect all .py files
    for root, _, files in os.walk(PROJECT_ROOT):
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                all_py_files.add(full_path)

    # Scan for imports inside Python files
    for py_file in all_py_files:
        with open(py_file, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                match = re.match(r"^\s*(from|import) ([a-zA-Z0-9_\.]+)", line)
                if match:
                    imported_modules.add(match.group(2).replace(".", "/") + ".py")

    # Find orphaned .py files (not imported anywhere)
    orphaned_files = [f for f in all_py_files if not any(mod in f for mod in imported_modules)]
    return orphaned_files

def find_large_files(size_mb=10):
    """Finds large files that may not be necessary."""
    large_files = []
    for root, _, files in os.walk(PROJECT_ROOT):
        for file in files:
            full_path = os.path.join(root, file)
            if os.path.getsize(full_path) > size_mb * 1024 * 1024:  # Convert MB to bytes
                large_files.append(full_path)
    return large_files

def find_junk_files():
    """Finds junk files based on patterns."""
    junk_files = []
    for root, _, files in os.walk(PROJECT_ROOT):
        for file in files:
            if any(re.match(pattern, file) for pattern in JUNK_PATTERNS):
                junk_files.append(os.path.join(root, file))
    return junk_files

def generate_cleanup_report():
    """Generates a report of files and folders to clean up."""
    print("\n🚀 Running Cleanup Report...\n")

    empty_folders = find_empty_folders()
    orphaned_files = find_orphaned_files()
    large_files = find_large_files()
    junk_files = find_junk_files()

    print("\n🔍 **Empty Folders:**")
    for folder in empty_folders:
        print(f"   🗂️  {folder}")

    print("\n🔍 **Orphaned Python Files (Not Imported Anywhere):**")
    for orphan in orphaned_files:
        print(f"   📄  {orphan}")

    print("\n🔍 **Large Files (>10MB):**")
    for large in large_files:
        print(f"   🛑  {large} ({os.path.getsize(large) / 1024 / 1024:.2f} MB)")

    print("\n🔍 **Junk Files (Temp, Logs, Backups):**")
    for junk in junk_files:
        print(f"   🗑️  {junk}")

    print("\n✅ **Review this list and confirm before deleting any files.**")

def delete_files(files):
    """Deletes files from the list."""
    for file in files:
        try:
            os.remove(file)
            print(f"🗑️ Deleted: {file}")
        except Exception as e:
            print(f"⚠️ Could not delete {file}: {e}")

def delete_folders(folders):
    """Deletes folders from the list."""
    for folder in folders:
        try:
            shutil.rmtree(folder)
            print(f"🗂️ Deleted folder: {folder}")
        except Exception as e:
            print(f"⚠️ Could not delete {folder}: {e}")

if __name__ == "__main__":
    generate_cleanup_report()

    confirm = input("\n⚠️ Do you want to delete these files? (yes/no): ").strip().lower()
    if confirm == "yes":
        delete_files(find_orphaned_files() + find_junk_files() + find_large_files())
        delete_folders(find_empty_folders())
        print("\n✅ Cleanup complete!")
    else:
        print("\n🚀 No changes made. Review the report and run again if needed.")
