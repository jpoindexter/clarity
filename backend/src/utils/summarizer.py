import json

import requests


def summarize_text(text: str, model: str = "mistral") -> str:
    """Summarizes input text using Ollama's AI model."""
    if not text.strip():
        return "⚠️ Error: Input text is empty."

    try:
        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={
                "model": model,
                "prompt": f"Summarize in ONE short sentence: {text}",
            },  # 🔥 Force brevity
            stream=True,
        )
        response.raise_for_status()

        summary = []

        for chunk in response.iter_lines():
            if chunk:
                try:
                    data = json.loads(chunk.decode("utf-8"))
                    if "response" in data:
                        summary.append(data["response"])
                except json.JSONDecodeError:
                    continue

        return " ".join(summary).strip() if summary else "⚠️ Error: No summary returned."

    except requests.exceptions.RequestException as e:
        return f"⚠️ Error: Ollama service unavailable - {e}"


if __name__ == "__main__":
    print(summarize_text("Test input"))
