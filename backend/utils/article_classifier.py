from backend.agents.dispatcher import run_agent_task

def classify_article(content: str, model: str = "llama3") -> list[str]:
    """
    Classify the article content using the local LLM via the 'classifier' agent.
    Returns a list of tags.
    """
    result = run_agent_task("classifier", content, model=model)
    if not result["success"]:
        return ["uncategorized"]

    # Split the result into tags — either comma-separated or space-delimited
    raw = result["result"]
    if "," in raw:
        return [tag.strip().lower() for tag in raw.split(",") if tag.strip()]
    else:
        return [tag.strip().lower() for tag in raw.split() if tag.strip()]