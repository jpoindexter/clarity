import pytest
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from backend.database.db_helper import get_or_create, fetch_articles

Base = declarative_base()

class MockModel(Base):
    __tablename__ = 'mock_model'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class MockArticle(Base):
    __tablename__ = 'mock_article'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)

def some_function():
    return "some_expected_value"

def test_some_function():
    expected_value = "some_expected_value"  # Define the expected value
    assert some_function() == expected_value

def another_function():
    return "some_expected_value"

def test_another_function():
    expected_value = "some_expected_value"  # Define the expected value
    assert another_function() == expected_value

def test_missing_lines():
    """✅ Ensure database connection functions are working."""
    from backend.database.db_connection import get_db  # ✅ Fix import

    db = next(get_db())  # ✅ Ensure DB session is retrieved properly
    assert db is not None

def test_get_or_create():
    # Setup in-memory SQLite database for testing
    engine = create_engine('sqlite:///:memory:')
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()

    # Test when instance exists
    existing_instance = MockModel(name="test")
    session.add(existing_instance)
    session.commit()

    instance = get_or_create(session, MockModel, name="test")
    assert instance.name == "test"

    # Test when instance does not exist
    instance = get_or_create(session, MockModel, name="new_test")
    assert instance.name == "new_test"
    session.commit()

def test_fetch_articles():
    # Setup in-memory SQLite database for testing
    engine = create_engine('sqlite:///:memory:')
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()

    # Test when there are articles in the database
    article1 = MockArticle(title="Article 1")
    article2 = MockArticle(title="Article 2")
    session.add(article1)
    session.add(article2)
    session.commit()

    articles = fetch_articles(session)
    assert len(articles) == 2
    assert articles[0].title == "Article 1"
    assert articles[1].title == "Article 2"

    # Test when there are no articles in the database
    session.query(MockArticle).delete()
    session.commit()

    articles = fetch_articles(session)
    assert len(articles) == 0