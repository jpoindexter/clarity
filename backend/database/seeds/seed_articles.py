 
from datetime import datetime
from sqlalchemy.orm import Session
from backend.database.db_connection import SessionLocal
from backend.models.article import SummarizedArticle

def seed_articles():
    db: Session = SessionLocal()

    test_data = [
        {
            "title": "AI in Elections",
            "summary": "A look at AI’s growing influence on political campaigns and public opinion shaping.",
            "timestamp": datetime.utcnow(),
            "source": "TechNews",
            "tone": "cautious",
            "manipulation_risk": 0.75,
        },
        {
            "title": "Climate Crisis Deepens",
            "summary": "New reports suggest climate change is accelerating faster than models predicted.",
            "timestamp": datetime.utcnow(),
            "source": "EarthDaily",
            "tone": "urgent",
            "manipulation_risk": 0.88,
        },
        {
            "title": "Stock Markets Rebound",
            "summary": "Markets show signs of recovery after a volatile quarter driven by policy shifts.",
            "timestamp": datetime.utcnow(),
            "source": "MarketWatch",
            "tone": "neutral",
            "manipulation_risk": 0.32,
        },
    ]

    for article in test_data:
        db.add(SummarizedArticle(**article))

    db.commit()
    db.close()
    print("✅ Seeded summarized_articles table with test data.")

if __name__ == "__main__":
    seed_articles()