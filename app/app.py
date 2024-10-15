from flask import Flask, request
from src.Dados import Dados
from src.Ajuda import Ajuda
from src.minha_resposta import minha_resposta
from src.DadoLegivel import DadoLegivel
from src.Requests import Requests

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
    "nome": "Guarulhos",
    "estado": "São Paulo"
}
"""
@app.route("/cidade/adicionar", methods=['POST'])
def adicionar_cidade():
    nome_da_cidade, nome_estado = Requests().buscar_dados('buscar_nome_estado_e_cidade')
    
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
@app.route("/bairro/adicionar", methods=['POST'])
def adicionar_bairro():
    nome_da_cidade, nome_bairro = Requests().buscar_dados('buscar_nome_cidade_e_bairro')
    Dados().adicionar_bairro(nome_bairro, nome_da_cidade)
    return minha_resposta("Bairro {} adicionado.".format(nome_bairro))

@app.route("/ver_todas_informacoes")
def ver_todas_informacoes():
    informacoes = Dados().listar_todos_dados()
    lista_informacoes_string = []
    for dado_informacao in informacoes:
        lista_informacoes_string.append(dado_informacao.nome + ", " + dado_informacao.tipo)
    return lista_informacoes_string

"""
{
    "nome": "Cidades de Amapá",
    "seletor_tabela": "table.wikitable.sortable tbody tr",
    "seletor_coluna": "td:nth-child(2) a",
    "endereco": "https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Amap%C3%A1_por_popula%C3%A7%C3%A3o"
}
"""
@app.route("/receita/adicionar",  methods=['POST'])
def adicionar_receita():
    nome_receita, seletor_tabela, seletor_coluna, endereco = Requests().buscar_dados('buscar_dados_request_nova_receita')
    Dados().adicionar_receita(nome_receita, seletor_tabela, seletor_coluna, endereco)
    return minha_resposta('Receita {} adicionada'.format(nome_receita))

@app.route("/receita/rodar",  methods=['POST'])
def rodar_receita():
    return minha_resposta('Receita rodada.')
