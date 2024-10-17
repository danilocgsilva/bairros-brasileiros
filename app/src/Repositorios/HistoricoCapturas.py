from banco_dados.VariaveisConexaoBanco import VariaveisConexaoBanco
import mysql.connector

class HistoricoCapturas:
    def __init__(self):
        variaveisConexaoBanco = VariaveisConexaoBanco()
        self.recursodb = mysql.connector.connect(
            host=variaveisConexaoBanco.buscarHost(),
            user=variaveisConexaoBanco.buscarUsuarioBanco(),
            password=variaveisConexaoBanco.buscarSenhaBanco(),
            database=variaveisConexaoBanco.buscarNomeDoBanco()
        )
        
    def salva(self):
        query = "INSERT INTO historico_capturas (nome, seletor_tabela, seletor_coluna, endereco) VALUES (%s, %s, %s, %s);"
    