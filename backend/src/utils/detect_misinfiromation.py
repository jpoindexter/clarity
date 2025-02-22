# backend/src/utils/ai_analysis.py
import requests
import json

def detect_misinformation(text: str) -> dict:
    """
    Analyzes text for misinformation patterns using AI.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: Misinformation analysis results (e.g., credibility score, detected biases).
    """
    if not text.strip():
        return {"error": "Input text is empty."}

    try:
        response = requests.post(
            "http://127.0.0.1:11434/api/analyze",  # Change URL if different
            json={"text": text}
        )
        response.raise_for_status()

        raw_data = response.text  # Capture raw response
        print(f"🔍 AI Response: {raw_data}")  # Debugging print

        return json.loads(raw_data)

    except requests.exceptions.RequestException as e:
        return {"error": f"AI service unavailable. Details: {e}"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON response from AI service."}