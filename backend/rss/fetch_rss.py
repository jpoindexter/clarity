import os
import logging
import feedparser
from backend.rss.rss_feeds import RSS_FEEDS
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

# ✅ Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("🚀 Loading T5-small model for local summarization...")
tokenizer = T5Tokenizer.from_pretrained("t5-small")
model = T5ForConditionalGeneration.from_pretrained("t5-small")
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)
logging.info(f"✅ Summarization model loaded on {device}")

# ✅ Get MAX_ARTICLES from environment or default to 5
MAX_ARTICLES = int(os.getenv("MAX_ARTICLES", 5))

logging.info("🔥 Fetching RSS Feeds with MAX_ARTICLES=%d", MAX_ARTICLES)


def summarize_text(text):
    """Summarizes input text using the T5 model (runs locally)."""
    if not text or len(text.split()) < 50:  # ✅ Skip summarization for short articles
        return text

    logging.info("🔍 Summarizing article content...")
    inputs = tokenizer(
        "summarize: " + text, return_tensors="pt", max_length=512, truncation=True
    )
    inputs = {k: v.to(device) for k, v in inputs.items()}

    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=150,
        min_length=30,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary


def fetch_and_process_rss():
    """
    ✅ Fetches RSS feeds, extracts articles, ensures required fields,
    and summarizes them safely.
    """
    articles = []
    seen_urls = set()  # ✅ Deduplication: Track seen URLs

    for rss_url in RSS_FEEDS:
        logging.info(f"🔥 Fetching RSS Feed: {rss_url}")
        parsed_feed = feedparser.parse(rss_url)

        if not parsed_feed.entries:
            logging.warning(f"⚠️ WARNING: No entries found in {rss_url}")
            continue

        logging.info(
            f"✅ Successfully fetched feed: "
            f"{parsed_feed.feed.get('title', 'Unknown Source')}"
        )

        # ✅ Extract source name
        source_name = parsed_feed.feed.get("title", "Unknown Source")

        for entry in parsed_feed.entries:
            if len(articles) >= MAX_ARTICLES:
                break

            url = entry.get("link", "https://unknown.com")

            # ✅ Deduplication: Skip if URL already processed
            if url in seen_urls:
                continue
            seen_urls.add(url)

            title = entry.get("title", "No Title")
            published_at = entry.get("published", "2025-02-21T00:00:00Z")

            # ✅ Improved Content Extraction: Try multiple fields
            summary_source = (
                entry.get("content", [{}])[0].get("value")
                or entry.get("summary")
                or entry.get("description")
                or title
            )

            logging.info(
                f"🔍 Processing Article: {title} | 🌐 {url}"
            )

            summary = summarize_text(summary_source)

            articles.append(
                {
                    "title": title,
                    "url": url,
                    "summary": summary,
                    "source": source_name,
                    "published_at": published_at,
                }
            )

            logging.info(f"✅ Summary Processed: {summary[:100]}...")

        if len(articles) >= MAX_ARTICLES:
            break

    logging.info(f"🚀 Fetching complete. Total articles fetched: {len(articles)}")
    return articles


if __name__ == "__main__":
    fetch_and_process_rss()
