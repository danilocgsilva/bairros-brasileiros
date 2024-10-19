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
        endereco: str,
        tipo_localidade: str
    ):
        query = "INSERT INTO receitas (nome, seletor_tabela, seletor_coluna, endereco, tipo_localidade) VALUES (%s, %s, %s, %s, %s);"
        local_cursor = self.recursodb.cursor()
        local_cursor.execute(query, (nome_receita, seletor_tabela, seletor_coluna, endereco, tipo_localidade))
        self.recursodb.commit()
        
    def buscar_por_nome(self):
        return Receita()
    
    def buscar_por_id(self, id: int) -> Receita:
        query = "SELECT id, nome, seletor_tabela, seletor_coluna, endereco FROM receitas WHERE id = %s;"
        local_cursor = self.recursodb.cursor()
        local_cursor.execute(query, (id, ))
        meus_resultados = local_cursor.fetchall()
        receitas_encontradas = []
        for dado_cru in meus_resultados:
            receita = Receita(dado_cru[0], dado_cru[1], dado_cru[2], dado_cru[3], dado_cru[4])
            receitas_encontradas.append(receita)
        if len(receitas_encontradas) == 0:
            raise Exception("Não foi encontrada a receita no banco de daddos de id = {}.".format(id))
        return receitas_encontradas[0]