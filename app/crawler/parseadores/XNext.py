"""
Classe responsável por analisar a tag do ocorrência de uma linha html e retornar
  o local, segundo regras específicas.
"""
from crawler.parseadores.IParseador import IParseador
from entidades.Local import Local
import re

class XNext(IParseador):
    def __init__(self, next_num, sec_next = None):
        self.next_num = next_num
        self.sec_next = sec_next
    
    def buscar_dado_iteracao(self, dado_local):
        for x in range(self.next_num):
            dado_local = dado_local.next
        
        if self.sec_next:
            pre_parte = str(dado_local)
            dado_local = pre_parte + dado_local.next
            
        mensage_invalidade = self._verifica_validacao(dado_local)
        if mensage_invalidade is not "":
            raise Exception(mensage_invalidade)

        return Local(dado_local, "cidade")

    def _verifica_validacao(self, local_nome) -> bool:
        if not type(local_nome).__name__ == "str":
            return "Não foi possível achar uma string de nome com a receita deste parseador."
        
        if re.search("\n", local_nome):
            return "Caractere de newline não é permitido."

        if re.search("<", local_nome) or re.search(">", local_nome):
            return "A receita não conseguiu navegar até a informação."

        return ""