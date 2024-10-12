import abc

class ProcessadorInterface(abc.ABC):
    @abc.abstractmethod
    def processar_sucesso(self):
        pass