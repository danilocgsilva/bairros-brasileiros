from src.DadoLegivel import DadoLegivel
from entidades.Estado import Estado
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