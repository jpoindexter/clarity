import os
import shutil
import logging
import difflib
from datetime import datetime

# Define Paths
FRONTEND_DIR = "frontend/components"
LOGS_DIR = "logs/scan"
LOG_FILE = os.path.join(LOGS_DIR, f"frontend_fix_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")
MERGED_LOG = os.path.join(LOGS_DIR, "merged_files.log")

# Ensure logs directory exists
os.makedirs(LOGS_DIR, exist_ok=True)

# Configure logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Define correct structure
STRUCTURE = {
    "UI": ["Button.js", "Modal.js", "index.js"],
    "News": ["ArticleCard.js", "NewsList.js", "index.js"],
    "Filters": ["SearchBar.js", "SourceDropdown.js", "DateFilter.js", "index.js"],
    "Graph": ["NewsGraph.js", "index.js"],
    "Common": ["Layout.js", "Header.js", "Footer.js", "index.js"]
}

def ensure_directory_exists(path):
    """Creates a directory if it does not exist"""
    if not os.path.exists(path):
        os.makedirs(path)
        logging.info(f"[CREATED DIR] {path}")

def scan_frontend_files():
    """Scans frontend/components/ for existing files, ignoring node_modules/"""
    file_locations = {}
    for root, _, files in os.walk("frontend"):
        if "node_modules" in root or "/." in root:
            continue

        for file in files:
            if file.endswith((".js", ".tsx")):
                file_path = os.path.join(root, file)
                if file not in file_locations:
                    file_locations[file] = file_path
                else:
                    logging.warning(f"[DUPLICATE] {file} found in multiple locations: {file_locations[file]} and {file_path}")
    return file_locations

def find_closest_match(filename, target_list):
    """Finds the closest match for a filename in the target list using fuzzy comparison."""
    match = difflib.get_close_matches(filename, target_list, n=1, cutoff=0.7)
    return match[0] if match else None

def merge_files(source, target):
    """Merges two files by appending the content of source to target."""
    try:
        with open(target, "a") as target_file, open(source, "r") as source_file:
            target_file.write("\n// ---- Merged Content ----\n")
            target_file.write(source_file.read())

        os.remove(source)  # Delete the original after merging
        logging.info(f"[MERGED] {source} → {target}")
        return True
    except Exception as e:
        logging.error(f"[ERROR] Merging {source} failed: {e}")
        return False

def move_and_fix_files(file_locations):
    """Moves, merges, renames similar files, and deletes bad ones."""
    merged_files = []

    for folder, files in STRUCTURE.items():
        folder_path = os.path.join(FRONTEND_DIR, folder)
        ensure_directory_exists(folder_path)  # Ensure target directory exists

        for file in files:
            old_path = file_locations.get(file)
            new_path = os.path.join(folder_path, file)

            # If file exists, check for merge
            if old_path:
                if os.path.exists(new_path):
                    merged = merge_files(old_path, new_path)
                    if merged:
                        merged_files.append(f"{old_path} → {new_path}")
                else:
                    shutil.move(old_path, new_path)
                    logging.info(f"[MOVED] {old_path} → {new_path}")

            else:
                # Check for similar names
                closest_match = find_closest_match(file, file_locations.keys())
                if closest_match:
                    old_path = file_locations[closest_match]
                    logging.info(f"[RENAMED] {closest_match} → {file}")
                    shutil.move(old_path, new_path)
                else:
                    # Create Placeholder if File Doesn't Exist
                    with open(new_path, "w") as f:
                        f.write(f"// Placeholder for {file}\n")
                    logging.info(f"[CREATED] Placeholder: {new_path}")

    # Log merged files
    with open(MERGED_LOG, "w") as merge_log:
        merge_log.write("\n".join(merged_files))

def cleanup_orphaned_files():
    """Deletes files that don’t belong in the structure."""
    for root, _, files in os.walk(FRONTEND_DIR):
        for file in files:
            if file not in sum(STRUCTURE.values(), []):
                file_path = os.path.join(root, file)
                logging.info(f"[DELETED] Orphaned file removed: {file_path}")
                os.remove(file_path)

def create_index_files():
    """Generates index.js files to export components from each folder"""
    for folder in STRUCTURE.keys():
        folder_path = os.path.join(FRONTEND_DIR, folder)
        index_path = os.path.join(folder_path, "index.js")

        if os.path.exists(index_path):
            logging.info(f"[SKIPPED] index.js already exists in {folder}.")
            continue

        with open(index_path, "w") as f:
            exports = [
                f'export {{ default as {file.split(".")[0]} }} from "./{file}";'
                for file in STRUCTURE[folder] if file != "index.js"
            ]
            f.write("\n".join(exports) + "\n")
        logging.info(f"[INDEX] Generated index.js for {folder}")

def main():
    logging.info("🚀 Starting Full Auto-Merge & Cleanup...")

    # Scan files
    file_locations = scan_frontend_files()

    # Move, merge, rename, and create placeholders
    move_and_fix_files(file_locations)

    # Delete orphaned files that don’t belong
    cleanup_orphaned_files()

    # Generate index.js files
    create_index_files()

    logging.info("✅ Full frontend structure fixed successfully!")
    print(f"✅ Frontend restructuring completed. Logs saved to {LOG_FILE}")
    print(f"📝 Merged files tracked in {MERGED_LOG}")

if __name__ == "__main__":
    main()
