from crawler.processadores.ProcessadorInterface import ProcessadorInterface
from src.Dados import Dados
from src.Repositorios.Estados import Estados

"""
Salva uma cidade no banco de dados, em função do nome e da sigla dada entre parênteses.
ex.:
    São Paulo (SP)
"""
class ProcessadorCapturaCidadeSigla(ProcessadorInterface):
    def __init__(self):
        self.nomes_estados_pelas_siglas = {}
        todos_estados_siglas = Estados().buscar_todos()
        for estado in todos_estados_siglas:
            self.nomes_estados_pelas_siglas[estado.sigla] = estado.nome
    
    def processar_sucesso(self, nome_local: str):
        nome_cidade, nome_estado = self._separarCidadeEEstadoNomes()
        Dados().adicionar_cidade(nome_cidade, nome_estado)
        
    def esta_pronto(self):
        if self.tipo == None or self.nome == None:
            return False
        return True
    
    def _separarCidadeEEstadoNomes(self, nome_cidade_com_sigla_estado):
        return "", ""