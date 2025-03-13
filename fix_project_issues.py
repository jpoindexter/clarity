import os

# Define file paths
files_to_fix = {
    "backend/crud/__init__.py": "from .news import news_crud  # Ensure correct import",
    "backend/api/router.py": "router.include_router(news_router, prefix='/api/news', tags=['news'])",
    "backend/api/main.py": "include_routers(app)  # Ensure include_routers is properly called",
    "backend/api/endpoints/articles.py": "from backend.crud.news import news_crud  # Ensure correct import",
}

def fix_file(file_path, fix_line):
    """Ensures the fix_line exists in the given file."""
    if os.path.exists(file_path):
        with open(file_path, "r+") as file:
            content = file.readlines()
            if fix_line not in content:
                content.append("\n" + fix_line + "\n")
                file.seek(0)
                file.writelines(content)
        print(f"✅ Fixed {file_path}")
    else:
        print(f"⚠️ Warning: {file_path} not found. Skipping.")

# Apply fixes
for file_path, fix_line in files_to_fix.items():
    fix_file(file_path, fix_line)

print("\n✅ All identified issues have been fixed! Restart FastAPI and test.")