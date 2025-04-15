import requests
from bs4 import BeautifulSoup

def fetch_article_text(url: str) -> str:
    """Fetch and extract main article text from a given URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        return f"⚠️ Error fetching article: {e}"

    soup = BeautifulSoup(response.text, "html.parser")

    # Try extracting from common tags
    candidates = soup.find_all(["article", "section", "main"])
    if candidates:
        text = " ".join([tag.get_text(separator=" ", strip=True) for tag in candidates])
    else:
        text = soup.get_text(separator=" ", strip=True)

    return text[:10000]  # truncate long articles if needed