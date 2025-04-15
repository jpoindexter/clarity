from pydantic import BaseModel
from typing import List, Optional

class AnalyzeRequest(BaseModel):
    text: str

class ContradictionResponse(BaseModel):
    contradictions_found: bool
    contradictions: List[str]
    error: Optional[str] = None