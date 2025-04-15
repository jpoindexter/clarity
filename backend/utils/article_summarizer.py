from backend.utils.ollama_client import run_ollama

def summarize_article(article_text: str, model: str = "mistral") -> str:
    """Summarize the input article text using a local LLM via Ollama."""
    if not article_text or not isinstance(article_text, str) or not article_text.strip():
        return "⚠️ Error: Article text is empty or invalid."

    prompt = f"Summarize the following article in 3-4 concise sentences:\n\n{article_text.strip()}"
    return run_ollama(prompt, model=model)