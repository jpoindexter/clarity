import os
import re

# ✅ Define the files to fix
FILES_TO_FIX = {
    "backend/api/router.py": [
        (r'router.include_router\(news_router, prefix="/api/api/news"\)', 
         'router.include_router(news_router, prefix="/api/news")'),
        (r'router.include_router\(articles_router, prefix="/api/api/articles"\)', 
         'router.include_router(articles_router, prefix="/api/articles")'),
        (r'router.include_router\(search_router, prefix="/api/api/search"\)', 
         'router.include_router(search_router, prefix="/api/search")')
    ],
    "backend/api/endpoints/news.py": [
        (r'APIRouter\(prefix="", tags=\["news"\]\)', 
         'APIRouter(prefix="/api/news", tags=["news"])')
    ],
    "backend/crud/__init__.py": [
        (r'from \.news import news', 
         'from .news import news_crud')
    ],
    "backend/schemas/news.py": [
        (r'class NewsSchema\(BaseModel\)', 
         'class News(BaseModel)')
    ],
    "backend/api/main.py": [
        (r'from backend.api.router import include_routers', 
         'from backend.api.router import include_routers\ninclude_routers(app)')
    ],
}


# ✅ Function to apply fixes
def apply_fixes():
    for file_path, replacements in FILES_TO_FIX.items():
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                content = file.read()

            for pattern, replacement in replacements:
                content = re.sub(pattern, replacement, content)

            with open(file_path, "w") as file:
                file.write(content)
            
            print(f"✅ Successfully processed {file_path}. Fixes applied.")
        else:
            print(f"⚠️ Warning: {file_path} not found. Skipping.")

        
# ✅ Run fixes
if __name__ == "__main__":
    apply_fixes()
    print("\n🚀 All fixes applied! Restart FastAPI and test.")
