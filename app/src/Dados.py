from banco_dados.VariaveisConexaoBanco import VariaveisConexaoBanco
import mysql.connector
from src.TiposLocais import TiposLocais
from entidades.Estado import Estado
from entidades.Cidade import Cidade
from src.Repositorios.Locais import Locais
from src.Repositorios.Receitas import Receitas
from src.Repositorios.Estados import Estados
from src.Repositorios.Cidades import Cidades

class Dados:
    def __init__(self):
        variaveisConexaoBanco = VariaveisConexaoBanco()
        self.recursodb = mysql.connector.connect(
            host=variaveisConexaoBanco.buscarHost(),
            user=variaveisConexaoBanco.buscarUsuarioBanco(),
            password=variaveisConexaoBanco.buscarSenhaBanco(),
            database=variaveisConexaoBanco.buscarNomeDoBanco()
        )
        
    def adicionar_receita(
        self, 
        nome_receita: str, 
        seletor_tabela: str, 
        seletor_coluna: str, 
        endereco: str,
        tipo_localidade: str,
        nome_localidade_pai: str
    ):
        Receitas().salva(nome_receita, seletor_tabela, seletor_coluna, endereco, tipo_localidade, nome_localidade_pai)
        
    def adicionar_cidade(self, nome_cidade: str, nome_estado: str):
        estados = Locais().buscar_estados(nome_estado)
        estado = None
        if len(estados) == 0:
            raise Exception("O nome do estado não existe")
        estado = estados[0]
        cidade_ja_cadastrada = self._cidade_ja_cadastrada(nome_cidade, estado)
        if cidade_ja_cadastrada:
            raise Exception("A cidade {} já foi cadastrada para o estado {}.".format(nome_cidade, nome_estado))
        self._adicionar_local(nome_cidade, estado.id, TiposLocais.cidade)
        
    def adicionar_bairro(self, bairro: str, cidade: str, estado: str):
        if not self._nome_da_cidade_existe(cidade, estado):
            raise Exception("O nome da cidade não existe")
        cidade = Cidades().buscar_por_nome(cidade, estado)
        self._adicionar_local(bairro, cidade.id, TiposLocais.bairro)
        
    def listar_todos_dados(self) -> list:
        return Locais().listar_todos_dados()
        
    def _cidade_ja_cadastrada(self, nome_cidade: str, estado: Estado) -> bool:
        local_cursor =  self.recursodb.cursor()
        local_cursor.execute("SELECT id, local FROM locais WHERE local = %s AND parentalidade = %s", (nome_cidade, estado.id, ))
        resultados = local_cursor.fetchall()
        return len(resultados) > 0
        
    def _adicionar_local(self, nome_local: str, parentalidade: int, tipo: TiposLocais):
        local_cursor = self.recursodb.cursor()
        local_cursor.execute("INSERT INTO locais (local, tipo_localidade, parentalidade) VALUES (%s, %s, %s);", (nome_local, tipo.value, parentalidade))
        self.recursodb.commit()
        
    def _nome_da_cidade_existe(self, cidade: str, estado: str) -> bool:
        estado = Estados().buscar_por_nome(estado)
        query = "SELECT id, local FROM locais WHERE parentalidade = %s AND local = %s;"
        local_cursor = self.recursodb.cursor()
        local_cursor.execute(query, (estado.id, cidade, ))
        meus_resultados = local_cursor.fetchall()
        cidades = []
        for cidade_resultado in meus_resultados:
            cidades.append(Cidade(cidade_resultado[0], cidade_resultado[1]))
        return len(cidades) == 1
        
    
