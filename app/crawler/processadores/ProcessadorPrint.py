from crawler.processadores.ProcessadorInterface import ProcessadorInterface

class ProcessadorPrint(ProcessadorInterface):
    def processar_sucesso(self, conteudo):
        print(conteudo)
