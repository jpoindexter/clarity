from pydantic import BaseModel
from datetime import datetime
from typing import List

class SummarizedArticleCreate(BaseModel):
    title: str
    url: str
    summary: str
    tone: str
    tags: List[str]
    source: str
    raw_text: str
    timestamp: datetime
    manipulation_risk: float