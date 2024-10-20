from crawler.processadores.ProcessadorInterface import ProcessadorInterface
from src.Dados import Dados

class ProcessadorCaptura(ProcessadorInterface):
    def __init__(self):
        self.tipo = None
        self.nome = None
        
    def configurar_nome(self, nome: str):
        self.nome = nome
    
    def configurar_tipo(self, tipo: str):
        if not tipo in ["cidade", "bairro"]:
            raise Exception("O tipo {} não é válido.".format(tipo))
        self.tipo = tipo
    
    def processar_sucesso(self, conteudo: str):
        if self.tipo == "cidade":
            Dados().adicionar_cidade(conteudo, self.nome)
        else:
            raise Exception("O processador não tem tipo definido.")
        
    def esta_pronto(self):
        if self.tipo == None or self.nome == None:
            return False
        return True