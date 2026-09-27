from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class ChatRequest(BaseModel):
    well_id: int | None = None
    message: str


@router.post("/chat")
def chat(body: ChatRequest):
    return {
        "well_id": body.well_id,
        "reply": "The assistant is not connected yet.",
    }
