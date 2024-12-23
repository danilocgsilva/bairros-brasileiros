from bs4 import BeautifulSoup
from src.Repositorios.HistoricoBuscas import HistoricoBuscas
from src.Repositorios.HistoricoCapturas import HistoricoCapturas
from crawler.ICrawler import ICrawler
from crawler.parseadores.Subselect import Subselect
import requests
import datetime
from entidades.Receita import Receita


"""
Classe responsável por fazer a busca da informação.
propriedade processador: Define o que fazer com a inforação capturada. Pode ser
  apenas um "print" em tela, ou pode ser que precisa salvar o registro em um
  banco de dados.
método buscarConteudo: faz o processamento do conteúdo, em função do processador dado.
"""
class CrawlerTabela(ICrawler):
    def __init__(self):
        self.processador = None
        self.endereco = None
        self.seletor_tabela = None
        self.seletor_coluna = None
        self.erros = 0
        self.sucessos = 0
        self.next_next = False
        self.next_num = None
        self.parseador = None
        
    def adicionar_processador(self, processador):
        if self.processador != None:
            raise Exception('O processador já foi adicionado.')
        self.processador = processador

    def buscarConteudoReceita(self, receita: Receita):
        historicoBuscasIniciado = HistoricoBuscas().inicia(receita.id)
        self.buscarConteudo(historicoBuscasIniciado)
    
    def buscarConteudo(self, historicoBuscasIniciado = None):
        if not self.processador.esta_pronto():
            raise Exception(
                'O processador não está pronto. Verifique a implementação do método esta_pronto para resolver is requisitos do processador: mensagem: '\
                + self.processador.busca_mensagem_erro()
            )
        
        if not historicoBuscasIniciado:
            historicoBuscasIniciado = HistoricoBuscas().inicia()
        historicoCapturas = HistoricoCapturas()
        
        erros_preparacao = self._verificar_erros_validacao()
        if len(erros_preparacao) > 0:
            raise Exception('Houveram impedimentos para o processamento: ' + ', '.join(erros_preparacao))
            
        response = requests.get(self.endereco)
        htmlcru = response.content
        conteudo_parseado = BeautifulSoup(htmlcru, "html.parser")
        linhas_tabela_cidades_amapa = conteudo_parseado.select(self.seletor_tabela)
        print("Temos " + str(len(linhas_tabela_cidades_amapa)) + " ocorências.")
        
        for cidade in linhas_tabela_cidades_amapa:
            if self._eHeader(cidade):
                continue
            
            dado_cidade = None
            try:
                dado_cidade = self.parseador.buscar_dado_iteracao(cidade)
                self._processar_sucesso(dado_cidade.nome, historicoCapturas, historicoBuscasIniciado.busca_id)
            except Exception as e:
                self._registra_erro(historicoCapturas, historicoBuscasIniciado, str(e))
                continue
            
        return "Sucessos: {}, erros: {}.".format(self.sucessos, self.erros)
            
    def _verificar_erros_validacao(self):
        erros_preparacao = []
        
        if self.processador == None:
            erros_preparacao.append("Não é possível processar. Adicione um processador (propriedade processador: ProcessadorInterface).")
        if self.endereco == None:
            erros_preparacao.append("Não é possível processar. Adicione endereco web (propriedade endereco).")
        if self.seletor_tabela == None:
            erros_preparacao.append("Não é possível processar. Coloque um seletor para a tabela contendo a informação (propriedade: seletor_tabela)")
            
        return erros_preparacao

    def _eHeader(self, elemento_buscado) -> bool:
        celulas_header = elemento_buscado.select("th")
        if len(celulas_header) > 0:
            return True
        return False
    
    def _registra_erro(self, historicoCapturas, historicoBuscasIniciado, mensagem):
        historicoCapturas.salva(datetime.datetime.now(), 0, historicoBuscasIniciado.busca_id, mensagem)
        self.processador.processar_erro(mensagem)
        self.erros += 1
        
    def _processar_sucesso(self, nome_local, historicoCapturas, historico_busca_id):
        self.processador.processar_sucesso(nome_local)
        self.sucessos += 1
        historicoCapturas.salva(datetime.datetime.now(), 1, historico_busca_id)
        