from sqlalchemy.orm import Session
from src.models.article import Article  # ✅ Correct import for database models
from src.schemas.news import NewsCreate  # ✅ Ensure schemas are in `schemas/`

class NewsCRUD:
    """CRUD operations for News data."""
    
    def create_news(self, db: Session, news: NewsCreate) -> Article:
        """Creates a new news article entry in the database."""
        new_article = Article(**news.dict())
        db.add(new_article)
        db.commit()
        db.refresh(new_article)
        return new_article

    def get_news(self, db: Session, news_id: int) -> Article | None:
        """Fetches a single news article by its ID."""
        return db.query(Article).filter(Article.id == news_id).first()

    def get_news_list(self, db: Session, skip: int = 0, limit: int = 100) -> list[Article]:
        """Retrieves a paginated list of news articles."""
        return db.query(Article).offset(skip).limit(limit).all()

    def update_news(self, db: Session, news_id: int, news: NewsCreate) -> Article | None:
        """Updates an existing news article if it exists."""
        existing_article = db.query(Article).filter(Article.id == news_id).first()
        if existing_article:
            for key, value in news.dict().items():
                setattr(existing_article, key, value)
            db.commit()
            db.refresh(existing_article)
        return existing_article

    def delete_news(self, db: Session, news_id: int) -> bool:
        """Deletes a news article by ID."""
        existing_article = db.query(Article).filter(Article.id == news_id).first()
        if existing_article:
            db.delete(existing_article)
            db.commit()
            return True
        return False

# ✅ Instantiate CRUD object for use in API
news = NewsCRUD()
