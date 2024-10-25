from src.Repositorios.Conexao import Conexao
from entidades.Estado import Estado

class Estados(Conexao):
    def buscar_por_nome(self, nome_estado: str, sigla = False) -> Estado:
        local_cursor = self.recursodb.cursor()
        query = self._buscar_query(sigla)
        local_cursor.execute(query, (nome_estado, ))
        meus_resultados = local_cursor.fetchall()
        estados = []
        for dado_cru in meus_resultados:
            if sigla:
                estado = Estado(dado_cru[0], dado_cru[1], dado_cru[2])
            else:
                estado = Estado(dado_cru[0], dado_cru[1])
            estados.append(estado)
        if len(estados) == 0:
            raise Exception("O estado buscado não existe!")
        return estados[0]
    
    def _buscar_query(self, sigla = None):
        if sigla:
            return "SELECT l.id, l.local, s.sigla FROM locais l LEFT JOIN siglas_estados s ON s.estado_id = l.id WHERE l.tipo_localidade = 3 AND l.local = %s;"
        else:
            return "SELECT id, local FROM locais WHERE tipo_localidade = 3 AND local = %s;"
        
    def buscar_todos(self) -> list:
        query = "SELECT l.id, l.local, s.sigla FROM locais l LEFT JOIN siglas_estados s ON s.estado_id = l.id WHERE l.tipo_localidade = 3;"
        local_cursor = self.recursodb.cursor()
        local_cursor.execute(query)
        meus_resultados = local_cursor.fetchall()
        estados = []
        for dado_cru in meus_resultados:
            estado = Estado(dado_cru[0], dado_cru[1], dado_cru[2])
            estados.append(estado)
        return estados
        