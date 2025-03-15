"""
Utility module for fetching data from external sources.
Handles network requests with proper error handling.
"""

import requests
import logging
from requests.exceptions import RequestException, Timeout, HTTPError

DEFAULT_TIMEOUT = 10  # Set a reasonable timeout in seconds
logger = logging.getLogger(__name__)  # Added logger for debugging


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
        logger.error(f"Invalid URL provided: {url}")
        raise ValueError(f"Invalid URL: {url}")

    try:
        logger.info(f"Fetching data from: {url}")
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)

        # Ensure response is JSON before returning
        try:
            return response.json()
        except ValueError as json_err:
            logger.error(f"Invalid JSON response from {url}")
            raise ValueError(f"Invalid JSON response from {url}") from json_err

    except Timeout as exc:
        logger.error(f"Request timed out for URL: {url}")
        raise Timeout(f"Request timed out for URL: {url}") from exc
    except HTTPError as http_err:
        logger.error(f"HTTP error for URL: {url}: {http_err}")
        raise HTTPError(f"HTTP error occurred: {http_err}") from http_err
    except RequestException as req_err:
        logger.error(f"Network error for URL: {url}: {req_err}")
        raise RequestException(f"Network error occurred: {req_err}") from req_err


# ✅ Added final newline for best practices
