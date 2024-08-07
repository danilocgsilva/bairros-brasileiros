from utils.Buscar_Arquivos_Aplicacao import Buscar_Arquivos_Aplicacao
from comandos.Adicionar_Cidade import Adicionar_Cidade
from comandos.Listar_Cidades import Listar_Cidades

def mostrar_comandos():
    buscar_arquivos_aplicacao = Buscar_Arquivos_Aplicacao()
    comandos_arquivos = buscar_arquivos_aplicacao.buscar_nome_arquivos_comandos()

    print("Comandos disponíveis:")

    objeto_comandos = []
    for arquivo_comando in comandos_arquivos:
        nome_classe = arquivo_comando.split(".")[0]
        class_obj = globals()[nome_classe]
        objeto_comandos.append(class_obj())
        
    for objeto_comando in objeto_comandos:
        print(objeto_comando.getNome())
        
mostrar_comandos()
        