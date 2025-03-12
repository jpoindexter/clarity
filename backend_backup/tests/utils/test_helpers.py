from backend.utils.helpers import clean_text


def test_clean_text():
    text = "  Hello, World!  "
    cleaned_text = clean_text(text)
    assert cleaned_text == "Hello, World!"
