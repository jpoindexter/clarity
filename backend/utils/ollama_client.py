import requests
import logging

logger = logging.getLogger(__name__)

def run_ollama(prompt: str, model: str = "llama3", timeout: int = 30, system_prompt: str | None = None) -> str:
    """
    Calls a local Ollama model to process a prompt.

    Args:
        prompt (str): The prompt to send to the model.
        model (str): The Ollama model to use.
        timeout (int): Request timeout in seconds.
        system_prompt (str | None): Optional system prompt for the model.

    Returns:
        str: The model's response or fallback message.
    """
    try:
        json_payload = {
            "model": model,
            "prompt": prompt.strip(),
            "stream": False
        }
        if system_prompt:
            json_payload["system"] = system_prompt

        response = requests.post(
            "http://localhost:11434/api/generate",
            json=json_payload,
            timeout=timeout
        )
        response.raise_for_status()
        data = response.json()
        return data.get("response", "").strip()

    except requests.exceptions.RequestException as e:
        logger.error("Ollama request failed: %s", e)
        return "⚠️ Error: Ollama service unavailable"

    except (ValueError, KeyError, TypeError) as e:
        logger.error("Invalid response format from Ollama: %s", e)
        return "⚠️ Error: Invalid response from Ollama"