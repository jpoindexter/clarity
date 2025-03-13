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
    response = client.post("/", json={"text": "Test input"})
    assert response.status_code == 200
    assert response.json() == {"analysis": "Analysis result for: Test input"}


def test_analyze_multiple_texts():
    """✅ Ensure multiple text analysis endpoint works correctly."""
    response = client.post("/multiple", json={"texts": ["Text 1", "Text 2"]})
    assert response.status_code == 200
    assert response.json() == {
        "analyses": ["Analysis result for: Text 1", "Analysis result for: Text 2"]
    }
