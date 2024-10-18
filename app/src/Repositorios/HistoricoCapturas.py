from banco_dados.VariaveisConexaoBanco import VariaveisConexaoBanco
from src.Repositorios.MensagensErrosCapturas import MensagensErrosCapturas
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
        
    def salva(self, data_captura, sucesso: int, historico_buscas_id: int, mensagem_erro = None):
        query = "INSERT INTO historico_capturas (data_captura, sucesso, historico_buscas_id) VALUES (%s, %s, %s);"
        local_cursor = self.recursodb.cursor()
        local_cursor.execute(query, (data_captura, sucesso, historico_buscas_id))
        self.recursodb.commit()
        if mensagem_erro:
            self._registra_erro(mensagem_erro, local_cursor.lastrowid)
        
    def _registra_erro(self, mensagem_erro: str, captura_id: int):
        MensagensErrosCapturas().salva(mensagem_erro, captura_id)