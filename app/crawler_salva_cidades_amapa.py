#import sys
#sys.path.append("..") 
from crawler.CrawlerTabela import CrawlerTabela
from crawler.processadores.ProcessadorCaptura import ProcessadorCaptura
            
crawler = CrawlerTabela()
crawler.endereco = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Amap%C3%A1_por_popula%C3%A7%C3%A3o'
crawler.seletor_tabela = 'table.wikitable.sortable tbody tr'
crawler.seletor_coluna = 'td:nth-child(2) a'

processador_captura = ProcessadorCaptura()
processador_captura.configurar_nome("Amapá")
processador_captura.configurar_tipo("cidade")
    
crawler.processador = processador_captura

resultado = crawler.buscarConteudo()
print(resultado)
