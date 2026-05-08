from fastapi import APIRouter

from app.schemas.job_schema import JobRequest
from app.services.ai_service import calculate_similarity

router = APIRouter()

@router.post("/analyze")
def analyze_resume(data: JobRequest):

    score = calculate_similarity(
        data.resume_text,
        data.job_description
    )

    return {
        "similarity_score": round(score, 2)
    }