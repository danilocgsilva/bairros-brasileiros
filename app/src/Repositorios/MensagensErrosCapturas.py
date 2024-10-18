from banco_dados.VariaveisConexaoBanco import VariaveisConexaoBanco
import mysql.connector

class MensagensErrosCapturas:
    def __init__(self):
        variaveisConexaoBanco = VariaveisConexaoBanco()
        self.recursodb = mysql.connector.connect(
            host=variaveisConexaoBanco.buscarHost(),
            user=variaveisConexaoBanco.buscarUsuarioBanco(),
            password=variaveisConexaoBanco.buscarSenhaBanco(),
            database=variaveisConexaoBanco.buscarNomeDoBanco()
        )
        
    def salva(self, mensagem_erro: str, id_captura: int):
        query = "INSERT INTO mensagens_erros_capturas (mensagem, historico_capturas_id) VALUES (%s, %s);"
        local_cursor = self.recursodb.cursor()
        local_cursor.execute(query, (mensagem_erro, id_captura, ))
        self.recursodb.commit()
        