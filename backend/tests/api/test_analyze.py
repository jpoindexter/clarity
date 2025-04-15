from fastapi import FastAPI
from fastapi.testclient import TestClient

# ✅ Explicitly import the module
import backend.api.endpoints.analyze as analyze_module

# ✅ Ensure FastAPI is properly configured
app = FastAPI()
app.include_router(analyze_module.router)

client = TestClient(app)

def test_analyze_text():
    """✅ Ensure single text analysis endpoint works correctly."""
    response = client.post("/api/analyze", json={"text": "Test input"})
    assert response.status_code == 200
    assert response.json() == {
        "analysis": "Analysis result for input text: Test input",
        "input": "Test input"
    }

def test_analyze_multiple_texts():
    """✅ Ensure multiple text analysis endpoint works correctly."""
    response = client.post("/api/analyze/multiple", json={"texts": ["Text 1", "Text 2"]})
    assert response.status_code == 200
    assert response.json() == {
        "analyses": [
            {"input": "Text 1", "result": "Analysis result for: Text 1"},
            {"input": "Text 2", "result": "Analysis result for: Text 2"}
        ]
    }

def test_analyze_contradiction():
    """✅ Ensure contradiction detection returns structured output."""
    response = client.post("/api/analyze/contradiction", json={"text": "The article says it will rain, but later says it will be sunny."})
    assert response.status_code == 200
    data = response.json()
    assert "contradictions_found" in data
    assert isinstance(data["contradictions_found"], bool)
    assert "contradictions" in data
    assert isinstance(data["contradictions"], list)