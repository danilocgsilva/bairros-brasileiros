import abc

class ProcessadorInterface(abc.ABC):
    @abc.abstractmethod
    def processar_sucesso(self):
        pass
    
    def processar_erro(self):
        pass
    
    @abc.abstractmethod
    def esta_pronto(self) -> bool:
        pass
    
    @abc.abstractmethod
    def busca_mensagem_erro(self) -> str:
        pass
    
