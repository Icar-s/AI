from pypdf import PdfReader
from io import BytesIO

def extract_text_from_pdf(file_bytes:bytes) -> str:
    pdf = PdfReader(BytesIO(file_bytes))

    text = ""

    for page in pdf.pages:
        text += page.extract_text()

    return text