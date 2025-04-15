from backend.utils.contradiction_detector import detect_contradictions

def test_detect_contradictions_basic():
    result = detect_contradictions("The article says the sky is blue, then says it is green.")
    assert isinstance(result, dict)
    assert "contradictions_found" in result
    assert "contradictions" in result
    assert isinstance(result["contradictions"], list)