def test_summarizer():
    assert summarize("This is a test sentence.") == "This is a test sentence."
    assert summarize("Short.") == "Short."
    assert summarize("A long sentence that needs summarizing.") == "A long sentence that needs summarizing."
    assert summarize("") == ""