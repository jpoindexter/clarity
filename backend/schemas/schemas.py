from pydantic import BaseModel
from typing import List
from datetime import datetime

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