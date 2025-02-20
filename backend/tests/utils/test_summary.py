def test_summary_function():
    assert summary_function("Hello World") == "Hello World"
    assert summary_function("") == ""
    assert summary_function("This is a test") == "This is a test"