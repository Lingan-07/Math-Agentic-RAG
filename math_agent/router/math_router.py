from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from core.guardrails import validate_math_query
from core.agent import math_agent_route
from pydantic import Field

router = APIRouter()

class Question(BaseModel):
    query: str

class Feedback(BaseModel):
    Question: str = Field(alias="question")
    Feedback: str = Field(alias="feedback")
    

@router.post("/ask")
async def ask_math_question(question: Question):

    if not validate_math_query(question.query):
        raise HTTPException(status_code=400, detail="Only math queries are allowed.")
    
    result = await math_agent_route(question.query)
    return {"response": result}


@router.post("/feedback")
async def collect_feedback(feedback: Feedback):
    import json, os

    os.makedirs("feedback", exist_ok=True)
    file_path = "feedback/feedback.json"

    entry = feedback.model_dump()

    data = []
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            for line in f:
                if line.strip():
                    data.append(json.loads(line))
    data.append(entry)

    with open(file_path, "w") as f:
        for d in data:
            f.write(json.dumps(d) + "\n")

    return {"status": "Feedback recorded 🙌"}