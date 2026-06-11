from fastapi import APIRouter
from app.models.sme import SMERequest

router = APIRouter()

@router.post("/recommend")
def recommend(request: SMERequest):
    return {"message": "Request received.",
    "data": request.model_dump()
    }