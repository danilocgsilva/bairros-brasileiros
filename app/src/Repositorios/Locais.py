from src.DadoLegivel import DadoLegivel
from entidades.Estado import Estado
from entidades.Cidade import Cidade
from banco_dados.VariaveisConexaoBanco import VariaveisConexaoBanco
import mysql.connector

class Locais:
    def __init__(self):
        variaveisConexaoBanco = VariaveisConexaoBanco()
        self.recursodb = mysql.connector.connect(
            host=variaveisConexaoBanco.buscarHost(),
            user=variaveisConexaoBanco.buscarUsuarioBanco(),
            password=variaveisConexaoBanco.buscarSenhaBanco(),
            database=variaveisConexaoBanco.buscarNomeDoBanco()
        )
    
    def listar_todos_dados(self) -> list:
        query = "SELECT lo.local, tl.tipo FROM locais lo LEFT JOIN tipos_locais tl ON tl.id = lo.tipo_localidade;"
        local_cursor = self.recursodb.cursor()
        local_cursor.execute(query)
        meus_resultados = local_cursor.fetchall()
        dados_legiveis = []
        for dado_cru in meus_resultados:
            dados_legiveis.append(DadoLegivel(dado_cru[0], dado_cru[1]))
        return dados_legiveis
    
    def buscar_estados(self, nome_do_estado: str) -> list:
        estados = []
        local_cursor = self.recursodb.cursor()
        local_cursor.execute("SELECT id, local FROM locais WHERE tipo_localidade = %s AND local = %s;", (3, nome_do_estado, ))
        meus_resultados = local_cursor.fetchall()
        for estado_resultado in meus_resultados:
            estados.append(Estado(id=estado_resultado[0], nome=estado_resultado[1]))
        return estados
    
    def cidade_existe(self, nome_cidade, nome_estado) -> bool:
        estados = self.buscar_estados(nome_estado)
        estado = estados[0]
        local_cursor = self.recursodb.cursor()
        query = "SELECT id FROM locais WHERE tipo_localidade = %s AND parentalidade = %s"
        local_cursor.execute(query, (2, estado.id, ))
        meus_resultados = local_cursor.fetchall()
        cidades = []
        for cidade_resultado in meus_resultados:
            cidades.append(Cidade(id=cidade_resultado[0], nome=cidade_resultado[1]))
        return len(cidades) == 1
        
    