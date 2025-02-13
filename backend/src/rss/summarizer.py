import ollama  # ✅ Ensure Ollama is installed and available

def summarize_text(text: str, model: str = "mistral") -> str:
    """
    Summarizes input text using Ollama's AI model.

    Args:
        text (str): The input text to summarize.
        model (str): The AI model to use for summarization (default: "mistral").

    Returns:
        str: The summarized text, or an error message if summarization fails.
    """
    if not text.strip():
        return "⚠️ Error: Input text is empty. Provide valid content for summarization."

    try:
        response = ollama.generate(model=model, prompt=f"Summarize: {text}")
        return response["response"] if "response" in response else "⚠️ No summary generated."
    except Exception as e:
        print(f"❌ Error summarizing text: {e}")
        return "⚠️ Error: Summarization failed."

if __name__ == "__main__":
    sample_text = "Artificial intelligence is transforming industries by enhancing efficiency, automating tasks, and enabling data-driven decision-making."
    summary = summarize_text(sample_text)
    print(f"🔍 Summary: {summary}")
