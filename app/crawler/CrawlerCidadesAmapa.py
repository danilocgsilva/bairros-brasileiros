# from flask import request
import requests
from bs4 import BeautifulSoup

class CrawlerCidadesAmapa:
    def buscarConteudo(self):
        # response = requests.get("https://www.scrapingcourse.com/ecommerce/")
        # Primeiro, tenha o html: "https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Amap%C3%A1_por_popula%C3%A7%C3%A3o"
        # Este html contém a lista de todos os municípios do Amapá 
        response = requests.get("https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Amap%C3%A1_por_popula%C3%A7%C3%A3o")
        htmlcru = response.content
        conteudo_parseado = BeautifulSoup(htmlcru, "html.parser")
        # Depois, devo fazer o select do elemento que contém a lista 
        linhas_tabela_cidades_amapa = conteudo_parseado.select("table.wikitable.sortable tbody tr")
        lista_cidades = []
        for cidade in linhas_tabela_cidades_amapa:
            if self._eHeader(cidade):
                continue
            ultimo_elemento_contendo_dado = cidade.select("td:nth-child(2) a")[0]
            dado_cidade = ultimo_elemento_contendo_dado.contents[0]
            lista_cidades.append(dado_cidade)
            print(dado_cidade)
            
    def _eHeader(self, elemento_buscado) -> bool:
        celulas_header = elemento_buscado.select("th")
        if len(celulas_header) > 0:
            return True
        return False
            
crawler = CrawlerCidadesAmapa()
crawler.buscarConteudo()
