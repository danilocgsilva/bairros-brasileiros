import sys
sys.path.append('./buscas_individuais')
from crawler_cidades_amapa_metodo3 import buscar_cidades_amapa3
from crawler_todas_cidades_brasileiras import buscar_todas_cidades_brasileiras
from crawler_busca_bairros_macapa import busca_bairros_macapa
from crawler_salva_bairros_macapa import salva_bairros_macapa
from crawler_print_cidades_brasileiras import buscar_todas_cidades_brasileiras2

sargv = sys.argv

if len(sargv) == 1:
    print("É preciso informar qual o tipo de busca que se deseja fazer")
    exit()

tipo_busca = sargv[1]
    
if tipo_busca == "cidades_amapa_3":
    buscar_cidades_amapa3()
    exit()
    
if tipo_busca == "salva_bairros_amapa":
    salva_bairros_macapa()
    exit()
    
if tipo_busca == "todas_cidades_brasileiras":
    buscar_todas_cidades_brasileiras()
    exit()
    
if tipo_busca == "todas_cidades_brasileiras_2":
    buscar_todas_cidades_brasileiras()
    exit()
    
if tipo_busca == "bairros_macapa":
    busca_bairros_macapa()
    exit()
    
if tipo_busca == "print_todas_cidades":
    buscar_todas_cidades_brasileiras2()
    exit()
    
print("É preciso indicar como primeiro argumento o tipo de busca individual:")
print(" * cidades_amapa")
