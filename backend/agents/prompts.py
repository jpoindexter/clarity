from backend.agents.types import AgentType

def get_prompt_template(agent: AgentType, content: str) -> str:
    if agent == AgentType.SUMMARIZER:
        return f"Summarize the following in 3-5 sentences:\n\n{content.strip()}"

    elif agent == AgentType.CONTRADICTION:
        return (
            "Analyze this text for internal contradictions. "
            "List specific conflicting statements or logical inconsistencies:\n\n" + content.strip()
        )

    return f"⚠️ No prompt defined for agent: {agent.value}"