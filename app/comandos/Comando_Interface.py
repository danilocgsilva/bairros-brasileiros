import abc

class Comando_Interface(abc.ABC):
    
    @abc.abstractmethod
    def getNome(self) -> str:
        pass