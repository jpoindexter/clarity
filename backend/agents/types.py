from enum import Enum

class AgentType(str, Enum):
    SUMMARIZER = "summarizer"
    CONTRADICTION = "contradiction"