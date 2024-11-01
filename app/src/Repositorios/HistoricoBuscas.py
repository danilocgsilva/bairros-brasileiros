from banco_dados.VariaveisConexaoBanco import VariaveisConexaoBanco
import mysql.connector
import datetime
from src.Repositorios.Conexao import Conexao
from entidades.HistoricoBusca import HistoricoBusca

class HistoricoBuscas(Conexao):
    def __init__(self):
        super().__init__()
        self.busca_id = None
        self.buscas_totais = False
        
    def pedir_buscas_totais(self):
        self.buscas_totais = True
        
    def inicia(
        self, 
        receita_id = None
    ):
        if receita_id:
            query = "INSERT INTO historico_buscas (receita_id) VALUES (%s);"
            local_cursor = self.recursodb.cursor()
            local_cursor.execute(query, (receita_id, ))
        else:
            query = "INSERT INTO historico_buscas VALUES ();"
            local_cursor = self.recursodb.cursor()
            local_cursor.execute(query)
        self.busca_id = local_cursor.lastrowid
        self.recursodb.commit()
        return self
    
    def buscar_todos(self) -> list:
        local_cursor = self.recursodb.cursor()
        lista_buscas = []
        
        if self.buscas_totais:
            local_cursor.execute(self.query_buscas_totais())
            meus_resultados = local_cursor.fetchall()
            for resultado_query in meus_resultados:
                lista_buscas.append(
                    HistoricoBusca(
                        resultado_query[0],
                        resultado_query[1],
                        resultado_query[2],
                        resultado_query[3],
                        resultado_query[4],
                        resultado_query[5],
                        resultado_query[6]
                    )
                )
        else:
            query = "SELECT id, receita_id FROM historico_buscas;"
            local_cursor.execute(query)
            meus_resultados = local_cursor.fetchall()
            for resultado_query in meus_resultados:
                lista_buscas.append(
                    HistoricoBusca(
                        resultado_query[0],
                        resultado_query[1]
                    )
                )
        return lista_buscas
            
    def query_buscas_totais(self) -> str:
        return """
SELECT
	hc.historico_buscas_id,
    hb.receita_id,
	COUNT(hc.historico_buscas_id),
    lateral_data_fim.min_data_captura,
    lateral_data_inicio.max_data_captura,
    lateral_sucessos.sucessos,
    lateral_fracassos.lateral_fracassos
FROM
	historico_capturas hc
LEFT JOIN
	historico_buscas hb ON hc.historico_buscas_id = hb.id
    ,
LATERAL (
	SELECT
    	MAX(hcdl.data_captura) as max_data_captura
    FROM
    	historico_capturas hcdl
    WHERE
    	hcdl.historico_buscas_id = hc.historico_buscas_id
) lateral_data_inicio
,
LATERAL (
	SELECT
    	MIN(hcdl.data_captura) as min_data_captura
    FROM
    	historico_capturas hcdl
    WHERE
    	hcdl.historico_buscas_id = hc.historico_buscas_id
) lateral_data_fim
,
LATERAL (
	SELECT
    	COUNT(hcdl.sucesso) as sucessos
    FROM
    	historico_capturas hcdl
    WHERE
    	hcdl.historico_buscas_id = hc.historico_buscas_id
    AND
    	hcdl.sucesso = 1
) lateral_sucessos,
LATERAL (
	SELECT
    	COUNT(hcdl.sucesso) as lateral_fracassos
    FROM
    	historico_capturas hcdl
    WHERE
    	hcdl.historico_buscas_id = hc.historico_buscas_id
    AND
    	hcdl.sucesso = 0
) lateral_fracassos
GROUP BY
	hc.historico_buscas_id, 
	lateral_data_inicio.max_data_captura, 
	lateral_data_fim.min_data_captura,
	lateral_sucessos.sucessos,
	lateral_fracassos.lateral_fracassos
;
"""
    