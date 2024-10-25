from crawler.parseadores.IParseador import IParseador
from entidades.Local import Local

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
            
        dado_string = str(dado_local)
        return Local(dado_string, "cidade")
