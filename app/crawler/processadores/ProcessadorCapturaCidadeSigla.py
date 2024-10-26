from crawler.processadores.ProcessadorInterface import ProcessadorInterface
from src.Repositorios.Estados import Estados
from src.SeparaNomeCidadeSiglaEstado import SeparaNomeCidadeSiglaEstado
from src.Repositorios.Cidades import Cidades

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
            
    def processar_sucesso(self, nome_local_com_sigla: str):
        nome_cidade, nome_estado = self._separarCidadeEEstadoNomes(nome_local_com_sigla)
        Cidades().adicionar_cidade(nome_cidade, nome_estado)

    def processar_erro(self, mensagem: str):
        print("ERRO! " + mensagem)
        
    def esta_pronto(self):
        return True
    
    def _separarCidadeEEstadoNomes(self, nome_cidade_com_sigla_estado):
        separadorSiglaNome = SeparaNomeCidadeSiglaEstado(nome_cidade_com_sigla_estado)
        cidade, sigla = separadorSiglaNome.separa()
        return cidade, self.nomes_estados_pelas_siglas[sigla]
