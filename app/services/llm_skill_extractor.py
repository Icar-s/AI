from app.ai.ollama_client import ask_llm


def extract_skills_with_llm(text: str):

    prompt = f"""
    Extract only the technologies and programming tools
    from this text.

    Return only a comma separated list.

    Text:
    {text}
    """

    response = ask_llm(prompt)

    print("\nLLM RESPONSE:")
    print(response)

    skills = [
        skill.strip()
        for skill in response.split(",")
    ]

    return skills