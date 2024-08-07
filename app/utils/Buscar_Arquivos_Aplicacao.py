import os
import re

class Buscar_Arquivos_Aplicacao:
    def buscar_nome_arquivos_comandos(self):
        comandos = []
        arquivos = os.listdir('/app/comandos/')
        for arquivo in arquivos:
            if \
                not re.search("_Interface.py$", arquivo) and \
                not re.search("__pycache__", arquivo\
            ):
                comandos.append(arquivo)
        
        return comandos
    