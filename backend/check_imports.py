import os
import re

# Define the base directory (adjust if needed)
BASE_DIR = "backend"

# Define the pattern to match old `src.` import references
PATTERN = re.compile(r"from\s+src\.(\S+)|import\s+src\.(\S+)")

# Store results
outdated_imports = {}

# Walk through all Python files in the backend directory
for root, _, files in os.walk(BASE_DIR):
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)

            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            for i, line in enumerate(lines, start=1):
                match = PATTERN.search(line)
                if match:
                    outdated_imports.setdefault(file_path, []).append((i, line.strip()))

# Output results
if outdated_imports:
    print("\n🚨 Outdated `src/` references found:\n")
    for file, issues in outdated_imports.items():
        print(f"📌 {file}:")
        for line_num, content in issues:
            print(f"  - Line {line_num}: {content}")
    print("\n🔍 Review and update the import paths to match the new structure.")
else:
    print("✅ No outdated `src/` references found. Imports are clean!")
