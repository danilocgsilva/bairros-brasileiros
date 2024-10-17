from bs4 import BeautifulSoup
from src.Repositorios.HistoricoBuscas import HistoricoBuscas
from src.Repositorios.HistoricoCapturas import HistoricoCapturas
import requests
import re
import datetime

class CrawlerTabela:
    def __init__(self):
        self.processador = None,
        self.endereco = None
        self.seletor_tabela = None,
        self.seletor_coluna = None
    
    def buscarConteudo(self):
        bistoricoBuscasIniciado = HistoricoBuscas().inicia(datetime.datetime.now(), 1)
        historicoCapturas = HistoricoCapturas()
        
        erros_preparacao = self._verificar_erros_validacao()
        if len(erros_preparacao) > 0:
            raise Exception('Houveram impedimentos para o processamento: ' + ', '.join(erros_preparacao))
            
        response = requests.get(self.endereco)
        htmlcru = response.content
        conteudo_parseado = BeautifulSoup(htmlcru, "html.parser")
        linhas_tabela_cidades_amapa = conteudo_parseado.select(self.seletor_tabela)
        for cidade in linhas_tabela_cidades_amapa:
            if self._eHeader(cidade):
                continue
            ultimo_elemento_contendo_dado = cidade.select(self.seletor_coluna)[0]
            dado_cidade_obj = ultimo_elemento_contendo_dado.contents[0]
            dado_cidade = str(dado_cidade_obj)
            if not self._validaDado(dado_cidade):
                continue
            try:
                self.processador.processar_sucesso(dado_cidade)
                historicoCapturas.salva()
            except Exception as e:
                pass

        bistoricoBuscasIniciado.finaliza()
            
    def _verificar_erros_validacao(self):
        erros_preparacao = []
        
        if self.processador == None:
            erros_preparacao.append("Não é possível processar. Adicione um processador (propriedade processador: ProcessadorInterface).")
        if self.endereco == None:
            erros_preparacao.append("Não é possível processar. Adicione endereco web (propriedade endereco).")
        if self.seletor_tabela == None:
            erros_preparacao.append("Não é possível processar. Coloque um seletor para a tabela contendo a informação (propriedade: seletor_tabela)")
        if self.seletor_coluna == None:
            erros_preparacao.append("Não é possível processar. Coloque um seletor para a coluna da informação (propriedade: seletor_coluna)")
            
        return erros_preparacao

    def _eHeader(self, elemento_buscado) -> bool:
        celulas_header = elemento_buscado.select("th")
        if len(celulas_header) > 0:
            return True
        return False

    def _validaDado(self, dado):
        if not type(dado).__name__ == 'str':
            return False
        if re.search(r"<", dado):
            return False
        return True