import json
import requests


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
        return "⚠️ Error: Input text is empty."

    try:
        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={
                "model": model,
                "prompt": f"Summarize in ONE short sentence: {text}",
            },  # 🔥 Force brevity, now within 88 chars
            stream=True,
        )
        response.raise_for_status()

        summary: list[str] = []

        for chunk in response.iter_lines():
            if not chunk:
                continue

            try:
                data = json.loads(chunk.decode("utf-8"))
                if "response" in data:
                    summary.append(data["response"])
            except json.JSONDecodeError:
                continue  # ✅ Skip invalid JSON

        return (
            " ".join(summary).strip() if summary else "⚠️ Error: No summary returned."
        )  # ✅ Manually split to fit within 88 chars

    except requests.exceptions.RequestException as e:
        return f"⚠️ Error: Ollama service unavailable.\n➜ Details: {e}"


if __name__ == "__main__":
    print(summarize_text("Test input"))
