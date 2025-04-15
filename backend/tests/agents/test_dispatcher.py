from backend.agents.dispatcher import run_agent_task

def test_summarizer_agent_dispatch():
    result = run_agent_task("summarizer", "AI is transforming industries.")
    assert result["success"] is True
    assert isinstance(result["result"], str)
    assert "AI" in result["result"]

def test_contradiction_agent_dispatch():
    result = run_agent_task("contradiction", "It will rain tomorrow. Later it says it will be sunny.")
    assert result["success"] is True
    assert isinstance(result["result"], str)

def test_unknown_agent_type():
    result = run_agent_task("nonsense", "Text")
    assert result["success"] is False
    assert result["error"].startswith("Unknown agent type")