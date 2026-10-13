from fastapi import APIRouter, HTTPException

from ..schemas import CareerAssistantRequest
from ..services.career_assistant import (
    CareerAssistantConfigurationError,
    CareerAssistantServiceError,
    answer_career_question,
)

router = APIRouter(prefix="/api/assistant", tags=["Career Assistant"])


@router.post("/chat")
async def chat(data: CareerAssistantRequest):
    try:
        answer = await answer_career_question(data)
    except CareerAssistantConfigurationError as error:
        raise HTTPException(status_code=503, detail=str(error)) from error
    except CareerAssistantServiceError as error:
        raise HTTPException(status_code=502, detail=str(error)) from error

    return {"answer": answer}
