from src.Repositorios.Conexao import Conexao

class MensagensErrosCapturas(Conexao):
    def salva(self, mensagem_erro: str, id_captura: int):
        query = "INSERT INTO mensagens_erros_capturas (mensagem, historico_capturas_id) VALUES (%s, %s);"
        local_cursor = self.recursodb.cursor()
        local_cursor.execute(query, (mensagem_erro, id_captura, ))
        self.recursodb.commit()
        