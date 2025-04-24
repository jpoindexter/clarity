def standardize_tags(raw_tags: list[str]) -> list[dict]:
    """
    Convert a list of strings into AgentTag-style dictionaries.
    Example:
    ["economy", "ai"] → [{"id": "economy", "label": "Economy", ...}, ...]
    """
    return [
        {
            "id": tag.lower().replace(" ", "_"),
            "label": tag.title(),
            "type": "signal",
            "severity": "medium",
            "confidence": 0.9,
            "client_visible": True,
        }
        for tag in raw_tags if isinstance(tag, str)
    ]
