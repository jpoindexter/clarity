from backend.utils.ollama_client import run_ollama
from backend.agents.prompts import get_prompt_template
from backend.agents.types import AgentType
import logging

logger = logging.getLogger(__name__)

def run_agent_task(agent: str, input_text: str, model: str = "llama3") -> dict:
    """
    Dispatches an AI task to the appropriate model and prompt template.
    Args:
        agent (str): Agent type like 'summarizer', 'contradiction', etc.
        input_text (str): Text to analyze.
        model (str): Ollama model to use.
    Returns:
        dict: Structured response with result or error.
    """
    try:
        agent_enum = AgentType(agent)
    except ValueError:
        return {
            "agent": agent,
            "model": model,
            "result": None,
            "success": False,
            "error": f"Unknown agent type: {agent}"
        }

    prompt = get_prompt_template(agent_enum, input_text)
    try:
        response = run_ollama(prompt, model=model)
        return {
            "agent": agent_enum.value,
            "model": model,
            "result": response.strip(),
            "success": True,
            "error": None
        }
    except Exception as e:
        logger.error("Agent dispatch error [%s]: %s", agent_enum, e)
        return {
            "agent": agent_enum.value,
            "model": model,
            "result": None,
            "success": False,
            "error": str(e)
        }

def test_classifier_agent_dispatch():
    result = run_agent_task("classifier", "Markets crash amid political unrest.")
    assert result["success"] is True
    assert isinstance(result["result"], str)
    assert "," in result["result"] or len(result["result"].split()) > 1