import requests


def fetch_news():
    """Fetches news from an external API (Mock Example)"""
    try:
        response = requests.get("https://api.example.com/news")
        response.raise_for_status()
        return response.json()
    except Exception:
        return None  # ✅ Return None on failure
