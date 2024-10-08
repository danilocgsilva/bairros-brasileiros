from VariaveisConexaoBanco import VariaveisConexaoBanco
import mysql.connector

class Dados:
    def adicionar_cidade(string: str):
        variaveisConexaoBanco = VariaveisConexaoBanco()
        recursodb = mysql.connector.connect(
            host=variaveisConexaoBanco.buscarHost(),
            user=variaveisConexaoBanco.buscarUsuarioBanco(),
            password=variaveisConexaoBanco.buscarSenhaBanco(),
            database=variaveisConexaoBanco.buscarNomeDoBanco()
        )
        local_cursor = recursodb.cursor()
        local_cursor.execute("INSERT INTO locais (local, tipo_localidade) VALUES (%s, %s);", ("Guarulhos", 2))
        recursodb.commit()