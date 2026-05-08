from fastapi import APIRouter, UploadFile, File
from app.utils.pdf_reader import extract_text_from_pdf

router = APIRouter()

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    contents = await file.read()

    extracted_text = extract_text_from_pdf(contents)
    

    return{
        "filename": file.filename,
        "content_type": file.content_type,
        "text": extracted_text[:10000]
    }