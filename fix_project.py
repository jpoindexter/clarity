import os
import re

# List of files to fix
FILES_TO_FIX = [
    "backend/api/main.py",
    "backend/api/router.py",
    "backend/api/endpoints/news.py",
    "backend/api/endpoints/articles.py",
    "backend/api/endpoints/search.py",
    "backend/crud/news.py",
    "backend/crud/__init__.py",
    "backend/schemas/news.py",
]

# Correct imports
IMPORT_FIXES = {
    "from backend.crud.news import get_news": "from backend.crud.news import news_crud",
    "from backend.crud.news import news_crud_crud": "from backend.crud.news import news_crud",
    "from backend.api.router import include_routers": "from backend.api.router import include_routers as include",
}

# Fix route prefixes
ROUTE_FIXES = {
    "prefix=\"/api/api/news\"": "prefix=\"/api/news\"",
    "prefix=\"/api/api/articles\"": "prefix=\"/api/articles\"",
    "prefix=\"/api/api/search\"": "prefix=\"/api/search\"",
    "prefix=\"/api/api/contradictions\"": "prefix=\"/api/contradictions\"",
}

# Fix double imports and duplicates
def clean_imports(content):
    content = re.sub(r"from backend.crud.news import news_crud_crud", "from backend.crud.news import news_crud", content)
    content = re.sub(r"from backend.crud.news import get_news", "from backend.crud.news import news_crud", content)
    return content

# Fix route prefixes
def fix_routes(content):
    for old_route, new_route in ROUTE_FIXES.items():
        content = content.replace(old_route, new_route)
    return content

# Process all files
def fix_all_files():
    for file_path in FILES_TO_FIX:
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                content = file.read()

            # Apply fixes
            content = clean_imports(content)
            content = fix_routes(content)

            with open(file_path, "w") as file:
                file.write(content)

            print(f"✅ Fixed {file_path}")

# Run the script
if __name__ == "__main__":
    fix_all_files()
    print("\n🚀 All issues fixed! Restart FastAPI and test your endpoints.")