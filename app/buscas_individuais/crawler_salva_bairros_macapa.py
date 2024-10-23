import sys
sys.path.append("")
from crawler.CrawlerTabela import CrawlerTabela
from crawler.processadores.ProcessadorCaptura import ProcessadorCaptura
            
crawler = CrawlerTabela()
crawler.endereco = 'https://pt.wikipedia.org/wiki/Lista_de_bairros_de_Macap%C3%A1'
crawler.seletor_tabela = '.wikitable.sortable.plainrowheaders tbody tr'
crawler.seletor_coluna = 'td:nth-child(1) a'

processador_captura = ProcessadorCaptura()
processador_captura.configurar_nome("Macapá")
processador_captura.configurar_tipo("bairro")
processador_captura.estado = "Amapá"
    
crawler.processador = processador_captura

resultado = crawler.buscarConteudo()
print(resultado)
