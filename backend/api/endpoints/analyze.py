from fastapi import APIRouter
from pydantic import BaseModel

<<<<<<< HEAD
router = APIRouter()
=======
router = APIRouter(prefix="/api/analyze")
>>>>>>> e7de5aae97128e25160c3ae83bd7e7b38dfd0917


class AnalyzeRequest(BaseModel):
    text: str


class AnalyzeMultipleRequest(BaseModel):
    texts: list[str]


@router.post("/")
def analyze_text(request: AnalyzeRequest):
<<<<<<< HEAD
    return {"analysis": f"Analysis result for: {request.text}"}
=======
    return {
        "analysis": f"Analysis result for input text: {request.text}",
        "input": request.text
    }
>>>>>>> e7de5aae97128e25160c3ae83bd7e7b38dfd0917


@router.post("/multiple")
def analyze_multiple_texts(request: AnalyzeMultipleRequest):
<<<<<<< HEAD
    return {"analyses": [f"Analysis result for: {text}" for text in request.texts]}
=======
    return {
        "analyses": [
            {"input": text, "result": f"Analysis result for: {text}"}
            for text in request.texts
        ]
    }
>>>>>>> e7de5aae97128e25160c3ae83bd7e7b38dfd0917
