from crawler.Crawler import Crawler
from crawler.processadores.ProcessadorPrint import ProcessadorPrint
            
crawler = Crawler()
crawler.endereco = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Amap%C3%A1_por_popula%C3%A7%C3%A3o'
crawler.seletor_tabela = 'table.wikitable.sortable tbody tr'
crawler.seletor_coluna = 'td:nth-child(2) a'
crawler.processador = ProcessadorPrint()

crawler.buscarConteudo()