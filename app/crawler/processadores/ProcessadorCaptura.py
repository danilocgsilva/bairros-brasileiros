from crawler.processadores.ProcessadorInterface import ProcessadorInterface

class ProcessadorCaptura(ProcessadorInterface):
    def processar_sucesso(self, conteudo: str):
        print(conteudo)