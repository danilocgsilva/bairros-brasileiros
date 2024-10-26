from crawler.parseadores.IParseador import IParseador
from crawler.processadores.ProcessadorInterface import ProcessadorInterface

class Receita:
    def __init__(
        self, 
        id: int, 
        nome: str, 
        seletor_tabela: str,
        parseador: IParseador,
        processador: ProcessadorInterface,
        endereco: str,
        tipo_localidade: str
    ):
        self.id = id
        self.nome = nome
        self.seletor_tabela = seletor_tabela
        self.parseador = parseador
        self.processador = processador
        self.endereco = endereco
        self.tipo_localidade = tipo_localidade
