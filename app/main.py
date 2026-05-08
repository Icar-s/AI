from fastapi import FastAPI

from app.routes.resume_routes import router as resume_router
from app.routes.ai_routes import router as ai_router

app = FastAPI()

app.include_router(resume_router)
app.include_router(ai_router)
