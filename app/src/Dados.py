from VariaveisConexaoBanco import VariaveisConexaoBanco
import mysql.connector
from src.TiposLocais import TiposLocais

class Dados:
    def adicionar_cidade(self, nome_cidade: str):
        self._adicionar_local(nome_cidade, TiposLocais.cidade)
        
    def _adicionar_local(self, nome_local: str, tipo: TiposLocais):
        variaveisConexaoBanco = VariaveisConexaoBanco()
        recursodb = mysql.connector.connect(
            host=variaveisConexaoBanco.buscarHost(),
            user=variaveisConexaoBanco.buscarUsuarioBanco(),
            password=variaveisConexaoBanco.buscarSenhaBanco(),
            database=variaveisConexaoBanco.buscarNomeDoBanco()
        )
        local_cursor = recursodb.cursor()
        local_cursor.execute("INSERT INTO locais (local, tipo_localidade) VALUES (%s, %s);", (nome_local, tipo.value))
        recursodb.commit()