import json
import requests

def summarize(text: str, model: str = "mistral") -> str:
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

    url = "http://127.0.0.1:11434/api/generate"
    payload = {
        "model": model,
        "prompt": f"Summarize in ONE short sentence: {text}",
    }

    try:
        response = requests.post(url, json=payload, stream=True)
        response.raise_for_status()

        summary = []

        for chunk in response.iter_lines():
            if not chunk:
                continue

            try:
                data = json.loads(chunk.decode("utf-8"))
                if "response" in data:
                    summary.append(data["response"].strip())
            except json.JSONDecodeError:
                continue  # ✅ Skip invalid JSON

        return " ".join(summary).strip() if summary else "⚠️ Error: No summary returned."

    except requests.exceptions.ConnectionError:
        return "⚠️ Error: Cannot connect to Ollama service. Ensure it's running."
    except requests.exceptions.Timeout:
        return "⚠️ Error: Ollama service timed out. Try again."
    except requests.exceptions.RequestException as e:
        return f"⚠️ Error: Ollama service unavailable. ➜ Details: {str(e)}"

# ✅ Standalone test mode
if __name__ == "__main__":
    test_text = "Artificial intelligence is transforming the world."
    print(summarize(test_text))
