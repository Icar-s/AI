from pydantic import BaseModel

class JobRequest(BaseModel):
    resume_text: str
    job_description: str