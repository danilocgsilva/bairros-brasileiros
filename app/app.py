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

@app.route("/adicionar/cidade")
def adicionar_cidade():
    Dados().adicionar_cidade()
    return minha_resposta("Guarulhos adicionada.")
