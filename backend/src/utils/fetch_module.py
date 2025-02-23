"""
Utility module for fetching data from external sources.
Handles network requests with proper error handling.
"""

import requests
from requests.exceptions import RequestException, Timeout, HTTPError

DEFAULT_TIMEOUT = 10  # Set a reasonable timeout in seconds


def fetch_data(url: str, timeout: int = DEFAULT_TIMEOUT) -> dict:
    """
    Fetches JSON data from a given URL.

    Args:
        url (str): The API endpoint to fetch data from.
        timeout (int, optional): Timeout for the request. Defaults to DEFAULT_TIMEOUT.

    Returns:
        dict: JSON response from the API.

    Raises:
        ValueError: If the URL is invalid.
        Timeout: If the request times out.
        HTTPError: If the request fails with an HTTP error.
        RequestException: For other network-related errors.
    """
    if not url.startswith(("http://", "https://")):
        raise ValueError(f"Invalid URL: {url}")

    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        return response.json()
    except Timeout as exc:
        raise Timeout(f"Request timed out for URL: {url}") from exc
    except HTTPError as http_err:
        raise HTTPError(f"HTTP error occurred: {http_err}") from http_err
    except RequestException as req_err:
        raise RequestException(f"Network error occurred: {req_err}") from req_err


# ✅ Final newline added below
