from banco_dados.VariaveisConexaoBanco import VariaveisConexaoBanco
import mysql.connector
from src.TiposLocais import TiposLocais
from entidades.Estado import Estado
from src.DadoLegivel import DadoLegivel

class Dados:
    def __init__(self):
        variaveisConexaoBanco = VariaveisConexaoBanco()
        self.recursodb = mysql.connector.connect(
            host=variaveisConexaoBanco.buscarHost(),
            user=variaveisConexaoBanco.buscarUsuarioBanco(),
            password=variaveisConexaoBanco.buscarSenhaBanco(),
            database=variaveisConexaoBanco.buscarNomeDoBanco()
        )
    
    def adicionar_cidade(self, nome_cidade: str, nome_estado: str):
        estados = self._buscar_estados(nome_estado)
        estado = None
        if len(estados) == 0:
            raise Exception("O nome do estado não existe")
        estado = estados[0]
        cidade_ja_cadastrada = self._cidade_ja_cadastrada(nome_cidade, estado)
        if cidade_ja_cadastrada:
            raise Exception("A cidade {} já foi cadastrada para o estado {}.".format(nome_cidade, nome_estado))
        self._adicionar_local(nome_cidade, estado.id, TiposLocais.cidade)
        
    def adicionar_bairro(self, bairro: str, cidade: str):
        if not self._nome_da_cidade_existe(cidade):
            raise Exception("O nome da cidade não existe")
        self._adicionar_local(bairro, 4, TiposLocais.bairro)
        
    def listar_todos_dados(self) -> list:
        query = "SELECT lo.local, tl.tipo FROM locais lo LEFT JOIN tipos_locais tl ON tl.id = lo.tipo_localidade;"
        local_cursor = self.recursodb.cursor()
        local_cursor.execute(query)
        meus_resultados = local_cursor.fetchall()
        dados_legiveis = []
        for dado_cru in meus_resultados:
            dados_legiveis.append(DadoLegivel(dado_cru[0], dado_cru[1]))
        return dados_legiveis
        
        
    def _cidade_ja_cadastrada(self, nome_cidade: str, estado: Estado) -> bool:
        local_cursor =  self.recursodb.cursor()
        local_cursor.execute("SELECT id, local FROM locais WHERE local = %s AND parentalidade = %s", (nome_cidade, estado.id, ))
        resultados = local_cursor.fetchall()
        return len(resultados) > 0
        
    def _buscar_estados(self, nome_do_estado: str) -> list:
        estados = []
        local_cursor = self.recursodb.cursor()
        local_cursor.execute("SELECT id, local FROM locais WHERE tipo_localidade = %s AND local = %s;", (3, nome_do_estado, ))
        meus_resultados = local_cursor.fetchall()
        for estado_resultado in meus_resultados:
            estados.append(Estado(id=estado_resultado[0], nome=estado_resultado[1]))
        return estados
        
    def _adicionar_local(self, nome_local: str, parentalidade: int, tipo: TiposLocais):
        local_cursor = self.recursodb.cursor()
        local_cursor.execute("INSERT INTO locais (local, tipo_localidade, parentalidade) VALUES (%s, %s, %s);", (nome_local, tipo.value, parentalidade))
        self.recursodb.commit()