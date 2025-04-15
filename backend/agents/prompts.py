from backend.agents.types import AgentType

def get_prompt_template(agent: AgentType, content: str) -> str:
    if agent == AgentType.SUMMARIZER:
        return f"Summarize the following in 3-5 sentences:\n\n{content.strip()}"

    elif agent == AgentType.CONTRADICTION:
        return (
            "Analyze this text for internal contradictions. "
            "List specific conflicting statements or logical inconsistencies:\n\n" + content.strip()
        )
    
    elif agent == AgentType.CLASSIFIER:
        return (
            "Classify the following text by tagging it with relevant categories such as topic, tone, bias, or threat level. "
            "Return a comma-separated list of 2–5 tags:\n\n" + content.strip()
        )
 
    return f"⚠️ No prompt defined for agent: {agent.value}"