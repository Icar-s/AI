# AI Resume Analyzer 

Sistema de análise inteligente de currículos usando IA local, comparação semântica e API backend em FastAPI.

O projeto compara um currículo em PDF com uma descrição de vaga e retorna:
- Score de similaridade
- Skills encontradas no currículo
- Skills exigidas na vaga
- Skills faltantes

Tudo rodando localmente com modelo de IA via Ollama.

---

#  Demonstração

O usuário:
1. Envia um currículo em PDF
2. Cola uma descrição de vaga
3. O sistema processa e retorna a análise

---

#  Como funciona

1. PDF é convertido em texto
2. LLM local (Phi3 via Ollama) extrai skills do texto
3. Skills são normalizadas
4. Embeddings são usados para cálculo de similaridade semântica
5. Resultado é retornado via API
6. CLI exibe resultado formatado no terminal

---

# 🏗️ Arquitetura

CLI (Rich Terminal)
↓
FastAPI Backend
↓
Ollama (Phi3 LLM)
↓
Skill Extraction
↓
Embedding Model
↓
Cosine Similarity
↓
JSON Response

---

# 🧪 Funcionalidades

- Upload de PDF de currículo
- Extração de texto de PDF
- Extração de skills via LLM local
- Normalização de texto
- Comparação de skills com vaga
- Cálculo de similaridade
- Interface CLI estilizada
- API documentada via Swagger

---

# 🧰 Tecnologias utilizadas

## Backend
- Python
- FastAPI
- Uvicorn

## IA / NLP
- Ollama (inferência local)
- Phi3 (LLM)
- Sentence Transformers (embeddings)
- NLP básico (normalização e parsing)

## Processamento
- PyMuPDF / PDF parsing
- Regex
- JSON parsing

## CLI
- Rich (interface)
- Requests (consumo da API)

## Infra / Dev Tools
- Git
- Virtualenv
- Windows Terminal / CMD
- Batch scripts (.bat automation)

---

# ⚙️ Como rodar o projeto

## Execute o start.bat e aguarde até que na janela AI Resume Analyzer inicie a interface da ferramenta

# 📊 Exemplo de saída

## Similarity Score: 81%

Matched Skills:
- Python
- FastAPI
- PostgreSQL

Missing Skills:
- Docker
- AWS

#  Objetivo do projeto

## Demonstrar:

Integração de IA local em aplicações reais
Arquitetura backend moderna com FastAPI
Processamento de texto com NLP
Uso de embeddings para similaridade semântica
Construção de CLI interativa
Automação de execução de sistemas completos

# ⚠️ Observações
O projeto utiliza modelo local (Ollama)
Pode consumir CPU/RAM durante execução
Recomendado fechar aplicações pesadas ao rodar

👨‍💻 Autor

Icaro Santos 

GitHub: https://github.com/Icar-s
LinkedIn: https://www.linkedin.com/in/icarush/