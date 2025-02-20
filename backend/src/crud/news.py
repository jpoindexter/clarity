from typing import Optional

from sqlalchemy.orm import Session

from backend.src.models.news import News
from backend.src.schemas.news import News as NewsSchema


class NewsCRUD:
    def create(self, db: Session, obj_in: NewsSchema) -> NewsSchema:
        """✅ Create a new news item."""
        new_news = News(**obj_in.model_dump())
        db.add(new_news)
        db.commit()
        db.refresh(new_news)
        return NewsSchema.model_validate(new_news)

    def get(self, db: Session, news_id: int) -> Optional[NewsSchema]:
        """✅ Retrieve a single news item."""
        news_item = db.query(News).filter(News.id == news_id).first()
        return NewsSchema.model_validate(news_item) if news_item else None

    def get_all_news(self, db: Session):
        """✅ Retrieve all news items."""
        return db.query(News).all()

    def update(self, db: Session, news_id: int, obj_in: dict) -> Optional[NewsSchema]:
        """✅ Update an existing news item."""
        db_news = db.query(News).filter(News.id == news_id).first()
        if not db_news:
            return None

        for key, value in obj_in.items():
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
