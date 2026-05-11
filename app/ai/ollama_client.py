import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def ask_llm(prompt: str):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "phi3",
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.1,
                "num_predict": 60
            }
        }
    )

    data = response.json()

    return data["response"]