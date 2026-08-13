# Importa as classes necessárias do FastAPI, módulo os e glob
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import glob

# Cria a instância principal da aplicação FastAPI
app = FastAPI()

# Configura o middleware CORS para aceitar requisições de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define o caminho absoluto da pasta de imagens
# Isso garante que o servidor encontre a pasta independente de onde for executado
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Lista de figurinhas com id, nome, categoria e URL da imagem
# O imagem_url aponta para o endpoint próprio de cada figurinha
figurinhas = [
    {"id":  1, "nome": "Alan Turing",         "categoria": "IA",             "imagem_url": "/figurinhas/1/imagem"},
    {"id":  2, "nome": "John McCarthy",       "categoria": "IA",             "imagem_url": "/figurinhas/2/imagem"},
    {"id":  3, "nome": "Sam Altman",          "categoria": "IA",             "imagem_url": "/figurinhas/3/imagem"},
    {"id":  4, "nome": "Geoffrey Hinton",     "categoria": "IA",             "imagem_url": "/figurinhas/4/imagem"},
    {"id":  5, "nome": "Yann LeCun",          "categoria": "IA",             "imagem_url": "/figurinhas/5/imagem"},
    {"id":  6, "nome": "Guido van Rossum",    "categoria": "Python",         "imagem_url": "/figurinhas/6/imagem"},
    {"id":  7, "nome": "Tim Peters",          "categoria": "Python",         "imagem_url": "/figurinhas/7/imagem"},
    {"id":  8, "nome": "Ray Hettinger",       "categoria": "Python",         "imagem_url": "/figurinhas/8/imagem"},
    {"id":  9, "nome": "Travis Oliphant",     "categoria": "Python",         "imagem_url": "/figurinhas/9/imagem"},
    {"id": 10, "nome": "Wes McKinney",        "categoria": "Python",         "imagem_url": "/figurinhas/10/imagem"},
    {"id": 11, "nome": "Edgar Codd",          "categoria": "Banco de Dados", "imagem_url": "/figurinhas/11/imagem"},
    {"id": 12, "nome": "Larry Ellison",       "categoria": "Banco de Dados", "imagem_url": "/figurinhas/12/imagem"},
    {"id": 13, "nome": "Michael Stonebraker", "categoria": "Banco de Dados", "imagem_url": "/figurinhas/13/imagem"},
    {"id": 14, "nome": "Salvatore Sanfilippo","categoria": "Banco de Dados", "imagem_url": "/figurinhas/14/imagem"},
    {"id": 15, "nome": "Eliot Horowitz",      "categoria": "Banco de Dados", "imagem_url": "/figurinhas/15/imagem"},
    {"id": 16, "nome": "Linus Torvalds",      "categoria": "Open Source",    "imagem_url": "/figurinhas/16/imagem"},
    {"id": 17, "nome": "Dennis Ritchie",      "categoria": "Open Source",    "imagem_url": "/figurinhas/17/imagem"},
    {"id": 18, "nome": "Richard Stallman",    "categoria": "Open Source",    "imagem_url": "/figurinhas/18/imagem"},
    {"id": 19, "nome": "Bill Gates",          "categoria": "Pioneers",       "imagem_url": "/figurinhas/19/imagem"},
    {"id": 20, "nome": "Steve Jobs",          "categoria": "Pioneers",       "imagem_url": "/figurinhas/20/imagem"},
    {"id": 21, "nome": "Paulo Silveira",      "categoria": "Alura",          "imagem_url": "/figurinhas/21/imagem"},
    {"id": 22, "nome": "Guilherme Silveira",  "categoria": "Alura",          "imagem_url": "/figurinhas/22/imagem"},
    {"id": 23, "nome": "Gus Fune",            "categoria": "Alura",          "imagem_url": "/figurinhas/23/imagem"},
    {"id": 24, "nome": "Mauricio Aniche",     "categoria": "Alura",          "imagem_url": "/figurinhas/24/imagem"},
    {"id": 25, "nome": "Andre Bessa",         "categoria": "Alura",          "imagem_url": "/figurinhas/25/imagem"},
    {"id": 26, "nome": "Guilherme Louro",     "categoria": "Alura",          "imagem_url": "/figurinhas/26/imagem"},
    {"id": 27, "nome": "Gi Dionisio",         "categoria": "Alura",          "imagem_url": "/figurinhas/27/imagem"},
    {"id": 28, "nome": "Vinicius Dias",       "categoria": "Alura",          "imagem_url": "/figurinhas/28/imagem"},
    {"id": 29, "nome": "Rafa Ballerini",      "categoria": "Alura",          "imagem_url": "/figurinhas/29/imagem"},
    # {"id": 30, "nome": "???",               "categoria": "???",             "imagem_url": "/figurinhas/30/imagem"},  # ainda não disponível
]


# Define o endpoint GET na rota "/figurinhas"
# Retorna a lista completa de figurinhas com suas imagens
@app.get("/figurinhas")
def listar_figurinhas():
    return figurinhas


# Define o endpoint GET na rota "/figurinhas/{id}/imagem"
# Usa glob para encontrar o arquivo com prefixo "{id:02d}" na pasta figurinhas/
# Retorna 404 se não encontrar, ou FileResponse com o arquivo encontrado
@app.get("/figurinhas/{id}/imagem")
def imagem_figurinha(id: int):
    # Padrão: dois dígitos (ex: "01", "29") seguido de qualquer coisa que não seja número
    padrao = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")
    arquivos = glob.glob(padrao)

    if not arquivos:
        raise HTTPException(status_code=404, detail="Imagem não encontrada")

    return FileResponse(arquivos[0])
