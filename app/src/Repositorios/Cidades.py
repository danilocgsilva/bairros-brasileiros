from src.Repositorios.Conexao import Conexao
from src.Repositorios.Estados import Estados
from entidades.Cidade import Cidade
from entidades.Estado import Estado

class Cidades(Conexao):
    def buscar_por_nome(self, nome_cidade: str, nome_estado: str) -> Cidade:
        estado = Estados().buscar_por_nome(nome_estado)
        query = "SELECT id, local FROM locais WHERE tipo_localidade = 2 AND local = %s AND parentalidade = %s;"
        local_cursor = self.recursodb.cursor()
        local_cursor.execute(query, (nome_cidade, estado.id, ))
        meus_resultados = local_cursor.fetchall()
        cidades = []
        for dado_cru in meus_resultados:
            cidades.append(Cidade(dado_cru[0], dado_cru[1]))
        if len(cidades) == 0:
            raise Exception("A cidade buscada não existe no estado {}.".format(nome_estado))
        return cidades[0]
