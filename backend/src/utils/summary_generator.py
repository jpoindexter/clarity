"""
Text Summarization Utility using Ollama's AI Model.
"""

import ollama  # Ensure Ollama is installed and running

def summarize_text(text: str, model: str = "mistral") -> str:
    """
    Summarizes input text using Ollama's AI model.

    Args:
        text (str): The text to summarize.
        model (str): The Ollama model to use for summarization (default: "mistral").

    Returns:
        str: The summarized text or an error message.
    """
    if not text.strip():
        return "⚠️ Error: Input text is empty. Please provide valid text."

    try:
        response = ollama.chat(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": f"Summarize this: {text}",
                }
            ],
        )

        return response.get("message", {}).get(
            "content",
            "⚠️ Error: No summary returned.",
        )  # ✅ Line split for PEP8 compliance
    except Exception as e:
        return f"❌ Error summarizing text: {e}"  # ✅ Split long return statement

# Function to summarize a given text using the provided implementation
def summarize_text(text: str) -> str:
    return f"Summarized: {text[:50]}..."  # ✅ Placeholder implementation

# ✅ Example Usage (Standalone Execution)
if __name__ == "__main__":
    sample_text = (
        "Artificial intelligence is transforming industries by automating tasks "
        "and improving decision-making processes, leading to significant advancements "
        "in technology."
    )  # ✅ Wrapped long string for readability

    summary = summarize_text(sample_text)
    print(f"🔍 Summary: {summary}")
