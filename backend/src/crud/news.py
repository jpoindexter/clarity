from typing import Optional
from sqlalchemy.orm import Session
from datetime import datetime
from backend.src.models.news import News
from backend.src.schemas.news import News as NewsSchema, NewsCreate, NewsUpdate  # ✅ Fixed import

class NewsCRUD:
    def create(self, db: Session, obj_in: NewsCreate) -> NewsSchema:
        """✅ Create a new news item."""
        new_news = News(
            title=obj_in.title,
            content=obj_in.content,
            source=obj_in.source,
            url=obj_in.url,
            published_at=obj_in.published_at if obj_in.published_at else datetime.utcnow()  # ✅ Ensure it exists
        )
        db.add(new_news)
        db.commit()
        db.refresh(new_news)
        return NewsSchema.model_validate(new_news)

    def get(self, db: Session, news_id: int) -> Optional[NewsSchema]:
        """✅ Retrieve a single news item."""
        news_item = db.query(News).filter(News.id == news_id).first()
        return NewsSchema.model_validate(news_item) if news_item else None

    def get_all_news(self, db: Session) -> list[NewsSchema]:
        """✅ Retrieve all news items."""
        return [NewsSchema.model_validate(news) for news in db.query(News).all()]

    def update(self, db: Session, news_id: int, obj_in: NewsUpdate) -> Optional[NewsSchema]:
        """✅ Update an existing news item."""
        db_news = db.query(News).filter(News.id == news_id).first()
        if not db_news:
            return None

        update_data = obj_in.dict(exclude_unset=True)  # ✅ Ensures only provided fields are updated
        for key, value in update_data.items():
            setattr(db_news, key, value)

        db.commit()
        db.refresh(db_news)
        return NewsSchema.model_validate(db_news)

    def remove(self, db: Session, news_id: int) -> Optional[NewsSchema]:
        """✅ Delete a news item and return it if successful."""
        db_news = db.query(News).filter(News.id == news_id).first()
        if not db_news:
            return None

        db.delete(db_news)
        db.commit()
        return NewsSchema.model_validate(db_news)


# ✅ Create an instance of NewsCRUD
news_crud = NewsCRUD()
