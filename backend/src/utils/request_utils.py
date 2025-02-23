"""
Request Utilities Module
Provides reusable functions for making API requests.
"""

import json
import requests


def send_post_request(api_url: str, text: str, timeout: int = 10) -> dict | None:
    """
    Sends a POST request to an API with a JSON payload.

    Args:
        api_url (str): The target API endpoint.
        text (str): The text content to send.
        timeout (int, optional): Request timeout in seconds. Defaults to 10.

    Returns:
        dict | None: JSON response if successful, else None.
    """
    headers = {"Content-Type": "application/json"}
    payload = json.dumps({"text": text})

    try:
        response = requests.post(
            api_url, data=payload, headers=headers, timeout=timeout
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as exc:
        print(f"Request failed: {exc}")
        return None
