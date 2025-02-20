from backend.src.utils.fetch_module import fetch_news


def test_fetch_news_failure(mocker):
    """✅ Ensure fetch_news handles network errors correctly"""
    mocker.patch(
        "requests.get", side_effect=Exception("Network Error")
    )  # ✅ Fixed import path

    response = fetch_news()
    assert response is None  # ✅ Ensure failure is handled gracefully
