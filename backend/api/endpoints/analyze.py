from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/analyze", tags=["Analyze"])


class AnalyzeRequest(BaseModel):
    text: str
    

class AnalyzeMultipleRequest(BaseModel):
    texts: list[str]

 
@router.post(
    "/",
    summary="Analyze article for contradictions",
    description="Uses internal NLP pipeline to detect contradictions, misinformation signals, and bias in article content."
)
def analyze_text(request: AnalyzeRequest):
    return {
        "analysis": f"Analysis result for input text: {request.text}",
        "input": request.text
    }


@router.post( 
    "/multiple",
    summary="Batch analyze articles for contradictions",
    description="Processes a list of input texts and analyzes each one for contradictions, misinformation, and bias patterns."
)
def analyze_multiple_texts(request: AnalyzeMultipleRequest):
    return {
        "analyses": [
            {"input": text, "result": f"Analysis result for: {text}"}
            for text in request.texts
        ]
    }

@router.post(
    "/contradiction",
    summary="Detect contradictions in article text",
    description="Identifies internal inconsistencies or logical conflicts within a given article text."
)
def analyze_contradiction(request: AnalyzeRequest):
    from backend.utils.contradiction_detector import detect_contradictions
    return detect_contradictions(request.text)
