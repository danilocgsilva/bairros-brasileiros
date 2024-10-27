import abc

class ICrawler(abc.ABC):
    @abc.abstractmethod
    def buscarConteudo(self, historicoBuscasIniciado = None):
        pass
