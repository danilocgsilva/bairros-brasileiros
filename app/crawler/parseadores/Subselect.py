from entidades.Local import Local
from crawler.parseadores.IParseador import IParseador

class Subselect(IParseador):
    def __init__(self, selector: str):
        self.selector = selector
    
    def buscar_dado_iteracao(self, dado_local):
        ultimo_elemento_contendo_dado = dado_local.select(self.selector)[0]

        dado_cidade_obj = ultimo_elemento_contendo_dado.contents[0]
        dado_cidade = str(dado_cidade_obj)
        
        return Local(dado_cidade, "bairro")
