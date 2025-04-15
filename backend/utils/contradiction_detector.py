from backend.utils.ollama_client import run_ollama

def detect_contradictions(text: str) -> dict:
    if not text or not isinstance(text, str) or not text.strip():
        return {
            "contradictions_found": False,
            "contradictions": [],
            "error": "⚠️ Error: Empty or invalid input text."
        }

    prompt = (
        "Analyze the following text for internal contradictions or logical inconsistencies. "
        "If any contradictions are found, list them clearly. If none are found, respond with 'No contradictions found.'\n\n"
        f"Text:\n{text.strip()}"
    )

    response = run_ollama(prompt, model="llama3")
    contradictions = []

    if response and "no contradictions found" not in response.lower():
        contradictions = [line.strip() for line in response.split("\n") if line.strip()]

    return {
        "contradictions_found": bool(contradictions),
        "contradictions": contradictions
    }