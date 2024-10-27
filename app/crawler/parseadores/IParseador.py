import abc

class IParseador(abc.ABC):
    @abc.abstractmethod
    def buscar_dado_iteracao(self, dado):
        pass
    

