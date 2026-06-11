from fastapi import APIRouter

router = APIRouter()

@router.post("/recommend")
def recommend():
    return {"message": "API is working, logic not built yet"}