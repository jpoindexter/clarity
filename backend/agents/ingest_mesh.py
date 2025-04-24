import time
import threading
from datetime import datetime
from sqlalchemy.orm import Session
from urllib.parse import urlparse
from backend.database.db_connection import SessionLocal
from backend.utils.article_fetcher import fetch_article_text
from backend.utils.article_summarizer import summarize_article
from backend.utils.article_classifier import classify_article
from backend.utils.tag_utils import standardize_tags
from backend.rss.parser import fetch_and_parse_feed
from backend.models.article import SummarizedArticle
from backend.schemas.article import SummarizedArticleCreate
from backend.crud.articles import save_summarized_article
from backend.agents.mesh_sources import (
    fetch_from_gdelt,
    fetch_from_google_news_rss,
    fetch_from_bbc_rss,
    fetch_from_nyt_rss,
    fetch_from_reuters_rss,
    fetch_from_mediastack,
    fetch_from_common_crawl
)

INTERVAL_SECONDS = 300  # 5 minutes

def ingest_once():
    sources = (
        fetch_from_gdelt()
        + fetch_from_google_news_rss()
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

    print(f"🧾 Batch summary — Total: {len(sources)}, Processed: {counts['processed']}, Saved: {counts['saved']}, Skipped: {counts['skipped']}, Errors: {counts['errors']}")
    db.close()
 
def start_ingest_mesh():
    def loop():
        while True:
            print("🔁 Ingesting feeds...")
            ingest_once()
            time.sleep(INTERVAL_SECONDS)

    thread = threading.Thread(target=loop, daemon=True)
    thread.start()