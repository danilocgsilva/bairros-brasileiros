import os
import re

class Buscar_Arquivos_Aplicacao:
    def buscarComandos(self):
        comandos = []
        arquivos = os.listdir('/app/comandos/')
        for arquivo in arquivos:
            if not re.search("_Interface.py$", arquivo):
                comandos.append(arquivo)
        
        return comandos
    