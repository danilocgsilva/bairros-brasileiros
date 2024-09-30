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
    
    def migrar_estrutura(self):
        dbcursor = self.mydb.cursor()
        dbcursor.execute(self._buscarQueryMigration())
    
    def escrever_tipos_localidades(self):
        query_use = "USE bairros_brasileiros"
        query_insert_tipo_bairro = "INSERT INTO tipos_locais (tipo) VALUES ('bairro');"
        query_insert_tipo_cidade = "INSERT INTO tipos_locais (tipo) VALUES ('cidade');"
        query_insert_tipo_estado = "INSERT INTO tipos_locais (tipo) VALUES ('estado');"
        dbcursor = self.mydb.cursor()
        
        dbcursor.execute(query_use)
        dbcursor.execute(query_insert_tipo_bairro)
        dbcursor.execute(query_insert_tipo_cidade)
        dbcursor.execute(query_insert_tipo_estado)
        self.mydb.commit()
    
    def _buscarQueryMigration(self):
        path = os.path.join('migrations', 'migration.sql')
        file = open(path, "r")
        query = file.read()
        return query
