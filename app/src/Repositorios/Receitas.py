import mysql.connector
from banco_dados.VariaveisConexaoBanco import VariaveisConexaoBanco
from entidades.Receita import Receita

class Receitas:
    def __init__(self):
        variaveisConexaoBanco = VariaveisConexaoBanco()
        self.recursodb = mysql.connector.connect(
            host=variaveisConexaoBanco.buscarHost(),
            user=variaveisConexaoBanco.buscarUsuarioBanco(),
            password=variaveisConexaoBanco.buscarSenhaBanco(),
            database=variaveisConexaoBanco.buscarNomeDoBanco()
        )
        
    def salva(
        self, 
        nome_receita: str, 
        seletor_tabela: str, 
        seletor_coluna: str, 
        endereco: str
    ):
        query = "INSERT INTO receitas (nome, seletor_tabela, seletor_coluna, endereco) VALUES (%s, %s, %s, %s);"
        local_cursor = self.recursodb.cursor()
        local_cursor.execute(query, (nome_receita, seletor_tabela, seletor_coluna, endereco))
        self.recursodb.commit()
        
    def buscar_por_nome(self):
        return Receita()
        