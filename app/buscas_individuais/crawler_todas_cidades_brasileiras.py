from crawler.CrawlerTabela import CrawlerTabela
from crawler.processadores.ProcessadorPrint import ProcessadorPrint
from crawler.parseadores.Subselect import Subselect

def buscar_todas_cidades_brasileiras():
    crawler = CrawlerTabela()
    crawler.endereco = "https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil#H"
    crawler.seletor_tabela = '.mw-content-ltr.mw-parser-output li'
    crawler.processador = ProcessadorPrint()

    resultado = crawler.buscarConteudo()
    print(resultado)
