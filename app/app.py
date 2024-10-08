from flask import Flask, request
from src.Dados import Dados
from src.Ajuda import Ajuda
from src.minha_resposta import minha_resposta

app = Flask(__name__)

@app.route("/")
def default():
    return "Bairros brasileiros"
        
@app.route("/banco/ajuda")
def banco_ajuda():
    ajuda = Ajuda()
    return minha_resposta(ajuda.db())

"""
{
    "nome": "Diadema"
}
"""
@app.route("/adicionar/cidade")
def adicionar_cidade():
    dados_json = request.json
    nome_da_cidade = dados_json["nome"]
    Dados().adicionar_cidade(nome_da_cidade)
    return minha_resposta("{} adicionada.".format(nome_da_cidade))
