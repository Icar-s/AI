from pydantic import BaseModel

class AnalysisResponse(BaseModel):
    similarity_score: float
    resume_skills: list[str]
    job_skills: list[str]
    matched_skills: list[str]
    missing_skills: list[str]