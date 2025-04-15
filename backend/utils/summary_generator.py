"""
Summary Generator - AI-Powered Text Summarization
Handles text summarization using AI models.
"""

import logging
from typing import Optional
from backend.utils.ollama_client import run_ollama
import requests

logger = logging.getLogger(__name__)

SAMPLE_TEXT = """Artificial intelligence (AI) is intelligence demonstrated by machines,
as opposed to natural intelligence displayed by animals including humans."""


def summarize_text(text: str) -> Optional[str]: 
    """
    Generates a summary of the provided text using a locally running Ollama model.

    Args:
        text (str): The text to summarize. 

    Returns:
        Optional[str]: A summarized version of the input text.
    """
    if not text or not isinstance(text, str) or not text.strip():
        logger.warning("Received empty text for summarization.")
        return "⚠️ Error: Input text is empty."

    try:
        prompt = f"Summarize this text:\n{text.strip()}"
        return run_ollama(prompt, model="mistral")
    except Exception as exc:
        logger.error("Summarization failed: %s", exc)
        return "⚠️ Error: Failed to summarize text"
    
# ✅ Added a final newline below    
