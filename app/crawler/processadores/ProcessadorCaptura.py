from crawler.processadores.ProcessadorInterface import ProcessadorInterface
from src.Dados import Dados

class ProcessadorCaptura(ProcessadorInterface):
    def processar_sucesso(self, conteudo: str):
        Dados().adicionar_cidade(conteudo, "Amapá")