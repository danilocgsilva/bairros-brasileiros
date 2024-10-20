from src.Repositorios.Conexao import Conexao
from entidades.Estado import Estado

class Estados(Conexao):
    def buscar_por_nome(self, nome_estado: str) -> Estado:
        query = "SELECT id, local FROM locais WHERE tipo_localidade = 3 AND local = %s;"
        local_cursor = self.recursodb.cursor()
        local_cursor.execute(query, (nome_estado, ))
        meus_resultados = local_cursor.fetchall()
        estados = []
        for dado_cru in meus_resultados:
            estados.append(Estado(dado_cru[0], dado_cru[1]))
        if len(estados) == 0:
            raise Exception("O estado buscado não existe!")
        return estados[0]
    