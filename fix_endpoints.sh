#!/bin/bash

echo "🔧 Fixing API Endpoint Registrations..."

# Fix router imports in `backend/api/router.py`
sed -i '' 's/from backend.api.endpoints.news import router as news_router/from backend.api.endpoints.news import router as news_router\nfrom backend.api.endpoints.articles import router as articles_router\nfrom backend.api.endpoints.search import router as search_router\nfrom backend.api.endpoints.contradiction import router as contradiction_router/g' backend/api/router.py

# Ensure correct API prefix usage in `router.py`
sed -i '' 's@app.include_router(news_router, prefix="/api/news"@app.include_router(news_router, prefix="/news"@g' backend/api/router.py
sed -i '' 's@app.include_router(articles_router, prefix="/api/articles"@app.include_router(articles_router, prefix="/articles"@g' backend/api/router.py
sed -i '' 's@app.include_router(search_router, prefix="/api/search"@app.include_router(search_router, prefix="/search"@g' backend/api/router.py
sed -i '' 's@app.include_router(contradiction_router, prefix="/api/contradictions"@app.include_router(contradiction_router, prefix="/contradictions"@g' backend/api/router.py

echo "✅ API Endpoint Registrations Fixed!"