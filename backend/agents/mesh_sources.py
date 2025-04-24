from sqlalchemy.orm import Session
from urllib.parse import urlparse
from backend.models import SummarizedArticle  # Ensure correct model path
from backend.utils.article_fetcher import fetch_article_text  # Ensure the fetch function is correct
from backend.utils.content_processing import summarize_article, classify_article, standardize_tags  # Correct import
from backend.schemas import SummarizedArticleCreate  # Ensure correct schema path
from datetime import datetime
from backend.crud import save_summarized_article  # Ensure CRUD function path
from backend.database import SessionLocal  # Ensure session path

def ingest_once():
    from backend.agents.mesh_sources import (
        fetch_from_gdelt,
        fetch_from_google_news_rss,
        fetch_from_bbc_rss,
        fetch_from_nyt_rss,
        fetch_from_reuters_rss,
        fetch_from_mediastack,
        fetch_from_common_crawl
    )

    sources = (
        fetch_from_gdelt()
        + fetch_from_google_news_rss()  # Directly use Google News RSS
        + fetch_from_bbc_rss()
        + fetch_from_nyt_rss()
        + fetch_from_reuters_rss()
        + fetch_from_mediastack()
        + fetch_from_common_crawl()
    )
    
    counts = {
        "processed": 0,
        "skipped": 0,
        "saved": 0, 
        "errors": 0
    }

    db = SessionLocal()  # Open a new session
    for entry in sources:
        url = entry.get("url")
        if not url or not urlparse(url).scheme or not urlparse(url).netloc:
            print(f"❌ Invalid URL: {entry.get('title', 'Unknown Title')}")
            counts["errors"] += 1
            continue
        counts["processed"] += 1
        
        existing = db.query(SummarizedArticle).filter_by(url=url).first()
        if existing:
            print(f"⏩ Skipping duplicate: {url}")
            counts["skipped"] += 1
            continue

        try:
            content = fetch_article_text(url)
            if not content or len(content) < 100:
                print(f"❌ Skipping short content for {url}")
                continue
            
            summary = summarize_article(content)
            raw_tags = classify_article(content)
            tags = standardize_tags(raw_tags)
            
            item = SummarizedArticleCreate(
                title=entry.get("title", "Untitled"),
                url=url,
                summary=summary,
                tone="neutral",
                tags=tags,
                source="rss",
                raw_text=content,
                timestamp=datetime.utcnow(),
                manipulation_risk=0.0
            )
            
            save_summarized_article(db, item)
            print(f"✅ Saved: {item.title[:60]}")
            counts["saved"] += 1
        except Exception as e:
            print(f"❌ Error processing {url}: {e}")
            counts["errors"] += 1

    print(f"🧾 Batch summary — Total: {len(sources)}, Saved: {counts['saved']}, Skipped: {counts['skipped']}, Errors: {counts['errors']}")
    db.close()  # Close the session 