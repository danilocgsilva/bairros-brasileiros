from banco_dados.VariaveisConexaoBanco import VariaveisConexaoBanco
import mysql.connector
import datetime
from src.Repositorios.Conexao import Conexao
from entidades.HistoricoBusca import HistoricoBusca

class HistoricoBuscas(Conexao):
    def __init__(self):
        super().__init__()
        self.busca_id = None
        
    def inicia(
        self, 
        receita_id = None
    ):
        if receita_id:
            query = "INSERT INTO historico_buscas (receita_id) VALUES (%s);"
            local_cursor = self.recursodb.cursor()
            local_cursor.execute(query, (receita_id, ))
        else:
            query = "INSERT INTO historico_buscas VALUES ();"
            local_cursor = self.recursodb.cursor()
            local_cursor.execute(query)
        self.busca_id = local_cursor.lastrowid
        self.recursodb.commit()
        return self
    
    def buscar_todos(self) -> list:
        query = "SELECT id, receita_id FROM historico_buscas;"
        local_cursor = self.recursodb.cursor()
        local_cursor.execute(query)
        meus_resultados = local_cursor.fetchall()
        lista_buscas = []
        for resultado_query in meus_resultados:
            lista_buscas.append(HistoricoBusca(resultado_query[0], resultado_query[1]))
        return lista_buscas
    