from banco_dados.VariaveisConexaoBanco import VariaveisConexaoBanco
import mysql.connector
import datetime

class HistoricoBuscas:
    def __init__(self):
        variaveisConexaoBanco = VariaveisConexaoBanco()
        self.recursodb = mysql.connector.connect(
            host=variaveisConexaoBanco.buscarHost(),
            user=variaveisConexaoBanco.buscarUsuarioBanco(),
            password=variaveisConexaoBanco.buscarSenhaBanco(),
            database=variaveisConexaoBanco.buscarNomeDoBanco()
        )
        self.busca_id = None
        
    def inicia(
        self, 
        data_inicio: str, 
        receita_id: int
    ):
        query = "INSERT INTO historico_buscas (data_inicio, receita_id) VALUES (%s, %s);"
        local_cursor = self.recursodb.cursor()
        local_cursor.execute(query, (data_inicio, receita_id, ))
        self.busca_id = local_cursor.lastrowid
        self.recursodb.commit()
        return self
    
    def finaliza(self):
        query = "UPDATE historico_buscas SET data_fim = %s WHERE id = %s;"
        local_cursor = self.recursodb.cursor()
        local_cursor.execute(query, (datetime.datetime.now(), self.busca_id, ))
        self.recursodb.commit()
        