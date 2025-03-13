import pytest
from backend.utils.request_utils import send_post_request


@pytest.fixture
def mock_api_url():
    """✅ Provides a mock API URL for testing"""
    return "https://mockapi.com/endpoint"


@pytest.fixture
def mock_success_response(mocker):
    """✅ Mock a successful API response"""
    return mocker.patch(
        "requests.post",
        return_value=mocker.Mock(
            json=lambda: {"message": "Success"}, status_code=200
        ),
    )


@pytest.fixture
def mock_error_response(mocker):
    """✅ Mock an API error response"""
    return mocker.patch("requests.post", side_effect=Exception("API error"))


def test_send_post_request_success(mock_success_response, mock_api_url):
    """✅ Ensure send_post_request works correctly when API responds with JSON"""
    result = send_post_request(mock_api_url, "Test message")
    assert result == {"message": "Success"}, "❌ Expected valid JSON response"


def test_send_post_request_error(mock_error_response, mock_api_url):
    """✅ Ensure it handles API errors properly"""
    result = send_post_request(mock_api_url, "Test message")
    assert result is None, "❌ Expected None on API failure"
