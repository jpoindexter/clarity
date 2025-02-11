import os
import shutil
import logging
from datetime import datetime

# Define paths
FRONTEND_DIR = "frontend/components"
LOGS_DIR = "logs/scan"
LOG_FILE = os.path.join(LOGS_DIR, f"frontend_restructure_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

# Ensure logs directory exists
os.makedirs(LOGS_DIR, exist_ok=True)

# Configure logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Define the target structure
STRUCTURE = {
    "UI": ["Button.js", "Modal.js", "index.js"],
    "News": ["ArticleCard.js", "NewsList.js", "index.js"],
    "Filters": ["SearchBar.js", "SourceDropdown.js", "DateFilter.js", "index.js"],
    "Graph": ["NewsGraph.js", "index.js"],
    "Common": ["Layout.js", "Header.js", "Footer.js", "index.js"]
}

def ensure_directory_exists(path):
    """Create a directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)
        logging.info(f"[CREATE] Directory: {path}")

def move_existing_files():
    """Move existing files into the correct structure."""
    for folder, files in STRUCTURE.items():
        folder_path = os.path.join(FRONTEND_DIR, folder)
        ensure_directory_exists(folder_path)

        for file_name in files:
            old_path = os.path.join("frontend", file_name)
            new_path = os.path.join(folder_path, file_name)

            if os.path.exists(old_path) and not os.path.exists(new_path):
                shutil.move(old_path, new_path)
                logging.info(f"[MOVE] {old_path} → {new_path}")

def create_missing_files():
    """Create missing placeholder files to ensure the structure is complete."""
    for folder, files in STRUCTURE.items():
        folder_path = os.path.join(FRONTEND_DIR, folder)

        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    f.write(f"// Placeholder for {file_name}\n")
                logging.info(f"[CREATE] Placeholder: {file_path}")

def create_index_files():
    """Generate index.js files for each component folder to simplify imports."""
    for folder in STRUCTURE.keys():
        folder_path = os.path.join(FRONTEND_DIR, folder)
        index_path = os.path.join(folder_path, "index.js")

        if not os.path.exists(index_path):
            with open(index_path, "w") as f:
                exports = [f'export {{ default as {file.split(".")[0]} }} from "./{file}";' for file in STRUCTURE[folder] if file != "index.js"]
                f.write("\n".join(exports) + "\n")
            logging.info(f"[INDEX] Generated index.js for {folder}")

def main():
    """Execute the full restructuring process."""
    logging.info("🚀 Starting Frontend Restructuring...")

    move_existing_files()
    create_missing_files()
    create_index_files()

    logging.info("✅ Frontend restructuring completed successfully!")
    print(f"✅ Frontend restructuring completed. Logs saved to {LOG_FILE}")

if __name__ == "__main__":
    main()
