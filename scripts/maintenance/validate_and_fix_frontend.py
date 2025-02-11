import os
import shutil
import logging
from datetime import datetime

# Define Paths
FRONTEND_DIR = "frontend/components"
LOGS_DIR = "logs/scan"
LOG_FILE = os.path.join(LOGS_DIR, f"frontend_fix_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

# Ensure logs directory exists
os.makedirs(LOGS_DIR, exist_ok=True)

# Configure logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Define the correct structure
STRUCTURE = {
    "UI": ["Button.js", "Modal.js", "index.js"],
    "News": ["ArticleCard.js", "NewsList.js", "index.js"],
    "Filters": ["SearchBar.js", "SourceDropdown.js", "DateFilter.js", "index.js"],
    "Graph": ["NewsGraph.js", "index.js"],
    "Common": ["Layout.js", "Header.js", "Footer.js", "index.js"]
}

# Detects all `.js` and `.tsx` files in frontend/, excluding node_modules/
def scan_frontend_files():
    file_locations = {}
    for root, _, files in os.walk("frontend"):
        # Skip node_modules and any hidden directories
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

# Moves existing files to correct locations
def move_files(file_locations):
    for folder, files in STRUCTURE.items():
        folder_path = os.path.join(FRONTEND_DIR, folder)
        os.makedirs(folder_path, exist_ok=True)

        for file in files:
            if file in file_locations:
                old_path = file_locations[file]
                new_path = os.path.join(folder_path, file)

                # Ask before overwriting duplicates
                if os.path.exists(new_path):
                    response = input(f"⚠️ {file} already exists in {folder}. Overwrite? (y/n): ").strip().lower()
                    if response != 'y':
                        logging.info(f"[SKIPPED] {file} already exists in {folder}. No overwrite.")
                        continue

                try:
                    shutil.move(old_path, new_path)
                    logging.info(f"[MOVED] {old_path} → {new_path}")
                except FileNotFoundError:
                    logging.error(f"[ERROR] File not found: {old_path}. Skipping.")

# Creates missing placeholders
def create_missing_files():
    for folder, files in STRUCTURE.items():
        folder_path = os.path.join(FRONTEND_DIR, folder)

        for file in files:
            file_path = os.path.join(folder_path, file)
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    f.write(f"// Placeholder for {file}\n")
                logging.info(f"[CREATED] Placeholder: {file_path}")

# Generates index.js files
def create_index_files():
    for folder in STRUCTURE.keys():
        folder_path = os.path.join(FRONTEND_DIR, folder)
        index_path = os.path.join(folder_path, "index.js")

        if not os.path.exists(index_path):
            with open(index_path, "w") as f:
                exports = [f'export {{ default as {file.split(".")[0]} }} from "./{file}";' for file in STRUCTURE[folder] if file != "index.js"]
                f.write("\n".join(exports) + "\n")
            logging.info(f"[INDEX] Generated index.js for {folder}")

def main():
    logging.info("🚀 Starting Frontend Validation & Fixing...")

    # Scan for existing files, excluding node_modules/
    file_locations = scan_frontend_files()

    # Move files safely
    move_files(file_locations)

    # Create placeholders
    create_missing_files()

    # Generate index.js files
    create_index_files()

    logging.info("✅ Frontend validation & restructuring completed successfully!")
    print(f"✅ Frontend restructuring completed. Logs saved to {LOG_FILE}")

if __name__ == "__main__":
    main()
