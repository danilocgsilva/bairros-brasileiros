import os
from VariaveisConexaoBanco import VariaveisConexaoBanco
import mysql.connector

class MigracaoDB:
    def __init__(self):
        variaveisConexaoBanco = VariaveisConexaoBanco()
        self.mydb = mysql.connector.connect(
            host = variaveisConexaoBanco.buscarHost(),
            user = variaveisConexaoBanco.buscarUsuarioBanco(),
            password = variaveisConexaoBanco.buscarSenhaBanco()
        )
        self.dbcursor = self.mydb.cursor()
    
    def migrar_estrutura(self):
        dbcursor = self.mydb.cursor()
        dbcursor.execute(self._buscarQueryMigration())
    
    def escrever_tipos_localidades(self):
        query_use = "USE bairros_brasileiros"
        self.dbcursor.execute(query_use)
        
        self._insert_tipo_local('bairro')
        self._insert_tipo_local('cidade')
        self._insert_tipo_local('estado')

        self.mydb.commit()
    
    def _buscarQueryMigration(self):
        path = os.path.join('migrations', 'migration.sql')
        file = open(path, "r")
        query = file.read()
        return query
    
    def _insert_tipo_local(self, tipo: str):
        query_insert_tipo_estado = "INSERT INTO tipos_locais (tipo) VALUES ('{0}');"
        self.dbcursor.execute(query_insert_tipo_estado.format(tipo))
        
