from flask import Flask, request
from src.Dados import Dados
from src.Ajuda import Ajuda
from src.minha_resposta import minha_resposta
from src.Requests import Requests
from src.Repositorios.Receitas import Receitas
from crawler.CrawlerTabela import CrawlerTabela
from src.Repositorios.HistoricoBuscas import HistoricoBuscas

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
    "tipo_localidade": "cidade"
    "id_localidade_pai": "9"
}
"""
@app.route("/receita/adicionar",  methods=['POST'])
def adicionar_receita():
    nome_receita, seletor_tabela, seletor_coluna, endereco, tipo_localidade, id_localidade_pai = Requests().buscar_dados('buscar_dados_request_nova_receita')
    Dados().adicionar_receita(nome_receita, seletor_tabela, seletor_coluna, endereco, tipo_localidade, id_localidade_pai)
    return minha_resposta('Receita {} adicionada'.format(nome_receita))

"""
{
    "receita_id": 1
}
"""
@app.route("/receita/rodar",  methods=['POST'])
def rodar_receita():
    id_receita = None
    try:
        id_receita = Requests().buscar_dados('receita_id')
        receita = Receitas().buscar_por_id(id_receita)
    except Exception as e:
        return minha_resposta('Erro: ' + str(e), 500)
    
    crawler = CrawlerTabela()
    crawler.endereco = receita.endereco
    crawler.adicionar_processador(receita.processador)
    crawler.parseador = receita.parseador
    crawler.seletor_tabela = receita.seletor_tabela
    crawler.buscarConteudoReceita(receita)

    return minha_resposta('Receita rodada. Sucessos: ' + str(crawler.sucessos) + ", erros: " + str(crawler.erros))

@app.route("/receitas",  methods=['GET'])
def listar_receitas():
    receitas = Dados.buscarTodasReceitas()
    receitas_nomes = list(map(lambda x: { 'id': x.id, 'nome': x.nome}, receitas))
    return minha_resposta(receitas_nomes)

@app.route("/buscas/historico", methods=['GET'])
def busca_historico():
    historico_buscas_raw = HistoricoBuscas().buscar_todos()
    historico_buscas_output = []
    for historico_busca in historico_buscas_raw:
        historico_buscas_output.append({"id": historico_busca.id, "receita_id": historico_busca.receita_id})
    return minha_resposta(historico_buscas_output)
