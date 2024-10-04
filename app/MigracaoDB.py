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
        # self.dbcursor = self.mydb.cursor()
    
    def migrar_estrutura(self):
        self.dbcursor = self.mydb.cursor()
        #self.dbcursor.nextset()
        #dbcursor = self.mydb.cursor()
        self.dbcursor.execute(self._buscarQueryMigration())
        #dbcursor.execute(self._buscarQueryMigration())
        # dbcursor.close()
        # self.dbcursor.close()
        # self.mydb.commit()
    
    def escrever_tipos_localidades(self):
        # self.dbcursor = self.mydb.cursor()
        query_use = "USE bairros_brasileiros"
        #dbcursor = self.mydb.cursor()
        #dbcursor.execute(query_use)
        self.dbcursor.nextset()
        self.dbcursor.execute(query_use)
        
        mensagens = []
        
        bairro_inserido = self._insert_tipo_local('bairro')
        mensagens.append(self._construir_mensagem('bairro', bairro_inserido))
        
        cidade_inserida = self._insert_tipo_local('cidade')
        mensagens.append(self._construir_mensagem('cidade', cidade_inserida))
        
        estado_inserido = self._insert_tipo_local('estado')
        mensagens.append(self._construir_mensagem('estado', estado_inserido))

        #self.dbcursor.close()
        # self.mydb.commit()
        
        
        return "\n".join(mensagens)
    
    def _buscarQueryMigration(self):
        path = os.path.join('migrations', 'migration.sql')
        file = open(path, "r")
        query = file.read()
        return query
    
    def _insert_tipo_local(self, tipo: str):
        query_check = "SELECT tipo FROM tipos_locais WHERE tipo = '{0}';"
        self.dbcursor.execute(query_check.format(tipo))
        resultados = self.dbcursor.fetchall()
        if len(resultados) == 0:
            query_insert_tipo_estado = "INSERT INTO tipos_locais (tipo) VALUES ('{0}');"
            self.dbcursor.execute(query_insert_tipo_estado.format(tipo))
            return True
        else:
            return False
        
    def _construir_mensagem(self, tipo, sucesso):
        if self._insert_tipo_local(tipo):
            return "Tipo de local " + tipo + " adicionado."
        else:
            return "Tipo de local " + tipo + " já tinha sido inserido."
