from entidades.Receita import Receita
from src.Repositorios.Conexao import Conexao

class Receitas(Conexao):
    def salva(
        self, 
        nome_receita: str, 
        seletor_tabela: str, 
        seletor_coluna: str, 
        endereco: str,
        tipo_localidade: str,
        nome_localidade_pai: str
    ):
        query = "INSERT INTO receitas (nome, seletor_tabela, seletor_coluna, endereco, tipo_localidade, nome_localidade_pai) VALUES (%s, %s, %s, %s, %s, %s);"
        local_cursor = self.recursodb.cursor()
        local_cursor.execute(query, (nome_receita, seletor_tabela, seletor_coluna, endereco, tipo_localidade, nome_localidade_pai))
        self.recursodb.commit()
        
    def buscar_por_nome(self):
        return Receita()
    
    def buscar_por_id(self, id: int) -> Receita:
        query = "SELECT id, nome, seletor_tabela, seletor_coluna, endereco, tipo_localidade, nome_localidade_pai FROM receitas WHERE id = %s;"
        local_cursor = self.recursodb.cursor()
        local_cursor.execute(query, (id, ))
        meus_resultados = local_cursor.fetchall()
        receitas_encontradas = []
        for dado_cru in meus_resultados:
            receita = Receita(dado_cru[0], dado_cru[1], dado_cru[2], dado_cru[3], dado_cru[4], dado_cru[5], dado_cru[6])
            receitas_encontradas.append(receita)
        if len(receitas_encontradas) == 0:
            raise Exception("Não foi encontrada a receita no banco de daddos de id = {}.".format(id))
        return receitas_encontradas[0]