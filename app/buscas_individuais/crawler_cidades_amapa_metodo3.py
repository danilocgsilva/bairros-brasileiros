import sys
sys.path.append("")
from crawler.CrawlerTabela import CrawlerTabela
from crawler.processadores.ProcessadorPrint import ProcessadorPrint
from crawler.parseadores.Subselect import Subselect

def buscar_cidades_amapa3():
    crawler = CrawlerTabela()
    crawler.endereco = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Amap%C3%A1_por_popula%C3%A7%C3%A3o'
    crawler.seletor_tabela = 'table.wikitable.sortable tbody tr'
    crawler.parseador = Subselect('td:nth-child(2) a')
    #crawler.seletor_coluna = 'td:nth-child(2) a'
    crawler.processador = ProcessadorPrint()

    resultado = crawler.buscarConteudo()
    print(resultado)
