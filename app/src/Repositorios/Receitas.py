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
    
    def bucar_por_id(self) -> Receita:
        query = "SELECT id, nome, seletor_tabela, seletor_coluna, endereco FROM receitas WHERE id = %s;"
        local_cursor = self.recursodb.cursor()
        local_cursor.execute(query)
        meus_resultados = local_cursor.fetchall()
        for dado_cru in meus_resultados:
            receita = Receita(
                dado_cru[0],
                dado_cru[2],
                dado_cru[3],
                dado_cru[4]
            )
        return receita