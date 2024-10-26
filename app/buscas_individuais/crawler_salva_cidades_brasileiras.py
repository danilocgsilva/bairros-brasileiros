from crawler.CrawlerTabela import CrawlerTabela
from crawler.processadores.ProcessadorPrint import ProcessadorPrint
from crawler.processadores.ProcessadorCapturaCidadeSigla import ProcessadorCapturaCidadeSigla
from crawler.parseadores.XNext import XNext

def salva_todas_cidades_brasileiras():
    crawler = CrawlerTabela()
    crawler.endereco = "https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil"
    crawler.seletor_tabela = '.mw-content-ltr.mw-parser-output li'
    parseador = XNext(2, 1)
    crawler.processador = ProcessadorCapturaCidadeSigla()
    crawler.parseador = parseador

    resultado = crawler.buscarConteudo()
    print(resultado)