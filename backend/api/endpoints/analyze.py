from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class AnalyzeRequest(BaseModel):
    text: str


class AnalyzeMultipleRequest(BaseModel):
    texts: list[str]


@router.post("/")
def analyze_text(request: AnalyzeRequest):
    return {"analysis": f"Analysis result for: {request.text}"}


@router.post("/multiple")
def analyze_multiple_texts(request: AnalyzeMultipleRequest):
    return {"analyses": [f"Analysis result for: {text}" for text in request.texts]}
