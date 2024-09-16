import os
from VariaveisConexaoBanco import VariaveisConexaoBanco
import mysql.connector

class MigracaoDB:

    def migrar(self):
        variaveisConexaoBanco = VariaveisConexaoBanco()
        mydb = mysql.connector.connect(
            host = variaveisConexaoBanco.buscarHost(),
            user = variaveisConexaoBanco.buscarUsuarioBanco(),
            password = variaveisConexaoBanco.buscarSenhaBanco()
        )
        dbcursor = mydb.cursor()
        dbcursor.execute(self._buscarQueryMigration())
    
    def _buscarQueryMigration(self):
        path = os.path.join('migrations', 'migration.sql')
        file = open(path, "r")
        query = file.read()
        return query
