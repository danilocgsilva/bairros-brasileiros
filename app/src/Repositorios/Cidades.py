from src.Repositorios.Conexao import Conexao
from src.Repositorios.Estados import Estados
from src.Repositorios.Locais import Locais
from src.TiposLocais import TiposLocais
from entidades.Cidade import Cidade

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
    
    def adicionar_cidade(self, nome_cidade: str, nome_estado: str):
        estados = Locais().buscar_estados(nome_estado)
        estado = None
        if len(estados) == 0:
            raise Exception("O nome do estado não existe")
        estado = estados[0]
        cidade_ja_cadastrada = self._cidade_ja_cadastrada(nome_cidade, estado)
        if cidade_ja_cadastrada:
            raise Exception("A cidade {} já foi cadastrada para o estado {}.".format(nome_cidade, nome_estado))
        self._adicionar_local(nome_cidade, estado.id, TiposLocais.cidade)
