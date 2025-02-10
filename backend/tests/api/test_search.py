# backend/tests/api/test_search.py
def test_search():
    response = client.get("/search?q=AI")
    assert response.status_code == 200
    assert "results" in response.json()
