from crawler.processadores.ProcessadorInterface import ProcessadorInterface

class ProcessadorPrint(ProcessadorInterface):
    def processar_sucesso(self, conteudo: str):
        print(conteudo)
        
    def esta_pronto(self)-> bool:
        return True
