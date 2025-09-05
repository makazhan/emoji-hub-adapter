from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_emojis():
    # placeholder data
    return {"emojis": ["😀", "😎", "🔥"]}
