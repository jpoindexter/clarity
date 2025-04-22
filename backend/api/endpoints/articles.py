from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# ✅ Database & Models
from backend.database.db_connection import get_db
from backend.models.article import Article  # ✅ Using Article model
from backend.models.article import SummarizedArticle  # New import

# ✅ Schemas 
from backend.schemas.article import Article as ArticleSchema
from backend.schemas.article import ArticleOut
from backend.schemas.article import ArticleCreate  # ✅ Correct Schema
from backend.schemas.article import ArticleIngestRequest, SummarizedArticleCreate
from backend.models.article import SummarizedArticle  # ✅ Correct model for DB queries
from backend.utils.article_fetcher import fetch_article_text
from backend.utils.article_summarizer import summarize_article
from backend.utils.article_classifier import classify_article  # New import
from backend.rss.parser import fetch_and_parse_feed
from backend.crud.articles import save_summarized_article

# Helper function to standardize tags into AgentTag schema
def standardize_tags(raw_tags: list[str]) -> list[dict]:
    return [
        {
            "id": tag.lower().replace(" ", "_"),
            "label": tag,
            "type": "signal",
            "severity": "medium",
            "confidence": 0.9,
            "client_visible": True
        }
        for tag in raw_tags
    ]

# ✅ Initialize Router (Correct Prefix)
router = APIRouter(prefix="/articles", tags=["Articles"])
 
# 🔹 **Retrieve All Articles** 


@router.get(
    "/",
    response_model=dict[str, list[ArticleOut]],
    summary="Retrieve all articles",
    description="Returns a list of ingested articles from the database."
)
def get_articles(db: Session = Depends(get_db)):
    """ 
    Retrieve all stored articles. 

    Returns:
        dict[str, list[ArticleOut]]: Dictionary with key "articles" containing a list of stored articles.
    """
    articles = (
        db.query(SummarizedArticle)
        .filter(SummarizedArticle.summary.isnot(None))
        .order_by(SummarizedArticle.timestamp.desc())
        .limit(100)
        .all()
    )
    return {"articles": [ArticleOut.from_orm(a) for a in articles]}

# 🔹 **Create a New Article Entry**


@router.post(    
    "/",
    response_model=ArticleSchema,
    summary="Add a new article",
    description="Stores a new article with full metadata into the database."
)
def create_article(article: ArticleCreate, db: Session = Depends(get_db)):
    """
    Create a new article entry.

    Args:
        article (ArticleCreate): Data for the new article.
        db (Session): Database session.

    Returns:
        ArticleSchema: The created article.
    """
    new_article = Article(
        title=article.title,
        summary=article.summary,
        content=article.content,
        source=article.source,
        url=article.url,
        published_at=article.published_at or datetime.utcnow(),
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article

# 🔹 **Ingest Article(s) from RSS or URL**

@router.post(
    "/ingest",
    response_model=dict,
    summary="Ingest article(s) from RSS or URL",
    description="Fetches article(s) from a given URL or RSS feed and returns summarized content."
) 
def ingest_articles(request: ArticleIngestRequest, db: Session = Depends(get_db)):
    try: 
        if request.source == "url":
            text = fetch_article_text(request.input)
            if not text:
                print("⚠️ No extractable content — saving with fallback summary.")
                text = "No extractable content"
            summary = summarize_article(text)
            raw_tags = classify_article(text)
            if not isinstance(raw_tags, list):
                raise HTTPException(status_code=500, detail="Agent failed to return valid tag list.")
            tags = standardize_tags(raw_tags)
            existing = db.query(SummarizedArticle).filter_by(url=request.input).first()  # Updated line
            if existing:
                print("⛔ Already ingested — skipping DB insert.")
                return {"status": "duplicate", "id": existing.id}
            summarized_data = SummarizedArticleCreate(
                title="Untitled",
                url=request.input,
                summary=summary,
                tags=tags, 
                tone="neutral",
                source="url",  
                raw_text=text,
                flags=["fallback_summary"],
                status="degraded"
            )
            save_summarized_article(db, summarized_data)
            return {"status": "success"}

        elif request.source == "rss":
            articles = fetch_and_parse_feed(request.input)
            results = []
            for entry in articles:
                content = fetch_article_text(entry.get("url", ""))
                print(f"\n🧪 FEED ENTRY → {entry.get('title', 'Untitled')}")
                print(f"🔹 Content Length (original): {len(content)}")
                if not content or len(content) < 100:
                    print("⛔ Skipped: Not enough usable content. Trying fallback...")
                    fallback_content = (
                        entry.get("summary") or
                        entry.get("description") or
                        entry.get("content", [{}])[0].get("value", "")
                    )
                    print(f"🔁 Fallback Content Length: {len(fallback_content)}")
                    if not fallback_content or len(fallback_content) < 100:
                        print("⛔ Final Skip: No usable fallback content.")
                        continue
                    content = fallback_content
                summary = summarize_article(content)
                raw_tags = classify_article(content)
                if not isinstance(raw_tags, list):
                    raise HTTPException(status_code=500, detail="Agent failed to return valid tag list.")
                tags = standardize_tags(raw_tags)
                summarized_data = SummarizedArticleCreate(
                    title=entry.get("title", "Untitled"),
                    url=entry.get("url"),
                    summary=summary, 
                    tags=tags,
                    tone="neutral",
                    source="rss",
                    raw_text=content
                )
                save_summarized_article(db, summarized_data)
                results.append({
                    "title": entry.get("title", "Untitled"),
                    "url": entry.get("url"),
                    "summary": summary,
                    "source": "rss",
                    "published": entry.get("published", datetime.utcnow().isoformat()),
                    "tags": tags
                })
            return {"status": "success"}
 
    except Exception as e:
        import traceback
        print("\n🚨 Ingest Failed:") 
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))

    raise HTTPException(status_code=400, detail="Invalid source type.")