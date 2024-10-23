import sys
sys.path.append('./buscas_individuais')
from crawler_cidades_amapa_metodo3 import buscar_cidades_amapa3
from crawler_todas_cidades_brasileiras import buscar_todas_cidades_brasileiras
from crawler_busca_bairros_macapa import busca_bairros_macapa

sargv = sys.argv

if len(sargv) == 1:
    print("É preciso informar qual o tipo de busca que se deseja fazer")
    exit()

tipo_busca = sargv[1]
    
if tipo_busca == "cidades_amapa_3":
    buscar_cidades_amapa3()
    exit()
    
if tipo_busca == "todas_cidades_brasileiras":
    buscar_todas_cidades_brasileiras()
    exit()
    
if tipo_busca == "bairros_macapa":
    busca_bairros_macapa()
    exit()
    
print("É preciso indicar como primeiro argumento o tipo de busca individual:")
print(" * cidades_amapa")
