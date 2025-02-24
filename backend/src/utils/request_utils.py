"""
Request Utilities Module
Provides reusable functions for making API requests.
"""

import json
import requests
from typing import Optional


def send_post_request(api_url: str, text: str, timeout: int = 10) -> Optional[dict]:
    """
    Sends a POST request to an API with a JSON payload.

    Args:
        api_url (str): The target API endpoint.
        text (str): The text content to send.
        timeout (int, optional): Request timeout in seconds. Defaults to 10.

    Returns:
        Optional[dict]: JSON response if successful, else None.
    """
    headers = {"Content-Type": "application/json"}
    payload = json.dumps({"text": text})

    try:
        response = requests.post(
            api_url, data=payload, headers=headers, timeout=timeout
        )
        response.raise_for_status()  # Raises an error for HTTP errors (4xx, 5xx)
        return response.json()

    except requests.exceptions.JSONDecodeError:
        print("❌ Response is not valid JSON.")
        return None

    except requests.exceptions.RequestException as exc:
        print(f"❌ Request failed: {exc}")
        return None
