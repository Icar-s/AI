# AI Resume Analyzer

AI Resume Analyzer is a local-first prototype for evaluating how well a resume matches a job description. It processes a PDF resume, extracts relevant skills with a local LLM, compares them semantically with embeddings, and returns a similarity score along with the matched and missing skills.

## Overview

The project combines a FastAPI backend, a terminal-based CLI, and local AI inference through Ollama. It is designed for experimentation, demos, and small-scale resume analysis workflows without depending on external cloud services.

## What the application does

1. Accepts a resume in PDF format.
2. Extracts the text from the PDF.
3. Uses a local LLM via Ollama to identify relevant technical skills.
4. Normalizes and compares the extracted skills against the job description.
5. Computes semantic similarity using sentence embeddings.
6. Returns a JSON response that can be consumed by the CLI or by external clients.

## Key features

- Resume PDF upload and parsing
- Local AI-based skill extraction
- Semantic similarity scoring with embeddings
- Comparison between resume skills and job requirements
- Interactive terminal interface
- REST API with FastAPI
- Automatic API documentation through Swagger UI

## Architecture

The application follows a simple pipeline:

CLI / client -> FastAPI endpoint -> PDF text extraction -> LLM skill extraction -> embedding-based similarity -> JSON response

## Tech stack

### Backend
- Python
- FastAPI
- Uvicorn

### AI and NLP
- Ollama
- Phi-3 model
- Sentence Transformers
- scikit-learn

### Document processing
- pypdf
- Regular expressions for text normalization

### CLI
- Rich
- Requests

## Prerequisites

Before running the project, make sure you have:

- Python 3.10 or newer
- Ollama installed and running locally
- The Phi-3 model available in Ollama

Install the model with:

```bash
ollama pull phi3
```

## Installation

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

On Windows, use:

```bash
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the project

### 1. Start the local model

```bash
ollama run phi3
```

### 2. Start the FastAPI server

```bash
uvicorn app.main:app --reload
```

The API will be available at:

- http://127.0.0.1:8000/docs for Swagger UI

### 3. Start the CLI

```bash
python cli.py
```

### Windows convenience script

A Windows batch script is also available:

```bash
start.bat
```

## API usage

### Endpoint

POST /analyze-resume

### Request format

The endpoint expects multipart form data with:

- file: the PDF resume file
- job_description: the target job description as a plain text string

### Example with curl

```bash
curl -X POST "http://127.0.0.1:8000/analyze-resume" \
  -F "file=@/path/to/resume.pdf" \
  -F "job_description=Python, FastAPI, PostgreSQL, Docker"
```

### Response example

```json
{
  "similarity_score": 0.81,
  "resume_skills": ["Python", "FastAPI", "PostgreSQL"],
  "job_skills": ["Python", "FastAPI", "Docker", "AWS"]
}
```

## Project structure

```text
.
├── app/
│   ├── ai/
│   │   ├── embedding_model.py
│   │   └── ollama_client.py
│   ├── main.py
│   ├── routes/
│   │   └── analysis_routes.py
│   ├── schemas/
│   ├── services/
│   │   ├── ai_service.py
│   │   └── llm_skill_extractor.py
│   └── utils/
│       ├── pdf_reader.py
│       └── text_cleaner.py
├── cli.py
├── requirements.txt
├── start.bat
```

## Notes

- This project is a prototype focused on local experimentation and simple resume screening use cases.
- Performance depends on the machine hardware and the availability of the local Ollama service.
- The skill extraction step is prompt-based and may require tuning for more accurate results.

## Author

Icaro Santos

- GitHub: https://github.com/Icar-s
- LinkedIn: https://www.linkedin.com/in/icarush/