from utils.Buscar_Arquivos_Aplicacao import Buscar_Arquivos_Aplicacao

def mostrar_comandos():
    buscar_arquivos_aplicacao = Buscar_Arquivos_Aplicacao()
    comandos = buscar_arquivos_aplicacao.buscarComandos()

    print("Comandos disponíveis:")

    for comando in comandos:
        print(" - " + comando)
        
mostrar_comandos()
        