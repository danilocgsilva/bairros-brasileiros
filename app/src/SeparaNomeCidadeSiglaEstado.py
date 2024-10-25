import re

class SeparaNomeCidadeSiglaEstado:
    def __init__(self, cidade_com_sigla: str):
        self.cidade_com_sigla = cidade_com_sigla
        
    def separa(self):
        if not self._formato_valido():
            raise Exception('A string não está no formato correto: Nome da Cidade (AA)')
        
        split1 = self.cidade_com_sigla.split("(")
        split2 = split1[1].split(")")
        cidade = split1[0].strip()
        sigla_estado = split2[0].strip()
        
        return cidade, sigla_estado
    
    def _formato_valido(self):
        if not re.search("\(", self.cidade_com_sigla):
            return False
        return True