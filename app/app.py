from utils.Buscar_Arquivos_Aplicacao import Buscar_Arquivos_Aplicacao
import importlib

def mostrar_comandos():
    buscar_arquivos_aplicacao = Buscar_Arquivos_Aplicacao()
    comandos_arquivos = buscar_arquivos_aplicacao.buscar_nome_arquivos_comandos()

    print("Comandos disponíveis:")

    classe_comandos = []
    for arquivo_comando in comandos_arquivos:
        nome_classe = arquivo_comando.split(".")[0]
        objeto_comando = importlib.import_module('comandos.' + nome_classe)
        print(" - " + nome_classe)
        
mostrar_comandos()
        