from crawler.processadores.ProcessadorInterface import ProcessadorInterface
from src.Dados import Dados

class ProcessadorCaptura(ProcessadorInterface):
    def __init__(self):
        self.tipo = None
        self.nome = None
        self.estado = None
        self.mensagem_erro = ""
        
    def configurar_nome(self, nome: str):
        self.nome = nome
    
    def configurar_tipo(self, tipo: str):
        if not tipo in ["cidade", "bairro"]:
            raise Exception("O tipo {} não é válido.".format(tipo))
        self.tipo = tipo
    
    def processar_sucesso(self, nome_local: str):
        if self.tipo == "cidade":
            Dados().adicionar_cidade(nome_local, self.nome)
        elif self.tipo == "bairro":
            if self.estado == None:
                raise Exception('É preciso determinar o estado para o processador. Propriedade: estado, processador: ProcessadorCaptura.')
            Dados().adicionar_bairro(nome_local, self.nome, self.estado)
        else:
            raise Exception("O processador não tem tipo definido.")
        
    def esta_pronto(self):
        if self.tipo == None or self.nome == None:
            self.mensagem_erro = "O processador precisa de um tipo e um nome."
            return False
        return True
    
    def busca_mensagem_erro(self) -> str:
        return self.mensagem_erro
