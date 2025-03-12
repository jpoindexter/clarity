import os
import re

# Define file paths
FILES_TO_FIX = {
    "router": "backend/api/router.py",
    "news": "backend/api/endpoints/news.py",
    "articles": "backend/api/endpoints/articles.py",
    "contradictions": "backend/api/endpoints/contradictions.py"
}

# Fix function
def fix_file(file_path, replacements):
    if not os.path.exists(file_path):
        print(f"⚠️ Warning: {file_path} not found. Skipping.")
        return

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    for old, new in replacements.items():
        content = re.sub(old, new, content)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"✅ Fixed {file_path}")

# Fix router.py
fix_file(FILES_TO_FIX["router"], {
    r'include_router\(news_router, prefix="/news"': 'include_router(news_router, prefix=""',
    r'include_router\(articles_router, prefix="/articles"': 'include_router(articles_router, prefix=""',
    r'include_router\(contradictions_router, prefix="/contradictions"': 'include_router(contradictions_router, prefix=""',
})

# Fix news.py
fix_file(FILES_TO_FIX["news"], {
    r'APIRouter\(prefix="/api/news"': 'APIRouter(prefix="", tags=["news"])'
})

# Fix articles.py
fix_file(FILES_TO_FIX["articles"], {
    r'APIRouter\(prefix="/api/articles"': 'APIRouter(prefix="", tags=["articles"])'
})

# Fix contradictions.py
fix_file(FILES_TO_FIX["contradictions"], {
    r'APIRouter\(prefix="/api/contradictions"': 'APIRouter(prefix="", tags=["contradictions"])'
})

print("\n✅ All route issues have been fixed! Restart FastAPI and test.")