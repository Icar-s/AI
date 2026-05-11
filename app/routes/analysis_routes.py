from fastapi import APIRouter, UploadFile, File, Form

from app.utils.pdf_reader import extract_text_from_pdf
from app.services.ai_service import calculate_similarity
from app.services.llm_skill_extractor import extract_skills_with_llm

router = APIRouter()


@router.post("/analyze-resume")
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):

    contents = await file.read()

    resume_text = extract_text_from_pdf(contents)

    resume_skills = extract_skills_with_llm(resume_text)

    job_skills = extract_skills_with_llm(job_description)

    similarity_score = calculate_similarity(
        " ".join(resume_skills),
        " ".join(job_skills)
    )

    return {
        "similarity_score": round(similarity_score, 2),
        "resume_skills": resume_skills,
        "job_skills": job_skills
    }