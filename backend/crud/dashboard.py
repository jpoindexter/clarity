from sqlalchemy.orm import Session
from sqlalchemy import func
from backend.database.models import Article
from datetime import datetime

def get_dashboard_summary(db: Session):
    total_articles = db.query(func.count(Article.id)).scalar()
    flagged_articles = db.query(func.count(Article.id)).filter(Article.summary.ilike("%⚠%")).scalar()
    top_sources = (
        db.query(Article.source, func.count(Article.source))
        .group_by(Article.source)
        .order_by(func.count(Article.source).desc())
        .limit(5)
        .all()
    )
    return {
        "total_articles": total_articles,
        "flagged_articles": flagged_articles,
        "last_updated": datetime.utcnow().isoformat(),
        "top_sources": [source for source, _ in top_sources]
    }