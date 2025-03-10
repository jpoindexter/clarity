import pytest
from backend.src.services.contradiction_detection import detect_contradictions

def test_contradiction_detection():
    articles = [
        {"headline": "Stock market rises", "content": "Stock market increased due to strong earnings."},
        {"headline": "Stock market drops", "content": "Stock market declined amid economic uncertainty."}
    ]
    contradictions = detect_contradictions(articles)
    
    assert len(contradictions) > 0
    assert ("Stock market rises", "Stock market drops") in contradictions
