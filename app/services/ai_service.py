from sklearn.metrics.pairwise import cosine_similarity

from app.ai.embedding_model import model
from app.utils.text_cleaner import clean_text


def calculate_similarity(resume_text: str, job_description: str):

    resume_text = clean_text(resume_text)

    job_description = clean_text(job_description)

    resume_embedding = model.encode(
    resume_text,
    normalize_embeddings=True
    )

    job_embedding = model.encode(
        job_description,
        normalize_embeddings=True
    )

    similarity_score = cosine_similarity(
        [resume_embedding],
        [job_embedding]
    )

    return float(similarity_score[0][0])