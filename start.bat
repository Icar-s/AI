@echo off
title AI Resume Analyzer

echo ============================================
echo Starting AI Resume Analyzer...
echo ============================================

:: Ativa UTF-8 no terminal (resolve ASCII quebrado)
chcp 65001 > nul

:: Ativa venv
call venv\Scripts\activate

echo.
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Starting Ollama...
start cmd /k "ollama run phi3"

timeout /t 8 > nul

echo.
echo Starting FastAPI server...
start cmd /k "uvicorn app.main:app --reload"

timeout /t 5 > nul

echo.
echo Starting CLI...
python cli.py

pause