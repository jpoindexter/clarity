from backend.utils.summarizer import summarize_text


def test_summarize_text():
    """✅ Ensure text summarization returns a string"""
    text = "AI-powered tools are transforming industries by automating complex tasks."
    summary = summarize_text(text)
    assert isinstance(summary, str)
    assert len(summary) > 0  # ✅ Ensure it doesn't return an empty string
