from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class AnalyzeRequest(BaseModel):
    text: str

@router.post("/")
def analyze_text(request: AnalyzeRequest):
    return {"analysis": f"Analysis result for: {request.text}"}
