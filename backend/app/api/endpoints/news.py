from typing import Any, List, Dict

from fastapi import APIRouter, Depends, HTTPException
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from crud import news as crud
from api import deps
from config.config import settings
from backend.tests.utils.news import create_random_news
from backend.tests.utils.utils import random_lower_string

router = APIRouter()


@router.get("/api/news", response_model=List[schemas.News])
def read_news(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve news.
    """
    news = crud.news.get_multi(db, skip=skip, limit=limit)
    return news


@router.post("/", response_model=schemas.News)
def create_news(
    *,
    db: Session = Depends(deps.get_db),
    news_in: schemas.NewsCreate,
) -> Any:
    """
    Create new news.
    """
    news = crud.news.create(db, obj_in=news_in)
    return news


@router.put("/{id}", response_model=schemas.News)
def update_news(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    news_in: schemas.NewsUpdate,
) -> Any:
    """
    Update a news.
    """
    news = crud.news.get(db, id=id)
    if not news:
        raise HTTPException(status_code=404, detail="News not found")
    news = crud.news.update(db, db_obj=news, obj_in=news_in)
    return news


@router.get("/{id}", response_model=schemas.News)
def read_news_by_id(
    id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve news by id.
    """
    news = crud.news.get(db, id=id)
    if not news:
        raise HTTPException(status_code=404, detail="News not found")
    return news


@router.delete("/{id}", response_model=schemas.News)
def delete_news(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete a news.
    """
    news = crud.news.get(db, id=id)
    if not news:
        raise HTTPException(status_code=404, detail="News not found")
    news = crud.news.remove(db, id=id)
    return news


def test_create_news(
    client: TestClient, db: Session, normal_user_token_headers: Dict[str, str]
) -> None:
    data = {"title": "foo", "content": "bar"}
    r = client.post(
        f"{settings.API_V1_STR}/news/", headers=normal_user_token_headers, json=data,
    )
    assert r.status_code == 200
    created_news = r.json()
    assert created_news["title"] == "foo"
    assert created_news["content"] == "bar"


def test_get_news(
    client: TestClient, db: Session, normal_user_token_headers: Dict[str, str]
) -> None:
    news = create_random_news(db)
    r = client.get(
        f"{settings.API_V1_STR}/news/{news.id}",
        headers=normal_user_token_headers,
    )
    assert r.status_code == 200
    returned_news = r.json()
    assert returned_news["title"] == news.title
    assert returned_news["content"] == news.content


def test_read_news(
    client: TestClient, db: Session, normal_user_token_headers: Dict[str, str]
) -> None:
    create_random_news(db)
    create_random_news(db)
    r = client.get(f"{settings.API_V1_STR}/news/", headers=normal_user_token_headers)
    assert r.status_code == 200
    all_news = r.json()
    assert len(all_news) > 1
    for news in all_news:
        assert "title" in news

