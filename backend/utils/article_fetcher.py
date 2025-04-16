import requests
from newspaper import Article
import trafilatura
from trafilatura.settings import use_config
from bs4 import BeautifulSoup

# 🧠 CLARITY CONTENT LADDER
# This function implements a multi-layer fallback system for reliably extracting article text.
# It tries the following steps in order:
# 1. Newspaper3k — Fast and structured if available.
# 2. Trafilatura — Lightweight but smart extraction with custom user-agent.
# 3. BeautifulSoup — Raw HTML scan of all <p> tags.
# 4. (Coming Soon) AMP variant, Wayback Machine, News APIs, and Playwright fallback.
#
# Each layer includes logging and a minimum character count to ensure usable content is returned to the AI pipeline.
def fetch_article_text(url: str) -> str:
    """Fetch article text using newspaper3k with trafilatura and BS4 fallback."""
    try:
        article = Article(url)
        article.download()
        article.parse()
        text = article.text
        if text and len(text) > 200:
            return text[:10000]
    except Exception as e:
        print(f"⚠️ Newspaper3k failed: {e}")

    try:
        config = use_config()
        config.set("DEFAULT", "user_agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
        downloaded = trafilatura.fetch_url(url, config=config)
        if downloaded:
            content = trafilatura.extract(downloaded)
            if content and len(content) > 200:
                return content[:10000]
    except Exception as e:
        print(f"❌ Trafilatura fallback failed: {e}")

    # Final fallback: raw HTML + paragraph text
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        paragraphs = soup.find_all("p")
        raw_text = " ".join(p.get_text() for p in paragraphs)
        if raw_text and len(raw_text) > 200:
            return raw_text[:10000]
    except Exception as e:
        print(f"❌ Final fallback (BS4) failed: {e}")

    return ""