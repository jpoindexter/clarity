"""
Utility module for fetching data from external sources.
Handles network requests with proper error handling.
"""

import requests
import logging
from requests.exceptions import RequestException, Timeout, HTTPError
from json.decoder import JSONDecodeError

DEFAULT_TIMEOUT = 10  # Set a reasonable timeout in seconds
HEADERS = {"User-Agent": "ClarityAI-FetchModule/1.0"}  # Standard User-Agent header
logger = logging.getLogger(__name__)  # Added logger for debugging


def fetch_data(url: str, timeout: int = DEFAULT_TIMEOUT, headers: dict = None) -> dict:
    """
    Fetches JSON data from a given URL.

    Args:
        url (str): The API endpoint to fetch data from.
        timeout (int, optional): Timeout for the request. Defaults to DEFAULT_TIMEOUT.
        headers (dict, optional): Additional headers to include in the request.

    Returns:
        dict: JSON response from the API.

    Raises:
        ValueError: If the URL is invalid.
        Timeout: If the request times out.
        HTTPError: If the request fails with an HTTP error.
        RequestException: For other network-related errors.
        JSONDecodeError: If the response is not valid JSON.

    Example Usage:
        response = fetch_data("https://api.example.com/data")
    """
    if not url.startswith(("http://", "https://")):
        logger.error("Invalid URL provided: %s", url)
        raise ValueError(f"Invalid URL: {url}")

    try:
        logger.info("Fetching data from: %s", url)
        response = requests.get(url, timeout=timeout, headers=headers or HEADERS)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)

        # Ensure response is JSON before returning
        content_type = response.headers.get("Content-Type", "")
        if "application/json" not in content_type:
            logger.error(
                "Non-JSON response received from %s (Content-Type: %s)",
                url, content_type
            )
            raise TypeError(f"Expected JSON response but got {content_type}")

        logger.info("Successfully received JSON response from: %s", url)
        return response.json()

    except Timeout as exc:
        logger.error("Request timed out for URL: %s - %s", url, exc)
        raise Timeout(f"Request timed out for URL: {url}") from exc
    except HTTPError as http_err:
        logger.error(
            "HTTP error for URL: %s (Status Code: %s): %s",
            url, response.status_code, http_err
        )
        raise HTTPError(f"HTTP error occurred: {http_err}") from http_err
    except JSONDecodeError as json_err:
        logger.error("Invalid JSON response from %s: %s", url, json_err)
        raise JSONDecodeError(
            f"Invalid JSON response from {url}", doc="", pos=0
        ) from json_err
    except RequestException as req_err:
        logger.error("Network error for URL: %s: %s", url, req_err)
        raise RequestException(f"Network error occurred: {req_err}") from req_err


def fetch_news(url: str, timeout: int = DEFAULT_TIMEOUT, headers: dict = None) -> list:
    """
    Fetches news articles from an external API endpoint.

    Args:
        url (str): The API endpoint to fetch news from.
        timeout (int, optional): Timeout for the request. Defaults to DEFAULT_TIMEOUT.
        headers (dict, optional): Additional headers to include in the request.

    Returns:
        list: A list of news articles as JSON objects.
    """
    response = fetch_data(url, timeout, headers)
    return response.get("articles", [])  # Assuming API response contains "articles" key
