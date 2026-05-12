import requests

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.progress import Progress


console = Console()

API_URL = "http://127.0.0.1:8000/analyze-resume"

console.print(
    Panel.fit(
        "[bold red]⚠ WARNING / AVISO ⚠[/bold red]\n\n"
        
        "[yellow]"
        "This application uses a local AI model and may temporarily "
        "consume high CPU and RAM usage during analysis.\n\n"
        
        "Your computer may experience slowdowns or freezing while "
        "processing resumes.\n\n"
        
        "It is strongly recommended to close unnecessary applications "
        "and save your documents before continuing."
        "[/yellow]\n\n"

        "[cyan]"
        "Esta aplicação utiliza um modelo de IA local e pode consumir "
        "muito processamento e memória RAM durante a análise.\n\n"

        "Seu computador pode apresentar lentidão ou travamentos "
        "temporários enquanto o currículo é processado.\n\n"

        "É altamente recomendado fechar aplicativos desnecessários "
        "e salvar seus documentos antes de continuar."
        "[/cyan]",
        
        border_style="red"
    )
)
def normalize_skill(skill: str):

    return (
        skill.lower()
        .replace('"', '')
        .replace(".", "")
        .replace("-", "")
        .replace("_", "")
        .strip()
    )

def main():

    console.print(
        Panel.fit(
            "[bold green]AI Resume Analyzer[/bold green]\n"
            "[yellow]FastAPI + Ollama + Phi3[/yellow]",
            border_style="green"
        )
    )

    pdf_path = Prompt.ask(
        "[cyan]Digite o caminho do PDF[/cyan]"
    )

    job_description = Prompt.ask(
        "[magenta]Cole a descrição da vaga[/magenta]"
    )

    with Progress() as progress:

        task = progress.add_task(
            "[green]Analisando currículo...",
            total=100
        )

        with open(pdf_path, "rb") as file:

            response = requests.post(
                API_URL,
                files={
                    "file": file
                },
                data={
                    "job_description": job_description
                }
            )

        progress.update(task, advance=100)

    result = response.json()

    similarity_score = result["similarity_score"]

    resume_skills = result["resume_skills"]

    job_skills = result["job_skills"]

    matched_skills = []

    missing_skills = []

    resume_normalized = [
        normalize_skill(skill)
        for skill in resume_skills
    ]

    for skill in job_skills:

        normalized_skill = (
            skill.lower()
            .replace('"', '')
            .strip()
        )

        if normalized_skill in resume_normalized:
            matched_skills.append(skill)

        else:
            missing_skills.append(skill)

    console.print()

    console.print(
        Panel.fit(
            f"[bold green]Similarity Score:[/bold green] "
            f"{round(similarity_score * 100)}%",
            border_style="green"
        )
    )

    table = Table(title="Skills Analysis")

    table.add_column(
        "Matched Skills",
        style="green"
    )

    table.add_column(
        "Missing Skills",
        style="red"
    )

    max_len = max(
        len(matched_skills),
        len(missing_skills)
    )

    for i in range(max_len):

        matched = (
            matched_skills[i]
            if i < len(matched_skills)
            else ""
        )

        missing = (
            missing_skills[i]
            if i < len(missing_skills)
            else ""
        )

        table.add_row(
            matched,
            missing
        )

    console.print(table)

    console.print(
        Panel.fit(
            
        )
    )

if __name__ == "__main__":
    main()