from sqlalchemy.orm import Session

from backend.models.article import Article
<<<<<<< HEAD
=======
from backend.models.news import News
>>>>>>> e7de5aae97128e25160c3ae83bd7e7b38dfd0917


def get_or_create(db: Session, model, defaults=None, **kwargs):
    """
    ✅ Retrieve an existing object or create a new one if not found.
    """
    instance = db.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        params = {**kwargs, **(defaults or {})}
        instance = model(**params)
        db.add(instance)
        db.commit()
        db.refresh(instance)
        return instance


def fetch_articles(db: Session):
    """
    ✅ Retrieve all articles from the database.
    """
    return db.query(Article).all()
