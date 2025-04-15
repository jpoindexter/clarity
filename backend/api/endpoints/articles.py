from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# ✅ Database & Models
from backend.database.db_connection import get_db
from backend.models.article import Article  # ✅ Using Article model

# ✅ Schemas
from backend.schemas.article import Article as ArticleSchema
from backend.schemas.article import ArticleCreate  # ✅ Correct Schema
from backend.schemas.article import ArticleIngestRequest, SummarizedArticle
from backend.utils.article_fetcher import fetch_article_text
from backend.utils.article_summarizer import summarize_article
from backend.utils.article_classifier import classify_article  # New import

# ✅ Initialize Router (Correct Prefix)
router = APIRouter(prefix="/articles", tags=["Articles"])

# 🔹 **Retrieve All Articles** 


@router.get(
    "/",
    response_model=list[ArticleSchema],
    summary="Retrieve all articles",
    description="Returns a list of ingested articles from the database."
)
def get_articles(db: Session = Depends(get_db)):
    """
    Retrieve all stored articles. 

    Returns:
        list[ArticleSchema]: List of stored articles.
        If no articles exist, returns an empty list.
    """
    articles = db.query(Article).all()
    return articles if articles else []  # ✅ Returns an empty list instead of 404

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
    response_model=list[SummarizedArticle],
    summary="Ingest article(s) from RSS or URL",
    description="Fetches article(s) from a given URL or RSS feed and returns summarized content."
)
def ingest_articles(request: ArticleIngestRequest):
    if request.source == "url":
        text = fetch_article_text(request.input)
        summary = summarize_article(text)
        tags = classify_article(text)  # Classifying the article
        return [{
            "title": "Untitled",
            "url": request.input,
            "summary": summary,
            "source": "url",
            "published": datetime.utcnow().isoformat(),
            "tags": tags  # Adding tags to the response
        }]

    elif request.source == "rss":
        from backend.rss.feed_parser import parse_feed
        articles = parse_feed(request.input)
        results = []
        for entry in articles:
            content = entry.get("summary", "") or entry.get("content", "")
            summary = summarize_article(content)
            tags = classify_article(content)  # Classifying the article
            results.append({
                "title": entry.get("title", "Untitled"),
                "url": entry.get("url"),
                "summary": summary,
                "source": "rss",
                "published": entry.get("published", datetime.utcnow().isoformat()),
                "tags": tags  # Adding tags to the response
            })
        return results

    raise HTTPException(status_code=400, detail="Invalid source type.")