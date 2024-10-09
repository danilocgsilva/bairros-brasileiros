from flask import Flask, request
from src.Dados import Dados
from src.Ajuda import Ajuda
from src.minha_resposta import minha_resposta

app = Flask(__name__)

def buscar_nome_estado_e_cidade():
    dados_json = request.json
    return dados_json["nome"], dados_json["estado"]

def buscar_nome_cidade_e_bairro():
    dados_json = request.json
    return dados_json["cidade"], dados_json["nome"]

@app.route("/")
def default():
    return "Bairros brasileiros"
        
@app.route("/banco/ajuda")
def banco_ajuda():
    ajuda = Ajuda()
    return minha_resposta(ajuda.db())

"""
{
    "nome": "Guarulhos",
    "estado": "São Paulo"
}
"""
@app.route("/adicionar/cidade", methods=['POST'])
def adicionar_cidade():
    nome_da_cidade, nome_estado = buscar_nome_estado_e_cidade()
    
    try:
        Dados().adicionar_cidade(nome_da_cidade, nome_estado)
        return minha_resposta("{} adicionada.".format(nome_da_cidade), 200)
    except Exception as e:
        return minha_resposta(str(e), 400)

"""
{
    "nome": "Macedo",
    "cidade": "Guarulhos"
}
"""
@app.route("/adicionar/bairro")
def adicionar_bairro():
    nome_da_cidade, nome_bairro = buscar_nome_cidade_e_bairro()
    
    Dados().adicionar_bairro(nome_bairro, nome_da_cidade)
    return minha_resposta("Bairro {} adicionado.".format(nome_bairro))


