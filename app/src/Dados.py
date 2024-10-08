from VariaveisConexaoBanco import VariaveisConexaoBanco
import mysql.connector
from src.TiposLocais import TiposLocais

class Dados:
    def adicionar_cidade(self, nome_cidade: str, nome_estado: str):
        if not self._nome_do_estado_existe(nome_estado):
            raise Exception("O nome do estado não existe")
        self._adicionar_local(nome_cidade, TiposLocais.cidade)
        
    def adicionar_bairro(self, bairro: str, cidade: str):
        if not self._nome_da_cidade_existe(cidade):
            raise Exception("O nome da cidade não existe")
        self._adicionar_local(bairro, TiposLocais.bairro)
        
    def _nome_do_estado_existe(self, nome_do_estado: str) -> bool:
        variaveisConexaoBanco = VariaveisConexaoBanco()
        recursodb = mysql.connector.connect(
            host=variaveisConexaoBanco.buscarHost(),
            user=variaveisConexaoBanco.buscarUsuarioBanco(),
            password=variaveisConexaoBanco.buscarSenhaBanco(),
            database=variaveisConexaoBanco.buscarNomeDoBanco()
        )
        local_cursor = recursodb.cursor()
        local_cursor.execute("SELECT local FROM locais WHERE tipo_localidade = %s AND local = %s;", (3, nome_do_estado, ))
        myresult = local_cursor.fetchall()
        return len(myresult) > 0
        
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